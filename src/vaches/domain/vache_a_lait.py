from src.vaches.domain.vache import Vache
from src.vaches.domain.errors.exceptions import InvalidVacheException
from src.vaches.strategies.standard_milk import StandardMilk

class VacheALait(Vache):

    def __init__(self, petit_nom:str, poids:float):
        super().__init__(petit_nom, poids)
        self._lait_disponible = 0.0
        self._lait_total_produit = 0.0
        self._lait_total_traite = 0.0
        
        # Injection de la stratégie
        self._rumination_strategy = StandardMilk()
    
    @property
    def lait_disponible(self) -> float:
        return self._lait_disponible
    
    @property
    def lait_total_produit(self) -> float:
        return self._lait_total_produit
    
    @property
    def lait_total_traite(self) -> float:
        return self._lait_total_traite
    
    def traire(self, litres:float) -> float:
        if litres <= 0:
            raise InvalidVacheException("Quantite a traire doit etre positive")
        if litres > self._lait_disponible:
            raise InvalidVacheException("Quantite a traire depasse le lait disponible")
        self._lait_disponible -= litres
        self._lait_total_traite += litres
        return litres
    
    def __str__(self) -> str:
        super().__str__()
        return (
            f"{self._petit_nom} (poids: {self._poids:.1f} kg, age: {self._age}, panse: {self._panse:.1f})\n"
            f"Lait disponible : {self._lait_disponible:.1f} L\n"
            f"Lait total produit : {self._lait_total_produit:.1f} L\n"
            f"Lait total trait : {self._lait_total_traite:.1f} L"
        )