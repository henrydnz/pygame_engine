from pygame import Vector2, key, K_w, K_s, K_a, K_d, K_UP, K_DOWN, K_LEFT, K_RIGHT

def get_wasd_input_direction_vector(keys, direction) -> None:
    if keys[K_w]: direction.y -= 1
    if keys[K_s]: direction.y += 1
    if keys[K_a]: direction.x -= 1
    if keys[K_d]: direction.x += 1

def get_arrows_input_direction_vector(keys, direction) -> None:
    if keys[K_UP]: direction.y -= 1
    if keys[K_DOWN]: direction.y += 1
    if keys[K_LEFT]: direction.x -= 1
    if keys[K_RIGHT]: direction.x += 1

def get_both_input_direction_vector(keys, direction) -> None:
    if keys[K_w] or keys[K_UP]: direction.y -= 1
    if keys[K_s] or keys[K_DOWN]: direction.y += 1
    if keys[K_a] or keys[K_LEFT]: direction.x -= 1
    if keys[K_d] or keys[K_RIGHT]: direction.x += 1

# mode = 0 -> wasd movement
# mode = 1 -> arrows movement
# mode = 2 -> both
def input_movement(mode = 2):
    keys = key.get_pressed()
    direction = Vector2(0, 0)

    match mode:
        case 0:
            get_arrows_input_direction_vector(keys, direction)
        case 1:
            get_wasd_input_direction_vector(keys, direction)
        case 2:
            get_both_input_direction_vector(keys, direction)

    if direction.length() > 0:
        return direction.normalize()

    return direction

# TODO: funcao de input customizada -> input_movement mode 4
