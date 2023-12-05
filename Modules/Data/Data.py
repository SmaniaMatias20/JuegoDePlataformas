import sqlite3

# Path "Modules\Data\scores.db"

def create_level_table(db_path):
    """
    Brief: Crea la tabla 'Match' en la base de datos si no existe.

    Descripción:
        Esta función se conecta a la base de datos especificada y crea la tabla 'Match' si aún no existe.
        La tabla 'Match' tiene las columnas 'id_player' (clave primaria), 'name_player', 'score_player',
        y 'level_type'.

    Parámetros:
        - db_path (str): Ruta al archivo de la base de datos.

    Retorno:
        Ninguno
    """
    with sqlite3.connect(db_path) as connection:
        try:
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
    """
    Brief: Inserta datos del jugador en la tabla 'Match' de la base de datos.

    Descripción:
        Esta función se conecta a la base de datos especificada e inserta datos del jugador en la
        tabla 'Match'. Los datos incluyen el nombre del jugador, la puntuación y el tipo de nivel.

    Parámetros:
        - db_path (str): Ruta al archivo de la base de datos.
        - player_name (str): Nombre del jugador.
        - player_score (int): Puntuación del jugador.
        - level_type (str): Tipo de nivel.

    Retorno:
        Ninguno
    """
    with sqlite3.connect(db_path) as connection:
        try:
            sentence = f"INSERT INTO Match (name_player, score_player, level_type) VALUES ('{player_name}', {player_score}, '{level_type}' )"
            connection.execute(sentence)
        except sqlite3.OperationalError as e:
            print(f"Error: {e}")
        except Exception as exc:
            print(f"Error: {exc}")

def get_top_scores(db_path):
    """
    Brief: Obtiene los tres puntajes más altos con nombres de la tabla 'Match' en la base de datos.

    Descripción:
        Esta función se conecta a la base de datos especificada y realiza una consulta para obtener
        los tres puntajes más altos con los nombres correspondientes desde la tabla 'Match'.

    Parámetros:
        - db_path (str): Ruta al archivo de la base de datos.

    Retorno:
        list: Lista de tuplas que contienen nombres de jugadores y sus puntajes, ordenados por puntaje descendente.
    """
    with sqlite3.connect(db_path) as connection:
        try:
            sentence = "SELECT name_player, score_player FROM Match ORDER BY score_player DESC LIMIT 3"
            result = connection.execute(sentence).fetchall()

            return result
        except sqlite3.OperationalError as e:
            print(f"Error: {e}")
        except Exception as exc:
            print(f"Error: {exc}")