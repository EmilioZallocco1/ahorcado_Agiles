from pytest_bdd import scenarios, given, when, then, parsers
from ahorcado import JuegoAhorcado

scenarios("../features/ganar_con_algunos_errores.feature")

@given(parsers.cfparse('un juego nuevo con la palabra "{palabra}"'), target_fixture="juego")
def given_juego(palabra):
    j = JuegoAhorcado()
    j.palabra_objetivo = palabra.lower()
    return j

@when(parsers.cfparse('adivino las letras "{lista}"'))
def adivino_letras(juego, lista):
    for l in [x.strip() for x in lista.split(",") if x.strip()]:
        juego.ingresar_letra(l)

@then(parsers.cfparse('el estado del juego es "{esperado}"'))
def estado_esperado(juego, esperado):
    assert juego.estado_partida() == esperado

@then(parsers.cfparse('la palabra visible es "{visible}"'))
def palabra_visible(juego, visible):
    def norm(s: str) -> str:
        return "".join(s.split()).lower()
    assert norm(juego.mostrar_palabra()) == norm(visible)

@then(parsers.cfparse('la cantidad de errores es {n:d}'))
def cantidad_errores(juego, n):
    assert juego.errores == n