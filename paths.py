import os
import sys

#Check if the file is runnning as script or as exceutable file and set the path for database
if getattr(sys, 'frozen', False):
    BASE_DIR = sys._MEIPASS
    DATA_PATH = os.path.join(BASE_DIR, "quiz_game.db")

else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DATA_PATH = os.path.join(BASE_DIR, "database", "quiz_game.db")

#Path to the logo
LOGO_PATH = os.path.join(BASE_DIR, "atm_logo.png")

#Path to the sample database
SAMPLE_PATH = os.path.join(BASE_DIR, "database", "sample_quiz_data.db")