
:warning: Everything between << >> needs to be replaced (remove << >> after replacing)

# Pong 
## CS110 B1 Final Project Semester 1, 2024

## Team Members

Michael Truong

***

## Project Description

A game of pong where opponents try to score in each other's goals. There will be a ball and controllable walls. When the ball hits a wall, the ball will go the opposite direction

***    

## GUI Design

### Initial Design

![initial gui](c:\final-project-michael\template_final_project-master\assets\gui.jpg)

### Final Design

![final gui]

## Program Design

### Features

1. Start Menu
2. Game score
3. Controllable walls
4. Balls that bounce 
5. Ability to add more balls

### Classes

- << You should have a list of each of your classes with a description >>

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

Step 1: Hit the ball with the pong table
Expected Results: The ball bounces
Step 2: Let the ball hit the wall
Expected Results: The ball bounces off the wall

Test Case 3 - Test if the ball resets if there is no hit by the paddles:

Step 1: Let the ball fall through the bottom
Expected Results: The ball spawns back in the middle
Step 2: Let the ball fall through the top
Expected Results: The ball spawns back in the middle

Test Case 4 - Test if the score keeper works:

Step 1: Let the ball get hit by the bottom paddle
Expected Results: +1 is added to the score for the bottom paddle
Step 2: Let the ball get hit by the top paddle
Expected Results: +1 is added to the score for the top paddle

Test Case 5 - Test if the end works:

Step 1: Let the ball fall through the bottom
Expected Results: The game ends and the winner is the bottom paddle
Step 2: Let the ball fall through the top
Expected Results: The game ends and the winner is the top paddle


