# test_file.py #
import typer

if __name__ == "__main__":
        typer.initialise("TYPER TEST PROGRAM", "-start .... help")

while True:
        typer.get_input("Test question? ")