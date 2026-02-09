from typing import Optional
from src.vaches.domain.vache import Vache
from src.vaches.domain.vache_a_lait import VacheALait
from src.vaches.domain.errors.exceptions import InvalidVacheException
from src.vaches.nourriture.TypeNourriture import TypeNourriture


class PieNoire(VacheALait):
    COEFFICIENT_NUTRITIONNEL = {
        TypeNourriture.HERBE: 1.0,
        TypeNourriture.FOIN: 0.8,
        TypeNourriture.CEREALES: 1.2,
        TypeNourriture.PAILLE: 0.5,
        TypeNourriture.MARGUERITE: 1.1,
    }

    def __init__(self, petit_nom: str, poids: float, nb_taches_blanches: int = 0, nb_taches_noires: int = 0):
        self._valider_taches(nb_taches_blanches, nb_taches_noires)
        super().__init__(petit_nom, poids)
        self._valider_etat()
        
        self._nb_taches_blanches = nb_taches_blanches
        self._nb_taches_noires = nb_taches_noires
        self._ration = {}

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

    def ruminer(self) -> None:
        panse_avant = self._panse
        if self._ration:
            facteur = sum(
                quantite * self.COEFFICIENT_NUTRITIONNEL.get(type_nourriture, 1.0)
                for type_nourriture, quantite in self._ration.items()
            )
            lait_produit = VacheALait.RENDEMENT_LAIT * facteur
        else:
            lait_produit = panse_avant * VacheALait.RENDEMENT_LAIT
        if self._lait_disponible + lait_produit > self.PRODUCTION_LAIT_MAX:
            raise InvalidVacheException("Production de lait depasserait le maximum autorise")
        Vache.ruminer(self)
        
        self._lait_disponible += lait_produit
        self._lait_total_produit += lait_produit
        
        self.post_rumination(panse_avant, lait_produit)

    def post_rumination(self, panse_avant: float, lait: float) -> None:
        self._ration = {}

    def __str__(self) -> str:
        lait_str = (
            f"Lait disponible : {self._lait_disponible:.1f} L\n"
            f"Lait total produit : {self._lait_total_produit:.1f} L\n"
            f"Lait total trait : {self._lait_total_traite:.1f} L"
        )
        return (
            f"{self._petit_nom} (poids: {self._poids:.1f} kg, age: {self._age}, panse: {self._panse:.1f})\n"
            f"Taches blanches: {self._nb_taches_blanches}, Taches noires: {self._nb_taches_noires}\n"
            f"{lait_str}"
        )

