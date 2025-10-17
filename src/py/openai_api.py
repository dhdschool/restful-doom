import openai
import dotenv
from enum import Enum
from tool_calls import *
import json


OPENAI_API_KEY = dotenv.get_key(".env", "OPENAI_API_KEY")
client = openai.OpenAI(api_key=OPENAI_API_KEY)

SYSTEM_PROMPT = """
You are an game controller for the hit 1994 game DOOM.
You will recieve messages in real time from inside the game, but cannot communicate back with the user.
Your job is to decide whether to call a tool. 
Call tools liberally, and infer what the user might mean as they have short input windows. 
If no tool should be called, reply with no content. 
Do NOT write any conversational text. 
Output ONLY a tool call or nothing.
"""

def llm_call(user_chat: str):
    response = client.chat.completions.create(
        model="gpt-5-nano",
        messages=[
            {
            "role":"developer",
            "content":SYSTEM_PROMPT
            },
            {
            "role":"user",
            "content":user_chat
            }
        ],
        tools=tools,
        tool_choice="auto"
    )
    
    calls = response.choices[0].message.tool_calls
    for call in calls:
        if call.type != "function":
            continue
        
        name = call.function.name
        kwargs = json.loads(call.function.arguments)
        
        if name == "spawn_imp":
            spawn_imp(**kwargs)
        elif name == "heal_player":
            heal_player(**kwargs)
    
