import random

class JuegoAhorcado:
    MAX_ERRORES = 6
    PALABRAS = ["perro", "gato", "casa", "flor"]

    def __init__(self, palabra_objetivo: str = None):
        # Si no se pasa palabra, se elige una al azar
        self.palabra_objetivo = (palabra_objetivo or random.choice(self.PALABRAS)).lower()
        self.letras_correctas = set()
        self.letras_incorrectas = set()
        self.errores = 0

    def estado_partida(self):
        if all(c in self.letras_correctas for c in self.palabra_objetivo):
            return "ganaste"
        if self.errores == self.MAX_ERRORES:
            return "perdiste"
        return None

    def mostrar_palabra(self):
        return " ".join(
            c if c in self.letras_correctas else "_"
            for c in self.palabra_objetivo
        )

    def _snapshot(self, acierto):
        return {
            "acierto": acierto,
            "palabra_oculta": self.mostrar_palabra(),
            "errores": self.errores,
            "letras_correctas": list(self.letras_correctas),
            "letras_incorrectas": list(self.letras_incorrectas),
        }

    def ingresar_letra(self, letra: str):
        ch = (letra or "").lower()

        if self.errores >= self.MAX_ERRORES or self.estado_partida() == "ganaste":
            return self._snapshot(None)

        if len(ch) != 1 or not ch.isalpha():
            self.errores += 1
            return self._snapshot(False)

        if ch in self.letras_correctas or ch in self.letras_incorrectas:
            return self._snapshot(None)

        if ch in self.palabra_objetivo:
            self.letras_correctas.add(ch)
            return self._snapshot(True)
        else:
            self.letras_incorrectas.add(ch)
            self.errores += 1
            return self._snapshot(False)

    def ingresar_palabra(self, palabra: str):
        intento = (palabra or "").lower()

        if self.errores >= self.MAX_ERRORES or self.estado_partida() == "ganaste":
            return self._snapshot(None)

        if intento == self.palabra_objetivo:
            self.letras_correctas.update(set(self.palabra_objetivo))
            snap = self._snapshot(True)
            snap["palabra_oculta"] = self.palabra_objetivo
            snap["resultado"] = "ganaste"
            return snap
        else:
            self.errores += 1
            return self._snapshot(False)

    def jugar_consola(self):  

        print(" Ahorcado — adiviná la palabra")
        print("Pistas:", "_ " * len(self.palabra_objetivo))
        while self.estado_partida() is None:
            print(f"\nPalabra: {self.mostrar_palabra()}    Errores: {self.errores}/{self.MAX_ERRORES}")
            jugada = input("Ingresá una letra o arriesgá la palabra completa: ").strip()

            if len(jugada) == 1:
                snap = self.ingresar_letra(jugada)
            else:
                snap = self.ingresar_palabra(jugada)

            if snap["acierto"] is True:
                print("¡Acierto!")
            elif snap["acierto"] is False:
                print(" Error.")
            else:
                print("Jugada repetida o partida finalizada.")

        estado = self.estado_partida()
        print(f"\nResultado: {estado.upper()}")
        print("La palabra era:", self.palabra_objetivo)


if __name__ == "__main__": 
    JuegoAhorcado().jugar_consola()
