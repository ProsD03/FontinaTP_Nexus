from rich.console import Console
from libs.styles import info, warning, error, critical, success
from libs.protocol import FontinaFactory
from libs.dbConnector import SQLiteConnector
from twisted.internet.endpoints import TCP4ServerEndpoint
from twisted.internet import reactor

def mainLoop():
  console.clear()
  console.log("🧀 FontinaTP Nexus Server v0.0.1 by ProsD")
  with console.status("[cyan]Starting Server..."):
    dbInst = SQLiteConnector("fontina")
    endpoint = TCP4ServerEndpoint(reactor, 8007)
    endpoint.listen(FontinaFactory(dbInst, False))
    reactor.run()
  continueVar = True
  console.log("Server started. Listening on port xxxx", style=success)
  while continueVar:
    return

if __name__ == "__main__":
  console = Console()
  mainLoop()