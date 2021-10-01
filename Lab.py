from pgl import GWindow, GRect
from random import choice, randint

WIDTH = 500
HEIGHT = 500
BOX_SIZE = 50


def rand_color():
    """Generates a random color."""
    color = "#"
    for _ in range(6):
        color += choice("0123456789ABCDEF")
    return color


def create_filled_rect(x, y, w, h):
    """Creates a rectangle filled with a random color."""
    r = GRect(x, y, w, h)
    r.set_filled(True)
    r.set_color(rand_color())
    return r


def play_game():
    """Plays the clicky box game."""

    def click_callback(event):
        """Callback on mouse click event."""
        x = event.get_x()
        y = event.get_y()
        if target.contains(x, y):
            target.set_location(
                randint(0, WIDTH - BOX_SIZE), randint(0, HEIGHT - BOX_SIZE)
            )
            target.set_color(rand_color())

    gw = GWindow(WIDTH, HEIGHT)
    target = create_filled_rect(
        WIDTH / 2 - BOX_SIZE / 2, HEIGHT / 2 - BOX_SIZE / 2, BOX_SIZE, BOX_SIZE
    )
    gw.add(target)
    gw.add_event_listener("mousedown", click_callback)


if __name__ == "__main__":
    play_game()
