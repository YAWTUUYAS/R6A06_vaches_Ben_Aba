from vaches.strategies.protocols.rumination_strategy import RuminationStrategy


class DefaultNoMilk(RuminationStrategy):

    def calculer_lait(self, vache, panse_avant: float) -> float:
        return 0.0

    def stocker_lait(self, vache, lait: float) -> None:
        pass

    def post_rumination(self, vache, panse_avant: float, lait: float) -> None:
        pass
