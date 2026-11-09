from pygame import Surface, display, Rect
from objects.gameObject import GameObject

class Renderer:
    def __init__(self,
                 width: int, height: int,
                 caption: str | None = None, icon: Surface | None = None,
                 flag_list: list[int] | None = None, vsync: bool = False) -> None:

        flags = 0
        if flag_list is not None:
            for f in flag_list:
                flags |= f

        self.width = width
        self.height = height

        self.screen = display.set_mode((self.width, self.height), vsync=vsync, flags=flags)

        if caption is not None:
            display.set_caption(caption)

        if icon is not None:
            display.set_icon(icon)

    # a ordem dos sources importa
    def render(self, sources: list[Surface | GameObject]) -> None:
        for source in sources:
            if isinstance(source, Surface):
                self.screen.blit(source, source.get_rect())
            if isinstance(source, GameObject):
                source.blit(self.screen)

        display.flip()