from random import randint

# Main Class that tracks the player's and bot's stats ####################
class Player():

    def __init__(self):

        self.lives = 3
        self.blocks = 3
        self.bullets = 0
    
    # Function that adjusts the lives
    def live_change (self, live_change):

        self.lives = self.lives + live_change
    
    # Function that adjusts the blocks
    def block_change (self, block_change):

        self.blocks = self.blocks + block_change
    
    # Function that adjusts the bullets
    def bullet_change (self, bullet_change):

        self.bullets = self.bullets + bullet_change

###########################################################################

def play_bot(player, bot, difficulty, player_move):

    bot_move = bot_choose_input()
    
    # Easy Bot ###########################################################################
    if difficulty == "easy":

        # if the bot has 0 blocks left, already 3 bullets or no bullets left, he gets asked to make another input
        while (bot.blocks == 0 and bot_move == "block") or (bot.bullets == 3 and bot_move == "load") or (bot.bullets == 0 and bot_move == "shoot"):

            bot_move = bot_choose_input()
    
        return bot_move

    # Normal Bot #########################################################################
    elif difficulty == "normal":

        bot_move = bot_choose_input()

        # if the bot has 0 blocks left, already 3 bullets or no bullets left, he gets asked to make another input 
        # also check if the player has bullets (if not, block is not advisable) & if an agressive finish is possible
        while (bot.blocks == 0 and bot_move == "block") or (bot.bullets == 3 and bot_move == "load") or (bot.bullets == 0 and bot_move == "shoot") \
        or (player.bullets == 0 and bot_move == "block") or ((player.lives + player.blocks + player.bullets) <= bot.bullets and bot_move != "shoot"):

            bot_move = bot_choose_input()
    
        return bot_move

    # Impossible Bot ######################################################################
    elif difficulty == "impossible":

        bot_move = bot_choose_input()

        # if the bot has 0 blocks left, already 3 bullets or no bullets left, he gets asked to make another input 
        # also check if the player has bullets (if not, block is not advisable) & if an agressive finish is possible
        # also block if the player shoots
        while (bot.blocks == 0 and bot_move == "block") or (bot.bullets == 3 and bot_move == "load") or (bot.bullets == 0 and bot_move == "shoot") \
            or (player.bullets == 0 and bot_move == "block") or ((player.lives + player.blocks + player.bullets) <= bot.bullets and bot_move != "shoot")\
            or (player_move == "shoot" and bot.blocks != 0 and bot_move != "block"):

            bot_move = bot_choose_input()
            
        return bot_move

def bot_choose_input():

    key = randint(1,3)

    if key == 1:
        input = "shoot"

    elif key == 2:
        input = "block"

    elif key == 3:
        input = "load"

    return input


def adjust_stats (player, player_move, opponent_move):

    # adjusts bullets
    if player_move == "shoot":
        player.bullet_change(-1)

    if player_move == "load":
        player.bullet_change(1)
    
    # adjust blocks
    if player_move == "block":
        player.block_change(-1)

    if player_move != "block" and player.blocks != 3:
        player.block_change(1)

    # adjust lives
    if opponent_move == "shoot" and player_move != "block":
        player.live_change(-1)