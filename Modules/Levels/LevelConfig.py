from Modules.Values.Assets import *
from Modules.Values.EColors import *
from Modules.Characters.Hero import *

import pygame as py

class LevelConfig:
    
    def __init__(self, size):
        """
        Brief: Inicializa un objeto de la clase LevelConfig.

        Descripción:
            Este método inicializa un objeto de la clase LevelConfig, que representa el juego.
            Configura la pantalla, el tiempo máximo, el tiempo inicial y otras propiedades del juego.

        Parámetros:
            - size (tuple): Una tupla que especifica el tamaño de la pantalla.

        Retorno:
            Ninguno
        """
        py.mixer.init()

        self.complete = False
        self.pause = False
        self.size = size
        self.screen = py.display.set_mode(self.size)
        self.running = True
        self.DEBUG = False
        self.set_fps(25)
        self.clock = py.time.Clock()
        self.set_caption("Juego Segundo Parcial")
        self.set_icon(GAME_ICON)
        self.max_time = 180000
        self.start_time = py.time.get_ticks()
        self.time_remaining = 180
        
        

    def update(self, list_events):
        """
        Brief: Actualiza el estado del juego.

        Descripción:
            Este método actualiza el estado del juego, gestionando eventos de teclado como la tecla TAB,
            obteniendo teclas presionadas, y llenando la pantalla.

        Parámetros:
            - list_events (list): Lista de eventos que afectan el estado del juego.

        Retorno:
            Ninguno
        """
        for event in list_events:
            if event.type == py.KEYDOWN:
                if event.key == py.K_TAB:
                    self.change_mode()
        self.get_pressed()
        self.fill_screen()
        

    def draw_hitbox(self):
        """
        Brief: Dibuja las cajas de colisión en el juego.

        Descripción:
            Este método dibuja las cajas de colisión de los elementos en el juego,
            incluyendo plataformas, héroe, trampas, objetos, enemigos, objetos que caen y proyectiles.

        Parámetros:
            Ninguno

        Retorno:
            Ninguno
        """
        if self.get_mode():

            for pl in self.platforms:
                for key in pl.rect:
                    py.draw.rect(self.screen, EColors.RED.value, pl.rect[key], 3)

            for key in self.hero.rect:
                    py.draw.rect(self.screen, EColors.GREEN.value, self.hero.rect[key], 3)
            
            for trap in self.traps:
                for key in trap.rect:
                    py.draw.rect(self.screen, EColors.DARK_ORANGE.value, trap.rect[key], 3)
            
            for item in self.items:
                for key in item.rect:
                    py.draw.rect(self.screen, EColors.DARK_VIOLET.value, item.rect[key], 3)
            
            for enemy in self.enemys:
                for key in enemy.rect:
                    py.draw.rect(self.screen, EColors.LIGHT_CYAN.value, enemy.rect[key], 3)

            for fo in self.falling_objects:
                for key in fo.rect:
                    py.draw.rect(self.screen, EColors.PINK.value, fo.rect[key], 3)
            
            for projectile in self.hero.list_projectile:
                for key in projectile.rect:
                    py.draw.rect(self.screen, EColors.YELLOW.value, projectile.rect[key], 3)



        
    def get_pressed(self):
        """
        Brief: Obtiene las teclas presionadas.

        Descripción:
            Este método actualiza la lista de teclas presionadas en el juego.

        Parámetros:
            Ninguno

        Retorno:
            Ninguno
        """
        self.pressed_keys = py.key.get_pressed()  
    
    def show_score(self, text):
        """
        Brief: Muestra la puntuación en la pantalla del juego.

        Descripción:
            Este método muestra la puntuación en la pantalla del juego utilizando una fuente y color específicos.

        Parámetros:
            - text (str): Texto que representa la puntuación a mostrar.

        Retorno:
            Ninguno
        """
        font = py.font.SysFont('Arial Black', 25, True)
        text = font.render(f"score: {text}", True, EColors.WHITE.value)
        self.screen.blit(text, (self.screen.get_width() - 200, self.screen.get_height() - 490))
  
    def set_caption(self, caption):
        """
        Brief: Establece el título de la ventana del juego.

        Descripción:
            Este método establece el título de la ventana del juego.

        Parámetros:
            - caption (str): Texto que representa el título de la ventana.

        Retorno:
            Ninguno
        """
        py.display.set_caption(caption)

    def set_icon(self, icon):
        """
        Brief: Establece el ícono de la ventana del juego.

        Descripción:
            Este método establece el ícono de la ventana del juego.

        Parámetros:
            - icon (str): Ruta del archivo de imagen que se utilizará como ícono.

        Retorno:
            Ninguno
        """
        self.icon_image = py.image.load(icon)
        py.display.set_icon(self.icon_image)

    def set_fps(self, FPS):
        """
        Brief: Establece la tasa de cuadros por segundo (FPS) del juego.

        Descripción:
            Este método establece la tasa de cuadros por segundo (FPS) del juego.

        Parámetros:
            - FPS (int): Número de cuadros por segundo que se establecerá.

        Retorno:
            Ninguno
        """
        self.FPS = FPS

    def set_music(self, music):
        """
        Brief: Establece la música de fondo del juego.

        Descripción:
            Este método establece la música de fondo del juego, configura el volumen y la reproduce.

        Parámetros:
            - music (str): Ruta del archivo de sonido que se utilizará como música de fondo.

        Retorno:
            Ninguno
        """
        self.music = py.mixer.Sound(music)
        self.music.set_volume(0.1)
        self.play_music()
        
    def set_volume(self, volume):
        """
        Brief: Establece el volumen de la música de fondo.

        Descripción:
            Este método establece el volumen de la música de fondo del juego.

        Parámetros:
            - volume (float): Valor que representa el volumen.

        Retorno:
            Ninguno
        """
        self.music.set_volume(volume)

    def play_music(self):
        """
        Brief: Reproduce la música de fondo.

        Descripción:
            Este método reproduce la música de fondo del juego.

        Parámetros:
            Ninguno

        Retorno:
            Ninguno
        """
        self.music.play(-1)

    def stop_music(self):
        """
        Brief: Detiene la reproducción de la música de fondo.

        Descripción:
            Este método detiene la reproducción de la música de fondo del juego.

        Parámetros:
            Ninguno

        Retorno:
            Ninguno
        """
        self.music.stop()

    def set_background_image(self, background):
        """
        Brief: Establece la imagen de fondo del juego.

        Descripción:
            Este método establece la imagen de fondo del juego y la escala según el tamaño de la pantalla.

        Parámetros:
            - background (str): Ruta del archivo de imagen que se utilizará como fondo.

        Retorno:
            Ninguno
        """
        self.background_image = py.image.load(background)
        self.background_image = py.transform.scale(self.background_image, self.size)

    def fill_screen(self, color=None):
        """
        Brief: Llena la pantalla del juego.

        Descripción:
            Este método llena la pantalla del juego con un color específico o una imagen de fondo.

        Parámetros:
            - color (tuple, optional): Tuple que representa el color en formato RGB. Si es None, utiliza la imagen de fondo.

        Retorno:
            Ninguno
        """
        if color != None:
            self.screen.fill(color)
        else:
            self.screen.blit(self.background_image, (0, 0))
    
    def change_mode(self):
        """
        Brief: Cambia el modo de depuración del juego.

        Descripción:
            Este método cambia el modo de depuración del juego, activándolo si estaba desactivado y viceversa.

        Parámetros:
            Ninguno

        Retorno:
            Ninguno
        """
        self.DEBUG = not self.DEBUG

    def get_mode(self):
        """
        Brief: Obtiene el estado del modo de depuración.

        Descripción:
            Este método devuelve el estado actual del modo de depuración del juego.

        Parámetros:
            Ninguno

        Retorno:
            bool: True si el modo de depuración está activado, False de lo contrario.
        """
        return self.DEBUG
    
    def create_text(self, message: str, color: tuple, size: int, font: str):
        """
        Brief: Crea un texto.

        Descripción:
            Este método crea un texto con un mensaje, color, tamaño y tipo de fuente específicos.

        Parámetros:
            - message (str): Mensaje que se mostrará en el texto.
            - color (tuple): Tuple que representa el color del texto en formato RGB.
            - size (int): Tamaño del texto.
            - font (str): Tipo de fuente del texto.

        Retorno:
            pygame.Surface: Superficie que representa el texto creado.
        """
        my_font = py.font.SysFont(font, size, True)
        created_message = my_font.render(message, 0, color)

        return created_message
    
    def apply_text(self, message: str, location_x: int, location_y: int, color: list, size: int, font: str = ""):
        """
        Brief: Aplica un texto en la pantalla del juego.

        Descripción:
            Este método crea un objeto de texto y lo aplica en la pantalla del juego en una posición específica.

        Parámetros:
            - message (str): Mensaje que se mostrará en el texto.
            - location_x (int): Posición en el eje X donde se aplicará el texto.
            - location_y (int): Posición en el eje Y donde se aplicará el texto.
            - color (tuple): Tuple que representa el color del texto en formato RGB.
            - size (int): Tamaño del texto.
            - font (str, opcional): Tipo de fuente del texto. Si no se proporciona, se utiliza la fuente predeterminada.

        Retorno:
            Ninguno
        """
        created_message = self.create_text(message, color, size, font)
        self.screen.blit(created_message, (location_x, location_y))

    def pause_game(self):
        """
        Brief: Pausa el juego.

        Descripción:
            Este método pausa el juego registrando el tiempo en el que se pausó.

        Parámetros:
            Ninguno

        Retorno:
            Ninguno
        """
        self.pause = True
        self.paused_time = py.time.get_ticks() - self.start_time

    def resume_game(self):
        """
        Brief: Reanuda el juego desde el estado de pausa.

        Descripción:
            Este método reanuda el juego desde el estado de pausa ajustando el tiempo de inicio.

        Parámetros:
            Ninguno

        Retorno:
            Ninguno
        """
        self.pause = False
        self.start_time = py.time.get_ticks() - self.paused_time

    def show_time(self):
        """
        Brief: Muestra el tiempo restante en la pantalla del juego.

        Descripción:
            Este método calcula y muestra el tiempo restante en minutos y segundos en la pantalla del juego.
            Aplica estilos de texto diferentes dependiendo del tiempo restante.

        Parámetros:
            Ninguno

        Retorno:
            Ninguno
        """

        if not self.pause:
            current_time = py.time.get_ticks() - self.start_time
            remaining_time = max(self.max_time - current_time, 0)
        else:
            remaining_time = max(self.max_time - self.paused_time, 0)

        remaining_seconds = remaining_time // 1000
        minutes = remaining_seconds // 60
        seconds = remaining_seconds % 60

        self.time_remaining = minutes * 60 + seconds

        message = f"{minutes:02}:{seconds:02}"

        if self.time_remaining <= 20:
            self.apply_text(message, 350, 10, EColors.RED.value, 30, "Arial Black")
        else:
            self.apply_text(message, 350, 10, EColors.WHITE.value, 30, "Arial Black")


    


    
