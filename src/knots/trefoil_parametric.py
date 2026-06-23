"""
Representación paramétrica inicial del nudo trébol.

Esta versión genera coordenadas 3D para usarlas después en visualización
o sonificación. No sustituye una representación topológica rigurosa,
pero sirve como primer puente geométrico-computacional.
"""

from __future__ import annotations

import numpy as np


def trefoil(t: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Devuelve una parametrización clásica del nudo trébol.

    Parámetros
    ----------
    t:
        Arreglo de valores entre 0 y 2*pi.

    Returns
    -------
    x, y, z:
        Coordenadas del nudo.
    """
    x = np.sin(t) + 2 * np.sin(2 * t)
    y = np.cos(t) - 2 * np.cos(2 * t)
    z = -np.sin(3 * t)
    return x, y, z


def sample_trefoil(n: int = 512) -> np.ndarray:
    """
    Muestrea el nudo trébol y devuelve un arreglo de forma (n, 3).
    """
    t = np.linspace(0, 2 * np.pi, n, endpoint=False)
    x, y, z = trefoil(t)
    return np.column_stack([x, y, z])


if __name__ == "__main__":
    pts = sample_trefoil()
    print(pts[:5])
