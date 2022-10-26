from program_shooter import Player

map_shoot = [
"                            ",
"   ###    ##   #  #   ###   ",
"   #  #  #  #  ## #  #      ",
"   ###   ####  ####  # ##   ",
"   #  #  #  #  # ##  #  #   ",
"   ###   #  #  #  #   ###   ",
"                            "
]

map_block = [

"                            ",
"###   #      ##    ###  #  #",
"#  #  #     #  #  #     # # ",
"###   #     #  #  #     ##  ",
"#  #  #     #  #  #     # # ",
"###   ####   ##    ###  #  #",
"                            "
]

map_load = [

"                            ",
"   #      ##    ##   ###    ",
"   #     #  #  #  #  #  #   ",
"   #     #  #  ####  #  #   ",
"   #     #  #  #  #  #  #   ",
"   ####   ##   #  #  ###    ",
"                            "
]

map_vs = [
"~~~~~~~~~~~~~~~~~~~~~~~~~~~~",
"     #       #   ######     ",
"      #     #   #           ",
"       #   #     #####      ",
"        # #           #     ",
"         #    @ ######  @   ",
"~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
]

##########################################################################################################################################$

# Function that prints given maps
def ui_print(map):

    for row in map:
        print(row)


# function that prints the battle & the stats of both opponents
def ui_print_battle(player, bot, action_bot, action_player):

    # 1. Print Bot Stats
    print("")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    ui_print_stats("Bot: ", bot.lives, bot.blocks, bot.bullets)

    # 2. print the action of the bot
    if action_bot == "shoot":
        ui_print(map_shoot)

    elif action_bot == "block":
        ui_print(map_block)
    
    elif action_bot == "load":
        ui_print(map_load)

    # 3. print vs map between
    ui_print(map_vs)

    # 4. print the action of the player
    if action_player == "shoot":
        ui_print(map_shoot)

    elif action_player == "block":
        ui_print(map_block)
    
    elif action_player == "load":
        ui_print(map_load)

    # 5. Print Player Stats
    ui_print_stats("Player: ", player.lives, player.blocks, player.bullets)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("")


# Function that prints the stats of the given player
def ui_print_stats(player, lives, blocks, bullets):

    print (player + str(lives) + " lives, " + str(blocks) + " blocks, " + str(bullets) + " bullets")

##########################################################################################################################################$

# Prints Tutorial
def ui_turorial(player, bot):

    print("Welcome to Load, Block or Shoot, Cowboy!")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    ui_print_stats(" Bot: ", bot.lives, bot.blocks, bot.bullets)
    print("")
    print("              ~ vs ~")
    print("")
    ui_print_stats("Player: ", player.lives, player.blocks, player.bullets)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("")

# Function that asks which difficulty the player wants to play
def ui_choose_difficulty():

    print("Please choose your difficulty:")
    print(" *easy* | *normal* | *impossible* ")

    difficulty = str(input())

    # check wrong input
    while difficulty != "easy" and difficulty != "normal" and difficulty != "impossible":
        print("---")
        print("Please try again!")
        print("---")
        difficulty = str(input())

        
    return difficulty

##########################################################################################################################################$

# Function that gets the next move from player
def ui_move():

    print("What is your next action, Cowboy?")
    print(" *shoot* | *block* | *load* ")
    answer = str(input())
    
    # check for wrong input
    while answer != "shoot" and answer != "block" and answer != "load":
        print("---")
        print("Please try again:")
        answer = str(input())

    return answer


# Function that asks the player if he would like to play again
def play_again():

    print("Do you want to play again? (Y or N)")
    answer = str(input())
    
    # check for wrong input
    while answer != "Y" and answer != "N":
        print("---")
        print("Please try again:")
        answer = str(input())

    if answer =="Y":
        return True
    else:
        return False

##########################################################################################################################################$

def msg_gameover (outcome):

    skull = [
    "  _____  ",
    " /     \\",
    "| () () |",
    " \  ^  / ",
    "  ||||| ",
    "  ||||| "
    ]

    trophy = [
    " .__.",
    "(|  |)",
    " (  )",
    " _)(_ "
    ]

    tie = [
    " .-*-.      .-*-.   ",
    "/.~*~.\\    /.~*~.\\",
    "| RIP |    | RIP |  ",
    "|_____|    |_____|  "
    ]

    if outcome == "Lost":
        ui_print(skull)
    
    elif outcome == "Won":
        ui_print(trophy)
    
    elif outcome == "Tied":
        ui_print(tie)

    print("------")
    print ("You " + outcome +"!")
    print("------")

