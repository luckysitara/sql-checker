from cx_Freeze import setup, Executable

setup(
    name="YourAppName",
    version="1.0",
    description="Description of your application",
    executables=[Executable("me1.py")]
)

