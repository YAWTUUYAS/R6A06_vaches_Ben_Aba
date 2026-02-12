from src.vaches.domain.errors.exceptions import InvalidVacheException
from vaches.strategies.protocols.rumination_strategy import RuminationStrategy


class StandardMilk(RuminationStrategy):

    def calculer_lait(self, vache, panse_avant: float) -> float:
        return panse_avant * RuminationStrategy.RENDEMENT_LAIT

    def stocker_lait(self, vache, lait: float) -> None:
        if vache._lait_disponible + lait > RuminationStrategy.PRODUCTION_LAIT_MAX:
            raise InvalidVacheException("Production de lait depasserait le maximum autorise")
        vache._lait_disponible += lait
        vache._lait_total_produit += lait

    def post_rumination(self, vache, panse_avant: float, lait: float) -> None:
        pass
