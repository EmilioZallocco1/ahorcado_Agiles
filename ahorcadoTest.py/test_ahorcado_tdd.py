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


def test_IngresaLetraYNoAcierta():
    g = AhorcadoGame()
    snap = g.ingresar_letra("z")

    assert snap["acierto"] is False
    assert snap["errores"] == 1
    assert "z" in snap["letras_incorrectas"]
    assert "z" not in snap["letras_correctas"]
    assert g.estado_partida() == "en progreso"


def test_IngresaLetraYSeRepite():
    g = AhorcadoGame()

    # primer intento: acierta
    snap1 = g.ingresar_letra("p")
    assert snap1["acierto"] is True
    assert snap1["errores"] == 0
    assert "p" in snap1["letras_correctas"]

    # segundo intento: misma letra -> no cambia estado ni suma error
    snap2 = g.ingresar_letra("p")
    assert snap2["acierto"] is None          # repetida: ni acierto ni error
    assert snap2["errores"] == 0             # no suma
    assert "p" in snap2["letras_correctas"]  # sigue marcada
    assert g.estado_partida() == "en progreso"


def test_ingresaPalabraYAcierta():
    g = AhorcadoGame()
    snap = g.ingresar_palabra("perro")

    assert snap["acierto"] is True
    assert snap["errores"] == 0
    assert snap["palabra_oculta"] == "perro"
    assert "p" in snap["letras_correctas"]
    assert "e" in snap["letras_correctas"]
    assert "r" in snap["letras_correctas"]
    assert "o" in snap["letras_correctas"]
    assert g.estado_partida() == "ganaste"

def test_IngresaPalabraYNoAcierta():
    g = AhorcadoGame()
    snap = g.ingresar_palabra("perra")

    assert snap["acierto"] is False
    assert snap["errores"] == 1
    assert g.estado_partida() == "en progreso"
