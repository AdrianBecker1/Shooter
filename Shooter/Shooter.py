from program_shooter import Player, play_bot, adjust_stats
from ui_shooter import ui_print, ui_print_battle, ui_print_stats, ui_move, play_again, msg_gameover, ui_choose_difficulty, ui_turorial


def play_shooter ():

    play = True

    
    ############### loop that runs as long as the player wants to play ###############
    while play:
        
        # starting values
        game_finished = False

        player = Player()
        bot = Player ()

        # Print Introduction
        ui_turorial(player, bot)

        # choose difficulty
        difficulty = ui_choose_difficulty()
        
        ########### loop that runs until the player dies #############################
        while not game_finished:

            # 1. Player makes a move ##########################################################
            player_move = ui_move()

            # if the player has 0 blocks left, already 3 bullets or no bullets left, he gets asked to make another input    
            while (player.blocks == 0 and player_move == "block") or (player.bullets == 3 and player_move == "load") or (player.bullets == 0 and player_move == "shoot"):

                print(player_move + " is not possible...")
                print("~~~~")
                player_move = ui_move()
            
            # 2. Bot makes a move #############################################################
            bot_move = play_bot(player, bot, difficulty, player_move)
            

            # Adjust the stats of the player #############################################################

            # 1. adjusts stats for player
            adjust_stats(player, player_move, bot_move)

            # 2. adjusts stats for bot
            adjust_stats(bot, bot_move, player_move)


            # Print the bot stats, then the battelfield, and then the player stats #######################
            ui_print_battle(player, bot, bot_move, player_move)


            # If the player & the bot have 0 lives #######################
            if player.lives == 0 and bot.lives == 0:
                msg_gameover ("Tied")
                game_finished = True

            # If the player has 0 lives, he lost #########################
            elif player.lives == 0:
                msg_gameover ("Lost")
                game_finished = True
                

            # If the bot has 0 lives, he lost ############################
            elif bot.lives == 0:
                msg_gameover ("Won")
                game_finished = True
                
            

        play = play_again()



###############################
play_shooter() # Play Function
###############################