import arcade
from animated_sprite import AnimatedSprite
from actor import Actor
from typing import List

WINDOW_WIDTH = 768
WINDOW_HEIGHT = 768
WINDOW_TITLE = "Animated Sprites"

class GameView(arcade.View):
    def __init__(self):
        super().__init__()

        arcade.set_background_color(arcade.color.WINE)

        # Create the camera
        camera_position = (-WINDOW_WIDTH//2, -WINDOW_HEIGHT//2)
        camera_projection = arcade.LRBT(left=0, right=WINDOW_WIDTH, bottom=0, top=WINDOW_HEIGHT)
        camera_viewport = self.window.rect
        self.main_camera = arcade.camera.Camera2D(position=camera_position, projection=camera_projection, viewport=camera_viewport)

        # Initialize data for cursor tracking and camera dragging
        self.current_cursor_point = [0.0, 0.0]
        self.previous_cursor_point = [0.0, 0.0]
        self.dragging_camera = False

        # Create the scene and animated sprites
        self.scene = arcade.Scene()
        for sprite in self.create_animated_sprites():
            self.scene.add_sprite("ANIMATED", sprite)
        self.player_character = self.create_animated_player_character()
        self.scene.add_sprite("ANIMATED", self.player_character)

        # Initialize data for user input
        self.input_move_north = False
        self.input_move_east = False
        self.input_move_south = False
        self.input_move_west = False
        self.input_animation_toggle = False

    def create_animated_sprites(self):
        """
        Creates a set of animated sprites, each playing a different animation.
        """
        sprites = []

        spritesheet = arcade.load_spritesheet(file_name="./assets/KVA55_2d_topdown_animation/idle_north.png", sprite_width=32, sprite_height=32, columns=8, count=8)
        sprite = AnimatedSprite(0, 32)
        sprite.add_animation(keyframes=spritesheet, name="anim", framerate=8, loop=True)
        sprite.play_animation("anim")
        sprites.append(sprite)

        spritesheet = arcade.load_spritesheet(file_name="./assets/KVA55_2d_topdown_animation/idle_east.png", sprite_width=32, sprite_height=32, columns=8, count=8)
        sprite = AnimatedSprite(32, 0)
        sprite.add_animation(keyframes=spritesheet, name="anim", framerate=8, loop=True)
        sprite.play_animation("anim")
        sprites.append(sprite)

        spritesheet = arcade.load_spritesheet(file_name="./assets/KVA55_2d_topdown_animation/idle_south.png", sprite_width=32, sprite_height=32, columns=8, count=8)
        sprite = AnimatedSprite(0, -32)
        sprite.add_animation(keyframes=spritesheet, name="anim", framerate=8, loop=True)
        sprite.play_animation("anim")
        sprites.append(sprite)

        spritesheet = arcade.load_spritesheet(file_name="./assets/KVA55_2d_topdown_animation/idle_west.png", sprite_width=32, sprite_height=32, columns=8, count=8)
        sprite = AnimatedSprite(-32, 0)
        sprite.add_animation(keyframes=spritesheet, name="anim", framerate=8, loop=True)
        sprite.play_animation("anim")
        sprites.append(sprite)

        spritesheet = arcade.load_spritesheet(file_name="./assets/KVA55_2d_topdown_animation/run_north.png", sprite_width=32, sprite_height=32, columns=8, count=8)
        sprite = AnimatedSprite(0, 64)
        sprite.add_animation(keyframes=spritesheet, name="anim", framerate=8, loop=True)
        sprite.play_animation("anim")
        sprites.append(sprite)

        spritesheet = arcade.load_spritesheet(file_name="./assets/KVA55_2d_topdown_animation/run_east.png", sprite_width=32, sprite_height=32, columns=8, count=8)
        sprite = AnimatedSprite(64, 0)
        sprite.add_animation(keyframes=spritesheet, name="anim", framerate=8, loop=True)
        sprite.play_animation("anim")
        sprites.append(sprite)

        spritesheet = arcade.load_spritesheet(file_name="./assets/KVA55_2d_topdown_animation/run_south.png", sprite_width=32, sprite_height=32, columns=8, count=8)
        sprite = AnimatedSprite(0, -64)
        sprite.add_animation(keyframes=spritesheet, name="anim", framerate=8, loop=True)
        sprite.play_animation("anim")
        sprites.append(sprite)

        spritesheet = arcade.load_spritesheet(file_name="./assets/KVA55_2d_topdown_animation/run_west.png", sprite_width=32, sprite_height=32, columns=8, count=8)
        sprite = AnimatedSprite(-64, 0)
        sprite.add_animation(keyframes=spritesheet, name="anim", framerate=8, loop=True)
        sprite.play_animation("anim")
        sprites.append(sprite)

        return sprites

    def create_animated_player_character(self):
        """
        Create a single animated sprite with multiple possible animations.
        """
        sprite = Actor(0, 0)

        spritesheet = arcade.load_spritesheet(file_name="./assets/KVA55_2d_topdown_animation/idle_north.png", sprite_width=32, sprite_height=32, columns=8, count=8)
        sprite.add_animation(keyframes=spritesheet, name="idle_north", framerate=8, loop=True)
        spritesheet = arcade.load_spritesheet(file_name="./assets/KVA55_2d_topdown_animation/idle_east.png", sprite_width=32, sprite_height=32, columns=8, count=8)
        sprite.add_animation(keyframes=spritesheet, name="idle_east", framerate=8, loop=True)
        spritesheet = arcade.load_spritesheet(file_name="./assets/KVA55_2d_topdown_animation/idle_south.png", sprite_width=32, sprite_height=32, columns=8, count=8)
        sprite.add_animation(keyframes=spritesheet, name="idle_south", framerate=8, loop=True)
        spritesheet = arcade.load_spritesheet(file_name="./assets/KVA55_2d_topdown_animation/idle_west.png", sprite_width=32, sprite_height=32, columns=8, count=8)
        sprite.add_animation(keyframes=spritesheet, name="idle_west", framerate=8, loop=True)

        spritesheet = arcade.load_spritesheet(file_name="./assets/KVA55_2d_topdown_animation/run_north.png", sprite_width=32, sprite_height=32, columns=8, count=8)
        sprite.add_animation(keyframes=spritesheet, name="run_north", framerate=8, loop=True)
        spritesheet = arcade.load_spritesheet(file_name="./assets/KVA55_2d_topdown_animation/run_east.png", sprite_width=32, sprite_height=32, columns=8, count=8)
        sprite.add_animation(keyframes=spritesheet, name="run_east", framerate=8, loop=True)
        spritesheet = arcade.load_spritesheet(file_name="./assets/KVA55_2d_topdown_animation/run_south.png", sprite_width=32, sprite_height=32, columns=8, count=8)
        sprite.add_animation(keyframes=spritesheet, name="run_south", framerate=8, loop=True)
        spritesheet = arcade.load_spritesheet(file_name="./assets/KVA55_2d_topdown_animation/run_west.png", sprite_width=32, sprite_height=32, columns=8, count=8)
        sprite.add_animation(keyframes=spritesheet, name="run_west", framerate=8, loop=True)

        sprite.play_animation("idle_south")

        return sprite

    def on_resize(self, width, height):
        self.main_camera.width = width
        self.main_camera.height = height
        self.main_camera.viewport = arcade.XYWH(0, 0, width, height, arcade.rect.AnchorPoint.BOTTOM_LEFT)

    def on_draw(self):
        self.clear()
        with self.main_camera.activate():
            self.scene.draw(pixelated=True)

    def on_update(self, delta_time):
        # Handle tracking cursor movement and camera dragging
        cursor_delta_x = self.current_cursor_point[0] - self.previous_cursor_point[0]
        cursor_delta_y = self.current_cursor_point[1] - self.previous_cursor_point[1]
        if self.dragging_camera:
            self.main_camera.position = (self.main_camera.position.x - cursor_delta_x, self.main_camera.position.y - cursor_delta_y)
        self.previous_cursor_point = self.current_cursor_point

        # Handle player character control inputs
        if self.input_move_north:
            self.player_character.movement.move_direction_input = [0.0, 1.0]
        elif self.input_move_east:
            self.player_character.movement.move_direction_input = [1.0, 0.0]
        elif self.input_move_south:
            self.player_character.movement.move_direction_input = [0.0, -1.0]
        elif self.input_move_west:
            self.player_character.movement.move_direction_input = [-1.0, 0.0]
        else:
            self.player_character.movement.move_direction_input = [0.0, 0.0]
        
        # Tick the animation of all animated sprites
        animated_sprites: List[AnimatedSprite] = self.scene["ANIMATED"]
        for sprite in animated_sprites:
            sprite.time_scale = 0.5 if self.input_animation_toggle else 1.0
            sprite.update(delta_time)

    def on_mouse_motion(self, x, y, dx, dy):
        # Update cursor tracking
        self.current_cursor_point = [x, y]

    def on_mouse_press(self, x, y, button, key_modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.dragging_camera = True

    def on_mouse_release(self, x, y, button, key_modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.dragging_camera = False

    def on_key_press(self, key, key_modifiers):
        match key:
            case arcade.key.W:
                self.input_move_north = True
            case arcade.key.A:
                self.input_move_west = True
            case arcade.key.S:
                self.input_move_south = True
            case arcade.key.D:
                self.input_move_east = True
            case arcade.key.SPACE:
                self.input_animation_toggle = not self.input_animation_toggle
        
    def on_key_release(self, key, key_modifiers):
        match key:
            case arcade.key.W:
                self.input_move_north = False
            case arcade.key.A:
                self.input_move_west = False
            case arcade.key.S:
                self.input_move_south = False
            case arcade.key.D:
                self.input_move_east = False


def main():
    window = arcade.Window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE, resizable=True)
    game = GameView()
    window.show_view(game)
    arcade.run()

if __name__ == "__main__":
    main()