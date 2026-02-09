from typing import Protocol

from src.vaches.domain.vache import Vache
from src.vaches.domain.vache_a_lait import VacheALait


class RuminationStrategy(Protocol):


    def calculer_lait(self, vache: "VacheALait", panse_avant: float) -> float:
        ...
    
    def stocker_lait(self, vache: "VacheALait", lait: float) -> None:
        ...

    def post_rumination(self, vache: "Vache", panse_avant: float, lait: float) -> None:
        ...