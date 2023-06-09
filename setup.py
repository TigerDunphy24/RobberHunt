from cx_Freeze import setup, Executable

# Definiere die Ausführungsdatei (deine Spiel-Datei)
game_file = Executable("C:\Users\eliah\Games\RobberHunt.py")

setup(
    name="RobberHunt",
    version="3.1",
    description="Dont get caught!",
    executables=[game_file]
)
