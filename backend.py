import sqlite3

# Database

def connect():
    conn = sqlite3.connect("favoriteMovies.db")
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS movies(
                id INTEGER PRIMARY KEY,
                director TEXT,
                title TEXT,
                year INTEGER,
                revenue INTEGER)""")
    conn.commit()
    conn.close()

connect()

# Functions

def save(director, title, year, revenue):
    conn = sqlite3.connect("favoriteMovies.db")
    c = conn.cursor()
    c.execute("INSERT INTO movies VALUES (NULL,?,?,?,?)", (director, title, year, revenue))
    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect("favoriteMovies.db")
    c = conn.cursor()
    c.execute("SELECT * FROM movies")
    rows = c.fetchall()
    conn.close()
    return rows

def search(director="", title="", year="", revenue=""):
    conn = sqlite3.connect("favoriteMovies.db")
    c = conn.cursor()
    c.execute("SELECT * FROM movies WHERE director=? OR title=? OR year=? OR revenue=?",
              (director, title, year, revenue))
    rows = c.fetchall()
    conn.close()
    return rows

def update(id,director,title,year,revenue):
    conn = sqlite3.connect("favoriteMovies.db")
    c = conn.cursor()
    c.execute("UPDATE movies SET director=?,title=?,year=?,revenue=? WHERE id=?",(director,title,year,revenue,id))
    conn.commit()
    conn.close()

def delete(id):
    conn = sqlite3.connect("favoriteMovies.db")
    c = conn.cursor()
    c.execute("DELETE FROM movies WHERE id=?",(id,))
    conn.commit()
    conn.close()

connect()

print(view())


