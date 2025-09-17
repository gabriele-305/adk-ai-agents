import uuid
from dotenv import load_dotenv
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types
from question_answering_agent import question_answering_agent

load_dotenv()

session_service_stateful = InMemorySessionService()

initial_state = {
    "user_name": "Cocco Ananas",
    "user_preferences": """
        I like to play Pickleball, Disc Golf nd Tennis.
        My favourite food is Mexican.
        My favourite TV show is Game of Thrones.
        Loves it when people like and subscribe to his cooking channel.
    """
}

#create a new session
APP_NAME = "Cocco Bot"
USER_ID = "cocco_ananas"
SESSION_ID = str(uuid.uuid4())
stateful_session = session_service_stateful.create_session(
    app_name=APP_NAME,
    user_id=USER_ID,
    session_id=SESSION_ID,
    state=initial_state
)
print(f"NEW SESSION CREATED! ({SESSION_ID})")

#create the runner (agents + sessions)
runner = Runner(
    app_name=APP_NAME,
    agent=question_answering_agent,
    session_service=session_service_stateful
)

new_message = types.Content(
    role="user", parts=[types.Part(text="What is Cocco's favourite TV show?")]
)

for event in runner.run(
    user_id=USER_ID,
    session_id=SESSION_ID,
    new_message=new_message
):
    if event.is_final_response():
        if event.content and event.content.parts:
            print(f"Final Response: {event.content.parts[0].text}")

print("==== Session Event Exploration ====")
session = session_service_stateful.get_session(
    app_name=APP_NAME, user_id=USER_ID, session_id=SESSION_ID
)

print("==== Final Session State ====")
for key, value in session.state.items():
    print(f"{key}: {value}")
    