from typing import Optional
from src.vaches.domain.vache import Vache
from src.vaches.domain.vache_a_lait import VacheALait
from src.vaches.domain.errors.exceptions import InvalidVacheException
from src.vaches.nourriture.type_nourriture import TypeNourriture
from src.vaches.strategies.pie_noire_milk import PieNoireMilk

class PieNoire(VacheALait):
    

    def __init__(self, petit_nom: str, poids: float, nb_taches_blanches: int = 0, nb_taches_noires: int = 0):
        self._valider_taches(nb_taches_blanches, nb_taches_noires)
        super().__init__(petit_nom, poids)
        self._valider_etat()
        
        self._nb_taches_blanches = nb_taches_blanches
        self._nb_taches_noires = nb_taches_noires
        self._ration = {}
        
        # Injection de la stratégie
        
        self._rumination_strategy = PieNoireMilk()

    @property
    def nb_taches_blanches(self) -> int:
        return self._nb_taches_blanches

    @property
    def nb_taches_noires(self) -> int:
        return self._nb_taches_noires

    @property
    def ration(self) -> dict:
        return self._ration.copy()
    
    def _valider_taches(self, nb_taches_blanches: int, nb_taches_noires: int) -> None:
        if not isinstance(nb_taches_blanches, int):
            raise InvalidVacheException("nb_taches_blanches doit être un entier")
        if not isinstance(nb_taches_noires, int):
            raise InvalidVacheException("nb_taches_noires doit être un entier")
        if nb_taches_blanches <= 0:
            raise InvalidVacheException("nb_taches_blanches doit être positif")
        if nb_taches_noires <= 0:
            raise InvalidVacheException("nb_taches_noires doit être positif")

    def valider_taches(self) -> None:
        self._valider_taches(self._nb_taches_blanches, self._nb_taches_noires)

    def valider_etat(self) -> None:
        super()._valider_etat()
        self.valider_taches()

    def brouter(self, quantite: float, nourriture: Optional[TypeNourriture] = None) -> None:
        super().brouter(quantite, nourriture=None)
        if nourriture is not None:
            if nourriture not in self._ration:
                self._ration[nourriture] = 0.0
            self._ration[nourriture] += quantite

    def __str__(self) -> str:
        super().__str__()
        return (
            f"{self._petit_nom} (poids: {self._poids:.1f} kg, age: {self._age}, panse: {self._panse:.1f})\n"
            f"Taches blanches: {self._nb_taches_blanches}, Taches noires: {self._nb_taches_noires}\n"
        )

