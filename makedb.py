import sqlite3

# Connect to the database (will create it if it doesn't exist)
conn = sqlite3.connect('test_database.db')
cursor = conn.cursor()

# Create the 'log' table with more columns
cursor.execute('''
CREATE TABLE IF NOT EXISTS log (
    id INTEGER PRIMARY KEY,
    time INTEGER,
    jobs_ran INTEGER,
    percentage_toned REAL,
    tone_hours REAL,
    most_time INTEGER
)
''')

# Insert some sample data
sample_data = [
    (10, 50, 80.5, 5.2, 45),
    (20, 60, 75.3, 4.8, 40)
]
cursor.executemany('INSERT INTO log (time, jobs_ran, percentage_toned, tone_hours, most_time) VALUES (?, ?, ?, ?, ?)', sample_data)

# Commit the changes and close the connection
conn.commit()
conn.close()
