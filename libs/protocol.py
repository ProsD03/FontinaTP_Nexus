from twisted.internet.protocol import Protocol, Factory
import json

class Fontina(Protocol):
  def __init__(self, factory):
    self.factory = factory
    self.db = factory.db
  def connectionMade(self):
    client = self.transport.getPeer()
    if(self.factory.auth):
      responseDict = {"status": "warning", "msg": "authRequired"}
      packet = json.dumps(responseDict).encode("ascii")
      self.transport.write(packet)
      return
    code = self.db.addClient(client.host, client.port)
    responseDict = {"status": "ok", "code": code}
    packet = json.dumps(responseDict).encode("ascii")
    self.transport.write(packet)


class FontinaFactory(Factory):
  def __init__(self, db, auth):
    self.db = db
    self.auth = auth
  def buildProtocol(self, addr):
    return Fontina(self)