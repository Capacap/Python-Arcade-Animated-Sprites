import numpy as np
from animated_sprite import AnimatedSprite
from math import atan2, degrees, hypot

class Actor(AnimatedSprite):
    def __init__(self, x: int, y: int) -> None:
        super().__init__(x, y)

        self.movement = Movement(self)
        self.animator = Animator(self)

    def update(self, delta_time: float) -> None:
        super().update(delta_time)
        self.movement.update(delta_time)
        self.animator.update()


class Movement:
    def __init__(self, actor: Actor) -> None:
        self.actor = actor

        self.max_speed = 200.0
        self.max_acceleration = 800.0
        self.max_deceleration = 1000.0

        self.heading = 180
        self.cardinal_heading = 180

        self.position = np.array([actor.center_x, actor.center_y])
        self.velocity = np.array([0.0, 0.0])
        self.speed = 0.0

        self.move_direction_input = np.array([0.0, 0.0])
        
    def update(self, delta_time: float) -> None:
        # Calculate the desired velocity based on the directional input
        direction = np.array(self.move_direction_input)
        direction_norm = np.linalg.norm(direction)
        direction = direction / direction_norm if direction_norm > 1.0 else direction
        target_velocity = (direction / direction_norm * self.max_speed) if direction_norm > 0.01 else np.zeros(2)

        # Calculate the acceleration to be applied
        acceleration_limit = self.max_acceleration if np.linalg.norm(target_velocity) > np.linalg.norm(self.velocity) else self.max_deceleration
        acceleration = (target_velocity - self.velocity) / delta_time
        acceleration_norm = np.linalg.norm(acceleration)
        acceleration = acceleration / acceleration_norm * acceleration_limit if acceleration_norm > acceleration_limit else acceleration

        # Update movement data and sprite position
        self.velocity += acceleration * delta_time
        self.speed = np.linalg.norm(self.velocity)
        self.position += self.velocity * delta_time
        self.actor.position = (self.position[0], self.position[1])

        # Calculate the new heading and nearest cardinal heading (north, east, south or west)
        if self.speed > 0.01:
            self.heading = round(degrees(atan2(self.velocity[0], self.velocity[1]))) % 360
            cardinal_headings = [0, 90, 180, 270, 360]
            self.cardinal_heading = min(cardinal_headings, key=lambda x: abs(self.heading - x))
            if self.cardinal_heading == 360:
                self.cardinal_heading = 0


class Animator:
    def __init__(self, actor: Actor) -> None:
        self.actor = actor

    def update(self):
        if self.actor.movement.speed > 0.01:
            # Play a run animation based on nearest cardinal heading
            match self.actor.movement.cardinal_heading:
                case   0: self.actor.play_animation("run_north",  preserve_time=True)
                case  90: self.actor.play_animation("run_east",   preserve_time=True)
                case 180: self.actor.play_animation("run_south",  preserve_time=True)
                case 270: self.actor.play_animation("run_west",   preserve_time=True)
        else:
            # Play an idle animation based on nearest cardinal heading
            match self.actor.movement.cardinal_heading:
                case   0: self.actor.play_animation("idle_north",  preserve_time=True)
                case  90: self.actor.play_animation("idle_east",   preserve_time=True)
                case 180: self.actor.play_animation("idle_south",  preserve_time=True)
                case 270: self.actor.play_animation("idle_west",   preserve_time=True)