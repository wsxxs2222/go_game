import pygame as p
import sys
import game_engine

# set basic parameters
BOARD_MARGIN = 40
BROADER_LINE_WIDTH = 6
LINE_WIDTH = 1
NUMBER_OF_LINES = 19
SPACES_BETWEEN_LINES = 32
WIDTH = 2*BOARD_MARGIN+(NUMBER_OF_LINES-1)*SPACES_BETWEEN_LINES+LINE_WIDTH+2*BROADER_LINE_WIDTH
HEIGHT = WIDTH


def main():
    p.init()
    # make the window
    screen = p.display.set_mode((WIDTH,HEIGHT))
    # event loop
    while True:
        for e in p.event.get():
            if e.type == p.QUIT:
                p.quit()
                sys.exit()
        draw_board_no_image(screen)
        p.display.flip()
    pass


def load_images():
    pass


def draw_game_state(screen, gs):
    draw_board_no_image(screen)
    draw_pieces(screen, gs)


def draw_pieces(screen, gs):
    pass


def draw_board_no_image(screen):
    # set background color
    screen.fill((234, 182, 118))
    # draw the bolded border
    p.draw.line(screen, "black", (0, 0), (0, HEIGHT), BROADER_LINE_WIDTH)
    p.draw.line(screen, "black", (0, BROADER_LINE_WIDTH//2), (WIDTH, BROADER_LINE_WIDTH//2), BROADER_LINE_WIDTH)
    p.draw.line(screen, "black", (WIDTH, 0), (WIDTH, HEIGHT), BROADER_LINE_WIDTH)
    p.draw.line(screen, "black", (0, HEIGHT), (WIDTH, HEIGHT), BROADER_LINE_WIDTH)
    for i in range(NUMBER_OF_LINES):
        # draw vertical lines
        p.draw.line(screen, "black", (BROADER_LINE_WIDTH + BOARD_MARGIN
                    + i * SPACES_BETWEEN_LINES, BROADER_LINE_WIDTH + BOARD_MARGIN),
                    (BROADER_LINE_WIDTH + BOARD_MARGIN
                    + i * SPACES_BETWEEN_LINES, BROADER_LINE_WIDTH + BOARD_MARGIN
                    + (NUMBER_OF_LINES-1) * SPACES_BETWEEN_LINES))
        # draw horizontal lines
        p.draw.line(screen, "black", (BROADER_LINE_WIDTH + BOARD_MARGIN, BROADER_LINE_WIDTH + BOARD_MARGIN
                                      + i * SPACES_BETWEEN_LINES),
                    (BROADER_LINE_WIDTH + BOARD_MARGIN
                     + (NUMBER_OF_LINES-1) * SPACES_BETWEEN_LINES, BROADER_LINE_WIDTH + BOARD_MARGIN
                     + i * SPACES_BETWEEN_LINES))


if __name__ == "__main__":
    main()