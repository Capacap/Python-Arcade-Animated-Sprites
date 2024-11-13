import arcade
from typing import List, Dict

class SpriteAnimation:
    def __init__(self, name: str, keyframes: List[int], framerate: int, loop: bool) -> None:
        self.name = name
        self.keyframes = keyframes
        self.framerate = framerate
        self.loop = loop
        self.length = len(keyframes)

class AnimatedSprite(arcade.Sprite):
    def __init__(self, x: int, y: int) -> None:
        super().__init__()
        self.center_x = x
        self.center_y = y
        self.time_scale = 1.0

        self._texture_file_path_to_index: Dict[str, int] = {}
        self._active_texture_index = -1
        self._name_to_animation: Dict[str, SpriteAnimation] = {}
        self._animation_time = 0.0
        self._active_animation: SpriteAnimation = None

    def add_animation(self, keyframes: List[arcade.Texture], name: str, framerate: int, loop: bool):
        animation_texture_indices = []
        for texture in keyframes:
            self.textures.append(texture)
            animation_texture_indices.append(len(self.textures) - 1)
        self._name_to_animation[name] = SpriteAnimation(name, animation_texture_indices, framerate, loop)

    def set_active_texture(self, texture_index: int) -> None:
        if texture_index != self._active_texture_index:
            self._active_texture_index = texture_index
            self.texture = self.textures[texture_index]

    def play_animation(self, animation_name: str, preserve_time: bool = False) -> None:
        animation = self._name_to_animation[animation_name]
        if animation != self._active_animation:
            self._active_animation = self._name_to_animation[animation_name]
            if not preserve_time:
                self._animation_time = 0.0

    def update(self, delta_time: float) -> None:
        super().update()
        if self._active_animation:
            self._animation_time += delta_time * self._active_animation.framerate * self.time_scale
            if self._active_animation.loop and self._animation_time > self._active_animation.length:
                self._animation_time -= self._active_animation.length

            frame_number = round(self._animation_time)
            if self._active_animation.loop:
                frame_number %= self._active_animation.length
            frame_number = min(frame_number, self._active_animation.length - 1)

            frame_index = self._active_animation.keyframes[frame_number]
            self.set_active_texture(frame_index)