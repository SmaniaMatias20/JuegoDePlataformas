import sqlite3

# Path "Modules\Data\scores.db"

def create_level_table(db_path):
    with sqlite3.connect(db_path) as connection:
        try:
            # CREATE TABLE
            sentence = '''
                        CREATE TABLE IF NOT EXISTS Match       
                        (
                            id_player INTEGER PRIMARY KEY AUTOINCREMENT,
                            name_player TEXT,
                            score_player INTEGER,
                            level_type TEXT
                        )
                        '''
            connection.execute(sentence)
        except sqlite3.OperationalError as e:
            print(f"Error: {e}")

def insert_player_data(db_path, player_name, player_score, level_type):
    with sqlite3.connect(db_path) as connection:
        try:
            # INSERT INTO TABLE
            sentence = f"INSERT INTO Match (name_player, score_player, level_type) VALUES ('{player_name}', {player_score}, '{level_type}' )"
            connection.execute(sentence)
            print(f"Player '{player_name}' with score '{player_score}' added successfully.")
        except sqlite3.OperationalError as e:
            print(f"Error: {e}")

def get_top_scores(db_path):
    with sqlite3.connect(db_path) as connection:
        try:
            # SELECT TOP 3 SCORES WITH NAMES
            sentence = "SELECT name_player, score_player FROM Match ORDER BY score_player DESC LIMIT 3"
            result = connection.execute(sentence).fetchall()
            print("Top 3 Scores:")
            for row in result:
                print(f"Player: {row[0]}, Score: {row[1]}")
            
            return result
        except sqlite3.OperationalError as e:
            print(f"Error: {e}")