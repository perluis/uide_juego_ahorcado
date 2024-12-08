"""
UIDE
CURSO: Lógica de Programación
NOMBRE: Luis Agapito Perez
PROYECTO: Juego del Ahorcado (Avance 75%)
--------------------------------------
"""

import tkinter as tk
from tkinter import messagebox, ttk
import json
import random
from unicodedata import normalize

# Definición de constantes
INTENTOS_MAXIMOS = 6

# Estados del dibujo del ahorcado completos
AHORCADO = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

class VentanaInicio:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Bienvenido al Juego del Ahorcado")
        
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0)

        # Estilo del título
        style = ttk.Style()
        style.configure("Green.TLabel", foreground="green", font=('Helvetica', 16, 'bold'))
        
        # Título
        titulo = ttk.Label(main_frame, 
                          text="JUEGO DEL AHORCADO", 
                          style="Green.TLabel")
        titulo.grid(row=0, column=0, pady=20)
        
        # Botones del menú
        btn_jugar = ttk.Button(main_frame, 
                              text="JUGAR",
                              command=self.iniciar_juego,
                              width=20)
        btn_jugar.grid(row=1, column=0, pady=10)
        
        btn_admin = ttk.Button(main_frame, 
                              text="ADMINISTRAR",
                              command=self.administrar,
                              width=20)
        btn_admin.grid(row=2, column=0, pady=10)
        
        btn_salir = ttk.Button(main_frame, 
                              text="SALIR",
                              command=self.root.quit,
                              width=20)
        btn_salir.grid(row=3, column=0, pady=10)

    def center_window(self):
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')

    def iniciar_juego(self):
        self.root.withdraw()
        game_window = tk.Toplevel()
        game_window.geometry("800x600")
        game_window.title("Juego del Ahorcado")
        app = AhorcadoGUI(game_window, self)
        app.crear_interfaz()
        game_window.protocol("WM_DELETE_WINDOW", lambda: self.cerrar_juego(game_window))

    def administrar(self):
        self.root.withdraw()
        admin_window = tk.Toplevel()
        admin_window.title("Administración de Palabras")
        admin_window.geometry("400x500")
        app = AhorcadoGUI(admin_window, self)
        app.mostrar_admin()

    def cerrar_juego(self, game_window):
        game_window.destroy()
        self.root.deiconify()

    def iniciar(self):
        self.center_window()
        self.root.mainloop()

class AhorcadoGUI:
    def __init__(self, root, ventana_inicio=None):
        self.root = root
        self.ventana_inicio = ventana_inicio
        self.palabra_secreta = ""
        self.letras_adivinadas = []
        self.intentos_restantes = INTENTOS_MAXIMOS
        self.letras_usadas = set()
        
        self.palabra_var = tk.StringVar()
        self.letras_usadas_var = tk.StringVar()
        self.intentos_var = tk.StringVar()
        self.ahorcado_var = tk.StringVar()
        
        self.palabras = self.cargar_palabras()

    def crear_interfaz(self):
        self.main_frame = ttk.Frame(self.root, padding="10")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Palabra oculta
        ttk.Label(self.main_frame, 
                 textvariable=self.palabra_var,
                 font=('Courier', 24)).grid(row=0, column=0, columnspan=2, pady=20)
        
        # Entrada de letra
        ttk.Label(self.main_frame, text="Ingresa una letra:").grid(row=1, column=0, pady=10)
        self.letra_entry = ttk.Entry(self.main_frame, width=5)
        self.letra_entry.grid(row=1, column=1, pady=10)
        self.letra_entry.bind('<Return>', lambda e: self.procesar_letra())
        
        # Botón intentar
        ttk.Button(self.main_frame,
                  text="Intentar",
                  command=self.procesar_letra).grid(row=2, column=0, columnspan=2, pady=10)
        
        # Letras usadas
        ttk.Label(self.main_frame, text="Letras usadas:").grid(row=3, column=0, pady=10)
        ttk.Label(self.main_frame, textvariable=self.letras_usadas_var).grid(row=3, column=1, pady=10)
        
        # Intentos restantes
        ttk.Label(self.main_frame, textvariable=self.intentos_var).grid(row=4, column=0, columnspan=2, pady=10)
        
        # Dibujo del ahorcado
        ttk.Label(self.main_frame,
                 textvariable=self.ahorcado_var,
                 font=('Courier', 14)).grid(row=5, column=0, columnspan=2, pady=10)
                 
        self.iniciar_juego()

    def cargar_palabras(self):
        try:
            with open('palabras.json', 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            return ["python", "programacion", "computadora"]

    def guardar_palabras(self):
        with open('palabras.json', 'w', encoding='utf-8') as f:
            json.dump(self.palabras, f, ensure_ascii=False)

    def mostrar_admin(self):
        # Frame principal para administración
        admin_frame = ttk.Frame(self.root, padding="10")
        admin_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Lista de palabras
        self.palabra_listbox = tk.Listbox(admin_frame, width=40, height=15)
        self.palabra_listbox.grid(row=0, column=0, columnspan=2, pady=10)
        
        for palabra in self.palabras:
            self.palabra_listbox.insert(tk.END, palabra)
        
        # Botones de administración
        ttk.Button(admin_frame,
                  text="Volver al Menú",
                  command=self.volver_menu).grid(row=1, column=0, columnspan=2, pady=20)

    def volver_menu(self):
        if self.ventana_inicio:
            self.root.destroy()
            self.ventana_inicio.root.deiconify()

    def iniciar_juego(self):
        if not self.palabras:
            messagebox.showerror("Error", "No hay palabras disponibles")
            return
        
        self.palabra_secreta = random.choice(self.palabras)
        self.letras_adivinadas = ["_"] * len(self.palabra_secreta)
        self.intentos_restantes = INTENTOS_MAXIMOS
        self.letras_usadas = set()
        self.actualizar_interfaz()
        self.letra_entry.focus()

    def procesar_letra(self):
        letra = normalize('NFKD', self.letra_entry.get().lower().strip())
        self.letra_entry.delete(0, tk.END)
        
        if not letra or len(letra) != 1 or not letra.isalpha():
            messagebox.showwarning("Error", "Por favor ingresa una sola letra.")
            return
        
        if letra in self.letras_usadas:
            messagebox.showinfo("Aviso", "Ya usaste esa letra.")
            return
        
        self.letras_usadas.add(letra)
        
        if letra in self.palabra_secreta:
            for i in range(len(self.palabra_secreta)):
                if self.palabra_secreta[i] == letra:
                    self.letras_adivinadas[i] = letra
            messagebox.showinfo("¡Bien!", "¡La letra está en la palabra!")
        else:
            self.intentos_restantes -= 1
            messagebox.showinfo("¡Oh no!", "La letra no está en la palabra")
        
        self.actualizar_interfaz()
        self.verificar_juego()
        self.letra_entry.focus()

    def actualizar_interfaz(self):
        self.palabra_var.set(" ".join(self.letras_adivinadas))
        self.letras_usadas_var.set(" ".join(sorted(self.letras_usadas)))
        self.intentos_var.set(f"Intentos restantes: {self.intentos_restantes}")
        self.ahorcado_var.set(AHORCADO[6 - self.intentos_restantes])

    def verificar_juego(self):
        if "_" not in self.letras_adivinadas:
            messagebox.showinfo("¡Felicitaciones!", "¡Ganaste!")
            if messagebox.askyesno("Nuevo Juego", "¿Quieres jugar otra vez?"):
                self.iniciar_juego()
            else:
                self.volver_menu()
        elif self.intentos_restantes == 0:
            messagebox.showinfo("Game Over", "¡Perdiste!")
            if messagebox.askyesno("Nuevo Juego", "¿Quieres intentar otra vez?"):
                self.iniciar_juego()
            else:
                self.volver_menu()

if __name__ == "__main__":
    app = VentanaInicio()
    app.iniciar()