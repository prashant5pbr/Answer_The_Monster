import sqlite3
from database import DataBase
import paths
from options import EnterName
from game import GamePlay, Character

#Function to save the data to the database
def save_data():
    #Create a connection to the database
    with sqlite3.connect(paths.DATA_PATH) as connection:
        #Create database
        db_file = DataBase(connection)

        #Create table
        db_file.create_table()

        #Fetch details to insert in the database table
        player_name = EnterName.name
        game_start_date = GamePlay.start_date
        game_start_time = GamePlay.start_time
        game_duration = GamePlay.duration
        player_score = GamePlay.score
        game_result = Character.status

        #Insert the data
        db_file.cursor.execute("""
                               insert or ignore into game_records (Played_As, Date, Start_Time, Duration, Score, Result)
                               values (?, ?, ?, ?, ?, ?)
                               """, (player_name, game_start_date, game_start_time, game_duration, player_score, game_result))
        
        #Save the changes
        db_file.connection.commit()