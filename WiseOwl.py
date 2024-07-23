import os
from tkinter import Tk
from tkinter.filedialog import asksaveasfilename
import pygetwindow as gw
import time
from pynput import mouse
from PIL import Image
import pystray
import tkinter.messagebox as messagebox

# Global variables
current_dir = os.path.dirname(os.path.abspath(__file__))
#icon_path = os.path.join(current_dir, "coruja.ico")
log_file = None
monitoring = True
listener = None

def get_log_file_path():
    """
    Opens a file dialog to get the path for the log file.
    Returns:
        str: Path selected by the user for the log file.
    """
    root = Tk()
    root.withdraw()
    file_path = asksaveasfilename(defaultextension=".txt", 
                                  filetypes=[("Text files", "*.txt")], 
                                  title="WiseOwl_log")
    root.destroy()
    return file_path

def get_active_window_title():
    """
    Retrieves the title of the active window.
    Returns:
        str: Title of the active window or "None" if no window is active.
    """
    active_window = gw.getActiveWindow()
    if active_window is not None:
        return active_window.title
    else:
        return "None"
    
def on_click(x, y, button, pressed):
    """
    Event handler for mouse clicks.
    Args:
        x (int): X-coordinate of the mouse click.
        y (int): Y-coordinate of the mouse click.
        button (mouse.Button): The mouse button clicked.
        pressed (bool): True if the button was pressed, False if released.
    """
    if monitoring and pressed:
        active_window = get_active_window_title()
        with open(log_file, "a") as f:
            f.write(f"{time.strftime('%d-%m-%Y %H:%M:%S')} - Click: {x}, {y}, {button}, Window: {active_window} \n")

def start_monitoring():
    global listener
    listener = mouse.Listener(on_click=on_click)
    listener.start()
    show_status_message("Iniciando vigília!")

def stop_monitoring():
    global listener
    if listener:
        listener.stop()
        listener = None
    show_status_message("Parando vigília!")

def toggle_monitoring(icon):
    """
    Toggles the monitoring state (start/stop).
    Args:
        icon (pystray.Icon): The application icon.
    """
    global monitoring
    monitoring = not monitoring
    if monitoring:
        start_monitoring()
        
    else:
        stop_monitoring()

def quit_program(icon):
    stop_monitoring()
    icon.stop()

def show_status_message(message):
    """
    Displays a message box with the given message.
    Args:
        message (str): Message to display.
    """
    messagebox.showinfo("Status da Aplicação", message)

def create_image():
    """
    Loads and returns the application icon image.
    Returns:
        Image: Loaded image object.
    """
    try:
        icon_path = os.path.join(os.path.dirname(__file__), "coruja.ico")
        image = Image.open(icon_path)
        return image
    except IOError as e:
        print(f"Erro ao carregar a imagem do ícone em {icon_path}: {e}")

icon = pystray.Icon("WiseOwl")
icon.icon = create_image()
icon.title = "WiseOwl"
icon.menu = pystray.Menu(
    pystray.MenuItem('Iniciar', toggle_monitoring),
    pystray.MenuItem('Parar' if monitoring else 'Iniciar', toggle_monitoring),
    pystray.MenuItem('Sair', quit_program)
)

if __name__ == "__main__":
    log_file = get_log_file_path()
    if log_file:
        start_monitoring()
        icon.run()
    else:
        print("Caminho Log_File não especificado. Fechando aplicação.")
