import random
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from ahorcado import JuegoAhorcado

app = FastAPI(title="API del Ahorcado")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

juego = None


@app.post("/nueva_partida")
def nueva_partida(palabra: str = "perro"):
    global juego
    juego = JuegoAhorcado(palabra)
    return {
        "palabra_oculta": juego.mostrar_palabra(),
        "errores": juego.errores,
        "letras_correctas": list(juego.letras_correctas),
        "letras_incorrectas": list(juego.letras_incorrectas),
        "estado": juego.estado_partida(),
    }


@app.post("/letra")
def jugar_letra(letra: str = Query(..., min_length=1, max_length=1)):
    if not juego:
        return {"error": "No hay partida activa."}
    snap = juego.ingresar_letra(letra)
    snap["estado"] = juego.estado_partida()
    return snap


@app.get("/palabra")
def obtener_palabra():
    palabra = random.choice(["perro", "gato", "jirafa"])
    return {"palabra": palabra}


@app.get("/estado")
def obtener_estado():
    if not juego:
        return {"error": "No hay partida activa."}
    data = {
        "palabra_oculta": juego.mostrar_palabra(),
        "errores": juego.errores,
        "letras_correctas": list(juego.letras_correctas),
        "letras_incorrectas": list(juego.letras_incorrectas),
        "estado": juego.estado_partida(),
    }
    if juego.estado_partida() == "perdiste":
        data["palabra_real"] = juego.palabra_objetivo
    return data

@app.get("/api/debug-palabra")
def debug_palabra():
    if juego:
        return {"palabra": juego.palabra_objetivo}
    return {"palabra": None}