import unittest
from tablero import Tablero
from tateti import Tateti
from jugador import Jugador
class TestGanador(unittest.TestCase):
    def setUp(self):
        self.tablero = Tablero() 
        self.tateti = Tateti()
    def test_inicio_tablero(self):
        tablero_inicio = [
                        ["","",""],
                        ["","",""],
                        ["","",""]
                    ]
        self.assertListEqual(self.tablero.contenedor,tablero_inicio)

    def test_colocar_ficha(self):
        self.tablero.contenedor[1][1] = 'x'
        self.assertEqual(self.tablero.contenedor[1][1], "x")
        tablero = [
                        ["","",""],
                        ["","x",""],
                        ["","",""]
                    ]
        self.assertListEqual(self.tablero.contenedor,tablero)
    
    def test_ganar_columna_0(self):
        self.tablero.contenedor[0][0] = 'x'
        self.assertEqual(self.tablero.contenedor[0][0], "x")
        self.tablero.contenedor[1][0] = 'x'
        self.assertEqual(self.tablero.contenedor[1][0], "x")
        self.tablero.contenedor[2][0] = 'x'
        self.assertEqual(self.tablero.contenedor[2][0], "x")

        tablero = [
                        ["x","",""],
                        ["x","",""],
                        ["x","",""]
                    ]
        self.assertListEqual(self.tablero.contenedor,tablero)

    def test_ganar_columna_1(self):
        self.tablero.contenedor[0][1] = '0'
        self.assertEqual(self.tablero.contenedor[0][1], "0")
        self.tablero.contenedor[1][1] = '0'
        self.assertEqual(self.tablero.contenedor[1][1], "0")
        self.tablero.contenedor[2][1] = '0'
        self.assertEqual(self.tablero.contenedor[2][1], "0")

        tablero = [
                        ["","0",""],
                        ["","0",""],
                        ["","0",""]
                    ]
        self.assertListEqual(self.tablero.contenedor,tablero)

    def test_ganar_columna_2(self):
        self.tablero.contenedor[0][2] = 'x'
        self.assertEqual(self.tablero.contenedor[0][2], "x")
        self.tablero.contenedor[1][2] = 'x'
        self.assertEqual(self.tablero.contenedor[1][2], "x")
        self.tablero.contenedor[2][2] = 'x'
        self.assertEqual(self.tablero.contenedor[2][2], "x")

        tablero = [
                        ["","","x"],
                        ["","","x"],
                        ["","","x"]
                    ]
        self.assertListEqual(self.tablero.contenedor,tablero)
    
    def test_ganar_fila_0(self):
        self.tablero.contenedor[0][0] = 'x'
        self.assertEqual(self.tablero.contenedor[0][0], "x")
        self.tablero.contenedor[0][1] = 'x'
        self.assertEqual(self.tablero.contenedor[0][1], "x")
        self.tablero.contenedor[0][2] = 'x'
        self.assertEqual(self.tablero.contenedor[0][2], "x")

        tablero = [
                        ["x","x","x"],
                        ["","",""],
                        ["","",""]
                    ]
        self.assertListEqual(self.tablero.contenedor,tablero)

    def test_ganar_fila_1(self):
        self.tablero.contenedor[1][0] = 'x'
        self.assertEqual(self.tablero.contenedor[1][0], "x")
        self.tablero.contenedor[1][1] = 'x'
        self.assertEqual(self.tablero.contenedor[1][1], "x")
        self.tablero.contenedor[1][2] = 'x'
        self.assertEqual(self.tablero.contenedor[1][2], "x")

        tablero = [
                        ["","",""],
                        ["x","x","x"],
                        ["","",""]
                    ]
        self.assertListEqual(self.tablero.contenedor,tablero)

    def test_ganar_fila_2(self):
        self.tablero.contenedor[2][0] = '0'
        self.assertEqual(self.tablero.contenedor[2][0], "0")
        self.tablero.contenedor[2][1] = '0'
        self.assertEqual(self.tablero.contenedor[2][1], "0")
        self.tablero.contenedor[2][2] = '0'
        self.assertEqual(self.tablero.contenedor[2][2], "0")

        tablero = [
                        ["","",""],
                        ["","",""],
                        ["0","0","0"]
                    ]
        self.assertListEqual(self.tablero.contenedor,tablero)
    
    def test_ganar_diagonal_1(self):
        self.tablero.contenedor[0][0] = '0'
        self.assertEqual(self.tablero.contenedor[0][0], "0")
        self.tablero.contenedor[1][1] = '0'
        self.assertEqual(self.tablero.contenedor[1][1], "0")
        self.tablero.contenedor[2][2] = '0'
        self.assertEqual(self.tablero.contenedor[2][2], "0")

        tablero = [
                        ["0","",""],
                        ["","0",""],
                        ["","","0"]
                    ]
        self.assertListEqual(self.tablero.contenedor,tablero)

    def test_ganar_diagonal_2(self):
        self.tablero.contenedor[0][2] = '0'
        self.assertEqual(self.tablero.contenedor[0][2], "0")
        self.tablero.contenedor[1][1] = '0'
        self.assertEqual(self.tablero.contenedor[1][1], "0")
        self.tablero.contenedor[2][0] = '0'
        self.assertEqual(self.tablero.contenedor[2][0], "0")

        tablero = [
                        ["","","0"],
                        ["","0",""],
                        ["0","",""]
                    ]
        self.assertListEqual(self.tablero.contenedor,tablero)
    
    def test_empate(self):
        self.tablero.contenedor[0][0] = '0'
        self.assertEqual(self.tablero.contenedor[0][0], "0")
        self.tablero.contenedor[0][1] = 'x'
        self.assertEqual(self.tablero.contenedor[0][1], "x")
        self.tablero.contenedor[0][2] = '0'
        self.assertEqual(self.tablero.contenedor[0][2], "0")
        self.tablero.contenedor[1][0] = 'x'
        self.assertEqual(self.tablero.contenedor[1][0], "x")
        self.tablero.contenedor[1][1] = '0'
        self.assertEqual(self.tablero.contenedor[1][1], "0")
        self.tablero.contenedor[2][0] = 'x'
        self.assertEqual(self.tablero.contenedor[2][0], "x")
        self.tablero.contenedor[1][2] = '0'
        self.assertEqual(self.tablero.contenedor[1][2], "0")
        self.tablero.contenedor[2][2] = 'x'
        self.assertEqual(self.tablero.contenedor[2][2], "x")
        self.tablero.contenedor[2][1] = '0'
        self.assertEqual(self.tablero.contenedor[2][1], "0")
        
        tablero = [
                        ["0","x","0"],
                        ["x","0","0"],
                        ["x","0","x"]
                    ]
        self.assertListEqual(self.tablero.contenedor,tablero)
    
    def test_crear_jugador(self):
        jugador = self.tateti.crear_jugador("Santi", "Abi") 
        self.assertIsInstance(jugador, Jugador) 
        self.assertEqual(jugador.jugador_x, "Santi")
        self.assertEqual(jugador.jugador_o, "Abi")

    def test_inicializacion(self):
        self.assertEqual(self.tateti.turno, "X")

    def test_cambiar_turno(self):
        self.tateti.cambiar_turno()
        self.assertEqual(self.tateti.turno, "O")
        self.tateti.cambiar_turno()
        self.assertEqual(self.tateti.turno, "X")

    def test_obtener_turno(self):
        jugador = self.tateti.crear_jugador("Santi", "Abi")

        self.tateti.turno = "X"
        self.assertEqual(self.tateti.obtener_turno(jugador), "Santi(X)")

        self.tateti.turno = "O"
        self.assertEqual(self.tateti.obtener_turno(jugador), "Abi(O)")

if __name__ == "__main__":
    unittest.main()



        