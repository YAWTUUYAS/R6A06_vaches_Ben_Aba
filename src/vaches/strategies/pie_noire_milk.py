from src.vaches.domain.vache import Vache
from src.vaches.domain.vache_a_lait import VacheALait
from src.vaches.domain.errors.exceptions import InvalidVacheException


class PieNoireMilk:

    def calculer_lait(self, vache: VacheALait, panse_avant: float) -> float:
        pie_noire = vache
        
        if pie_noire._ration:
            facteur = sum(
                qty * pie_noire.COEFFICIENT_NUTRITIONNEL.get(food_type, 1.0)
                for food_type, qty in pie_noire._ration.items()
            )
            return VacheALait.RENDEMENT_LAIT * facteur
        else:
            return panse_avant * VacheALait.RENDEMENT_LAIT

    def stocker_lait(self, vache: VacheALait, lait: float) -> None:
        if vache._lait_disponible + lait > VacheALait.PRODUCTION_LAIT_MAX:
            raise InvalidVacheException("Production de lait depasserait le maximum autorise")
        vache._lait_disponible += lait
        vache._lait_total_produit += lait

    def post_rumination(self, vache: Vache, panse_avant: float, lait: float) -> None:
        pie_noire = vache
        pie_noire._ration = {}
