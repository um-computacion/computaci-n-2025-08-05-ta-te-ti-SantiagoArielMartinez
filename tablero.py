class PosOcupadaException(Exception):
    ...


class Tablero:
    def __init__(self):
        self.contenedor = [
            ["", "", ""],
            ["", "", ""],
            ["", "", ""],
        ]

    def poner_la_ficha(self, fil, col, ficha):
        # ver si esta ocupado...
        if self.contenedor[fil][col] == "":
            self.contenedor[fil][col] = ficha
        else:
            raise PosOcupadaException("posición ocupada!")
        return self.contenedor
    
    def verificar_ganador(self):
                ##Ganador por fila
                for fila in self.contenedor:
                    if fila[0] == fila[1] == fila[2] != "":        
                        return True
                    
                ##Ganador por columna
                for i in self.contenedor[0]:
                        for col in range(3):                                                                 
                            if self.contenedor[0][col] == self.contenedor[1][col] == self.contenedor[2][col] != "":
                                return True 
                            
                ##Ganador por diagonal
                if self.contenedor[0][0] == self.contenedor[1][1] == self.contenedor[2][2] != "":  
                    return True
                if self.contenedor[0][2] == self.contenedor[1][1] == self.contenedor[2][0] != "":
                    return True
                
    def empate(self):
        for fila in self.contenedor:
            for col in fila:
                if col == "":
                    return False
        return True            
        
            
           
        