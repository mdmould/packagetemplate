import pytest
import numpy as np
import packagetemplate.arithmetic
import packagetemplate.geometry


def test_add():
    """Test packagetemplate.arithmetic.add function."""

    c = packagetemplate.arithmetic.add(1., 1.)
    assert c == 2.


def test_multiply():
    """Test packagetemplate.arithmetic.multiply function."""

    c = packagetemplate.arithmetic.multiply(1., 1.)
    assert c == 1.


def test_perimeterCircle():
    """Test packagetemplate.geometry.perimeterCircle function."""

    perim = packagetemplate.geometry.perimeterCircle(1.)
    assert perim == 2. * np.pi


def test_areaCircle():
    """Test packagetemplate.arithmetic.areaCircle functions."""

    area = packagetemplate.geometry.areaCircle(1.)
    assert area == np.pi
