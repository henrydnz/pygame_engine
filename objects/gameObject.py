from abc import ABC, abstractmethod
from pygame import Surface, Vector2, Rect

class GameObject(ABC):
    def __init__(self,
                 init_pos: tuple[int | float, int | float],
                 sprites: Surface | list[Surface]) -> None:

        self.pos = Vector2(init_pos)

        self.sprites = [sprites] if isinstance(sprites, Surface) else sprites
        self.current_sprite = 0
        self.sprite = self.sprites[self.current_sprite]

        # usado pra funcoes leves de rendering e position tracking
        self.bounding_box = self.sprite.get_rect(center=init_pos)

    @abstractmethod
    def update(self, delta_time: float) -> None: pass

    @abstractmethod
    def animate(self, anim_speed: float) -> None: pass

    # atualiza posicao centro de caixas (como bounding box e hitbox)
    def sync_bounding_box(self, boxes: list[Rect]) -> None:
        self.bounding_box.center = (round(self.pos.x), round(self.pos.y))

    # atualiza o sprite e da resize no bounding_box
    def set_sprite_anchor(self, new_sprite, anchor='center'):
        # pega coordenadas do anchor
        current_anchor_coords = getattr(self.bounding_box, anchor)

        # muda sprite
        self.sprite = new_sprite

        # atualiza coordenadas do anchor de acordo com sprite nova
        kwargs = {anchor: current_anchor_coords}
        self.bounding_box = self.sprite.get_rect(**kwargs)

        # atualiza coordenadas do centro do objeto
        self.pos = Vector2(self.bounding_box.center)

    def set_pos(self, x, y):
        self.pos = Vector2(x, y)

    def blit(self, surface: Surface) -> None:
        surface.blit(self.sprite, self.bounding_box)