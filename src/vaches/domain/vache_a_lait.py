from src.vaches.domain.vache import Vache

class VacheALait(Vache):
    RENDEMENT_LAIT:float = 1.1
    PRODUCTION_LAIT_MAX:float = 40.0

    def __init__(self, petit_nom:str, poids:float):
        super().__init__(petit_nom, poids)
        self._lait_disponible = 0.0
        self._lait_total_produit = 0.0
        self._lait_total_traite = 0.0
    
    @property
    def lait_disponible(self) -> float:
        return self._lait_disponible
    
    @property
    def lait_total_produit(self) -> float:
        return self._lait_total_produit
    
    @property
    def lait_total_traite(self) -> float:
        return self._lait_total_traite
    