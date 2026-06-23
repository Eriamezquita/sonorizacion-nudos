"""Nudo trébol: primer objeto de prueba.

El nudo trébol puede verse como el cierre de la trenza sigma_1^3. Aquí se usa
una representación discreta mínima para construir un primer ejemplo sonoro.
"""

from .representations import KnotDescriptor


def trefoil_descriptor() -> KnotDescriptor:
    """Devuelve una descripción simple del nudo trébol.

    La palabra [1, 1, 1] representa el cierre de sigma_1^3 de forma conceptual.
    Esta descripción es suficiente para el primer prototipo de sonificación,
    aunque en etapas posteriores debe conectarse con representaciones formales
    PD/BR o con datos calculados por herramientas especializadas.
    """
    return KnotDescriptor(
        name="Nudo trébol",
        crossing_number=3,
        braid_word=[1, 1, 1],
        crossing_signs=[1, 1, 1],
        notes="Primer prototipo: cierre de la trenza sigma_1^3.",
    )
