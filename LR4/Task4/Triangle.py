import Task4.GeometricFigure as GeometricFigure
import Task4.Color as Color
class Triangle(GeometricFigure.GeometricFigure):
    def __init__(self, base, height, angle, color):
        """Initialize"""
        super().__init__()
        self.base = base
        self.height = height
        self.angle = angle
        self.color = Color.Color(color)

    def calculate_area(self):
        """Calculate area"""
        import math
        return 0.5 * self.base * self.height * math.sin(math.radians(self.angle))

    def get_description(self):
        """Return description"""
        return "Triangle"

    def __str__(self):
        """String"""
        return "{} {} triangle with base {}, height {}, angle {} degrees, colored in {}.".format(
            self.get_description(), self.color.color, self.base, self.height, self.angle, self.color.color
        )


class ResizableMixin:
    def resize(self, base, height):
        """Resize"""
        self.base = base
        self.height = height


class ResizableTriangle(Triangle, ResizableMixin):
    pass

