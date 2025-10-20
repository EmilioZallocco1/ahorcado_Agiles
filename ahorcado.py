class JuegoAhorcado:
    MAX_ERRORES = 6

    def __init__(self, palabra_objetivo: str = "perro"):
        self.palabra_objetivo = palabra_objetivo.lower()
        self.letras_correctas = set()
        self.letras_incorrectas = set()
        self.errores = 0

    # ---------- Estado / visualización ----------
    def estado_partida(self):
        """Devuelve 'ganaste', 'perdiste' o None si sigue en juego."""
        if all(c in self.letras_correctas for c in self.palabra_objetivo):
            return "ganaste"
        if self.errores >= self.MAX_ERRORES:
            return "perdiste"
        return None

    def mostrar_palabra(self):
        return " ".join(
            c if c in self.letras_correctas else "_"
            for c in self.palabra_objetivo
        )

    def _snapshot(self, acierto):
        """Estructura de salida unificada para todas las acciones."""
        return {
            "acierto": acierto,
            "palabra_oculta": self.mostrar_palabra(),
            "errores": self.errores,
            "letras_correctas": list(self.letras_correctas),
            "letras_incorrectas": list(self.letras_incorrectas),
        }

    # ---------- Acciones del juego ----------
    def ingresar_letra(self, letra: str):
        ch = (letra or "").lower()

        # Partida ya terminada
        if self.errores >= self.MAX_ERRORES or self.estado_partida() == "ganaste":
            return self._snapshot(None)

        # Entrada inválida (vacío o >1 char o no alfabético) cuenta como error “amable”
        if len(ch) != 1 or not ch.isalpha():
            self.errores += 1
            return self._snapshot(False)

        # Ya jugada
        if ch in self.letras_correctas or ch in self.letras_incorrectas:
            return self._snapshot(None)

        # Verificar acierto
        if ch in self.palabra_objetivo:
            self.letras_correctas.add(ch)
            return self._snapshot(True)
        else:
            self.letras_incorrectas.add(ch)
            self.errores += 1
            return self._snapshot(False)

    def ingresar_palabra(self, palabra: str):
        intento = (palabra or "").lower()

        # Partida ya terminada
        if self.errores >= self.MAX_ERRORES or self.estado_partida() == "ganaste":
            return self._snapshot(None)

        if intento == self.palabra_objetivo:
            self.letras_correctas.update(set(self.palabra_objetivo))
            snap = self._snapshot(True)
            snap["palabra_oculta"] = self.palabra_objetivo
            snap["resultado"] = "ganaste"
            return snap
        else:
            # Contamos intento fallido como 1 error
            self.errores += 1
            return self._snapshot(False)

    # ---------- Bucle mínimo para jugar por consola ----------
    def jugar_consola(self):  # pragma: no cover
        """
        Modo interactivo mínimo por consola.
        No afecta el coverage (pragma).
        """
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

        # Fin
        estado = self.estado_partida()
        print(f"\nResultado: {estado.upper()}")
        print("La palabra era:", self.palabra_objetivo)


if __name__ == "__main__":  # pragma: no cover
    JuegoAhorcado().jugar_consola()
