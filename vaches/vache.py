from typing import Any
from vaches.exceptions import InvalidVacheException


class Vache:

    AGE_MAX: int = 25
    POIDS_MAX: float = 1000.0
    PANSE_MAX: float = 50.0
    POIDS_MIN_PANSE: float = 2.0
    RENDEMENT_RUMINATION: float = 0.25
    _NEXT_ID: int = 1

    def __init__(self, petit_nom: str, poids: float, age: int):
        self._id = Vache._NEXT_ID
        Vache._NEXT_ID += 1
        self._petit_nom = petit_nom
        self._poids = poids
        self._panse = 0.0
        self._age = age
        self._valider_etat()

    @property
    def petitNom(self) -> str:
        return self._petit_nom

    @property
    def poids(self) -> float:
        return self._poids

    @property
    def panse(self) -> float:
        return self._panse

    @property
    def age(self) -> int:
        return self._age  

    def _valider_etat(self) -> None:
        if not self._petit_nom or not self._petit_nom.strip():
            raise InvalidVacheException("Le petit nom ne peut pas être vide")
        if self._age is not None and (self._age > Vache.AGE_MAX or self._age < 0):
            raise InvalidVacheException("Age de la vache depasse l'age maximum autorise")
        if self._poids is not None and (self._poids > Vache.POIDS_MAX or self._poids <= 0):
            raise InvalidVacheException("Poids de la vache depasse le poids maximum autorise")
        if self._panse is not None and self._panse > Vache.PANSE_MAX:
            raise InvalidVacheException("Panse de la vache depasse la capacite maximum autorisee")


    def brouter(self, quantite: float, nourriture: Any | None = None) -> None:
        if quantite <= 0:
            raise InvalidVacheException("Quantite a brouter doit etre positive")
        if self._panse + quantite > Vache.PANSE_MAX:
            raise InvalidVacheException("Depassement de la capacite de la panse")
        self._panse += quantite
        if nourriture is not None:
            raise InvalidVacheException("Brouter avec nourriture typée n'est pas autorisé")
    
    def ruminer(self) -> None:
        if self._panse <= 0:
            raise InvalidVacheException("La panse est vide, rien a ruminer")
        panse_avant = self._panse
        gain = panse_avant * Vache.RENDEMENT_RUMINATION
        self._poids += gain
        self._panse = 0.0
    
    def vieillir(self) -> None:
        if (self._age == Vache.AGE_MAX):
            raise InvalidVacheException("ne peut pas vieillir si age maximal atteint")
        self._age +=1