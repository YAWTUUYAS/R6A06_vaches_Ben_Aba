from src.vaches.domain.errors.exceptions import InvalidVacheException
from vaches.strategies.protocols.rumination_strategy import RuminationStrategy


class PieNoireMilk(RuminationStrategy):

    def calculer_lait(self, vache, panse_avant: float) -> float:
        pie_noire = vache
        
        if pie_noire._ration:
            somme = 0
            for type_nourriture, quantite in pie_noire._ration.items():
                somme += quantite * pie_noire.COEFFICIENT_NUTRITIONNEL.get(type_nourriture)
            return RuminationStrategy.RENDEMENT_LAIT * somme
        else:
            return panse_avant * self.RENDEMENT_LAIT

    def stocker_lait(self, vache, lait: float) -> None:
        if vache._lait_disponible + lait > RuminationStrategy.PRODUCTION_LAIT_MAX:
            raise InvalidVacheException("Production de lait depasserait le maximum autorise")
        vache._lait_disponible += lait
        vache._lait_total_produit += lait

    def post_rumination(self, vache, panse_avant: float, lait: float) -> None:
        pie_noire = vache
        pie_noire._ration = {}
