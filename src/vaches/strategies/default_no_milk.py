from __future__ import annotations

from src.vaches.strategies.protocols.rumination_strategy import RuminationStrategy
from src.vaches.domain.vache import Vache
from src.vaches.domain.vache_a_lait import VacheALait


class DefaultNoMilk(RuminationStrategy):
    """Strategy for animals that do not produce/store milk.

    - `calculer_lait` always returns 0.0
    - `stocker_lait` is a no-op
    - `post_rumination` is a no-op (keeps default behaviour)
    """

    def calculer_lait(self, vache: VacheALait, panse_avant: float) -> float:
        return 0.0

    def stocker_lait(self, vache: VacheALait, lait: float) -> None:
        # No milk to store for this strategy
        return None

    def post_rumination(self, vache: Vache, panse_avant: float, lait: float) -> None:
        # Default no-op: keep the base Vache behaviour (weight gain handled elsewhere)
        return None
