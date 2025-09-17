from dotenv import load_dotenv
from google.adk.sessions import InMemorySessionService
from google.adk.runners import Runner
from utils import add_user_query_to_history, call_agent_async
import asyncio
from customer_service_agent.agent import customer_service_agent

load_dotenv()

# Using in-memory storage for this example (non-persistent)
session_service = InMemorySessionService()

initial_state = {
    "user_name": "Cocco Ananas",
    "purchased_course": [],
    "interaction_history": []
}

async def main_async():
    APP_NAME = "Customer support"
    USER_ID = "aiwithcocco"

    new_session = session_service.create_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        state = initial_state
    )
    SESSION_ID = new_session.id
    print(f"Created new session: {SESSION_ID}")

    runner = Runner(
        agent = customer_service_agent,
        session_service=session_service,
        app_name=APP_NAME
    )

    print("\nWelcome to Customer Service Chat!")
    print("Type 'exit' or 'quit' to end the conversation.\n")
    while True:
        user_input = input("You: ")

        if user_input.lower() in ["quit", "exit"]:
            print("Ending conversation. Goodbye!")
            break

        add_user_query_to_history(session_service, APP_NAME, USER_ID, SESSION_ID, user_input)

        await call_agent_async(runner, USER_ID, SESSION_ID, user_input)

    final_session = session_service.get_session(app_name=APP_NAME, user_id=USER_ID, session_id=SESSION_ID)
    print("\nFinal Session State:")
    for key, value in final_session.state.items():
        print(f"{key}: {value}")

def main():
    asyncio.run(main_async())

if __name__ == "__main__":
    main()
