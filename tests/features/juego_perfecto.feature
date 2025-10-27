Feature: El Juego Perfecto
  # Ganar sin cometer errores

  Scenario: El juego Perfecto
    Given un juego nuevo con la palabra "perro"
    When adivino las letras "p,e,r,o"
    Then el estado del juego es "ganaste"
    And la palabra visible es "perro"
    And la cantidad de errores es 0
