# tests/test_ahorcado_tdd.py
from ahorcado import JuegoAhorcado as AhorcadoGame

def test_IngresaLetraYAcierta():
    g = AhorcadoGame()
    snap = g.ingresar_letra("p")

    assert snap["acierto"] is True
    assert snap["errores"] == 0
    assert snap["palabra_oculta"].split()[0] == "p"
    assert "p" in snap["letras_correctas"]
    assert g.estado_partida() == "en progreso"
