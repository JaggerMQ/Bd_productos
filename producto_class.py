from colorama import  Fore, init

init()

class Base_de_datos():
        
    def __init__(self, Nombre, Apellido, Cedula):
        
        self.Nombre = Nombre
        self.Apellido = Apellido
        self.Cedula = Cedula
        
    @staticmethod
    def fecha(f_actual, f_vencimiento):
    
        diferencia = (f_vencimiento-f_actual).days
        a_punto_exp = 5
    
        if diferencia >= a_punto_exp:
            return f'{Fore.GREEN}VIGENTE'
        elif 0 < diferencia < a_punto_exp:
            return f'{Fore.YELLOW}A PUNTO DE EXPIRAR'
        return f'{Fore.RED}VENCIDO'
    
    def mostrar_consulta(self):
        
        print(f'\nEl producto del cliente {self.Nombre} {self.Apellido} de la cedula {self.Cedula} esta:')