#Class to create database and table
class DataBase:
    #Initialise the connection and the cursor object as instance attributes
    def __init__(self, connection):
        self.connection = connection
        self.cursor = self.connection.cursor()

    #Create table
    def create_table(self):
        self.cursor.execute("""
                       create table if not exists game_records(
                       Played_As TEXT,
                       Date TEXT,
                       Start_Time TEXT,
                       Duration TEXT,
                       Score TEXT,
                       Result TEXT,

                       PRIMARY KEY (Date, Start_Time)
                       )
                       """)
        
        #Save the changes
        self.connection.commit()