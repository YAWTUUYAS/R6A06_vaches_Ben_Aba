from src.vaches.domain.vache import Vache


class DefaultNoMilk:

    def calculer_lait(self, vache: Vache, panse_avant: float) -> float:
        return 0.0

    def stocker_lait(self, vache: Vache, lait: float) -> None:
        pass

    def post_rumination(self, vache: Vache, panse_avant: float, lait: float) -> None:
        pass
