import math
import random
import time
from graphics import GraphWin, Circle, Point, color_rgb

def get_random_color():
    return color_rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def get_random(move_amount):
    return random.randint(-move_amount, move_amount)

def did_collide(ball1: Circle, ball2: Circle):
    one_x = ball1.getCenter().getX()
    one_y = ball1.getCenter().getY()
    two_x = ball2.getCenter().getX()
    two_y = ball2.getCenter().getY()
    # this uses the distance formula to calculate the (squared) distance between
    # the centers of the circles
    # if that distance is less than the sum of their radii (squared) then they are colliding
    center_distance = math.pow(one_x - two_x, 2) + math.pow(one_y - two_y, 2)
    radii_sum = math.pow(ball1.getRadius() + ball2.getRadius(), 2)
    return center_distance <= radii_sum

# these check if the edge of the ball (center +/- radius) is on the wrong side of the wall
def hit_vertical(ball: Circle, win: GraphWin):
    return ball.getCenter().getX() - ball.getRadius() <= 0 or \
           ball.getCenter().getX() + ball.getRadius() >= win.getWidth()

def hit_horizontal(ball: Circle, win: GraphWin):
    return ball.getCenter().getY() - ball.getRadius() <= 0 or \
           ball.getCenter().getY() + ball.getRadius() >= win.getHeight()

def main():
    win = GraphWin("Bumpers!", 600, 400)
    win.setBackground('white')
    # it is possible for the balls to get stuck either continuously bouncing off a wall or each other
    # if their movement is greater than their radius.
    # this also depends on how the did_collide, hit_verticle, and hit_horizontal functions are defined.
    radius = 30
    ball_one_y_delta = get_random(15)
    ball_one_x_delta = get_random(15)
    ball_two_x_delta = get_random(15)
    ball_two_y_delta = get_random(15)

    # starting points
    ball_one = Circle(Point(100, 100), radius)
    ball_two = Circle(Point(300, 300), radius)

    ball_one_color = get_random_color()
    ball_two_color = get_random_color()

    ball_one.setFill(ball_one_color)
    ball_two.setFill(ball_two_color)

    ball_one.draw(win)
    ball_two.draw(win)

    running = True
    while running:
        # move each ball
        ball_one.move(ball_one_x_delta, ball_one_y_delta)
        ball_two.move(ball_two_x_delta, ball_two_y_delta)

        # check if balls collide with each other or a wall
        # in any case, they need to move in the opposite direction of the collision
        if did_collide(ball_one, ball_two):
            ball_one_x_delta *= -1
            ball_one_y_delta *= -1
            ball_two_x_delta *= -1
            ball_two_y_delta *= -1

        if hit_vertical(ball_one, win):
            ball_one_x_delta *= -1

        if hit_vertical(ball_two, win):
            ball_two_x_delta *= -1

        if hit_horizontal(ball_one, win):
            ball_one_y_delta *= -1

        if hit_horizontal(ball_two, win):
            ball_two_y_delta *= -1

        time.sleep(0.02)

        # optional close
        click_point = win.checkMouse()
        if click_point and click_point.getY() < 50 and click_point.getX() < 50:
            running = False

    win.close()

if __name__ == '__main__':
    main()
