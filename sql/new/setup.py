from cx_Freeze import setup, Executable

setup(
    name="SQL Grading System",
    version="1.0",
    description="Grading student SQL submissions",
    executables=[Executable("me2.py")],
)

