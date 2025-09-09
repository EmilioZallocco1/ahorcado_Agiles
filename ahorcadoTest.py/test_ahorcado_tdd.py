# tests/test_ahorcado_tdd.py
import pytest
from ahorcado import JuegoAhorcado as AhorcadoGame

def test_IngresaLetraYAcierta():
    """
    Caso: el jugador ingresa la letra 'p' y acierta, porque la palabra fija es 'perro'.
    Debe mostrar la letra descubierta, no sumar errores y marcar hit=True.
    """
    g = AhorcadoGame()             # palabra objetivo fija: "perro"
    snap = g.ingresar_letra("p")

    assert snap["hit"] is True
    assert snap["errors"] == 0
    assert snap["masked_word"].split()[0] == "p"
    assert "p" in snap["correct_letters"]
    assert g.result() == "in_progress"
