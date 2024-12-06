

# Pong 

## CS110 B1 Final Project Semester 1, 2024

## Team Members

Michael Truong


## Project Description

A game of pong where a player will try to keep the ball in play for as long as possible. There will be a ball and controllable walls. When the ball hits a wall, the ball will go the opposite direction and the score will increase. There are two gamemodes, one for unlimited plays and the other where there are only two tries.

**** I mistook the controller file for the main so it has to be ran through the controller file in src
***    

## GUI Design

### Initial Design

(c:\final-project-michael\template_final_project-master\assets\gui.jpg)

### Final Design

(C:\final-project-michael\template_final_project-master\assets\final gui.png)

## Program Design

### Features

1. Start Menu
2. Game score
3. Controllable paddles
4. Balls that bounce off paddles
5. Gamemode choice

### Classes

1. Ball class creates the ball used with customizable features
2. Rectangle class creates the paddles used, with customizable features
3. Divider class creates lines that divide the screen
4. Colors class are what I used to import files and images 

## ATP

Test Case 1 - Test if the keys properly move the two tables
| Step                 |Procedure             |Expected Results                   |
|----------------------|:--------------------:|----------------------------------:|
|  1                   | Run Program          | Two pong tables appear            |
|  2                   | Press and hold a     | bottom board moves left           |
|  3                   | press and hold d     | bottom board moves right          |
|  4                   | press and hold left  | top board moves left              |
|  5                   | press and hold right | top board moves right             |

Test Case 2 - Test if the ball bounces on on the table/walls

Step 1: Hit the ball with the pong table.
Expected Results: The ball bounces.
Step 2: Let the ball hit the wall.
Expected Results: The ball bounces off the wall.

Test Case 3 - Test if the ball resets if there is no hit by the paddles:

Step 1: Let the ball fall through the bottom.
Expected Results: The ball spawns back in the middle.
Step 2: Let the ball fall through the top.
Expected Results: The ball spawns back in the middle.

Test Case 4 - Test if the score keeper works:

Step 1: Let the ball get hit by the bottom paddle.
Expected Results: +1 is added to the score.
Step 2: Let the ball get hit by the top paddle.
Expected Results: +1 is added to the score .

Test Case 5 - Test if the end works:

Step 1: Let the ball fall through the bottom.
Expected Results: One life is lost.
Step 2: Let the ball fall through the top.
Expected Results: One life is lost.

Test Case 6 - Gamemode 1 unlimited

Step 1: Let the ball fall through the bottom. Reapeat many times.
Expected Results: The game should not end.

Test case 7 - Gamemode 2 two lives
StEP 1: Let the ball fall through the bottom. Repeat twice
Expected Results: The game ends and a window saying "you lose!" appears.


