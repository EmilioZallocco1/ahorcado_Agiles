class JuegoAhorcado:
    def __init__(self):
        self.palabra_objetivo = "perro"
        self.letras_correctas = set()
        self.letras_incorrectas = set()
        self.errores = 0

    def ingresar_letra(self, letra: str):
        ch = letra.lower()

        # 🔹 NUEVO: si la letra ya fue probada, no cambia nada
        if ch in self.letras_correctas or ch in self.letras_incorrectas:
            return {
                "acierto": None,  # ni acierto ni error
                "palabra_oculta": self.mostrar_palabra(),
                "errores": self.errores,
                "letras_correctas": list(self.letras_correctas),
                "letras_incorrectas": list(self.letras_incorrectas),
                "resultado": self.estado_partida()
            }

        if ch in self.palabra_objetivo:
            self.letras_correctas.add(ch)
            acierto = True
        else:
            self.letras_incorrectas.add(ch)
            self.errores += 1
            acierto = False

        return {
            "acierto": acierto,
            "palabra_oculta": self.mostrar_palabra(),
            "errores": self.errores,
            "letras_correctas": list(self.letras_correctas),
            "letras_incorrectas": list(self.letras_incorrectas),
            "resultado": self.estado_partida()
        }

    def mostrar_palabra(self):
        return " ".join(c if c in self.letras_correctas else "_" for c in self.palabra_objetivo)


    def ingresar_palabra(self, palabra: str):
        intento = palabra.lower()
        if intento == self.palabra_objetivo:
            self.letras_correctas.update(set(self.palabra_objetivo))
            return {
                "acierto": True,
                "palabra_oculta": self.palabra_objetivo,
                "errores": self.errores,
                "letras_correctas": list(self.letras_correctas),
                "letras_incorrectas": list(self.letras_incorrectas),
                "resultado": "ganaste"
            }
        else:
            self.errores += 1
            return {
                "acierto": False,
                "palabra_oculta": self.mostrar_palabra(),
                "errores": self.errores,
                "letras_correctas": list(self.letras_correctas),
                "letras_incorrectas": list(self.letras_incorrectas),
                "resultado": self.estado_partida()
            }
        
    def estado_partida(self):
        if all(c in self.letras_correctas for c in self.palabra_objetivo):
            return "ganaste"
        if self.errores >= 6:
            return "perdiste"
        return "en progreso"

if __name__ == "__main__":
    juego = JuegoAhorcado()
    print("Palabra oculta:", juego.mostrar_palabra())

    print("\nIntentando 'p'")
    print(juego.ingresar_letra("p"))

    print("\nIntentando 'z'")
    print(juego.ingresar_letra("z"))

    
    print("\nIntentando 'p'")
    print(juego.ingresar_letra("p"))

    print("\nEstado final:")
    print("Palabra:", juego.mostrar_palabra())
    print("Errores:", juego.errores)
    print("Resultado:", juego.estado_partida())
