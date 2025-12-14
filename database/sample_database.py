import sqlite3
from database.create_database import DataBase
import paths

#creating sample tables and inserting data
with sqlite3.connect(paths.SAMPLE_PATH) as connection:
    #Create database
    sample_db_file = DataBase(connection)

    #Create table
    sample_db_file.create_table()

    #Sample data
    sample_data = [
        ("Peter", "2025/12/10", "17:12:30", "00:01:30", "72.727", "win"),
        ("David", "2025/12/12", "09:16:42", "00:01:19", "8.333", "lose")
    ]

    #Insert data
    sample_db_file.cursor.executemany("""
                                  insert or ignore into game_records (Played_As, Date, Start_Time, Duration, Score, Result)
                                  values (?, ?, ?, ?, ?, ?)
                                  """, sample_data)
    
    #Save changes
    sample_db_file.connection.commit()