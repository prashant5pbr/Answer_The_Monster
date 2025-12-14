import os

#Path to the database
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "database", "quiz_game.db")

#Path to the sample database
SAMPLE_PATH = os.path.join(BASE_DIR, "database", "sample_quiz_data.db")