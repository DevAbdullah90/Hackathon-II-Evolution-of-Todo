from src.core.database import init_db
from src.models.task import Task
from src.models.conversation import Conversation
from src.models.message import Message

def main():
    print("Initializing database...")
    init_db()
    print("Database initialized.")

if __name__ == "__main__":
    main()
