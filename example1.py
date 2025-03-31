# Leer x cantidad de edad y calcular la media

class Edad:
    def __init__(self, edades): # Constructor de la clase
        self.edades = edades # Atributo de la clase

    def calcular_media(self): # Método para calcular la media de las edades 
        return sum(self.edades) / len(self.edades) # Retorna la media de las edades
    
    def mostar_media(self):
        media = self.calcular_media()
        return f"La media de las edades es: {media:.2f}" # Retorna un mensaje con la media de las edades
    
def main():
    edades = [] # Lista para almacenar las edades
        
    while True:
        try:
            edad = int(input("Ingrese una edad (o -1 para terminar): "))
            if edad == -1:
                break
            edades.append(edad)
        except ValueError:
            print("Error: Ingrese un número entero válido.")
        
    if( not edades):
        print("No se ingresaron edades.")
        return
    else:
        edades_obj = Edad(edades) # Crea un objeto de la clase Edades
        print(edades_obj.mostar_media()) # Muestra la media de las edades
    
if __name__ == "__main__":
    main() # Llama a la función main cuando se ejecuta el script