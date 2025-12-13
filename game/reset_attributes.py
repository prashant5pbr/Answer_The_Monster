from game.create_character import Character
from game.play import GamePlay
from game.timer import CountDown
#Lazy imported class Questioner

#Function to reset attributes and flags
def reset():
    Character.system_points = 50
    Character.player_handler.points = 50

    #Lazy import class Questioner
    from game.questions_answers import Questioner

    Questioner.answer_ready = False
    Questioner.question_number = 0
    Questioner.reset_questions = True

    CountDown.stop_timer = False

    GamePlay.game_on = False
    GamePlay.should_restart_game = False