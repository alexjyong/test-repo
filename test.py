import json
import sqlite3
import http.server
import socketserver

class YourClassName:
    def __init__(self, db):
        self.db = db

    def fetch_data(self):
        con = sqlite3.connect(self.db)
        cur = con.cursor()
        data = cur.execute("""SELECT * FROM log""").fetchone()
        con.close()
        return {
            'total_time': round(data[1]/60, 1),
            'jobs_ran': data[2],
            'percentage_toned': data[3],
            'tone_hours': data[4],
            'most_time': data[5]
        }

    def write_to_json(self):
        data = self.fetch_data()
        with open('data.json', 'w') as json_file:
            json.dump(data, json_file)

# Generate the data.json file
obj = YourClassName("test_database.db")
obj.write_to_json()

# Start the web server
PORT = 8000
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()
