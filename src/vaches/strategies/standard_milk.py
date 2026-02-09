from src.vaches.domain.vache import Vache
from src.vaches.domain.vache_a_lait import VacheALait
from src.vaches.domain.errors.exceptions import InvalidVacheException


class StandardMilk:

    def calculer_lait(self, vache: VacheALait, panse_avant: float) -> float:
        return panse_avant * VacheALait.RENDEMENT_LAIT

    def stocker_lait(self, vache: VacheALait, lait: float) -> None:
        if vache._lait_disponible + lait > VacheALait.PRODUCTION_LAIT_MAX:
            raise InvalidVacheException("Production de lait depasserait le maximum autorise")
        vache._lait_disponible += lait
        vache._lait_total_produit += lait

    def post_rumination(self, vache: Vache, panse_avant: float, lait: float) -> None:
        pass
