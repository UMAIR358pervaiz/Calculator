from cx_Freeze import *
import cx_Freeze


includefiles = ['Wwalczyszyn-Android-Style-Honeycomb-Calculator.ico']
base = None
if sys.platform == "win64":
    base = "Win64GUI"

shortcut_table = [
    
    ("DesktopShortcut", #Shortcut
     "DesktopFolder", # Directory_
     "Scientific Calculator", # Name
     "TARGETDIR", # Component
     "[TARGETDIR]\ScientificCalculator.exe", # Target
     None, # Arguments
     None, # Description
     None, # Hotkey
     None, # Icon
     None, # IconIndex
     None, # ShowCmd
     "TARGETDIR", # WkDir
     )
    
]

msi_data = {"Shortcut": shortcut_table}

# Chane some default MSI option and specify the use of the above Defined tables

bdist_msi_options = {'data':msi_data}
setup(
      Version = "1.0",
      description = "Scientific Calculator",
      author = "Umair Pervaiz",
      name = "Scientific Calculator",
      options = {'build_exe':{'include_files':includefiles}, "bdist_msi": bdist_msi_options,},
      executables=[
          Executable(
              script = "Scientific Calculator.py",
              base = base,
              icon = 'Wwalczyszyn-Android-Style-Honeycomb-Calculator.ico' 
              
         )
          
    ]
)
