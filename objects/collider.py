from pygame import Rect

class Collider:
    def __init__(self, hitbox_size: tuple[int, int], offset: tuple[int, int] = (0, 0)):
        self.center_offset = offset
        self.hitbox = Rect(0, 0, hitbox_size[0], hitbox_size[1])

    # atualiza posicao da hitbox dada posicao do entity
    def sync_hitbox(self, entity_center: tuple[int, int]):
        x = entity_center[0] + self.center_offset[0]
        y = entity_center[1] + self.center_offset[1]
        self.hitbox.center = (x, y)

    # muda tamanho da hitbox
    # CUIDADO: anchor topleft, precisa dar sync_hitbox dps de usar
    def set_hitbox_size(self, new_size: tuple[int, int]):
        self.hitbox.size = new_size

# TODO: collision methods