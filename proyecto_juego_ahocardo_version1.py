"""
UIDE
CURSO: Lógica de Programación
NOMBRE: Luis Agapito Perez
PROYECTO: Juego del Ahorcado
--------------------------------------
Este programa implementa el clásico juego del ahorcado usando:
- Tkinter para la interfaz gráfica
- Programación orientada a objetos
- Manejo de archivos para almacenar palabras

El juego consta de tres partes principales:
1. Menú principal (VentanaInicio)
2. Interfaz de juego (AhorcadoGUI)
3. Sistema de administración de palabras
"""

# Importaciones necesarias
import tkinter as tk        # Biblioteca principal para la interfaz gráfica
from tkinter import messagebox, ttk  # Componentes adicionales de la interfaz
import random              # Para selección aleatoria de palabras
from unicodedata import normalize    # Para manejar palabras con tildes

# Definición de constantes
INTENTOS_MAXIMOS = 6    # Número de intentos antes de perder el juego

# Estados del dibujo del ahorcado
# Cada elemento de la lista representa un estado del juego
# Se muestra estado inicial
AHORCADO = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''']  

class VentanaInicio:
    """
    Clase que maneja la ventana principal del juego.
    Muestra tres opciones principales:
    - JUGAR: Inicia una nueva partida
    - ADMINISTRAR: Permite gestionar las palabras
    - SALIR: Cierra el programa
    """
    def __init__(self):
        # Configuración de la ventana principal
        self.root = tk.Tk()
        self.root.title("Bienvenido al Juego del Ahorcado")
        #self.root.geometry("400x300")  # Tamaño inicial de la ventana
        
        # Frame principal para organizar los elementos
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0)

        # Crear un estilo personalizado para el texto en verde
        style = ttk.Style()
        style.configure("Green.TLabel", foreground="green", font=('Helvetica', 16, 'bold'))
        
        # Título del juego
        titulo = ttk.Label(main_frame, 
                          text="JUEGO DEL AHORCADO", 
                          font=('Helvetica', 16, 'bold'), 
                          style="Green.TLabel")
        titulo.grid(row=0, column=0, pady=20)
        
        # Botón de juego (sin implementación completa)
        btn_jugar = ttk.Button(main_frame, 
                              text="JUGAR",
                              command=self.iniciar_juego,
                              width=20)
        btn_jugar.grid(row=1, column=0, pady=10)

    def center_window(self):
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
        
    def iniciar_juego(self):
        """
        Método que se activará cuando el usuario presione JUGAR
        En la implementación completa:
        1. Ocultará la ventana principal
        2. Mostrará la ventana del juego
        3. Iniciará una nueva partida
        """
        print("Iniciar juego")
        pass

    def iniciar(self):
        self.center_window()
        self.root.mainloop()

class AhorcadoGUI:
    """
    Clase principal del juego que maneja:
    1. La lógica del juego
    2. La interfaz durante la partida
    3. El estado del juego
    4. La interacción con el jugador
    """
    def __init__(self, root, ventana_inicio=None):
        # Variables de control de ventanas
        self.root = root  # Ventana del juego
        self.ventana_inicio = ventana_inicio  # Referencia al menú principal
        
        # Variables del estado del juego
        self.palabra_secreta = ""          # Palabra que el jugador debe adivinar
        self.letras_adivinadas = []        # Letras correctas adivinadas
        self.intentos_restantes = INTENTOS_MAXIMOS  # Intentos disponibles
        self.letras_usadas = set()         # Conjunto de letras ya utilizadas
        
        # Variables de la interfaz (StringVar para actualización automática)
        self.palabra_var = tk.StringVar()        # Muestra la palabra con guiones y letras adivinadas
        self.letras_usadas_var = tk.StringVar()  # Muestra las letras ya intentadas
        self.intentos_var = tk.StringVar()       # Muestra intentos restantes
        self.ahorcado_var = tk.StringVar()       # Muestra el dibujo del ahorcado
        
        # Lista inicial de palabras (se expandirá en la versión completa)
        self.palabras = ["python", "programacion", "computadora"]

    def crear_interfaz(self):
        """
        Método que creará todos los elementos visuales del juego:
        - Palabra oculta con guiones
        - Campo para ingresar letras
        - Botón de intento
        - Visualización de letras usadas
        - Contador de intentos
        - Dibujo del ahorcado
        """
        pass

    def procesar_letra(self):
        """
        Método que procesará cada intento del jugador:
        1. Validará la letra ingresada
        2. Verificará si ya fue usada
        3. Actualizará la palabra si la letra es correcta
        4. Reducirá intentos si la letra es incorrecta
        5. Verificará victoria o derrota
        """
        pass

    def actualizar_interfaz(self):
        """
        Método que actualizará todos los elementos visuales:
        - Palabra con letras adivinadas
        - Lista de letras usadas
        - Número de intentos restantes
        - Estado del dibujo del ahorcado
        """
        pass

# Punto de entrada del programa
if __name__ == "__main__":
    app = VentanaInicio()
    app.root.mainloop()