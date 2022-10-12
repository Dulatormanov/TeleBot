import sqlite3 as sq
async def db_connect() -> None:
    global db, curr
    db = sq.connect('new db')
    curr = db.cursor()
    curr.execute("CREATE TABLE IF NOT EXISTS products(name TEXT, photo TEXT)")
    db.commit()
