import asyncio
import time
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types
from agents import mgr_agent
from config import APP_NAME, DEFAULT_USER_ID, DEFAULT_SESSION_ID

async def run_demo_task(query):
    session_service = InMemorySessionService()
    runner = Runner(
        agent=mgr_agent,
        app_name=APP_NAME,
        session_service=session_service,
    )

    await session_service.create_session(
        app_name=APP_NAME,
        user_id=DEFAULT_USER_ID,
        session_id=DEFAULT_SESSION_ID
    )

    print(f"\n--- Running Task: {query} ---")
    async for event in runner.run_async(
        user_id=DEFAULT_USER_ID,
        session_id=DEFAULT_SESSION_ID,
        new_message=types.Content(role="user", parts=[types.Part(text=query)])
    ):
        if event.is_final_response():
            print(f"Final Response: {event.content.parts[0].text}")

if __name__ == "__main__":
    queries = [
        "What is 1024 / 4?",
        "Check the mainframe status.",
        "Write a simple C function to add two numbers.",
        "Manager, please ask Ops to check the server and then ask Dev to write a script for it."
    ]

    for q in queries:
        asyncio.run(run_demo_task(q))
        time.sleep(2)
