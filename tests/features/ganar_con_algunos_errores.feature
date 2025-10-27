Feature: Ganar con algunos errores
  Scenario: Ganar luego de fallar algunas letras
    Given un juego nuevo con la palabra "perro"
    When adivino las letras "a,b,p,r,x,e,o"
    Then el estado del juego es "ganaste"
    And la palabra visible es "perro"
    And la cantidad de errores es 3