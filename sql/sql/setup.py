import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
build_exe_options = {"packages": ["os"], "excludes": ["tkinter"]}

base = None
if sys.platform == "win32":
    base = "Win32GUI"  # Tells the build script to hide the console.

setup(
    name="SQLGradingSystem",
    version="0.1",
    description="SQL Grading System",
    options={"build_exe": build_exe_options},
    executables=[Executable("me1.py", base=base)],
)

