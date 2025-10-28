Feature: Pierdo con algunos errores
  Scenario: Fallo varias letras y alcanzo el límite de errores sin completar la palabra
    Given un juego nuevo con la palabra "perro"
    When adivino las letras "p,x,r,a,b,c,d,f"
    Then el estado del juego es "perdiste"
    And la palabra visible es "p_rr_"
    And la cantidad de errores es 6
