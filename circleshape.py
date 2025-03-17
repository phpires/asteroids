import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def collision_check(self, circle_shape):
        radius_sum = circle_shape.radius + self.radius
        distance_between_two_shapes = pygame.math.Vector2.distance_to(self.position, circle_shape.position)
        if distance_between_two_shapes < radius_sum:
            return True
        return False