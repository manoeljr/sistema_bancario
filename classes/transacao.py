from abc import abstractproperty, ABC


class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        ...

    @abstractproperty
    def registrar(self, conta):
        ...
