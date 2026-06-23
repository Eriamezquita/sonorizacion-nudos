"""Mapeos de estructuras discretas a eventos sonoros."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, List


@dataclass(frozen=True)
class SoundEvent:
    """Evento sonoro elemental."""

    frequency: float
    duration: float
    amplitude: float
    label: str = ""


def map_range(value: float, in_min: float, in_max: float, out_min: float, out_max: float) -> float:
    """Mapea linealmente un valor de un intervalo a otro.

    Si el intervalo de entrada es degenerado, se devuelve el punto medio del
    intervalo de salida para evitar división entre cero.
    """
    if in_max == in_min:
        return (out_min + out_max) / 2
    normalized = (value - in_min) / (in_max - in_min)
    return out_min + normalized * (out_max - out_min)


def sequence_to_events(
    sequence: Iterable[int],
    base_frequency: float = 220.0,
    step_ratio: float = 2 ** (2 / 12),
    base_duration: float = 0.35,
    base_amplitude: float = 0.35,
) -> List[SoundEvent]:
    """Convierte una secuencia discreta en eventos sonoros.

    Regla inicial:
    - el signo controla dirección de la altura;
    - la magnitud controla cuántos pasos se aleja de la frecuencia base;
    - el signo positivo produce un sonido más agudo;
    - el signo negativo produce un sonido más grave;
    - cero produce silencio aproximado con amplitud cero.

    Esta regla es deliberadamente simple para que pueda documentarse y
    modificarse en la bitácora.
    """
    events: List[SoundEvent] = []
    for index, value in enumerate(sequence):
        if value == 0:
            frequency = base_frequency
            amplitude = 0.0
        else:
            frequency = base_frequency * (step_ratio ** value)
            amplitude = min(0.9, base_amplitude + 0.05 * abs(value))
        duration = base_duration + 0.04 * abs(value)
        events.append(
            SoundEvent(
                frequency=float(frequency),
                duration=float(duration),
                amplitude=float(amplitude),
                label=f"evento_{index}_valor_{value}",
            )
        )
    return events
