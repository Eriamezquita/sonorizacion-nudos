"""
Mapeos iniciales de propiedades de nudos a parámetros musicales.

Este archivo debe crecer gradualmente. Por ahora contiene funciones simples
para convertir signos de cruces en notas MIDI y duraciones.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class MusicalEvent:
    """Evento musical mínimo."""
    pitch: int
    duration: float
    velocity: int = 80


def crossing_sign_to_pitch(sign: int, base_pitch: int = 60, interval: int = 7) -> int:
    """
    Convierte el signo de un cruce en altura MIDI.

    sign > 0: sube desde la nota base.
    sign < 0: baja desde la nota base.
    sign = 0: conserva la nota base.
    """
    if sign > 0:
        return base_pitch + interval
    if sign < 0:
        return base_pitch - interval
    return base_pitch


def crossings_to_events(crossings: list[int], base_pitch: int = 60) -> list[MusicalEvent]:
    """
    Convierte una lista de signos de cruces en eventos musicales.
    """
    events: list[MusicalEvent] = []
    for i, sign in enumerate(crossings):
        pitch = crossing_sign_to_pitch(sign, base_pitch=base_pitch + i * 2)
        duration = 0.5 if sign >= 0 else 0.75
        velocity = 90 if sign > 0 else 65
        events.append(MusicalEvent(pitch=pitch, duration=duration, velocity=velocity))
    return events


if __name__ == "__main__":
    trefoil_crossings = [1, 1, 1]
    for event in crossings_to_events(trefoil_crossings):
        print(event)
