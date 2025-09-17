from google.adk.runners import Runner
from google.adk.sessions import DatabaseSessionService
from memory_agent.agent import memory_agent
from utils import call_agent_async
from dotenv import load_dotenv
import asyncio

load_dotenv()

db_url = "sqlite:///./my_agent_data.db"
session_service = DatabaseSessionService(db_url=db_url)

initial_state = {
    "user_name": "Cocco Ananas",
    "reminders": []
}

async def main_async():
    APP_NAME = "Memory agent"
    USER_ID = "aiwithcocco"

    existing_session = session_service.list_sessions(
        app_name=APP_NAME,
        user_id=USER_ID
    )

    if existing_session and len(existing_session.sessions) > 0:
        SESSION_ID = existing_session.sessions[0].id
        print(f"Continuing existing session: {SESSION_ID}")
    else:
        new_session = session_service.create_session(
            app_name=APP_NAME,
            user_id=USER_ID,
            state=initial_state
        )
        SESSION_ID = new_session.id
        print(f"Created new session: {SESSION_ID}")

    runner = Runner(
        agent=memory_agent,
        app_name=APP_NAME,
        session_service=session_service
    )

    print("\nWelcome to Memory Agent Chat!")
    print("Your reminders will be remembered across conversations.\n")
    print("Type 'exit' or 'quit' to end the conversation.\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() in ["exit", "quit"]:
            print("Ending conversation. Your data has been saved to the database.")
            break
        
        await call_agent_async(runner, USER_ID, SESSION_ID, user_input)

if __name__ == "__main__":
    asyncio.run(main_async())