"""
This is where your game begins. There are many ways to arrange this module.
High level (very general) pseudocode and things to consider:
- Set up the window
- Initialize the player
- Initialize an empty obstacle list for storing all of the obstacles
  that are currently on the screen
- Initialize the score to 0
- Start the game loop
    - get the key press
    - create obstacles
        - you do not want to create an obstacle every time through the loop
          (creating an obstacle roughly every 1/100 loops seems to work well) 
        - how can you create obstacles on random occasions through the loop?
        - when an obstacle is created, draw it to the screen and add it to the
          obstacles list
    - move the player
    - move obstacles, check for hits with the player, and check if the obstacle is done (off the screen)
        - if an obstacle is done, undraw it and remove it from the obstacles list
    - set the score text
    - sleep (try 0.01 seconds to start)
    - handle if there was a hit
        - the general flow for if there was a hit
            1. - If the score is the highest score, print the
                 high score text for three seconds, then remove it
                    - To keep track of high scores, any top five high score
                      needs to be saved to a text file called highscores.txt
            2. - Display the screen that asks the user if they still want to play
               - The width and height of the screen should be 60 % of the window's
                 width and height
               - You can consider putting this functionality in a function where calling the function
                 displays the screen, waits for the click, clears the screen, and returns the result (yes/no)
               - Wait for the user to click either the yes or no button
            3. - If the user clicks yes, reset the hero, score, and undraw/remove all obstacles
               - You can consider putting this reset functionality in a function
            4. - If the user clicks no, display the top 5 high scores of all time
               - Exit the game after an additional user click
"""