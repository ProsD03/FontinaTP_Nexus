from rich.console import Console
from rich.prompt import Prompt
from libs.styles import info, warning, error, critical, success


def mainLoop():
  console.clear()
  console.log("🧀 FontinaTP Nexus Server v0.0.1 by ProsD")
  console.log("Starting Server...", style=info)
  continueVar = True
  while continueVar:
    return

if __name__ == "__main__":
  console = Console()
  mainLoop()