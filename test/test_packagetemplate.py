import pytest
import numpy as np
import packagetemplate


def test_add():
    """Test awesomepackage.arithmetic.add function."""

    c = awesomepackage.arithmetic.add(1., 1.)
    assert c == 2.


def test_multiply():
    """Test awesomepackage.arithmetic.multiply function."""

    c = awesomepackage.arithmetic.multiply(1., 1.)
    assert c == 1.


def test_perimeterCircle():
    """Test awesomepackage.geometry.perimeterCircle function."""

    perim = awesomepackage.geometry.perimeterCircle(1.)
    assert perim == 2. * np.pi


def test_areaCircle():
    """Test awesomepackage.arithmetic.areaCircle functions."""

    area = awesomepackage.geometry.areaCircle(1.)
    assert area == np.pi
