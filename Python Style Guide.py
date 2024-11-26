#Python Style Guide 
#Boxiang Zhang
#11.26
#this program will answer questions RPG Nested Dictionaries Checklist

game_data = {
    "characters": {
        "hero": {
            "name": "Aragon",
            "class": "Warrior",
            "special_ability": "Sword Mastery",
            "description": "A brave warrior skilled in combat.",
        },
        "villain": {
            "name": "Morgath",
            "class": "Dark Sorcerer",
            "special_ability": "Dark Magic",
            "description": "An evil sorcerer seeking to conquer the world.",
        },
    },
    "inventory": {
        "sword": {
            "name": "Flameblade",
            "type": "Weapon",
            "description": "A sword imbued with the power of fire.",
        },
        "potion": {
            "name": "Healing Potion",
            "type": "Consumable",
            "description": "Restores 50 health points when used.",
        },
    },
    "locations": {
        "forest": {
            "name": "Enchanted Forest",
            "description": "A mystical forest filled with ancient magic.",
        },
        "castle": {
            "name": "Shadow Castle",
            "description": "The stronghold of Morgath, surrounded by dark energies.",
        },
    },
}

def print_characters():
    """Prints all characters with their details."""
    print("Characters:\n")
    for character, details in game_data["characters"].items():
        print(f"{details['name']} ({details['class']})")
        print(f"  Special Ability: {details['special_ability']}")
        print(f"  Description: {details['description']}")
        print("-" * 40)

def print_inventory():
    """Prints all inventory items with their details."""
    print("\nInventory Items:\n")
    for item, details in game_data["inventory"].items():
        print(f"{details['name']} ({details['type']})")
        print(f"  Description: {details['description']}")
        print("-" * 40)

def print_locations():
    """Prints all locations with their details."""
    print("\nLocations:\n")
    for location, details in game_data["locations"].items():
        print(f"{details['name']}")
        print(f"  Description: {details['description']}")
        print("-" * 40)

if __name__ == "__main__":
    print_characters()
    print_inventory()
    print_locations()
