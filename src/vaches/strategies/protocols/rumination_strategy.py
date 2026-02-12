from typing import Protocol

from src.vaches.nourriture.type_nourriture import TypeNourriture


class RuminationStrategy(Protocol):
    RENDEMENT_LAIT:float = 1.1
    PRODUCTION_LAIT_MAX:float = 40.0

    COEFFICIENT_NUTRITIONNEL = {
        TypeNourriture.HERBE: 1.0,
        TypeNourriture.FOIN: 0.8,
        TypeNourriture.CEREALES: 1.2,
        TypeNourriture.PAILLE: 0.5,
        TypeNourriture.MARGUERITE: 1.1,
    }

    def calculer_lait(self, vache, panse_avant: float) -> float:
        ...
    
    def stocker_lait(self, vache, lait: float) -> None:
        ...

    def post_rumination(self, vache, panse_avant: float, lait: float) -> None:
        ...