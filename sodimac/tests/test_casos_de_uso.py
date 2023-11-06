from ..black_box.casos_de_uso import iniciar_sesion, cerrar_sesion
import pytest

def test_iniciar_sesion():
    assert iniciar_sesion() == True

def test_cerrar_sesion():
	assert cerrar_sesion() == True
