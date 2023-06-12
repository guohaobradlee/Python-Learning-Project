"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random


BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).
INITIAL_Y_SPEED = 7.0  # Initial vertical speed for the ball.
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball.
LIVES = 3              # Control the times which user can restart the game.


class BreakoutGraphicsExtension:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH,
                 paddle_height=PADDLE_HEIGHT, paddle_offset=PADDLE_OFFSET,
                 brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS,
                 brick_width=BRICK_WIDTH, brick_height=BRICK_HEIGHT,
                 brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING,
                 title='Breakout'):

        # How many lives left.
        self.lives_left = LIVES

        # Calculate the score.
        self.score = 0

        # Create a graphical window, with some extra space.
        self.window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        self.window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=self.window_width, height=self.window_height, title=title)

        # Create a start label.
        self.start_label = GLabel(f'Click To Start The Game')
        self.start_label.color = 'hotpink'
        self.start_label.font = 'Verdana-30-bold'
        self.window.add(self.start_label, x=(self.window_width - self.start_label.width) / 2,
                        y=(self.window_height - self.start_label.height) / 2)

        # Create a paddle.
        self.paddle = GRect(PADDLE_WIDTH, PADDLE_HEIGHT, x=(self.window_width - PADDLE_WIDTH) / 2,
                            y=self.window_height - PADDLE_OFFSET)
        self.paddle.filled = True
        self.paddle.color = 'hotpink'
        self.paddle.fill_color = 'hotpink'
        self.window.add(self.paddle)

        # Create a lives label.
        self.lives_label = GLabel(f'Your Lives : {self.lives_left}')
        self.lives_label.color = 'hotpink'
        self.lives_label.font = 'Verdana-15-bold'
        self.window.add(self.lives_label, x=0, y=self.window.height)

        # Create a score label.
        self.score_label = GLabel(f'Score : {self.score}')
        self.score_label.color = 'hotpink'
        self.score_label.font = 'Verdana-15-bold'
        self.window.add(self.score_label, x=self.window.width - self.score_label.width, y=self.window.height)

        # Center a filled ball in the graphical window.
        self.ball = GOval(BALL_RADIUS * 2, BALL_RADIUS * 2, x=self.window_width / 2 - BALL_RADIUS,
                          y=self.window_height / 2 - BALL_RADIUS)
        self.ball.filled = True
        self.ball.color = 'hotpink'
        self.ball.fill_color = 'hotpink'
        self.window.add(self.ball)

        # Default initial velocity for the ball.
        self.__dx = random.randint(1, MAX_X_SPEED)
        self.__dy = INITIAL_Y_SPEED
        if random.random() > 0.5:
            self.__dx = -self.__dx

        # Determine whether game has been started.
        self.start_or_not = False
        # Initialize our mouse listeners.
        onmouseclicked(self.start)
        # Determine the game has started.
        onmousemoved(self.drag)

        # Draw bricks.
        for i in range(BRICK_ROWS):
            for j in range(BRICK_COLS):
                self.brick = GRect(BRICK_WIDTH, BRICK_HEIGHT)
                self.brick.filled = True
                if i == 1 and j == 1:
                    self.brick.color = 'lightpink'
                    self.brick.fill_color = 'lightpink'
                    self.window.add(self.brick, x=(BRICK_SPACING * i + BRICK_WIDTH * i),
                                    y=(BRICK_SPACING * j + BRICK_HEIGHT * j + BRICK_OFFSET))
                elif i == 2 and j == 2:
                    self.brick.color = 'lightpink'
                    self.brick.fill_color = 'lightpink'
                    self.window.add(self.brick, x=(BRICK_SPACING * i + BRICK_WIDTH * i),
                                    y=(BRICK_SPACING * j + BRICK_HEIGHT * j + BRICK_OFFSET))
                elif i == 0 and j == 2:
                    self.brick.color = 'lightpink'
                    self.brick.fill_color = 'lightpink'
                    self.window.add(self.brick, x=(BRICK_SPACING * i + BRICK_WIDTH * i),
                                    y=(BRICK_SPACING * j + BRICK_HEIGHT * j + BRICK_OFFSET))
                elif i == 0 and j == 3:
                    self.brick.color = 'lightpink'
                    self.brick.fill_color = 'lightpink'
                    self.window.add(self.brick, x=(BRICK_SPACING * i + BRICK_WIDTH * i),
                                    y=(BRICK_SPACING * j + BRICK_HEIGHT * j + BRICK_OFFSET))
                elif i == 1 and j == 4:
                    self.brick.color = 'lightpink'
                    self.brick.fill_color = 'lightpink'
                    self.window.add(self.brick, x=(BRICK_SPACING * i + BRICK_WIDTH * i),
                                    y=(BRICK_SPACING * j + BRICK_HEIGHT * j + BRICK_OFFSET))
                elif i == 2 and j == 5:
                    self.brick.color = 'lightpink'
                    self.brick.fill_color = 'lightpink'
                    self.window.add(self.brick, x=(BRICK_SPACING * i + BRICK_WIDTH * i),
                                    y=(BRICK_SPACING * j + BRICK_HEIGHT * j + BRICK_OFFSET))
                elif i == 2 and j == 6:
                    self.brick.color = 'lightpink'
                    self.brick.fill_color = 'lightpink'
                    self.window.add(self.brick, x=(BRICK_SPACING * i + BRICK_WIDTH * i),
                                    y=(BRICK_SPACING * j + BRICK_HEIGHT * j + BRICK_OFFSET))
                elif i == 1 and j == 7:
                    self.brick.color = 'lightpink'
                    self.brick.fill_color = 'lightpink'
                    self.window.add(self.brick, x=(BRICK_SPACING * i + BRICK_WIDTH * i),
                                    y=(BRICK_SPACING * j + BRICK_HEIGHT * j + BRICK_OFFSET))
                elif i == 0 and j == 6:
                    self.brick.color = 'lightpink'
                    self.brick.fill_color = 'lightpink'
                    self.window.add(self.brick, x=(BRICK_SPACING * i + BRICK_WIDTH * i),
                                    y=(BRICK_SPACING * j + BRICK_HEIGHT * j + BRICK_OFFSET))
                elif i == 1 and j == 7:
                    self.brick.color = 'lightpink'
                    self.brick.fill_color = 'lightpink'
                    self.window.add(self.brick, x=(BRICK_SPACING * i + BRICK_WIDTH * i),
                                    y=(BRICK_SPACING * j + BRICK_HEIGHT * j + BRICK_OFFSET))
                elif i == 4 and j == 1:
                    self.brick.color = 'lavenderblush'
                    self.brick.fill_color = 'lavenderblush'
                    self.window.add(self.brick, x=(BRICK_SPACING * i + BRICK_WIDTH * i),
                                    y=(BRICK_SPACING * j + BRICK_HEIGHT * j + BRICK_OFFSET))
                elif i == 3 and j == 2:
                    self.brick.color = 'lavenderblush'
                    self.brick.fill_color = 'lavenderblush'
                    self.window.add(self.brick, x=(BRICK_SPACING * i + BRICK_WIDTH * i),
                                    y=(BRICK_SPACING * j + BRICK_HEIGHT * j + BRICK_OFFSET))
                elif i == 3 and j == 3:
                    self.brick.color = 'lavenderblush'
                    self.brick.fill_color = 'lavenderblush'
                    self.window.add(self.brick, x=(BRICK_SPACING * i + BRICK_WIDTH * i),
                                    y=(BRICK_SPACING * j + BRICK_HEIGHT * j + BRICK_OFFSET))
                elif i == 3 and j == 4:
                    self.brick.color = 'lavenderblush'
                    self.brick.fill_color = 'lavenderblush'
                    self.window.add(self.brick, x=(BRICK_SPACING * i + BRICK_WIDTH * i),
                                    y=(BRICK_SPACING * j + BRICK_HEIGHT * j + BRICK_OFFSET))
                elif i == 3 and j == 5:
                    self.brick.color = 'lavenderblush'
                    self.brick.fill_color = 'lavenderblush'
                    self.window.add(self.brick, x=(BRICK_SPACING * i + BRICK_WIDTH * i),
                                    y=(BRICK_SPACING * j + BRICK_HEIGHT * j + BRICK_OFFSET))
                elif i == 3 and j == 6:
                    self.brick.color = 'lavenderblush'
                    self.brick.fill_color = 'lavenderblush'
                    self.window.add(self.brick, x=(BRICK_SPACING * i + BRICK_WIDTH * i),
                                    y=(BRICK_SPACING * j + BRICK_HEIGHT * j + BRICK_OFFSET))
                elif i == 4 and j == 7:
                    self.brick.color = 'lavenderblush'
                    self.brick.fill_color = 'lavenderblush'
                    self.window.add(self.brick, x=(BRICK_SPACING * i + BRICK_WIDTH * i),
                                    y=(BRICK_SPACING * j + BRICK_HEIGHT * j + BRICK_OFFSET))
                elif i == 5 and j == 2:
                    self.brick.color = 'lavenderblush'
                    self.brick.fill_color = 'lavenderblush'
                    self.window.add(self.brick, x=(BRICK_SPACING * i + BRICK_WIDTH * i),
                                    y=(BRICK_SPACING * j + BRICK_HEIGHT * j + BRICK_OFFSET))
                elif i == 5 and j == 6:
                    self.brick.color = 'lavenderblush'
                    self.brick.fill_color = 'lavenderblush'
                    self.window.add(self.brick, x=(BRICK_SPACING * i + BRICK_WIDTH * i),
                                    y=(BRICK_SPACING * j + BRICK_HEIGHT * j + BRICK_OFFSET))
                elif i == 6 and j == 1:
                    self.brick.color = 'lightpink'
                    self.brick.fill_color = 'lightpink'
                    self.window.add(self.brick, x=(BRICK_SPACING * i + BRICK_WIDTH * i),
                                    y=(BRICK_SPACING * j + BRICK_HEIGHT * j + BRICK_OFFSET))
                elif i == 6 and j == 2:
                    self.brick.color = 'lightpink'
                    self.brick.fill_color = 'lightpink'
                    self.window.add(self.brick, x=(BRICK_SPACING * i + BRICK_WIDTH * i),
                                    y=(BRICK_SPACING * j + BRICK_HEIGHT * j + BRICK_OFFSET))
                elif i == 6 and j == 3:
                    self.brick.color = 'lightpink'
                    self.brick.fill_color = 'lightpink'
                    self.window.add(self.brick, x=(BRICK_SPACING * i + BRICK_WIDTH * i),
                                    y=(BRICK_SPACING * j + BRICK_HEIGHT * j + BRICK_OFFSET))
                elif i == 6 and j == 4:
                    self.brick.color = 'lightpink'
                    self.brick.fill_color = 'lightpink'
                    self.window.add(self.brick, x=(BRICK_SPACING * i + BRICK_WIDTH * i),
                                    y=(BRICK_SPACING * j + BRICK_HEIGHT * j + BRICK_OFFSET))
                elif i == 6 and j == 5:
                    self.brick.color = 'lightpink'
                    self.brick.fill_color = 'lightpink'
                    self.window.add(self.brick, x=(BRICK_SPACING * i + BRICK_WIDTH * i),
                                    y=(BRICK_SPACING * j + BRICK_HEIGHT * j + BRICK_OFFSET))
                elif i == 6 and j == 6:
                    self.brick.color = 'lightpink'
                    self.brick.fill_color = 'lightpink'
                    self.window.add(self.brick, x=(BRICK_SPACING * i + BRICK_WIDTH * i),
                                    y=(BRICK_SPACING * j + BRICK_HEIGHT * j + BRICK_OFFSET))
                elif i == 6 and j == 7:
                    self.brick.color = 'lightpink'
                    self.brick.fill_color = 'lightpink'
                    self.window.add(self.brick, x=(BRICK_SPACING * i + BRICK_WIDTH * i),
                                    y=(BRICK_SPACING * j + BRICK_HEIGHT * j + BRICK_OFFSET))
                elif i == 7 and j == 1:
                    self.brick.color = 'lavenderblush'
                    self.brick.fill_color = 'lavenderblush'
                    self.window.add(self.brick, x=(BRICK_SPACING * i + BRICK_WIDTH * i),
                                    y=(BRICK_SPACING * j + BRICK_HEIGHT * j + BRICK_OFFSET))
                elif i == 7 and j == 2:
                    self.brick.color = 'lavenderblush'
                    self.brick.fill_color = 'lavenderblush'
                    self.window.add(self.brick, x=(BRICK_SPACING * i + BRICK_WIDTH * i),
                                    y=(BRICK_SPACING * j + BRICK_HEIGHT * j + BRICK_OFFSET))
                elif i == 7 and j == 3:
                    self.brick.color = 'lavenderblush'
                    self.brick.fill_color = 'lavenderblush'
                    self.window.add(self.brick, x=(BRICK_SPACING * i + BRICK_WIDTH * i),
                                    y=(BRICK_SPACING * j + BRICK_HEIGHT * j + BRICK_OFFSET))
                elif i == 7 and j == 4:
                    self.brick.color = 'lavenderblush'
                    self.brick.fill_color = 'lavenderblush'
                    self.window.add(self.brick, x=(BRICK_SPACING * i + BRICK_WIDTH * i),
                                    y=(BRICK_SPACING * j + BRICK_HEIGHT * j + BRICK_OFFSET))
                elif i == 7 and j == 5:
                    self.brick.color = 'lavenderblush'
                    self.brick.fill_color = 'lavenderblush'
                    self.window.add(self.brick, x=(BRICK_SPACING * i + BRICK_WIDTH * i),
                                    y=(BRICK_SPACING * j + BRICK_HEIGHT * j + BRICK_OFFSET))
                elif i == 7 and j == 6:
                    self.brick.color = 'lavenderblush'
                    self.brick.fill_color = 'lavenderblush'
                    self.window.add(self.brick, x=(BRICK_SPACING * i + BRICK_WIDTH * i),
                                    y=(BRICK_SPACING * j + BRICK_HEIGHT * j + BRICK_OFFSET))
                elif i == 7 and j == 7:
                    self.brick.color = 'lavenderblush'
                    self.brick.fill_color = 'lavenderblush'
                    self.window.add(self.brick, x=(BRICK_SPACING * i + BRICK_WIDTH * i),
                                    y=(BRICK_SPACING * j + BRICK_HEIGHT * j + BRICK_OFFSET))
                elif i == 8 and j == 1:
                    self.brick.color = 'lavenderblush'
                    self.brick.fill_color = 'lavenderblush'
                    self.window.add(self.brick, x=(BRICK_SPACING * i + BRICK_WIDTH * i),
                                    y=(BRICK_SPACING * j + BRICK_HEIGHT * j + BRICK_OFFSET))
                elif i == 8 and j == 2:
                    self.brick.color = 'lavenderblush'
                    self.brick.fill_color = 'lavenderblush'
                    self.window.add(self.brick, x=(BRICK_SPACING * i + BRICK_WIDTH * i),
                                    y=(BRICK_SPACING * j + BRICK_HEIGHT * j + BRICK_OFFSET))
                elif i == 8 and j == 3:
                    self.brick.color = 'lavenderblush'
                    self.brick.fill_color = 'lavenderblush'
                    self.window.add(self.brick, x=(BRICK_SPACING * i + BRICK_WIDTH * i),
                                    y=(BRICK_SPACING * j + BRICK_HEIGHT * j + BRICK_OFFSET))
                elif i == 8 and j == 4:
                    self.brick.color = 'lavenderblush'
                    self.brick.fill_color = 'lavenderblush'
                    self.window.add(self.brick, x=(BRICK_SPACING * i + BRICK_WIDTH * i),
                                    y=(BRICK_SPACING * j + BRICK_HEIGHT * j + BRICK_OFFSET))
                elif i == 8 and j == 5:
                    self.brick.color = 'lavenderblush'
                    self.brick.fill_color = 'lavenderblush'
                    self.window.add(self.brick, x=(BRICK_SPACING * i + BRICK_WIDTH * i),
                                    y=(BRICK_SPACING * j + BRICK_HEIGHT * j + BRICK_OFFSET))
                elif i == 8 and j == 6:
                    self.brick.color = 'lavenderblush'
                    self.brick.fill_color = 'lavenderblush'
                    self.window.add(self.brick, x=(BRICK_SPACING * i + BRICK_WIDTH * i),
                                    y=(BRICK_SPACING * j + BRICK_HEIGHT * j + BRICK_OFFSET))
                elif i == 8 and j == 7:
                    self.brick.color = 'lavenderblush'
                    self.brick.fill_color = 'lavenderblush'
                    self.window.add(self.brick, x=(BRICK_SPACING * i + BRICK_WIDTH * i),
                                    y=(BRICK_SPACING * j + BRICK_HEIGHT * j + BRICK_OFFSET))
                elif i == 9 and j == 1:
                    self.brick.color = 'lightpink'
                    self.brick.fill_color = 'lightpink'
                    self.window.add(self.brick, x=(BRICK_SPACING * i + BRICK_WIDTH * i),
                                    y=(BRICK_SPACING * j + BRICK_HEIGHT * j + BRICK_OFFSET))
                elif i == 9 and j == 2:
                    self.brick.color = 'lightpink'
                    self.brick.fill_color = 'lightpink'
                    self.window.add(self.brick, x=(BRICK_SPACING * i + BRICK_WIDTH * i),
                                    y=(BRICK_SPACING * j + BRICK_HEIGHT * j + BRICK_OFFSET))
                elif i == 9 and j == 3:
                    self.brick.color = 'lightpink'
                    self.brick.fill_color = 'lightpink'
                    self.window.add(self.brick, x=(BRICK_SPACING * i + BRICK_WIDTH * i),
                                    y=(BRICK_SPACING * j + BRICK_HEIGHT * j + BRICK_OFFSET))
                elif i == 9 and j == 4:
                    self.brick.color = 'lightpink'
                    self.brick.fill_color = 'lightpink'
                    self.window.add(self.brick, x=(BRICK_SPACING * i + BRICK_WIDTH * i),
                                    y=(BRICK_SPACING * j + BRICK_HEIGHT * j + BRICK_OFFSET))
                elif i == 9 and j == 5:
                    self.brick.color = 'lightpink'
                    self.brick.fill_color = 'lightpink'
                    self.window.add(self.brick, x=(BRICK_SPACING * i + BRICK_WIDTH * i),
                                    y=(BRICK_SPACING * j + BRICK_HEIGHT * j + BRICK_OFFSET))
                elif i == 9 and j == 6:
                    self.brick.color = 'lightpink'
                    self.brick.fill_color = 'lightpink'
                    self.window.add(self.brick, x=(BRICK_SPACING * i + BRICK_WIDTH * i),
                                    y=(BRICK_SPACING * j + BRICK_HEIGHT * j + BRICK_OFFSET))
                elif i == 9 and j == 7:
                    self.brick.color = 'lightpink'
                    self.brick.fill_color = 'lightpink'
                    self.window.add(self.brick, x=(BRICK_SPACING * i + BRICK_WIDTH * i),
                                    y=(BRICK_SPACING * j + BRICK_HEIGHT * j + BRICK_OFFSET))
                else:
                    self.brick.color = 'hotpink'
                    self.brick.fill_color = 'hotpink'
                    self.window.add(self.brick, x=(BRICK_SPACING * i + BRICK_WIDTH * i),
                                    y=(BRICK_SPACING * j + BRICK_HEIGHT * j + BRICK_OFFSET))
        # Calculate how many bricks exist.
        self.numbers_of_brick = BRICK_ROWS * BRICK_COLS

    def check_for_collision(self):
        ball_left = self.window.get_object_at(self.ball.x - 0.5, self.ball.y + BALL_RADIUS)
        ball_right = self.window.get_object_at(self.ball.x + 2 * BALL_RADIUS + 0.5, self.ball.y + BALL_RADIUS)
        ball_top = self.window.get_object_at(self.ball.x + BALL_RADIUS, self.ball.y - 0.5)
        ball_bottom = self.window.get_object_at(self.ball.x + BALL_RADIUS, self.ball.y + 2 * BALL_RADIUS + 0.5)
        # Check whether is lives label:
        if ball_left is self.lives_label:
            pass
        elif ball_right is self.lives_label:
            pass
        elif ball_top is self.lives_label:
            pass
        elif ball_bottom is self.lives_label:
            pass
        # Check whether is start label:
        if ball_left is self.start_label:
            pass
        elif ball_right is self.start_label:
            pass
        elif ball_top is self.start_label:
            pass
        elif ball_bottom is self.start_label:
            pass
        # Check whether is right edge.
        if self.ball.x + 2 * BALL_RADIUS > self.window.width:
            self.__dx = -self.__dx
        # Check whether is left edge.
        if self.ball.x < 0:
            self.__dx = -self.__dx
        # Check whether is upper edge.
        if self.ball.y < 0:
            self.__dy = -self.__dy
        # Check whether is paddle.
        if ball_bottom is self.paddle:
            self.__dy = -INITIAL_Y_SPEED
        elif ball_bottom is self.lives_label or self.start_label:
            pass
        # Check whether is brick.
        if ball_left is not None and ball_left is not self.paddle and ball_left is not self.lives_label\
                and ball_left is not self.score_label:
            self.window.remove(ball_left)
            self.window.remove(self.score_label)
            self.__dy = -self.__dy
            self.numbers_of_brick -= 1
            self.score += 1
            self.score_label = GLabel(f'Score : {self.score}')
            self.score_label.color = 'hotpink'
            self.score_label.font = 'Verdana-15-bold'
            self.window.add(self.score_label, x=self.window.width - self.score_label.width, y=self.window.height)
        elif ball_right is not None and ball_right is not self.paddle and ball_right is not self.lives_label\
                and ball_right is not self.score_label:
            self.window.remove(ball_right)
            self.window.remove(self.score_label)
            self.__dy = -self.__dy
            self.numbers_of_brick -= 1
            self.score += 1
            self.score_label = GLabel(f'Score : {self.score}')
            self.score_label.color = 'hotpink'
            self.score_label.font = 'Verdana-15-bold'
            self.window.add(self.score_label, x=self.window.width - self.score_label.width, y=self.window.height)
        elif ball_top is not None and ball_top is not self.paddle and ball_top is not self.lives_label\
                and ball_top is not self.score_label:
            self.window.remove(ball_top)
            self.window.remove(self.score_label)
            self.__dy = -self.__dy
            self.numbers_of_brick -= 1
            self.score += 1
            self.score_label = GLabel(f'Score : {self.score}')
            self.score_label.color = 'hotpink'
            self.score_label.font = 'Verdana-15-bold'
            self.window.add(self.score_label, x=self.window.width - self.score_label.width, y=self.window.height)
        elif ball_bottom is not None and ball_bottom is not self.paddle and ball_bottom is not self.lives_label\
                and ball_bottom is not self.score_label:
            self.window.remove(ball_bottom)
            self.window.remove(self.score_label)
            self.__dy = -self.__dy
            self.numbers_of_brick -= 1
            self.score += 1
            self.score_label = GLabel(f'Score : {self.score}')
            self.score_label.color = 'hotpink'
            self.score_label.font = 'Verdana-15-bold'
            self.window.add(self.score_label, x=self.window.width - self.score_label.width, y=self.window.height)

    def reset_ball(self):
        # Check whether is lower edge.
        if self.ball.y > self.window.height:
            self.lives_left -= 1
            self.window.remove(self.lives_label)
            self.lives_label = GLabel(f'Your Lives : {self.lives_left}')
            self.lives_label.color = 'hotpink'
            self.lives_label.font = 'Verdana-15-bold'
            self.window.add(self.lives_label, x=0, y=self.window.height)
            self.start_or_not = False
            self.window.add(self.ball, x=self.window_width / 2 - BALL_RADIUS,
                            y=self.window_height / 2 - BALL_RADIUS)

    def drag(self, mouse):
        if PADDLE_WIDTH / 2 <= mouse.x <= self.window.width - PADDLE_WIDTH / 2:
            self.paddle.x = mouse.x - PADDLE_WIDTH / 2

    def start(self, mouse):
        self.start_or_not = True
        self.window.remove(self.start_label)

    def get_dx(self):
        return self.__dx

    def get_dy(self):
        return self.__dy
