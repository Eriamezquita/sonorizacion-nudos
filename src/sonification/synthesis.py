"""Síntesis de audio simple en WAV.

Para prototipos iniciales se usa una onda sinusoidal con envolvente suave. La
meta no es producir una pieza final, sino verificar que el mapeo matemático se
puede escuchar y reproducir.
"""

from __future__ import annotations

import wave
from pathlib import Path
from typing import Iterable

import numpy as np

from .mapping import SoundEvent


def _sine_event(event: SoundEvent, sample_rate: int) -> np.ndarray:
    n_samples = max(1, int(event.duration * sample_rate))
    t = np.linspace(0.0, event.duration, n_samples, endpoint=False)
    signal = event.amplitude * np.sin(2 * np.pi * event.frequency * t)

    # Envolvente breve para evitar clics al inicio/final.
    fade_len = min(int(0.02 * sample_rate), n_samples // 2)
    if fade_len > 0:
        fade_in = np.linspace(0.0, 1.0, fade_len)
        fade_out = np.linspace(1.0, 0.0, fade_len)
        signal[:fade_len] *= fade_in
        signal[-fade_len:] *= fade_out
    return signal


def synthesize_events_to_wav(
    events: Iterable[SoundEvent],
    output_path: str | Path,
    sample_rate: int = 44100,
    gap: float = 0.04,
) -> Path:
    """Genera un archivo WAV mono a partir de eventos sonoros."""
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    chunks = []
    gap_samples = int(gap * sample_rate)
    silence = np.zeros(gap_samples)

    for event in events:
        chunks.append(_sine_event(event, sample_rate))
        if gap_samples > 0:
            chunks.append(silence)

    if not chunks:
        audio = np.zeros(sample_rate)
    else:
        audio = np.concatenate(chunks)

    max_abs = np.max(np.abs(audio)) if audio.size else 0.0
    if max_abs > 0:
        audio = audio / max_abs * 0.85

    pcm = np.int16(audio * 32767)

    with wave.open(str(output_path), "w") as wav_file:
        wav_file.setnchannels(1)
        wav_file.setsampwidth(2)
        wav_file.setframerate(sample_rate)
        wav_file.writeframes(pcm.tobytes())

    return output_path
