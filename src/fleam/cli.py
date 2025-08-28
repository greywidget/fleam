from rich import print
from typer import Typer

app = Typer(add_completion=False)


@app.command()
def run():
    print("It's a device for bloodletting init - just ask dhk")
