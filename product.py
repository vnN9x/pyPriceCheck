from datetime import datetime


class Product:
    def __init__(self, nome: str, link: str, preco: float, data: datetime) -> None:
        self._nome = nome
        self._link = link
        self._preco = preco
        self._data = data

@property
def nome(self) -> str:
    return self._nome

@property
def link(self) -> str:
    return self._link

@property
def preco(self) -> float:
    return self._preco

@property
def data(self) -> datetime:
    return self._data
