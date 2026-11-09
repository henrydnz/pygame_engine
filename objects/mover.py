from gameObject import GameObject
from pygame import Vector2

class Mover:
    def __init__(self, max_velocity, acceleration = 1, friction = 1):
        self.velocity = Vector2(0, 0)
        self.acceleration = acceleration
        self.max_velocity = max_velocity

        self.friction = friction

    # move o entity dado pra direcao dada. precisa de deltatime.
    def apply_movement_accel_frict(self, entity: GameObject, direction: Vector2, delta_time: float) -> None:
        if direction.length() > 0: # tem direcao, aplica aceleracao
            direction = direction.normalize()
            self.velocity.x += direction.x * self.acceleration * delta_time
            self.velocity.y += direction.y * self.acceleration * delta_time
        else: # n tem direcao, aplica friccao
            self.velocity *= self.friction

        # corta velocidade se ficar maior que a maxima
        if self.velocity.length() > self.max_velocity:
            self.velocity.scale_to_length(self.max_velocity)

        # parar na hora caso sem movimento e velocidade mt baixa
        if self.velocity.length() < 10 and direction.length() == 0:
            self.velocity.update(0, 0)

        entity.pos = Vector2(self.velocity.x, self.velocity.y) * delta_time

    def apply_movement_simple(self, entity: GameObject, direction: Vector2, delta_time: float) -> None:
            if direction.length() > 0:
                direction = direction.normalize()

            entity.pos = self.max_velocity * direction * delta_time