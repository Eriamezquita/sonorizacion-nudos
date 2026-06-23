"""Estructuras de datos para representar nudos de forma simple.

Este módulo no intenta sustituir bibliotecas especializadas de teoría de nudos.
Su objetivo es dar una representación mínima y transparente para construir
primeros prototipos de sonificación.
"""

from dataclasses import dataclass, field
from typing import List, Optional


@dataclass(frozen=True)
class KnotDescriptor:
    """Descripción mínima de un nudo para sonificación.

    Attributes
    ----------
    name:
        Nombre común del nudo.
    crossing_number:
        Número de cruces de la representación usada.
    braid_word:
        Secuencia simplificada de generadores de trenza. El signo representa
        generador positivo o inverso.
    crossing_signs:
        Lista de signos de cruces: +1 o -1.
    notes:
        Notas metodológicas sobre la representación.
    """

    name: str
    crossing_number: int
    braid_word: List[int] = field(default_factory=list)
    crossing_signs: List[int] = field(default_factory=list)
    notes: Optional[str] = None

    @property
    def writhe(self) -> int:
        """Suma de signos de los cruces de la representación."""
        return sum(self.crossing_signs)

    def as_event_sequence(self) -> List[int]:
        """Devuelve la secuencia principal que se usará para sonificar.

        Si existe palabra de trenza, se usa como secuencia principal. En caso
        contrario, se usan los signos de cruce.
        """
        if self.braid_word:
            return list(self.braid_word)
        return list(self.crossing_signs)
