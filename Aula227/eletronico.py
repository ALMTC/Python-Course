from log import LogFileMixin #, LogPrintMixin

class Eletronico():
    def __init__(self, nome):
        self._nome = nome
        self._ligado = False

    def ligar(self):
        if not self._ligado:
            self._ligado = True
            return True
        return False

    def desligar(self):
        if self._ligado:
            self._ligado = False
            return True
        return False

class Smartphone(Eletronico, LogFileMixin):
    def ligar(self):
        if super().ligar():
            self.log_success(f'{self._nome} foi ligado')
            return
        self.log_error(f'{self._nome} já está ligado')
        

    def desligar(self):
        if super().desligar():
            self.log_success(f'{self._nome} foi desligado')
            return
        self.log_error(f'{self._nome} já está desligado')