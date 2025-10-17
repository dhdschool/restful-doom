import requests
from enum import Enum
from random import randint

base_url = "http://localhost:6666/api/"

def spawn_imp(amount: int = 2):
    for i in range(amount):
        requests.post(
            base_url + "world/objects",
            json={
                "type":"IMP",
                "distance":200 + randint(-100, 100)
            }
        )

def heal_player(amount: int =50):
    response = requests.get(
        base_url + "player"
    ).json()
    
    print(f"Old health: {response["health"]}")
    
    new_health = response["health"] + amount
    new_response = {
        "health": new_health,
        "weapon": response["weapon"],
        "armor": response["armor"],
        "ammo": 0, "amount": response['ammo']['Bullets']
    }
    
    print(f"New health: {new_health}")
    
    requests.patch(
        base_url + "player",
        json=new_response
    )
    
tools = [
    {
        "type":"function",
        "function":{
            "name":"spawn_imp",
            "description":"Spawns a number of imps into the game world, specified by the amount parameter",
            "parameters":{
                "type":"object",
                "properties":{
                    "amount":{
                        "type":"integer",
                        "description": "How many imps to spawn."
                    }
                },
                "required": ["amount"]
            }
        }
    },
    
    {
        "type":"function",
        "function":{
            "name":"heal_player",
            "description":"Heals the player by an amount of health specified by the amount parameter",
            "parameters":{
                "type":"object",
                "properties":{
                    "amount":{
                        "type":"integer",
                        "description": "How much health to restore"
                    }
                },
                "required": ["amount"]
            }
        }
    },
]



    