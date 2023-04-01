"""
The Player class represents the main character in the game.

Constructor:
    Player(x_coord: int, y_coord: int)
        - Constructs the player based on the window's dimensions.
        - x_coord, y_coord - The max x and y coordinates of the window.
                             These are used for determining the dimensions
                             of the player.

Instance Variables:
    shape: Circle - The outline of the player.
                  - A radius of 4% of the y_coord value is recommended
                  - The circle's center can start at the center of the screen (half the x and y coords)
    shapes: List[Shape] (List of graphics objects)
                - This is a list of all the shapes used to make the player (this list must include
                  at least 2 items, the player outline and one additional shape)
                - When moving and drawing the player we will need this list
                  to move and draw every shape in the list
    x_coord, y_coord: int
                - store the x and y coords passed into the constructor
                - we will need these values to make sure the player stays on the screen
                  when moving and when resetting the player's position

Methods:
    draw(win: GraphWin) -> None
        Takes a GraphWin object as a parameter and draws the player (all of the players's components) to the win
    move(direction: string) -> None
        Moves the player in the given direction
        the direction parameter will be the string "Right", "Left", "Up", or "Down"
            this is the result of calling win.checkKey() in main.py
            move the player's shapes accordingly based on whether direction is "Right", "Left", "Up", or "Down"
        The player should not be able to move off the screen.
        The amount the player moves (the player's speed), should be a percentage of
        the x_coord (1.3% of x_coord is recommended)
    is_hit(obstacle: Obstacle) -> bool
        This method is given to you
        Takes an Obstacle object as a parameter and returns True if the Player and the obstacle are
        touching/overlapping, otherwise False.
        This can be used when checking if an obstacle hit the player
    reset() -> None
        Moves the Player to the starting position in the middle of the screen
        Consider using the Player's move method along with x_coord and y_coord instance variable
        This method can be used if the Player gets hit and selects to play again
"""


class Player:

    def is_hit(self, obstacle):
        player_shape = self.shape
        center = player_shape.getCenter()
        obs = obstacle.get_shape()
        center_distances_x = abs(center.getX() - obs.getCenter().getX())
        center_distances_y = abs(center.getY() - obs.getCenter().getY())
        obs_width = abs(obs.getP1().getX() - obs.getP2().getX())
        obs_height = abs(obs.getP1().getY() - obs.getP2().getY())

        if center_distances_x > (obs_width / 2 + player_shape.getRadius()): return False
        if center_distances_y > (obs_height / 2 + player_shape.getRadius()): return False
        if center_distances_x <= (obs_width / 2): return True
        if center_distances_y <= (obs_height / 2): return True

        corner_distance_sq = ((center_distances_x - obs_width / 2) ** 2) + (center_distances_y - obs_height / 2) ** 2

        return corner_distance_sq <= player_shape.getRadius() ** 2
