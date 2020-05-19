"""
Functions to perform geometric operations.
"""

import numpy as np


def perimeterCircle(r=1.):
    """Calculate the length of the perimeter of a circle.

    Parameters
    ----------
    r: float, optional (default=1.)
        Radius of the circle, r>0.

    Returns
    -------
    float
        Perimeter of the circle.

    """

    return 2. * np.pi * r


def areaCircle(r=1.):
    """Calculate the area of a circle.

    Parameters
    ----------
    r: float, optional (default=1.)
        Radius of the circle, r>0.

    Returns
    -------
    float
        Area of the circle.

    """

    return np.pi * r**2
