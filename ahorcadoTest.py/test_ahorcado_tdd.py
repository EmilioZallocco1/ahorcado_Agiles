# tests/test_ahorcado_tdd.py
from ahorcado import JuegoAhorcado as AhorcadoGame

def test_IngresaLetraYAcierta():
    g = AhorcadoGame()
    snap = g.ingresar_letra("p")

    assert snap["acierto"] is True
    assert snap["errores"] == 0
    assert "p" in snap["letras_correctas"]



def test_IngresaLetraYNoAcierta():
    g = AhorcadoGame()
    snap = g.ingresar_letra("z")

    assert snap["acierto"] is False
    assert snap["errores"] == 1
    assert "z" in snap["letras_incorrectas"]
    assert "z" not in snap["letras_correctas"]



def test_IngresaLetraYSeRepite():
    g = AhorcadoGame()

    snap1 = g.ingresar_letra("p")
    assert snap1["acierto"] is True
    assert snap1["errores"] == 0
    assert "p" in snap1["letras_correctas"]

    snap2 = g.ingresar_letra("p")
    assert snap2["acierto"] is None         
    assert snap2["errores"] == 0             
    assert "p" in snap2["letras_correctas"]  



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


def test_IngresaPalabraYNoAcierta():
    g = AhorcadoGame()
    snap = g.ingresar_palabra("perra")
    assert snap["acierto"] is False
    assert snap["errores"] == 1

def test_IngresaPalabraVacia():
    g = AhorcadoGame()
    snap = g.ingresar_palabra("")
    assert snap["acierto"] is False
    assert snap["errores"] == 1


def test_VisualizarAcierto():
    g = AhorcadoGame()
    snap = g.ingresar_letra("r")  # aparece dos veces en "perro"

    assert snap["acierto"] is True
    assert snap["palabra_oculta"] == "_ _ r r _"
    assert "r" in snap["letras_correctas"]
    assert snap["errores"] == 0
    assert g.mostrar_palabra() == "_ _ r r _"
