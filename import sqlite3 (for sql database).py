import sqlite3
from sqlite3 import Error

def create_connection():
    """Create a database connection to SQLite database."""
    connection = None
    try:
        connection = sqlite3.connect('healthhub.db')
        print(f"Connected to the database: {sqlite3.version}")
        return connection
    except Error as e:
        print(f"Error: {e}")
    return connection

def create_tables(connection):
    """Create tables if they don't exist."""
    try:
        cursor = connection.cursor()

        # Create a table for users
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username TEXT NOT NULL,
                password TEXT NOT NULL,
                email TEXT NOT NULL
            )
        ''')

        # Create a table for quiz results
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS quiz_results (
                id INTEGER PRIMARY KEY,
                user_id INTEGER,
                result TEXT NOT NULL,
                FOREIGN KEY (user_id) REFERENCES users (id)
            )
        ''')

        print("Tables created successfully.")

    except Error as e:
        print(f"Error: {e}")

def insert_user(connection, username, password, email):
    """Insert a new user into the 'users' table."""
    try:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO users (username, password, email) VALUES (?, ?, ?)",
                       (username, password, email))
        connection.commit()
        print("User inserted successfully.")
    except Error as e:
        print(f"Error: {e}")

def insert_quiz_result(connection, user_id, result):
    """Insert quiz results for a user into the 'quiz_results' table."""
    try:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO quiz_results (user_id, result) VALUES (?, ?)",
                       (user_id, result))
        connection.commit()
        print("Quiz result inserted successfully.")
    except Error as e:
        print(f"Error: {e}")

def query_users(connection):
    """Query and print all users."""
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        print("Users:")
        for user in users:
            print(user)
    except Error as e:
        print(f"Error: {e}")

def query_quiz_results(connection):
    """Query and print all quiz results."""
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM quiz_results")
        results = cursor.fetchall()
        print("Quiz Results:")
        for result in results:
            print(result)
    except Error as e:
        print(f"Error: {e}")

def main():
    connection = create_connection()

    if connection:
        create_tables(connection)

        insert_user(connection, 'john_doe', 'hashed_password', 'john@example.com')

        query_users(connection)

        insert_quiz_result(connection, 1, 'High Risk')

        query_quiz_results(connection)

        connection.close()
        print("Connection closed.")

if __name__ == '__main__':
    main()
