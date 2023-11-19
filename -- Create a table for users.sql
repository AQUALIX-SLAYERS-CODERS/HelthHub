-- Create a table for users
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    email TEXT NOT NULL
);

-- Create a table for quiz results
CREATE TABLE IF NOT EXISTS quiz_results (
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    result TEXT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users (id)
);
