from rich import print
from typer import Typer

app = Typer()


@app.command()
def run():
    print("It's a device for bloodletting init - just ask dhk")
