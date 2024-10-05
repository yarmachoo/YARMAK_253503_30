from abc import ABC, abstractmethod
class GeometricFigure(ABC):
    @abstractmethod
    def calculate_area(self):
        """Abstract method"""
        pass