# Student ID : 19000687
# Date of last Modification : 13/4/2021
# 4COM1037 programing coursework



import turtle
import random
import time

def Shapes_configuration():             # Adding all shapes to be used in snakes and ladders game
    turtle.addshape("Images/Snakes & Ladders Logo.gif")                 #browse a certain shape from Images folder in project directory and adds it to turtle
    turtle.addshape("Images/Snakes & Ladders Logo mini.gif")            #browse a certain shape from Images folder in project directory and adds it to turtle
    turtle.addshape("Images/Border.gif")                                #browse a certain shape from Images folder in project directory and adds it to turtle
    turtle.addshape("Images/VS.gif")                                    #browse a certain shape from Images folder in project directory and adds it to turtle

    turtle.addshape("Images/cow.gif")                                   #browse a certain shape from Images folder in project directory and adds it to turtle
    turtle.addshape("Images/bull.gif")                                  #browse a certain shape from Images folder in project directory and adds it to turtle
    turtle.addshape("Images/Dog.gif")                                   #browse a certain shape from Images folder in project directory and adds it to turtle
    turtle.addshape("Images/horse.gif")                                 #browse a certain shape from Images folder in project directory and adds it to turtle
    turtle.addshape("Images/Lion.gif")                                  #browse a certain shape from Images folder in project directory and adds it to turtle
    turtle.addshape("Images/Giraffe.gif")                               #browse a certain shape from Images folder in project directory and adds it to turtle
    turtle.addshape("Images/Kwala.gif")                                 #browse a certain shape from Images folder in project directory and adds it to turtle
    turtle.addshape("Images/Elephante.gif")                             #browse a certain shape from Images folder in project directory and adds it to turtle

    turtle.addshape("Images/ladder.gif")                                #browse a certain shape from Images folder in project directory and adds it to turtle
    turtle.addshape("Images/ladder2.gif")                               #browse a certain shape from Images folder in project directory and adds it to turtle
    turtle.addshape("Images/ladder3.gif")                               #browse a certain shape from Images folder in project directory and adds it to turtle
    turtle.addshape("Images/Level2/ladder3.gif")                        #browse a certain shape from Images folder in project directory and adds it to turtle
    turtle.addshape("Images/Level3/ladder3.gif")                        #browse a certain shape from Images folder in project directory and adds it to turtle

    turtle.addshape("Images/snake.gif")                                 #browse a certain shape from Images folder in project directory and adds it to turtle
    turtle.addshape("Images/snake2.gif")                                #browse a certain shape from Images folder in project directory and adds it to turtle
    turtle.addshape("Images/snake3.gif")                                #browse a certain shape from Images folder in project directory and adds it to turtle
    turtle.addshape("Images/Level2/snake3.gif")                         #browse a certain shape from Images folder in project directory and adds it to turtle
    turtle.addshape("Images/Level3/snake2.gif")  # browse a certain shape from Images folder in project directory and adds it to turtle

    turtle.addshape("Images/dice1.gif")                                 #browse a certain shape from Images folder in project directory and adds it to turtle
    turtle.addshape("Images/dice2.gif")                                 #browse a certain shape from Images folder in project directory and adds it to turtle
    turtle.addshape("Images/dice3.gif")                                 #browse a certain shape from Images folder in project directory and adds it to turtle
    turtle.addshape("Images/dice4.gif")                                 #browse a certain shape from Images folder in project directory and adds it to turtle
    turtle.addshape("Images/dice5.gif")                                 #browse a certain shape from Images folder in project directory and adds it to turtle
    turtle.addshape("Images/dice6.gif")                                 #browse a certain shape from Images folder in project directory and adds it to turtle

    turtle.addshape("Images/win.gif")                                   #browse a certain shape from Images folder in project directory and adds it to turtle

########################################################################################################################
########################################################################################################################

def setup_background():             # this function setups background color, turtle pen color as well as turtle speed at beginning of certain functions
    turtle.bgcolor("#81DB5D")       # Modifying background color to color code #81DB5D
    turtle.hideturtle()             # hides the turtle shape from being displayed on screen while drawing
    turtle.pencolor("#0039C7")      # Modifying pen color to color code #0039C7
    turtle.speed(10)                # Making turtle speed to 10 (Medium)
########################################################################################################################
########################################################################################################################

def Home_Page():                    # Displays Home screen visuals (starting screen)
    setup_background()              # calling setup_background function

    Logo = turtle.Turtle()          # Defining a new turtle called logo
    Logo.shape("Images/Snakes & Ladders Logo.gif")      # Changing logo shape to a certain shape found in Images folder
    Logo.penup()                    # Disables turtle from drawing on screen
    Logo.goto(0, 250)               # Makes turtle named Logo go to co-ordinates 0 on x axis and 250 on y axis
    ####################################################################################################################
    turtle1 = turtle.Turtle()       # Defining a new turtle called turtle1
    turtle1.left(90)                # Turns turtle named turtle1 90 degrees to the left
    turtle1.shape("turtle")         # Changing turtle1 shape to a pre-defined turtle shape called turtle
    turtle1.penup()                 # Disables turtle from drawing on screen
    turtle1.goto(-140, 15)          # Makes turtle named turtle1 go to co-ordinates -140 on x axis and 15 on y axis

    turtle.penup()                  # Disables turtle from drawing on screen
    turtle.goto(0, 0)               # Makes main turtle go to co-ordinates 0 on x axis and 0 on y axis
    turtle.write("Single Player", align="center", font=("Verdana", 25, "bold"))     # Makes main turtle write a message on screen with certain font and alignment properties

    border1 = turtle.Turtle()       # Defining a new turtle called border1
    border1.shape("Images/Border.gif")      # Changing border1 shape to a certain shape found in Images folder
    border1.penup()                 # Disables turtle from drawing on screen
    border1.goto(0, 15)             # Makes turtle named border1 go to co-ordinates 0 on x axis and 15 on y axis
    ####################################################################################################################
    turtle2 = turtle.Turtle()       # Defining a new turtle called turtle2
    turtle2.left(90)                # Turns turtle named turtle2 90 degrees to the left
    turtle2.shape("turtle")         # Changing turtle2 shape to a pre-defined turtle shape called turtle
    turtle2.penup()                 # Disables turtle from drawing on screen
    turtle2.goto(-145, -185)        # Makes turtle named turtle2 go to co-ordinates -145 on x axis and -185 on y axis

    turtle3 = turtle.Turtle()       # Defining a new turtle called turtle3
    turtle3.left(90)                # Turns turtle named turtle3 90 degrees to the left
    turtle3.shape("turtle")         # Changing turtle3 shape to a pre-defined turtle shape called turtle
    turtle3.penup()                 # Disables turtle from drawing on screen
    turtle3.goto(-125, -185)        # Makes turtle named turtle3 go to co-ordinates -125 on x axis and -185 on y axis

    turtle.goto(0, -200)            # Makes main turtle go to co-ordinates 0 on x axis and -200 on y axis
    turtle.write("Multi Player", align="center", font=("Verdana", 25, "bold"))  # Makes main turtle write a message on screen with certain font and alignment properties

    border2 = turtle.Turtle()       # Defining a new turtle called border2
    border2.hideturtle()            # Disables the turtle shape from showing on screen
    border2.shape("Images/Border.gif")      # Changing border2 shape to a certain shape found in Images folder
    border2.penup()                 # Disables turtle from drawing on screen
    border2.goto(0, -185)           # Makes turtle named border2 go to co-ordinates 0 on x axis and -185 on y axis
    border2.showturtle()            # Enables the turtle shape to be shown on screen
    ####################################################################################################################
    turtle.goto(0, -350)            # Makes main turtle go to co-ordinates 0 on x axis and -350 on y axis
    turtle.write("Note: Press 1 for Single Player and 2 for Multi Player.", align="center",
                 font=("Verdana", 18, "normal"))  # Makes main turtle write a message on screen with certain font and alignment properties

########################################################################################################################
########################################################################################################################

def Check_valid_answer(Number_List, calling_number):            # This function asks user to enter his choice and checks if his choice is found in the Number_List (choice list)
                                                                # If the user choice is correct it returns the answer of the user (His choice)
                                                                # Else it prints for the user a certain message according to the stage of the program identified by the calling number


    Answer = input("Please enter the appropriate number: ")     # Asks the user to input his choice
    No_Answer = True                                            # setting the value of No_Answer to True
    while No_Answer == True:                                    # loops until the user inputs a correct choice
        if Answer in Number_List:                               # checks if user input(Answer) is correct by checking if its found in Number_List
            No_Answer = False                                   # setting the value of No_Answer to False
            return int(Answer)                                  # returns the correct user Answer in an integer format
        else:                                                   # if user input is not valid
            No_Answer = True                                    # No_Answer value remains True
            print("User Input:", Answer)                        # prints the incorrect user input
            if calling_number == 1:                             # checks to see if calling_number value is equal to 1 (Stage 1)
                print("  Available options  ".center(50, "*"), "\n 1 For Single Player \t\t 2 For Multi Player")  #prints a certain message to user to clarify correct answer options
                print("  Please type a valid number  ".center(50, "*"), '\n')                                     #prints a certain message to user to ask for valid number
                Answer = input("Please enter 1 for Single Player and 2 for Multi-Player: ")                       # asks user to input another Answer
            elif calling_number == 2:                           # checks to see if calling_number value is equal to 2 (Stage 2)
                print("  Available options  ".center(50, "*"), "\n 1 For Easy \t\t 2 For Medium\t\t 3 For Hard")  # checks to see if calling_number value is equal to 2 (Stage 2)
                print("  Please type a valid number  ".center(50, "*"), '\n')                                     #prints a certain message to user to ask for valid number
                Answer = input("Please enter 1 for Easy , 2 for Medium and 3 for Hard: ")                         # asks user to input another Answer
            elif calling_number == 3:                           # checks to see if calling_number value is equal to 3 (Stage 3)
                print("  Available options  ".center(60, "*"),
                      "\n1 For cow\t\t2 For Bull\t\t3 For Dog\t\t",
                      "\n4 For Panda\t\t5 For Lion\t\t6 For Koala\t\t",
                      "\n7 For Elephant\t8 For Giraffe\t\t")                          # checks to see if calling_number value is equal to 2 (Stage 2)
                print("  Please type a valid number  ".center(60, "*"), '\n')                                     #prints a certain message to user to ask for valid number
                Answer = input("Please enter the appropriate number(1 to 8): ")                                   # asks user to input another Answer

########################################################################################################################
########################################################################################################################

def ask_player_name(user_choice1):                                  # This function asks for user name one or two times according to user_choice1 ( single or multi player)
                                                                    # then it returns the two player names (the second name is CPU by default if user_choice1 is 1 )
    if user_choice1 == 1:                                           # Checks if user choice is 1 (Single player)
        player1_name = input("\nPlease enter name for player 1: ")  # Asks user to input his/her name
        player2_name = "CPU"                                        # Assign player 2's name to CPU
    elif user_choice1 == 2:                                         # Checks if user choice is 2 (Multi-player)
        player1_name = input("\nPlease enter name for player 1: ")  # Asks user to input his/her name
        player2_name = input("\nPlease enter name for player 2: ")  # Asks user to input his/her name
    return player1_name,player2_name                                # returns player 1 and player 2's names

########################################################################################################################
########################################################################################################################

def Game_mode(user_choice1):                                        # Displays Game mode screen visuals (easy_medium_hard screen)
    turtle.clearscreen()                                            # This clears all screen properties and turtles previously used
    setup_background()                                              # Calls the function setup_background

    Logo = turtle.Turtle()                                          # Defines a new turtle named Logo
    Logo.shape("Images/Snakes & Ladders Logo.gif")                  # Changing Logo shape to a certain shape found in Images folder
    Logo.penup()                                                    # Disables turtle from drawing on screen
    player1_name,player2_name = ask_player_name(user_choice1)       # Calling ask_player_name function and retrieving player 1 and 2 names
    Logo.goto(0, 250)                                               # Makes turtle named Logo go to co-ordinates 0 on x axis and 250 on y axis
    ####################################################################################################################
    turtle1 = turtle.Turtle()                                       # Defines a new turtle named turtle1
    turtle1.left(90)                                                # Turns turtle named turtle1 90 degrees to the left
    turtle1.shape("turtle")                                         # Changing turtle1 shape to a pre-defined shape named turtle
    turtle1.penup()                                                 # Disables turtle from drawing on screen
    turtle1.goto(-140, 15)                                          # Makes turtle named turtle1 go to co-ordinates -140 on x axis and 15 on y axis

    turtle.penup()                                                  # Disables turtle from drawing on screen
    turtle.goto(0, 0)                                               # Makes main turtle go to co-ordinates 0 on x axis and 0 on y axis
    turtle.write("Easy", align="center", font=("Verdana", 25, "bold"))      # Makes main turtle write a message on screen with certain font and alignment properties

    border1 = turtle.Turtle()                                       # Defines a new turtle named border1
    border1.shape("Images/Border.gif")                              # Changing border1 shape to a certain shape found in Images folder
    border1.penup()                                                 # Disables turtle from drawing on screen
    border1.goto(0, 15)                                             # Makes turtle named border1 go to co-ordinates 0 on x axis and 15 on y axis
    ####################################################################################################################
    turtle2 = turtle.Turtle()                                       # Defines a new turtle named turtle2
    turtle2.left(90)                                                # Turns turtle named turtle2 90 degrees to the left
    turtle2.shape("turtle")                                         # Changing turtle2 shape to a pre-defined shape named turtle
    turtle2.penup()                                                 # Disables turtle from drawing on screen
    turtle2.goto(-145, -85)                                         # Makes turtle named turtle2 go to co-ordinates -145 on x axis and -85 on y axis

    turtle3 = turtle.Turtle()                                       # Defines a new turtle named turtle3
    turtle3.left(90)                                                # Turns turtle named turtle3 90 degrees to the left
    turtle3.shape("turtle")                                         # Changing turtle3 shape to a pre-defined shape named turtle
    turtle3.penup()                                                 # Disables turtle from drawing on screen
    turtle3.goto(-125, -85)                                         # Makes turtle named turtle3 go to co-ordinates -125 on x axis and -85 on y axis

    turtle.goto(0, -100)                                            # Makes main turtle go to co-ordinates 0 on x axis and -100 on y axis
    turtle.write("Medium", align="center", font=("Verdana", 25, "bold"))        # Makes main turtle write a message on screen with certain font and alignment properties

    border2 = turtle.Turtle()                                       # Defines a new turtle named border2
    border2.hideturtle()                                            # Disables the turtle shape to be shown on screen
    border2.shape("Images/Border.gif")                              # Changing border2 shape to a certain shape found in Images folder
    border2.penup()                                                 # Disables turtle from drawing on screen
    border2.goto(0, -85)                                            # Makes turtle named border2 go to co-ordinates 0 on x axis and -85 on y axis
    border2.showturtle()                                            # Enables the turtle shape to be shown on screen
    ####################################################################################################################
    turtle4 = turtle.Turtle()                                       # Defines a new turtle named turtle4
    turtle4.left(90)                                                # Turns turtle named turtle4 90 degrees to the left
    turtle4.shape("turtle")                                         # Changing turtle4 shape to a pre-defined shape named turtle
    turtle4.penup()                                                 # Disables turtle from drawing on screen
    turtle4.goto(-145, -205)                                        # Makes turtle named turtle4 go to co-ordinates -145 on x axis and -205 on y axis

    turtle5 = turtle.Turtle()                                       # Defines a new turtle named turtle5
    turtle5.left(90)                                                # Turns turtle named turtle5 90 degrees to the left
    turtle5.shape("turtle")                                         # Changing turtle5 shape to a pre-defined shape named turtle
    turtle5.penup()                                                 # Disables turtle from drawing on screen
    turtle5.goto(-125, -205)                                        # Makes turtle named turtle5 go to co-ordinates -125 on x axis and -205 on y axis

    turtle6 = turtle.Turtle()                                       # Defines a new turtle named turtle6
    turtle6.left(90)                                                # Turns turtle named turtle6 90 degrees to the left
    turtle6.shape("turtle")                                         # Changing turtle6 shape to a pre-defined shape named turtle
    turtle6.penup()                                                 # Disables turtle from drawing on screen
    turtle6.goto(-135, -185)                                        # Makes turtle named turtle6 go to co-ordinates -135 on x axis and -185 on y axis

    turtle.goto(0, -200)                                            # Makes main turtle go to co-ordinates 0 on x axis and -200 on y axis
    turtle.write("Hard", align="center", font=("Verdana", 25, "bold"))      # Makes main turtle write a message on screen with certain font and alignment properties

    border3 = turtle.Turtle()                                       # Defines a new turtle named border3
    border3.hideturtle()                                            # Disables the turtle shape to be shown on screen
    border3.shape("Images/Border.gif")                              # Changing border3 shape to a certain shape found in Images folder
    border3.penup()                                                 # Disables turtle from drawing on screen
    border3.goto(0, -185)                                           # Makes turtle named border3 go to co-ordinates 0 on x axis and -185 on y axis
    border3.showturtle()                                            # Enables the turtle shape to be shown on screen
    ####################################################################################################################
    turtle.goto(0, -350)                                            # Makes main turtle go to co-ordinates 0 on x axis and -350 on y axis
    turtle.write("Note: Press 1 for Easy , 2 for Medium and 3 for Hard.", align="center",
                 font=("Verdana", 18, "normal"))                    # Makes main turtle write a message on screen with certain font and alignment properties
    return player1_name,player2_name                                # returns player 1 and player 2 names to main function

########################################################################################################################
########################################################################################################################

def add_shapes(user_choice2 = 1):                                   # This function adds all snakes and ladders to the board according to user_choice2 (difficulty level chosen by user)
                                                                    # user_choice2 equal 1 means easy mode, 2 means medium mode and 3 means hard mode
    if user_choice2 ==1:                                            # Checks if user_choice2 is equal to 1 which means easy mode
        ladder = turtle.Turtle()                                    # Defines a new turtle named ladder
        ladder.shape("Images/ladder.gif")                           # Changing ladder shape to a certain shape found in Images folder
        ladder.penup()                                              # Disables turtle from drawing on screen
        ladder.goto(-100,-50)                                       # Makes turtle named ladder go to co-ordinates -100 on x axis and -50 on y axis

        ladder2 = turtle.Turtle()                                   # Defines a new turtle named ladder2
        ladder2.shape("Images/ladder2.gif")                         # Changing ladder2 shape to a certain shape found in Images folder
        ladder2.penup()                                             # Disables turtle from drawing on screen
        ladder2.goto(0,150)                                         # Makes turtle named ladder2 go to co-ordinates 0 on x axis and 150 on y axis

        ladder3 = turtle.Turtle()                                   # Defines a new turtle named ladder3
        ladder3.shape("Images/ladder3.gif")                         # Changing ladder3 shape to a certain shape found in Images folder
        ladder3.penup()                                             # Disables turtle from drawing on screen
        ladder3.goto(200,-100)                                      # Makes turtle named ladder3 go to co-ordinates 200 on x axis and -100 on y axis

        snake = turtle.Turtle()                                     # Defines a new turtle named snake
        snake.shape("Images/snake.gif")                             # Changing snake shape to a certain shape found in Images folder
        snake.penup()                                               # Disables turtle from drawing on screen
        snake.goto(100,100)                                         # Makes turtle named snake go to co-ordinates 100 on x axis and 100 on y axis

        snake2 = turtle.Turtle()                                    # Defines a new turtle named snake2
        snake2.shape("Images/snake2.gif")                           # Changing snake2 shape to a certain shape found in Images folder
        snake2.penup()                                              # Disables turtle from drawing on screen
        snake2.goto(0,-150)                                         # Makes turtle named snake2 go to co-ordinates 0 on x axis and -150 on y axis

        snake3 = turtle.Turtle()                                    # Defines a new turtle named snake3
        snake3.shape("Images/snake3.gif")                           # Changing snake3 shape to a certain shape found in Images folder
        snake3.penup()                                              # Disables turtle from drawing on screen
        snake3.goto(-200,-35)                                       # Makes turtle named snake3 go to co-ordinates -200 on x axis and -35 on y axis

    elif user_choice2 == 2:                                         # Checks if user_choice2 is equal to 2 which means medium mode
        snake = turtle.Turtle(shape="Images/snake.gif")             # Defines a new turtle named snake with a certain shape from Images folder
        snake.penup()                                               # Disables turtle from drawing on screen
        snake.goto(300,100)                                         # Makes turtle named snake go to co-ordinates 300 on x axis and 100 on y axis

        snake2 = turtle.Turtle(shape="Images/snake2.gif")           # Defines a new turtle named snake2 with a certain shape from Images folder
        snake2.penup()                                              # Disables turtle from drawing on screen
        snake2.goto(90,-250)                                        # Makes turtle named snake2 go to co-ordinates 90 on x axis and -250 on y axis

        snake4 = turtle.Turtle(shape="Images/snake2.gif")           # Defines a new turtle named snake4 with a certain shape from Images folder
        snake4.penup()                                              # Disables turtle from drawing on screen
        snake4.goto(90,50)                                          # Makes turtle named snake4 go to co-ordinates 90 on x axis and 50 on y axis

        snake3 = turtle.Turtle(shape="Images/Level2/snake3.gif")    # Defines a new turtle named snake3 with a certain shape from Images folder
        snake3.penup()                                              # Disables turtle from drawing on screen
        snake3.goto(-203, 0)                                        # Makes turtle named snake3 go to co-ordinates -203 on x axis and 0 on y axis

        ladder = turtle.Turtle(shape="Images/ladder.gif")           # Defines a new turtle named ladder with a certain shape from Images folder
        ladder.penup()                                              # Disables turtle from drawing on screen
        ladder.goto(-100,-50)                                       # Makes turtle named ladder go to co-ordinates -100 on x axis and -50 on y axis

        ladder2 = turtle.Turtle(shape="Images/ladder2.gif")         # Defines a new turtle named ladder2 with a certain shape from Images folder
        ladder2.penup()                                             # Disables turtle from drawing on screen
        ladder2.goto(0,150)                                         # Makes turtle named ladder2 go to co-ordinates 0 on x axis and 150 on y axis

        ladder3 = turtle.Turtle(shape="Images/Level2/ladder3.gif")  # Defines a new turtle named ladder3 with a certain shape from Images folder
        ladder3.penup()                                             # Disables turtle from drawing on screen
        ladder3.goto(390, -110)                                     # Makes turtle named ladder3 go to co-ordinates 390 on x axis and -110 on y axis

    else:                                                           # Checks if user_choice2 is not equal to 1 or 2, which means it is 3 for hard mode
        snake = turtle.Turtle(shape="Images/snake.gif")             # Defines a new turtle named snake with a certain shape from Images folder
        snake.penup()                                               # Disables turtle from drawing on screen
        snake.goto(454,-4)                                          # Makes turtle named snake go to co-ordinates 454 on x axis and -4 on y axis

        snake2 = turtle.Turtle(shape="Images/snake2.gif")           # Defines a new turtle named snake2 with a certain shape from Images folder
        snake2.penup()                                              # Disables turtle from drawing on screen
        snake2.goto(140,-235)                                       # Makes turtle named snake2 go to co-ordinates 140 on x axis and -235 on y axis

        snake5 = turtle.Turtle(shape="Images/snake2.gif")           # Defines a new turtle named snake5 with a certain shape from Images folder
        snake5.penup()                                              # Disables turtle from drawing on screen
        snake5.goto(-250,-310)                                      # Makes turtle named snake5 go to co-ordinates -250 on x axis and -310 on y axis

        snake6 = turtle.Turtle(shape="Images/Level3/snake2.gif")    # Defines a new turtle named snake6 with a certain shape from Images folder
        snake6.penup()                                              # Disables turtle from drawing on screen
        snake6.goto(215,195)                                        # Makes turtle named snake6 go to co-ordinates 215 on x axis and 195 on y axis

        snake3 = turtle.Turtle(shape="Images/Level2/snake3.gif")    # Defines a new turtle named snake3 with a certain shape from Images folder
        snake3.penup()                                              # Disables turtle from drawing on screen
        snake3.goto(-170, 78)                                       # Makes turtle named snake3 go to co-ordinates -170 on x axis and 78 on y axis

        snake4 = turtle.Turtle(shape="Images/snake.gif")            # Defines a new turtle named snake4 with a certain shape from Images folder
        snake4.penup()                                              # Disables turtle from drawing on screen
        snake4.goto(-15,-80)                                        # Makes turtle named snake4 go to co-ordinates -15 on x axis and -80 on y axis

        ladder = turtle.Turtle(shape="Images/ladder.gif")           # Defines a new turtle named ladder with a certain shape from Images folder
        ladder.penup()                                              # Disables turtle from drawing on screen
        ladder.goto(300,-155)                                       # Makes turtle named ladder go to co-ordinates 300 on x axis and -155 on y axis

        ladder2 = turtle.Turtle(shape="Images/ladder2.gif")         # Defines a new turtle named ladder2 with a certain shape from Images folder
        ladder2.penup()                                             # Disables turtle from drawing on screen
        ladder2.goto(-8,231)                                        # Makes turtle named ladder2 go to co-ordinates -8 on x axis and 231 on y axis

        ladder3 = turtle.Turtle(shape="Images/Level3/ladder3.gif")  # Defines a new turtle named ladder3 with a certain shape from Images folder
        ladder3.penup()                                             # Disables turtle from drawing on screen
        ladder3.goto(62, -175)                                    # Makes turtle named ladder3 go to co-ordinates 62 on x axis and -175 on y axis

        ladder4 = turtle.Turtle(shape="Images/ladder2.gif")         # Defines a new turtle named ladder4 with a certain shape from Images folder
        ladder4.penup()                                             # Disables turtle from drawing on screen
        ladder4.goto(380,315)                                       # Makes turtle named ladder4 go to co-ordinates 380 on x axis and 315 on y axis

########################################################################################################################
########################################################################################################################

def Make_Square(character_index):                                   # This function takes the character index and draws a square around the character which the player choose
    pencil = turtle.Turtle(visible=False)                           # Defines a new turtle named pencil which has a hidden shape property
    pencil.color("red")                                             # Changing turtle color to Red which is predefined in turtle library
    pencil.width(10)                                                # Adjusting turtle thickness to 10 pixels
    starting_point_Coordinations = [[0, 0], [-350, 150], [-150, 150], [50, 150], [250, 150], [-350, -50], [-150, -50],
                                    [50, -50], [250, -50]]          # This list contains all starting points from which we start drawing the square.
                                                                    # We have 8 characters so that means 8 starting points.
                                                                    # The first point [0,0] is not a starting point it is used to adjust index of list so it starts from 1

    pencil.penup()                                                  # Disables turtle from drawing on screen
    pencil.goto(starting_point_Coordinations[character_index][0], starting_point_Coordinations[character_index][1])     # telling turtle to go to starting_point_Coordinate referred to by the user from the list
    pencil.pendown()                                                # Enables turtle from drawing on screen
    for square_line in range(4):                                    # looping 4 times to draw 4 lines of square
        pencil.forward(100)                                         # Makes turtle named pencil move forward in the direction its facing by 100 pixels
        pencil.right(90)                                            # Turns turtle named pencil 90 degrees to the left

########################################################################################################################
########################################################################################################################

def Write_character_names():                                        # This function writes names of characters as well as the number they are referred to with
    characters = ['empty', '1 = Cow', '2 = Bull', '3 = Dog', '4 = Horse', '5 = Lion', '6 = Koala',
                  '7 = Elephant', '8 = Giraffe']                    # This list contains names of characters and their numbers.
                                                                    # The first string "empty" is not a character name it is used to adjust index of list so it starts from 1
    pencil = turtle.Turtle(visible=False)                           # Defines a new turtle named pencil which has a hidden shape property
    pencil.speed(0)                                                 # Making turtle speed to 0 (High speed)
    pencil.penup()                                                  # Disables turtle from drawing on screen
    pencil.goto(-350, 170)                                          # Makes turtle named pencil go to co-ordinates -350 on x axis and 170 on y axis
    for character_number in range(1, 5):                            # looping through the first 4 characters in list starting from index 1 till 4
        pencil.write(characters[character_number], align="left", font=("Verdana", 18, "normal"))  # writes the character name and number in the list on the screen which is referred to by character_number
        pencil.forward(200)                                         # Makes turtle named pencil move forward in the direction its facing by 200 pixels
    pencil.goto(-350, -30)                                          # Makes turtle named pencil go to co-ordinates -350 on x axis and -30 on y axis
    for character_number in range(5, 9):                            # looping through the last 4 characters in list starting from index 5 till 8
        pencil.write(characters[character_number], align="left", font=("Verdana", 18, "normal"))  # writes the character name and number in the list on the screen which is referred to by character_number
        pencil.forward(200)                                         # Makes turtle named pencil move forward in the direction its facing by 200 pixels

########################################################################################################################
########################################################################################################################

def Character_choosing(players_number):
    turtle.clearscreen()                                         # This clears all screen properties and turtles previously used
    setup_background()                                           # Calls the function setup_background

    cow = turtle.Turtle(shape="Images/cow.gif")                  # Defines a new turtle named cow with a certain shape from Images folder
    bull = turtle.Turtle(shape="Images/bull.gif")                # Defines a new turtle named bull with a certain shape from Images folder
    dog = turtle.Turtle(shape="Images/Dog.gif")                  # Defines a new turtle named dog with a certain shape from Images folder
    horse = turtle.Turtle(shape="Images/horse.gif")              # Defines a new turtle named horse with a certain shape from Images folder
    lion = turtle.Turtle(shape="Images/Lion.gif")                # Defines a new turtle named lion with a certain shape from Images folder
    giraffe = turtle.Turtle(shape="Images/Giraffe.gif")          # Defines a new turtle named giraffe with a certain shape from Images folder
    kwala = turtle.Turtle(shape="Images/Kwala.gif")              # Defines a new turtle named kwala with a certain shape from Images folder
    elephant = turtle.Turtle(shape="Images/Elephante.gif")       # Defines a new turtle named elephant with a certain shape from Images folder

    animals = ['nothing', cow, bull, dog, horse, lion, kwala, elephant, giraffe]     # list containing all character turtles which can be chosen by the user
                                                                                     # by putting all turtles in a list we can refer to each one of them by their list index number
                                                                                     # The first string "nothing" is not a turtle name it is used to adjust index of list so it starts from 1

    cow.penup()                                                 # Disables turtle from drawing on screen
    bull.penup()                                                # Disables turtle from drawing on screen
    dog.penup()                                                 # Disables turtle from drawing on screen
    horse.penup()                                               # Disables turtle from drawing on screen
    lion.penup()                                                # Disables turtle from drawing on screen
    kwala.penup()                                               # Disables turtle from drawing on screen
    elephant.penup()                                            # Disables turtle from drawing on screen
    giraffe.penup()                                             # Disables turtle from drawing on screen


    turtle.penup()                                              # Disables turtle from drawing on screen
    turtle.goto(0, 300)                                         # Makes main turtle go to co-ordinates 0 on x axis and 300 on y axis
    turtle.write("Please Choose the Characters to Start Game", align="center", font=("Verdana", 25, "normal"))      # Makes main turtle write a message on screen with certain font and alignment properties

    cow.goto(-300, 100)                                         # Makes turtle named pencil go to co-ordinates -350 on x axis and -30 on y axis
    bull.goto(-100, 100)                                        # Makes turtle named bull go to co-ordinates -100 on x axis and 100 on y axis
    dog.goto(100, 100)                                          # Makes turtle named dog go to co-ordinates 100 on x axis and 100 on y axis
    horse.goto(300, 100)                                        # Makes turtle named horse go to co-ordinates 300 on x axis and 100 on y axis
    lion.goto(-300, -100)                                       # Makes turtle named lion go to co-ordinates -300 on x axis and -100 on y axis
    kwala.goto(-100, -100)                                      # Makes turtle named kwala go to co-ordinates -100 on x axis and -100 on y axis
    elephant.goto(100, -100)                                    # Makes turtle named elephant go to co-ordinates -100 on x axis and -100 on y axis
    giraffe.goto(300, -100)                                     # Makes turtle named giraffe go to co-ordinates 300 on x axis and -100 on y axis

    Write_character_names()                                     # Calling the function Write_character_names()

    turtle.goto(0, -350)                                        # Makes main turtle go to co-ordinates 0 on x axis and -350 on y axis
    turtle.write("Note: Press the appropriate number referring to\n\tthe character you want (1 to 8).",
                 align="center", font=("Verdana", 18, "normal"))# Makes main turtle write a message on screen with certain font and alignment properties

    user_choices = []                                           # Defining an empty list that will store all player choices later on
    for Player in range(players_number):                        # looping according to player number
        user_choice3 = Check_valid_answer(['1', '2', '3', '4', '5', '6', '7', '8'], 3)      # Calling Check_valid_answer function and passing list of all choices and current stage number
                                                                                            # The valid user choice gets stored in user_choice3
        user_choices.append(animals[user_choice3])                                          # adding the player's choice to the user_choices list previously defined
        Make_Square(user_choice3)                                                           # Calling the Make_Square function and passing the correct user choice to it so it can draw a square around the character chosen
    if players_number == 1:                                                                 # Checks if number of players equals to 1 (which means single player and second player is gonna be the CPU)
        cpu_choice = random.randint(1, 8)                                                   # Getting a random number from 1 to 8 and storing it in cpu_choice
        user_choices.append(animals[cpu_choice])                                            # adding the CPU's choice to the user_choices list
        Make_Square(cpu_choice)                                                             # Calling the Make_Square function and passing the CPU's choice to it so it can draw a square around the character chosen

    time.sleep(1)                                           # Makes the program halt execution for 1 sec
    turtle.resetscreen()                                    # Resets all turtles to default properties and erases all their drawings
    turtle.clearscreen()                                    # This clears all screen properties and turtles previously used


    cow.hideturtle()                                        # Disables the turtle shape to be shown on screen
    bull.hideturtle()                                       # Disables the turtle shape to be shown on screen
    dog.hideturtle()                                        # Disables the turtle shape to be shown on screen
    horse.hideturtle()                                      # Disables the turtle shape to be shown on screen
    lion.hideturtle()                                       # Disables the turtle shape to be shown on screen
    kwala.hideturtle()                                      # Disables the turtle shape to be shown on screen
    elephant.hideturtle()                                   # Disables the turtle shape to be shown on screen
    giraffe.hideturtle()                                    # Disables the turtle shape to be shown on screen
    turtle.hideturtle()                                     # Disables the turtle shape to be shown on screen

    return user_choices[0], user_choices[1]                 # returns the 2 turtles stored in user_choices(whether 2 players or 1 player and a CPU)

########################################################################################################################
########################################################################################################################

def board(user_choice2=1):                                  # This function is used to draw board on screen

    setup_background()                                      # Calling the function setup_background
    if user_choice2 == 1:                                   # Checks if user_choice2 is equal to 1 (easy mode) and modifies the board properties accordingly
        x_coordinate = 250                                  # Assigns the value 250 to x_coordinate
        y_coordinate = 250                                  # Assigns the value 250 to y_coordinate
        difficulty_level = 11                               # Assigning the value 11 to difficulty level (Half the number of lines needed to draw the full board since in each for loop iteration we draw 2 lines)
        prior_switch_line = 4                               # prior switch is the line number right before making turtle switch from drawing horizontal lines to vertical lines
        after_switch_line = 6                               # after switch is the line number right after making turtle switch from drawing horizontal lines to vertical lines
        square_edge = 500                                   # Assigning the value 500 to square edge (the side length of the full board)
        small_square_edge = 100                             # Assigning the value 100 to small square edge (the side length of 1 small square)

    elif user_choice2 == 2:                                 # checks if user_choice2 is equal to 2 (medium mode) and modifies the board properties accordingly
        x_coordinate = 270                                  # Assigns the value 270 to x_coordinate
        y_coordinate = 350                                  # Assigns the value 350 to y_coordinate
        difficulty_level = 15                               # Assigning the value 15 to difficulty level (Half the number of lines needed to draw the full board since in each for loop iteration we draw 2 lines)
        prior_switch_line = 6                               # prior switch is the line number right before making turtle switch from drawing horizontal lines to vertical lines
        after_switch_line = 8                               # after switch is the line number right after making turtle switch from drawing horizontal lines to vertical lines
        square_edge = 700                                   # Assigning the value 700 to square edge (the side length of the full board)
        small_square_edge = 100                             # Assigning the value 100 to small square edge (the side length of 1 small square)

    elif user_choice2 == 3:                                 # checks if user_choice2 is equal to 3 (hard mode) and modifies the board properties accordingly
        x_coordinate = 300                                  # Assigns the value 300 to x_coordinate
        y_coordinate = 394                                  # Assigns the value 394 to y_coordinate
        difficulty_level = 21                               # Assigning the value 21 to difficulty level (Half the number of lines needed to draw the full board since in each for loop iteration we draw 2 lines)
        prior_switch_line = 9                               # prior switch is the line number right before making turtle switch from drawing horizontal lines to vertical lines
        after_switch_line = 11                              # after switch is the line number right after making turtle switch from drawing horizontal lines to vertical lines
        square_edge = 780                                   # Assigning the value 780 to square edge (the side length of the full board)
        small_square_edge = 78                              # Assigning the value 78 to small square edge (the side length of 1 small square)

    turtle.penup()                                          # Disables turtle from drawing on screen
    turtle.goto(-x_coordinate, y_coordinate)                # Makes main turtle go to co-ordinates -x_coordinate on x axis and y_coordinate on y axis
    turtle.pendown()                                        # Enables turtle from drawing on screen
    turtle.right(90)                                        # Turns main turtle 90 degrees to the left

    for board_lines in range(difficulty_level):             # looping for half number of lines in the board indicated by difficulty level
        if board_lines <= prior_switch_line or board_lines >= after_switch_line:        # Checking if we haven't reached the switch line or if we exceeded it
                                                                                        # Note: switch line is the line in which the program switch from drawing vertical lines to horizontal lines
            if board_lines % 2 == 0:                        # if we are not at switch line and board line is even we execute the following code
                turtle.forward(square_edge)                 # Makes main turtle move forward in the direction its facing by square_edge pixels
                turtle.left(90)                             # Turns main turtle 90 degrees to the left
                turtle.forward(small_square_edge)           # Makes main turtle move forward in the direction its facing by small_square_edge pixels
                turtle.left(90)                             # Turns main turtle 90 degrees to the left
            else:                                           # if we are not at switch line and board line is odd we execute the following code
                turtle.forward(square_edge)                 # Makes main turtle move forward in the direction its facing by square_edge pixels
                turtle.right(90)                            # Turns main turtle 90 degrees to the right
                turtle.forward(small_square_edge)           # Makes main turtle move forward in the direction its facing by small_square_edge pixels
                turtle.right(90)                            # Turns main turtle 90 degrees to the right
        elif board_lines % 2 == 0:                          # if we reached the switch line and the switch line is even we execute the following code
            turtle.forward(square_edge)                     # Makes main turtle move forward in the direction its facing by square_edge pixels
            turtle.right(90)                                # Turns main turtle 90 degrees to the right
            board_lines += 1                                # increment board lines
            difficulty_level += 1                           # increments the difficulty level
        else:                                               # if we reached the switch line and the switch line is odd we execute the following code
            turtle.forward(square_edge)                     # Makes main turtle move forward in the direction its facing by square_edge pixels
            turtle.left(90)                                 # Turns main turtle 90 degrees to the left

    turtle.forward(square_edge)                             # Makes main turtle move forward in the direction its facing by square_edge pixels

########################################################################################################################
########################################################################################################################

def dice_roll(user_choice2):                                # This function gets a random number dice and shows it on screen adn returns the random number
    if user_choice2 == 1:                                   # Checks if user_choice2 is equal to 1 (easy mode) and modifies the dice position accordingly
        dice = turtle.Turtle(visible=False)                 # Defines a new turtle named dice which has a hidden shape property
        dice.hideturtle()
        dice.penup()                                        # Disables turtle from drawing on screen
        dice.goto(-300, 0)                                  # Makes turtle named dice go to co-ordinates -300 on x axis and 0 on y axis
        dice.showturtle()                                   # Enables the turtle shape to be shown on screen
        random_dice_number = random.randint(1,6)            # gets a random integer between 1 and 6 then stores it in random dice number
        dice.shape("Images/dice"+str(random_dice_number)+".gif")        # modifies shape of dice according to random number we got
        return random_dice_number                           # returns the random dice number to the movement system
    elif user_choice2 == 2:                                 # Checks if user_choice2 is equal to 2 (medium mode) and modifies the dice position accordingly
        dice = turtle.Turtle(visible=False)                 # Defines a new turtle named dice which has a hidden shape property
        dice.penup()                                        # Disables turtle from drawing on screen
        dice.goto(-300, 0)                                  # Makes turtle named dice go to co-ordinates -300 on x axis and 0 on y axis
        dice.showturtle()                                   # Enables the turtle shape to be shown on screen
        random_dice_number = random.randint(1,6)            # gets a random integer between 1 and 6 then stores it in random dice number
        dice.shape("Images/dice"+str(random_dice_number)+".gif")        # modifies shape of dice according to random number we got
        return random_dice_number                           # returns the random dice number to the movement system
    elif user_choice2 == 3:                                 # Checks if user_choice2 is equal to 3 (hard mode) and modifies the dice position accordingly
        dice = turtle.Turtle(visible=False)                 # Defines a new turtle named dice which has a hidden shape property
        dice.penup()                                        # Disables turtle from drawing on screen
        dice.goto(-340, 0)                                  # Makes turtle named dice go to co-ordinates -340 on x axis and 0 on y axis
        dice.showturtle()                                   # Enables the turtle shape to be shown on screen
        random_dice_number = random.randint(1,6)            # gets a random integer between 1 and 6 then stores it in random dice number
        dice.shape("Images/dice"+str(random_dice_number)+".gif")        # modifies shape of dice according to random number we got
        return random_dice_number                           # returns the random dice number to the movement system

########################################################################################################################
########################################################################################################################

def Player2_coordinate_list(user_choice2):                          # This function makes a list of all the squares points for player 2 according to difficulty level and returns it
    player2_points = []                                             # Defining an empty list named player2 points
    if user_choice2 == 1:                                           # Checks if user_choice2 is equal to 1 (easy mode) and modifies the list points accordingly
        x_coordinate_list = [-225, -125, -25, 75, 175]              # Defining a list of all possible x axis coordinates
        y_coordinate = -310                                         # Defining y_coordinate starting point equals -310
        small_square_edge = 100                                     # Defining small square edge to 100 which is the small square
        rows_number = 5                                             # Defining rows number and  assigning value of 5 to it
    elif user_choice2 == 2:                                         # Checks if user_choice2 is equal to 2 (medium mode) and modifies the list points accordingly
        x_coordinate_list = [-245, -125, -25, 75, 175, 275, 375]    # Defining a list of all possible x axis coordinates
        y_coordinate = -417                                         # Defining y_coordinate starting point equals -417
        small_square_edge = 100                                     # Defining small square edge to 100 which is the small square
        rows_number = 7                                             # Defining rows number and  assigning value of 7 to it
    else:                                                           # if user_choice2 is equal to 3 (hard mode) and modifies the list points accordingly
        x_coordinate_list = [-285, -197, -119, -41, 37, 115, 193, 271, 349, 427]    # Defining a list of all possible x axis coordinates
        y_coordinate = -425                                         # Defining y_coordinate starting point equals -425
        small_square_edge = 78                                      # Defining small square edge to 78 which is the small square
        rows_number = 10                                            # Defining rows number and  assigning value of 10 to it

    x_coordinate_list.reverse()                                     # Reversing the x coordinate list values
    for list_rows in range(rows_number):                            # Looping for the number of rows needed
        x_coordinate_list.reverse()                                 # Reversing the x coordinate list each iteration cause snakes and ladders goes in a zig zag shape
        y_coordinate += small_square_edge                           # incrementing y_coordinate by small square edge after finishing all coordinates of 1 row
        for x_coordinate in x_coordinate_list:                      # looping through all x coordinates in x coordinate list
            player2_points.append([x_coordinate, y_coordinate])     # adding a list with x and y axis to the player2 points list
    return player2_points                                           # returns player2_points list to the movement function

########################################################################################################################
########################################################################################################################

def Player1_coordinate_list(user_choice2):                          # This function makes a list of all the squares points for player 1 according to difficulty level and returns it
    player1_points = []                                             # Defining an empty list named player2 points
    if user_choice2 == 1:                                           # Checks if user_choice2 is equal to 1 (easy mode) and modifies the list points accordingly
        x_coordinate_list = [-185, -100, 0, 100, 200]               # Defining a list of all possible x axis coordinates
        y_coordinate = -275                                         # Defining y_coordinate starting point equals -275
        small_square_edge = 100                                     # Defining small square edge to 100 which is the small square
        rows_number = 5                                             # Defining rows number and  assigning value of 5 to it
    elif user_choice2 == 2:                                         # Checks if user_choice2 is equal to 2 (medium mode) and modifies the list points accordingly
        x_coordinate_list = [-200, -100, 0, 100, 200, 300, 400]     # Defining a list of all possible x axis coordinates
        y_coordinate = -380                                         # Defining y_coordinate starting point equals -380
        small_square_edge = 100                                     # Defining small square edge to 100 which is the small square
        rows_number = 7                                             # Defining rows number and  assigning value of 7 to it
    else:                                                           # if user_choice2 is equal to 3 (hard mode) and modifies the list points accordingly
        x_coordinate_list = [-240, -162, -84, -6, 72, 150, 228, 306, 384, 462]      # Defining a list of all possible x axis coordinates
        y_coordinate = -407                                         # Defining y_coordinate starting point equals -407
        small_square_edge = 78                                      # Defining small square edge to 78 which is the small square
        rows_number = 10                                            # Defining rows number and  assigning value of 10 to it

    x_coordinate_list.reverse()                                     # Reversing the x coordinate list values
    for list_rows in range(rows_number):                            # Looping for the number of rows needed
        x_coordinate_list.reverse()                                 # Reversing the x coordinate list each iteration cause snakes and ladders goes in a zig zag shape
        y_coordinate += small_square_edge                           # incrementing y_coordinate by small square edge after finishing all coordinates of 1 row
        for x_coordinate in x_coordinate_list:                      # looping through all x coordinates in x coordinate list
            player1_points.append([x_coordinate, y_coordinate])     # adding a list with x and y axis to the player2 points list

    return player1_points                                           # returns player2_points list to the movement function

########################################################################################################################
########################################################################################################################

def Switch_player_turn(turn):                                       # This function reverses the turn
    return not(turn)                                                # returns switched turn boolean

########################################################################################################################
########################################################################################################################

def Check_Finish(new_square_position,user_choice2,score):           # This function checks if player reached final square position and is responsible for finishing game
    if user_choice2 == 1:                                           # Checks if user_choice2 is equal to 1 (easy mode) and modifies the list points accordingly
        if new_square_position == 25:                               # Checks if the new square position after adding dice number is the final position (25)
            win = turtle.Turtle()                                   # Defines a new turtle named win
            win.shape("Images/win.gif")                             # Changing win shape to a certain shape found in Images folder
            score += 1                                              # incrementing score of winner
            game_is_on = False                                      # changing value of game is on to false
            return game_is_on,score                                 # returns games is on (boolean) and score of player
        else:                                                       # if player is not at final position
            game_is_on = True                                       # game is on stays True
            return game_is_on,score                                 # returns games is on (boolean) and score of player
    elif user_choice2 == 2:                                         # Checks if user_choice2 is equal to 2 (medium mode) and modifies the list points accordingly
        if new_square_position == 49:                               # Checks if the new square position after adding dice number is the final position (49)
            win = turtle.Turtle()                                   # Defines a new turtle named win
            win.shape("Images/win.gif")                             # Changing win shape to a certain shape found in Images folder
            score += 1                                              # incrementing score of winner
            game_is_on = False                                      # changing value of game is on to false
            return game_is_on,score                                 # returns games is on (boolean) and score of player
        else:                                                       # if player is not at final position
            game_is_on = True                                       # game is on stays True
            return game_is_on,score                                 # returns games is on (boolean) and score of player
    elif user_choice2 == 3:                                         # if user_choice2 is equal to 3 (hard mode) and modifies the list points accordingly
        if new_square_position == 100:                              # Checks if the new square position after adding dice number is the final position (100)
            win = turtle.Turtle()                                   # Defines a new turtle named win
            win.shape("Images/win.gif")                             # Changing win shape to a certain shape found in Images folder
            score += 1                                              # incrementing score of winner
            game_is_on = False                                      # changing value of game is on to false
            return game_is_on,score                                 # returns games is on (boolean) and score of player
        else:                                                       # if player is not at final position
            game_is_on = True                                       # game is on stays True
            return game_is_on,score                                 # returns games is on (boolean) and score of player

########################################################################################################################
########################################################################################################################

def Check_Ladder(animal_points,animal,new_animal_square_position,user_choice2):             # This function checks if their is a ladder and updates position variables accordingly
    if user_choice2 == 1:                                                                   # Checks if user_choice2 is equal to 1 (easy mode)
        if new_animal_square_position == 5:                                                 # if player position is on square 5
            animal.goto(animal_points[15][0],animal_points[15][1])                          # makes player go to square 15
            new_animal_square_position = 15                                                 # update new animal square position
        elif new_animal_square_position == 9:                                               # if player position is on square 9
            animal.goto(animal_points[12][0], animal_points[12][1])                         # makes player go to square 12
            new_animal_square_position = 12                                                 # update new animal square position
        elif new_animal_square_position == 18:                                              # if player position is on square 18
            animal.goto(animal_points[23][0], animal_points[23][1])                         # makes player go to square 23
            new_animal_square_position = 23                                                 # update new animal square position
        return new_animal_square_position                                                   # returns the updated new animal square position
    if user_choice2 == 2:                                                                   # Checks if user_choice2 is equal to 2 (medium mode)
        if new_animal_square_position == 7:                                                 # if player position is on square 7
            animal.goto(animal_points[35][0],animal_points[35][1])                          # makes player go to square 35
            new_animal_square_position = 35                                                 # update new animal square position
        elif new_animal_square_position == 16:                                              # if player position is on square 16
            animal.goto(animal_points[27][0], animal_points[27][1])                         # makes player go to square 27
            new_animal_square_position = 27                                                 # update new animal square position
        elif new_animal_square_position == 31:                                              # if player position is on square 31
            animal.goto(animal_points[40][0], animal_points[40][1])                         # makes player go to square 40
            new_animal_square_position = 40                                                 # update new animal square position
        return new_animal_square_position                                                   # returns the updated new animal square position
    else:                                                                                   # if user_choice2 is equal to 3 (hard mode)
        if new_animal_square_position == 5:                                                 # if player position is on square 2
            animal.goto(animal_points[56][0],animal_points[56][1])                          # makes player go to square 59
            new_animal_square_position = 56                                                 # update new animal square position
        elif new_animal_square_position == 28:                                              # if player position is on square 28
            animal.goto(animal_points[33][0], animal_points[33][1])                         # makes player go to square 33
            new_animal_square_position = 33                                                 # update new animal square position
        elif new_animal_square_position == 77:                                              # if player position is on square 65
            animal.goto(animal_points[84][0], animal_points[84][1])                         # makes player go to square 76
            new_animal_square_position = 84                                                 # update new animal square position
        elif new_animal_square_position == 89:                                              # if player position is on square 89
            animal.goto(animal_points[92][0], animal_points[92][1])                         # makes player go to square 92
            new_animal_square_position = 92                                                 # update new animal square position
        return new_animal_square_position                                                   # returns the updated new animal square position

########################################################################################################################
########################################################################################################################

def Check_Snake(animal_points,animal,new_animal_square_position,user_choice2):              # This function checks if their is a snake and updates position variables accordingly
    if user_choice2 == 1:                                                                   # Checks if user_choice2 is equal to 1 (easy mode)
        if new_animal_square_position == 8:                                                 # if player position is on square 8
            animal.goto(animal_points[3][0],animal_points[3][1])                            # makes player go to square 3
            new_animal_square_position = 3                                                  # update new animal square position
        elif new_animal_square_position == 20:                                              # if player position is on square 20
            animal.goto(animal_points[1][0], animal_points[1][1])                           # makes player go to square 1
            new_animal_square_position = 1                                                  # update new animal square position
        elif new_animal_square_position == 24:                                              # if player position is on square 24
            animal.goto(animal_points[14][0], animal_points[14][1])                         # makes player go to square 14
            new_animal_square_position = 14                                                 # update new animal square position
        return new_animal_square_position                                                   # returns the updated new animal square position
    elif user_choice2 == 2:                                                                 # Checks if user_choice2 is equal to 2 (medium mode)
        if new_animal_square_position == 11:                                                # if player position is on square 11
            animal.goto(animal_points[4][0],animal_points[4][1])                            # makes player go to square 4
            new_animal_square_position = 4                                                  # update new animal square position
        if new_animal_square_position == 32:                                                # if player position is on square 32
            animal.goto(animal_points[25][0],animal_points[25][1])                          # makes player go to square 25
            new_animal_square_position = 25                                                 # update new animal square position
        elif new_animal_square_position == 37:                                              # if player position is on square 37
            animal.goto(animal_points[23][0], animal_points[23][1])                         # makes player go to square 23
            new_animal_square_position = 23                                                 # update new animal square position
        elif new_animal_square_position == 43:                                              # if player position is on square 43
            animal.goto(animal_points[1][0], animal_points[1][1])                           # makes player go to square 1
            new_animal_square_position = 1                                                  # update new animal square position
        return new_animal_square_position                                                   # returns the updated new animal square position
    else:                                                                                   # if user_choice2 is equal to 3 (hard mode)
        if new_animal_square_position == 20:                                                # if player position is on square 20
            animal.goto(animal_points[1][0],animal_points[1][1])                            # makes player go to square 1
            new_animal_square_position = 1                                                  # update new animal square position
        elif new_animal_square_position == 26:                                              # if player position is on square 26
            animal.goto(animal_points[15][0],animal_points[15][1])                          # makes player go to square 15
            new_animal_square_position = 15                                                 # update new animal square position
        elif new_animal_square_position == 57:                                              # if player position is on square 57
            animal.goto(animal_points[24][0], animal_points[24][1])                         # makes player go to square 24
            new_animal_square_position = 24                                                 # update new animal square position
        elif new_animal_square_position == 70:                                              # if player position is on square 70
            animal.goto(animal_points[31][0], animal_points[31][1])                         # makes player go to square 31
            new_animal_square_position = 31                                                 # update new animal square position
        elif new_animal_square_position == 87:                                              # if player position is on square 87
            animal.goto(animal_points[64][0], animal_points[64][1])                         # makes player go to square 64
            new_animal_square_position = 64                                                 # update new animal square position
        elif new_animal_square_position == 99:                                              # if player position is on square 99
            animal.goto(animal_points[22][0], animal_points[22][1])                         # makes player go to square 22
            new_animal_square_position = 22                                                 # update new animal square position
        return new_animal_square_position                                                   # returns the updated new animal square position

########################################################################################################################
########################################################################################################################

def Reverse_Function(animal_points,animal,new_animal_square_position,user_choice2):         # This function reverses the direction of movement if player exceeded final square and updates the new animal position
    if user_choice2 ==1:                                                                    # Checks if user_choice2 is equal to 1 (easy mode)
        largest_square_number = 25                                                          # Assigning value of 25 to largest square number  in case of easy mode
        largest_square_number_x_2 = 50                                                      # Assigning value of 50 to largest square_x_2 in case of easy mode (largest square num * 2)
    elif user_choice2 == 2:                                                                 # Checks if user_choice2 is equal to 2 (medium mode)
        largest_square_number = 49                                                          # Assigning value of 49 to largest square number in case of medium mode
        largest_square_number_x_2 = 98                                                      # Assigning value of 98 to largest square_x_2 in case of medium mode (largest square num * 2)
    elif user_choice2 ==3:                                                                  # if user_choice2 is equal to 3 (hard mode)
        largest_square_number = 100                                                         # Assigning value of 100 to largest square number in case of hard mode
        largest_square_number_x_2 = 200                                                     # Assigning value of 200 to largest square_x_2 in case of hard mode (largest square num * 2)

    if new_animal_square_position > largest_square_number:                                  # Checks if the new player position will exceed the largest square number in the board
        animal.goto(animal_points[largest_square_number][0],animal_points[largest_square_number][1])       # makes player go to final position (largest square number) before reversing
        new_animal_square_position = largest_square_number_x_2 - new_animal_square_position # stores the position that the animal should go to in animal points list after reversing direction  ex. in easy mode 50-27 = 23 which is the position the player should go to after reversing direction
        animal.goto(animal_points[new_animal_square_position][0], animal_points[new_animal_square_position][1])     # makes animal turtle go to the updated new animal square position (index) in the animal points list
        Truth = True                                                                        # Assigning value True to Truth boolean in order to check if the reverse function got activated (This means it got activated)
        return new_animal_square_position , Truth                                           # returning the new animal square position and the Truth boolean
    else:
        Truth = False                                                                       # Assigning value True to False boolean in order to check if the reverse function got activated (This means it didn't get activated)
        return new_animal_square_position , Truth                                           # returning the new animal square position and the Truth boolean

########################################################################################################################
########################################################################################################################

def No_skipping_lines(player,player_points,player_current_square,new_player_square_position,user_choice2):      # This function avoids skipping the lines while transversing through tha player coordinate points list
    if user_choice2 == 1:                                                                   # Checks if user_choice2 is equal to 1 (easy mode)
        go_up_points = [5,10,15,20]                                                         # storing squares in which u have to go up 1 row for next square position in a list called go_up_points
    elif user_choice2 == 2:                                                                 # Checks if user_choice2 is equal to 2 (medium mode)
        go_up_points = [7,14,21,28,35,42]                                                   # storing squares in which u have to go up 1 row for next square position in a list called go_up_points
    elif user_choice2 ==3:                                                                  # if user_choice2 is equal to 3 (hard mode)
        go_up_points = [10,20,30,40,50,60,70,80,90]                                         # storing squares in which u have to go up 1 row for next square position in a list called go_up_points

    for go_up_point in go_up_points:                                                        # looping through all list items
        if player_current_square <= go_up_point < new_player_square_position:               # checks if player current position <= go_up_point and if the new player position after adding dice number will exceed that point (that means it should go to the go up point then go up one square then proceed to the new square position it will go to)
            player.goto(player_points[go_up_point][0],player_points[go_up_point][1])        # making player go to the go up point position in player points list
            player.goto(player_points[go_up_point+1][0],player_points[go_up_point+1][1])    # making player go to the next position which is up one square

########################################################################################################################
########################################################################################################################

def Another_game_question():                                              # This function checks if user wants to play another game and returns a boolean to the main function indicating the user choice
    Pencel = turtle.Turtle(visible=False)                                 # Defines a new turtle named pencil which has a hidden shape property
    Pencel.penup()                                                        # Disables turtle from drawing on screen
    Pencel.goto(0,300)                                                    # Makes turtle named pencil go to co-ordinates 0 on x axis and 300 on y axis
    Pencel.write("Do You want to play another game?", align="center", font=("Verdana", 25, "bold"))     # makes turtle write on screen with custom font properties  ( ask the user if he wants to play another game)
    Pencel.goto(-50, 250)                                                 # Makes turtle named pencil go to co-ordinates -50 on x axis and 250 on y axis
    Pencel.write("Yes", align="center", font=("Verdana", 25, "bold"))     # makes turtle write on screen with custom font properties
    Pencel.goto(50, 250)                                                  # Makes turtle named pencil go to co-ordinates 50 on x axis and 250 on y axis
    Pencel.write("No", align="center", font=("Verdana", 25, "bold"))      # makes turtle write on screen with custom font properties
    Answer = input("Please enter 1 for Yes and 0 for No: ")               # Takes answer from user and stores it in a variable named answer
    No_Answer = True                                                      # Assigning value True to No answer indicating user haven't given a correct answer yet
    while No_Answer == True:                                              # looping till user inputs a correct answer
        if Answer == '1':                                                 # Checks if user Answer is equal to 1
            No_Answer = False                                             # Assigning value False to No answer indicating that the user have given a correct answer
            return True                                                   # returns True to the main function indicating user wants to play another game
        elif Answer == '0':                                               # Checks if user Answer is equal to 0
            No_Answer = False                                             # Assigning value False to No answer indicating that the user have given a correct answer
            return False                                                  # returns True to the main function indicating user wants to play another game
        else:                                                             # Checks if user input is incorrect
            No_Answer = True                                              # Assigning value True to No answer indicating user haven't given a correct answer yet
            print("pls enter a valid number")                             # prints a message to the user
            Answer = input("Please enter 1 for Yes and 0 for No: ")       # Takes answer from user and updates the variable named answer

########################################################################################################################
########################################################################################################################

def movement_system(player1_copy,player2_copy,user_choice2,score_player1,score_player2,player1_name,player2_name,user_choice1):         # This function is responsible for all the players movements till the end of game
    player1 = player1_copy.clone()                                        # cloning player1_copy with all its properties and making a new turtle named player1 in order to make the new turtle go on top of other shapes
    player2 = player2_copy.clone()                                        # cloning player2_copy with all its properties and making a new turtle named player2 in order to make the new turtle go on top of other shapes
    player1.speed(1)                                                      # modifying speed of turtle to 1 (slow)
    player2.speed(1)                                                      # modifying speed of turtle to 1 (slow)
    player1.showturtle()                                                  # Enables the turtle shape to be shown on screen
    player2.showturtle()                                                  # Enables the turtle shape to be shown on screen
    player1.penup()                                                       # Disables turtle from drawing on screen
    player2.penup()                                                       # Disables turtle from drawing on screen

    turn = True     # True refers to Cow       &        False refers to bull (assigning value True to turn boolean)
    player1_current_square = 1                                            # assigning value 1 to variable player1 current square (Starting Square)
    player2_current_square = 1                                            # assigning value 1 to variable player2 current square (Starting Square)
    player1_points =[[0,0]] + Player1_coordinate_list(user_choice2)       # adding a [0,0] to start of player1 coordinate list returned from the function in order to make index of coordinates start from 1
    player2_points = [[0,0]] + Player2_coordinate_list(user_choice2)      # adding a [0,0] to start of player2 coordinate list returned from the function in order to make index of coordinates start from 1
    player1.goto(player1_points[1])                                       # making player1 go to square 1 to start game
    player2.goto(player2_points[1])                                       # making player1 go to square 1 to start game

    print("!New Game\n")                                                  # prints New game to the user at start of each game

    game_is_on = True                                                     # assigning value True to game is on boolean indicating game is still not finished
    while game_is_on:                                                     # looping while game is on is True and game is still working
        if turn == True:                                                  # Checks if turn boolean value is tue indicating Cow's turn
            input(player1_name+" :Press Enter to roll dice")              # waits for user to press on enter
            dice_number = dice_roll(user_choice2)                         # getting a random number from dice roll function and storing it in dice num
            new_player1_square_position = player1_current_square + dice_number                                                     # adds dice num to player current position then stores it in new player1 square position which indicates final position of the turn
            new_player1_square_position,Truth = Reverse_Function(player1_points,player1,new_player1_square_position,user_choice2)  # Calling the Reverse Function and updates new player1 square position and Truth values in case the function got activated else the function returns same values again
            if Truth == True:                                             # checks if Truth value is equal to True indicating reverse function got activated
                new_player1_square_position = Check_Snake(player1_points, player1, new_player1_square_position,user_choice2)       # Calling the check snake Function and updates new player1 square position in case the function got activated else the function returns same values again
                player1_current_square = new_player1_square_position      # Assigning the value of the new player1 position to player1 current square in preparation for the next turn
                print(player1_name+" :You are on square",player1_current_square,end="\n\n")                                        # prints the current square number for the user
                turn = Switch_player_turn(turn)                           # Calls the switch player turn function to change turn and update the boolean
                continue                                                  # skips the rest of the turn and goes to the next iteration of while loop
            No_skipping_lines(player1,player1_points,player1_current_square,new_player1_square_position,user_choice2)              # Calls the no skipping lines function before moving the turtle in order to avoid skipping lines while transversing form previous point to the next point
            player1.goto(player1_points[new_player1_square_position][0],player1_points[new_player1_square_position][1])            # makes player1 go to the next point after adding the dice num
            new_player1_square_position = Check_Ladder(player1_points,player1,new_player1_square_position,user_choice2)            # Calling the Check_Ladder Function and updates new player1 square position in case the function got activated else the function returns same values again
            new_player1_square_position = Check_Snake(player1_points,player1,new_player1_square_position,user_choice2)             # Calling the Check_Snake Function and updates new player1 square position in case the function got activated else the function returns same values again
            game_is_on,score_player1 = Check_Finish(new_player1_square_position,user_choice2,score_player1)                        # Calling the Check_Finish Function and updates game is on boolean and the score_player1 value in case function got activated else the function returns same values again
            player1_current_square = new_player1_square_position          # Assigning the value of the new player1 position to player1 current square in preparation for the next turn
            turn = Switch_player_turn(turn)                               # Calls the switch player turn function to change turn and update the boolean
            print(player1_name+" :You are on square", player1_current_square,end="\n\n")                                           # prints the current square number for the user

        else:
            if user_choice1 == 2:                                         # Checks if its a  multi player (in case of a single player it doesnt ask from user to press enter for player2 )
                input(player2_name+" :Press Enter to roll dice")          # waits for user to press on enter
            dice_number = dice_roll(user_choice2)                         # getting a random number from dice roll function and storing it in dice num
            new_player2_square_position = player2_current_square + dice_number                                                          # adds dice num to player current position then stores it in new player2 square position which indicates final position of the turn
            new_player2_square_position, Truth = Reverse_Function(player2_points, player2, new_player2_square_position,user_choice2)    # Calling the Reverse Function and updates new player2 square position and Truth values in case the function got activated else the function returns same values again
            if Truth == True:                                             # checks if Truth value is equal to True indicating reverse function got activated
                new_player2_square_position = Check_Snake(player2_points, player2, new_player2_square_position,user_choice2)            # Calling the check snake Function and updates new player2 square position in case the function got activated else the function returns same values again
                player2_current_square = new_player2_square_position      # Assigning the value of the new player2 position to player2 current square in preparation for the next turn
                print(player2_name+" :You are on square",player2_current_square,end='\n\n')                                         # prints the current square number for the user
                turn = Switch_player_turn(turn)                           # Calls the switch player turn function to change turn and update the boolean
                continue                                                  # skips the rest of the turn and goes to the next iteration of while loop
            No_skipping_lines(player2, player2_points, player2_current_square, new_player2_square_position,user_choice2)                # Calls the no skipping lines function before moving the turtle in order to avoid skipping lines while transversing form previous point to the next point
            player2.goto(player2_points[new_player2_square_position][0], player2_points[new_player2_square_position][1])                # makes player2 go to the next point after adding the dice num
            new_player2_square_position = Check_Ladder(player2_points, player2, new_player2_square_position,user_choice2)               # Calling the Check_Ladder Function and updates new player2 square position in case the function got activated else the function returns same values again
            new_player2_square_position = Check_Snake(player2_points, player2, new_player2_square_position,user_choice2)                # Calling the Check_Snake Function and updates new player2 square position in case the function got activated else the function returns same values again
            game_is_on,score_player2 = Check_Finish(new_player2_square_position,user_choice2,score_player2)                             # Calling the Check_Finish Function and updates game is on boolean and the score_player2 value in case function got activated else the function returns same values again
            player2_current_square = new_player2_square_position          # Assigning the value of the new player2 position to player2 current square in preparation for the next turn
            turn = Switch_player_turn(turn)                               # Calls the switch player turn function to change turn and update the boolean
            print(player2_name+" :You are on square",player2_current_square,end="\n\n")                                             # prints the current square number for the user
    return score_player1,score_player2                                    # returns the scores of the 2 players after check finish updated them according to who won

########################################################################################################################
########################################################################################################################

def Numbers_on_board(user_choice2=1):                                   # This function puts numbers on the board
    turtle.penup()                                                      # Disables turtle from drawing on screen
    turtle.pencolor("#FF0022")                                          # Modifying pen color to color code #FF0022

    if user_choice2 == 1:                                               # Checks if user_choice2 is equal to 1 (easy mode)
        final_number = 26                                               # assigning value 26 to the variable final number (indicates final number to be written on screen is 25)
        x_axis = -100                                                   # assigning value -100 to the variable x_axis
        x_axis_incrementer = 100                                        # assigning value 100 to the variable x axis incrementer
        starting_x = -245                                               # assigning value -245 to the variable starting x (starting value of x)
        starting_y = -180                                               # assigning value -180 to the variable starting y (starting value of y)
        y_axis = 0                                                      # assigning value 0 to the variable y_axis
        new_horizontal_line = [6, 11, 16, 21]                           # Declaring a list of all points in which we go to new line

    elif user_choice2 == 2:                                             # checks if user_choice2 is equal to 2 (medium mode)
        final_number = 50                                               # assigning value 50 to the variable final number (indicates final number to be written on screen is 49)
        x_axis = -100                                                   # assigning value -100 to the variable x_axis
        x_axis_incrementer = 100                                        # assigning value 100 to the variable x axis incrementer
        starting_x = -265                                               # assigning value -265 to the variable starting x (starting value of x)
        starting_y = -285                                               # assigning value -285 to the variable starting y (starting value of y)
        y_axis = 0                                                      # assigning value 0 to the variable y_axis
        new_horizontal_line = [8, 15, 22, 29, 36, 43]                   # Declaring a list of all points in which we go to new line

    elif user_choice2 == 3:                                             # checks if user_choice2 is equal to 3 (hard mode)
        final_number = 101                                              # assigning value 101 to the variable final number (indicates final number to be written on screen is 100)
        x_axis = -78                                                    # assigning value -78 to the variable x_axis
        x_axis_incrementer = 78                                         # assigning value 78 to the variable x axis incrementer
        starting_x = -295                                               # assigning value -295 to the variable starting x (starting value of x)
        starting_y = -340                                               # assigning value -340 to the variable starting y (starting value of y)
        y_axis = 0                                                      # assigning value 0 to the variable y_axis
        new_horizontal_line = [11, 21, 31, 41, 51, 61, 71, 81, 91]      # Declaring a list of all points in which we go to new line

    switch = True                                                       # Declaring switch boolean in order to decrement in even rows and increment in odd rows
    for new_box_number in range(1, final_number):                       # looping till we write all numbers (final number)
        if new_box_number in new_horizontal_line:                       # if the new number is inside the new horizontal line list that means we need to go up 1 square
            y_axis += x_axis_incrementer                                # incrementing y_axis
            switch = not (switch)                                       # Reversing the value of switch
        elif switch == True:                                            # Checks if switch value is equal to True
            x_axis += x_axis_incrementer                                # incrementing x_axis
        else:                                                           # Checks if switch value is equal to False
            x_axis -= x_axis_incrementer                                # decrements x_axis
        turtle.goto(starting_x + x_axis, starting_y + y_axis)           # makes turtle go to the point in which the number is supposed to be written
        turtle.write("" + str(new_box_number), font=("Verdana", 20, "normal"))      # makes turtle write the square number (new box number)

########################################################################################################################
########################################################################################################################

def score_Display(score_player1,score_player2,player1_name,player2_name,user_choice2):          # This function displays the score of both players along with their names
    logo = turtle.Turtle(shape="Images/Snakes & Ladders Logo mini.gif")                         # Defines a new turtle named logo with a certain shape from Images folder
    vs =turtle.Turtle(shape="Images/VS.gif")                                                    # Defines a new turtle named vs with a certain shape from Images folder
    vs.penup()                                                                                  # Disables turtle from drawing on screen
    logo.penup()                                                                                # Disables turtle from drawing on screen
    turtle.hideturtle()                                                                         # Disables the turtle shape to be shown on screen

    if user_choice2 == 1:                                                                       # Checks if user_choice2 is equal to 1 (easy mode)
        logo.goto(0,350)                                                                        # Makes turtle named logo go to co-ordinates 0 on x axis and 350 on y axis
        turtle.goto(-480, 300)                                                                  # Makes main turtle go to co-ordinates -480 on x axis and 300 on y axis
        x_axis = -380                                                                           # assigning value -380 to the variable x_axis
        y_axis = 240                                                                            # assigning value 240 to the variable y_axis
        rectangle_length = 250                                                                  # assigning value 250 to the variable rectangle length (the rectangle containing the scores of the players and names)
        rectangle_width = 200                                                                   # assigning value 200 to the variable rectangle width (the rectangle containing the scores of the players and names)

    elif user_choice2 == 2:                                                                     # checks if user_choice2 is equal to 2 (medium mode)
        logo.goto(-390,350)                                                                     # Makes turtle named logo go to co-ordinates -390 on x axis and 350 on y axis
        turtle.goto(-490, 300)                                                                  # Makes main turtle go to co-ordinates -490 on x axis and 300 on y axis
        x_axis = -390                                                                           # assigning value -390 to the variable x_axis
        y_axis = 240                                                                            # assigning value 240 to the variable y_axis
        rectangle_length = 250                                                                  # assigning value 250 to the variable rectangle length (the rectangle containing the scores of the players and names)
        rectangle_width = 200                                                                   # assigning value 200 to the variable rectangle width (the rectangle containing the scores of the players and names)

    elif user_choice2 == 3:                                                                     # checks if user_choice2 is equal to 3 (hard mode)
        turtle.right(90)                                                                        # Turns main turtle 90 degrees to the right
        turtle.right(90)                                                                        # Turns main turtle 90 degrees to the right
        logo.goto(-400,350)                                                                     # Makes turtle named logo go to co-ordinates -400 on x axis and 350 on y axis
        turtle.goto(-490, 300)                                                                  # Makes main turtle go to co-ordinates -490 on x axis and 300 on y axis
        x_axis = -400                                                                           # assigning value -400 to the variable x_axis
        y_axis = 240                                                                            # assigning value 240 to the variable y_axis
        rectangle_length = 250                                                                  # assigning value 250 to the variable rectangle length (the rectangle containing the scores of the players and names)
        rectangle_width = 180                                                                   # assigning value 180 to the variable rectangle width (the rectangle containing the scores of the players and names)

    turtle.pendown()                                                                            # Enables turtle from drawing on screen
    turtle.width(5)                                                                             # Adjusting turtle thickness to 5 pixels
    for line in range(2):                                                                       # looping 2 times drawing 2 lines per iteration
        turtle.forward(rectangle_width)                                                         # Makes main turtle move forward in the direction its facing by rectangle width value pixels
        turtle.right(90)                                                                        # Turns main turtle 90 degrees to the right
        turtle.forward(rectangle_length)                                                        # Makes main turtle move forward in the direction its facing by rectangle length value pixels
        turtle.right(90)                                                                        # Turns main turtle 90 degrees to the right
    turtle.penup()                                                                              # Disables turtle from drawing on screen

    turtle.goto(x_axis,y_axis)                                                                  # Makes turtle named logo go to co-ordinates x_axis value on x axis and y_axis value on y axis
    turtle.write(player1_name, align="center",font=("Verdana", 18, "bold"))                     # Writes player1 name on the screen

    vs.goto(x_axis,220)                                                                         # Makes turtle named vs go to co-ordinates x_axis value on x axis and 220 on y axis

    turtle.goto(x_axis, y_axis-70)                                                              # Makes main turtle go to co-ordinates x_axis value on x axis and (y_axis value - 70) on y axis
    turtle.write(player2_name, align="center", font=("Verdana", 18, "bold"))                    # Writes player2 name on the screen

    turtle.goto(x_axis, y_axis-170)                                                             # Makes main turtle go to co-ordinates x_axis value on x axis and (y_axis value - 170) on y axis
    turtle.write(str(score_player1)+"    -    "+str(score_player2), align="center",font=("Verdana", 18, "bold"))        # makes turtle write scores of players on screen

########################################################################################################################
########################################################################################################################

def main():                                                         # This function puts all parts of code together
    user_wants_to_play = True                                       # assigning value True to user wants to play boolean
    score_player1 = 0                                               # assigning value 0 to score_player1 variable (this is were the score gets scored however many times the user keeps playing)
    score_player2 = 0                                               # assigning value 0 to score_player2 variable (this is were the score gets scored however many times the user keeps playing)
    turtle.setup(1000, 800, 0, 0)                                   # setups the turtle window size in pixels
    Shapes_configuration()                                          # Calling function Shapes_configuration
    Home_Page()                                                     # Calling function Home_Page
    user_choice1 = Check_valid_answer(['1', '2'], 1)                # Calling function check_valid_answer and getting user_choice1
    player1_name,player2_name = Game_mode(user_choice1)             # Calling function Game_mode and getting player names
    user_choice2 = Check_valid_answer(['1', '2', '3'], 2)           # Calling function check_valid_answer and getting user_choice2
    while user_wants_to_play:                                       # looping till the user doesn't want to play any more (user_wants_to_play becomes False)
        player1, player2 = Character_choosing(user_choice1)         # Calling Character choosing function and retrieving the 2 characters that the players will play with
        board(user_choice2)                                         # Calling board function and making the board
        Numbers_on_board(user_choice2)                              # Calling Numbers_on_board function and putting numbers on board
        add_shapes(user_choice2)                                    # Calling add shapes function which adds all shapes necessary for game
        score_Display(score_player1,score_player2,player1_name,player2_name,user_choice2)   # Calling score_Display function and displaying the score and players names
        score_player1,score_player2 = movement_system(player1,player2,user_choice2,score_player1,score_player2,player1_name,player2_name,user_choice1)     # Calling movement function and retrieving the updated scores after game finishes
        user_wants_to_play = Another_game_question()                # Calling Another_game_question and updating user_wants_to_play according to user input
    turtle.exitonclick()                                            # exits screen on clicking on the turtle menu after the game finishes
########################################################################################################################
########################################################################################################################


main()                                    # Calling main function

