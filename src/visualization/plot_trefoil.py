"""
Visualización básica del nudo trébol.
"""

from __future__ import annotations

import matplotlib.pyplot as plt
from src.knots.trefoil_parametric import sample_trefoil


def main() -> None:
    pts = sample_trefoil(800)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    ax.plot(pts[:, 0], pts[:, 1], pts[:, 2])
    ax.set_title("Nudo trébol: parametrización inicial")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")
    plt.show()


if __name__ == "__main__":
    main()
