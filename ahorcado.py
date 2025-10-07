class JuegoAhorcado:
    def __init__(self):
        self.palabra_objetivo = "perro"
        self.letras_correctas = set()
        self.letras_incorrectas = set()
        self.errores = 0

    def estado_partida(self):
        if all(c in self.letras_correctas for c in self.palabra_objetivo):
            return "ganaste"
        if self.errores >= 6:   # o el número de errores que define la derrota
            return "perdiste"


    def ingresar_letra(self, letra: str):
        ch = letra.lower()


        if self.errores >= 6:
            return {
                "acierto": None,
                "palabra_oculta": self.mostrar_palabra(),
                "errores": self.errores,
                "letras_correctas": list(self.letras_correctas),
                "letras_incorrectas": list(self.letras_incorrectas),
            }

        if ch in self.letras_correctas or ch in self.letras_incorrectas:
            return {
                "acierto": None,
                "palabra_oculta": self.mostrar_palabra(),  # ← agregado
                "errores": self.errores,
                "letras_correctas": list(self.letras_correctas),
                "letras_incorrectas": list(self.letras_incorrectas),
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
            "palabra_oculta": self.mostrar_palabra(),      # ← agregado
            "errores": self.errores,
            "letras_correctas": list(self.letras_correctas),
            "letras_incorrectas": list(self.letras_incorrectas),
        }

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
            }

    def mostrar_palabra(self):
        return " ".join(c if c in self.letras_correctas else "_" for c in self.palabra_objetivo)
#