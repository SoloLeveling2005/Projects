import sqlite3 as sql


def create_bd():
    with sql.connect("todo.db") as con:
        cur = con.cursor()
        cur.execute(f"""
                        CREATE TABLE IF NOT EXISTS users (
                            ID INTEGER NOT NULL,
                            user_id INTEGER NOT NULL,
                            info VARCHAR,
                            status VARCHAR NOT NULL,
                            prem_time INTEGER,
                            icon VARCHAR,
                            free_requests INTEGER,
                            PRIMARY KEY(ID AUTOINCREMENT)
                        )
                    """)
    with sql.connect("todo.db") as con:
        cur = con.cursor()
        cur.execute(f"""
                        CREATE TABLE IF NOT EXISTS admins (
                            ID INTEGER NOT NULL,
                            user_id INTEGER NOT NULL,
                            PRIMARY KEY(ID AUTOINCREMENT)
                        )
                    """)
    with sql.connect("todo.db") as con:
        cur = con.cursor()
        cur.execute(f"""
                        CREATE TABLE IF NOT EXISTS do (
                            user_id INTEGER NOT NULL,
                            where_you VARCHAR NOT NULL
                        )
                    """)
    with sql.connect("todo.db") as con:
        cur = con.cursor()
        cur.execute(f"""
                        CREATE TABLE IF NOT EXISTS connection_couple (
                            ID INTEGER NOT NULL,
                            first INTEGER NOT NULL,
                            second INTEGER NOT NULL,
                            PRIMARY KEY(ID AUTOINCREMENT)
                        )
                    """)
    with sql.connect("todo.db") as con:
        cur = con.cursor()
        cur.execute(f"""
                        CREATE TABLE IF NOT EXISTS connection_group (
                            ID INTEGER NOT NULL,
                            id_group VARCHAR NOT NULL,
                            admin INTEGER NOT NULL,         
                            user_id INTEGER NOT NULL,
                            how_many_people INTEGER NOT NULL,
                            PRIMARY KEY(ID AUTOINCREMENT)
                        )
                    """)
    with sql.connect("todo.db") as con:
        cur = con.cursor()
        cur.execute(f"""
                        CREATE TABLE IF NOT EXISTS request_connections_couple (
                            user_id INTEGER NOT NULL
                        )
                    """)
    with sql.connect("todo.db") as con:
        cur = con.cursor()
        cur.execute(f"""
                        CREATE TABLE IF NOT EXISTS request_connections_group (
                            user_id INTEGER NOT NULL
                        )
                    """)

    # Платный контент
    with sql.connect("todo.db") as con:
        cur = con.cursor()
        cur.execute(f"""
                           CREATE TABLE IF NOT EXISTS request_qiwi (
                               user_id INTEGER NOT NULL,
                               special_code VARCHAR NOT NULL
                           )
                       """)

    with sql.connect("todo.db") as con:
        cur = con.cursor()
        cur.execute(f"""
                           CREATE TABLE IF NOT EXISTS request_payment_with_confirmation (
                               user_id INTEGER NOT NULL,
                               special_code VARCHAR NOT NULL
                           )
                       """)