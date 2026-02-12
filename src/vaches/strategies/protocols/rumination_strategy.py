from typing import Protocol


class RuminationStrategy(Protocol):
    RENDEMENT_LAIT:float = 1.1
    PRODUCTION_LAIT_MAX:float = 40.0

    

    def calculer_lait(self, vache, panse_avant: float) -> float:
        ...
    
    def stocker_lait(self, vache, lait: float) -> None:
        ...

    def post_rumination(self, vache, panse_avant: float, lait: float) -> None:
        ...