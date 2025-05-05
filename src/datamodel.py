import uuid
import sqlite3

class FlashCard:
    name = "No Name"
    front = "Front"
    back = "Back"
    id = "123456789"

    def __init__(self, name, front, back):
        self.name = name
        self.front = front
        self.back = back
        self.id = uuid.uuid4()

    def save_flashcard(self):
        conn = sqlite3.connect("tutorial.db")
        cur = conn.cursor()
        cur.execute("INSERT INTO flashcards VALUES(?, ?, ?, ?)", (self.name, self.front, self.back, str(self.id)))
        conn.commit()
        conn.close()
