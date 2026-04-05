import pytest
from unittest.mock import patch, MagicMock
import numpy as np


@pytest.fixture
def imagen_array():
    """Array numpy simulando una imagen RGB 100x100."""
    return np.ones((100, 100, 3), dtype=np.uint8) * 255


@pytest.fixture
def lector():
    from nucleo.lector import LectorImagen
    return LectorImagen()


@pytest.fixture
def operaciones():
    from nucleo.operaciones import Operaciones
    return Operaciones()
