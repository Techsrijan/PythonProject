from cx_Freeze import setup, Executable
import os

os.environ['TCL_LIBRARY'] ="C:\\Users\\Ashwani\\AppData\\Local\\Programs\\Python\\Python35-32\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = "C:\\Users\\Ashwani\\AppData\\Local\\Programs\\Python\\Python35-32\\tcl\\tk8.6"
setup(name="install",
      version="2.0",
      author="Ashwani",
      description="My Installer",
      executables=[Executable(r"C:\Users\Ashwani\Desktop\gui\gui.py",
                   icon=r"C:\Users\Ashwani\Desktop\gui\Startup.ico",
                   shortcutName="Gui",
                   shortcutDir="DesktopFolder")]
     )
