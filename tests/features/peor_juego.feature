Feature: El peor juego
  Scenario: El peor juego
    Given un juego nuevo con la palabra "perro"
    When adivino las letras "a,b,c,d,f,g"
    Then el estado del juego es "perdiste"
    And la palabra visible es "_ _ _ _ _"
    And la cantidad de errores es 6
