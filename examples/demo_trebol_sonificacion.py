"""Demo 01: sonificación elemental del nudo trébol.

Ejecutar desde la raíz del repositorio:

    python examples/demo_trebol_sonificacion.py

Salida:
    outputs/audio/trebol_demo.wav
    outputs/figures/trebol_eventos.png
"""

from pathlib import Path
import sys

import matplotlib.pyplot as plt

# Permite ejecutar el ejemplo sin instalar el paquete.
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.knots import trefoil_descriptor
from src.sonification import sequence_to_events, synthesize_events_to_wav


def main() -> None:
    knot = trefoil_descriptor()
    sequence = knot.as_event_sequence()
    events = sequence_to_events(sequence, base_frequency=220.0)

    audio_path = ROOT / "outputs" / "audio" / "trebol_demo.wav"
    figure_path = ROOT / "outputs" / "figures" / "trebol_eventos.png"

    synthesize_events_to_wav(events, audio_path)

    figure_path.parent.mkdir(parents=True, exist_ok=True)
    indices = list(range(1, len(events) + 1))
    frequencies = [event.frequency for event in events]
    amplitudes = [event.amplitude for event in events]

    plt.figure(figsize=(7, 4))
    plt.plot(indices, frequencies, marker="o", label="Frecuencia")
    plt.xlabel("Evento sonoro")
    plt.ylabel("Frecuencia (Hz)")
    plt.title(f"Sonificación inicial: {knot.name}")
    for i, event in zip(indices, events):
        plt.text(i, event.frequency, f"amp={event.amplitude:.2f}", fontsize=8)
    plt.tight_layout()
    plt.savefig(figure_path, dpi=160)
    plt.close()

    print(f"Nudo: {knot.name}")
    print(f"Número de cruces: {knot.crossing_number}")
    print(f"Secuencia usada: {sequence}")
    print(f"Writhe de la representación: {knot.writhe}")
    print(f"Audio generado: {audio_path}")
    print(f"Figura generada: {figure_path}")


if __name__ == "__main__":
    main()
