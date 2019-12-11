from twisted.internet import reactor
from twisted.internet.protocol import ServerFactory, connectionDone
from twisted.protocols.basic import LineOnlyReceiver

class ServerProtocol(LineOnlyReceiver):
    factory: 'Server'
    login: str = None

    def connectionMade(self):
        self.factory.clients.append(self)

    def lineReceived(self, line: bytes):
        content = line.decode()
                

        if self.login is not None:
            content = str(self.login) + ": " + content
            if len(self.factory.last_ten_messages)<=10:
                self.factory.last_ten_messages.append(content.encode())
            else:
                self.factory.last_ten_messages.pop(0)
                self.factory.last_ten_messages.append(content.encode())

            for user in self.factory.clients:                
                if user is not self:                    
                    user.sendLine(content.encode())
        else:
            if content.startswith("login:"):
                NewLogin=content.replace("login:","")
                
                if self.LoginOccupied(NewLogin):
                    self.sendLine("Login is already occupied. Please, choose another one.".encode())
                    self.factory.clients.remove(self)
                else:
                    self.login=NewLogin
                    self.sendLine(str("Welcome, " + self.login + "!").encode()) 
                    self.send_history()
            else:
                self.sendLine("Invalid login! Please write login:<yourlogin>".encode())   
    def connectionLost(self,reason=connectionDone):
        self.factory.clients.remove(self)

    def LoginOccupied(self, NewLogin):
        for user in self.factory.clients:
            if user.login==NewLogin:
                return True
        return False

    def send_history(self):
        for MessageContent in self.factory.last_ten_messages:
            self.sendLine(MessageContent)
        

class Server(ServerFactory):
    protocol=ServerProtocol
    clients: list
    last_ten_messages: list

    def startFactory(self):
        self.clients=[]
        self.last_ten_messages=[]
        print('Server started')

    def stopFactory(self):
        print('Server stopped')

reactor.listenTCP(1234, Server())        
reactor.run()