
import ol_classes

def create_character(character_dict):
    """
    Generate a character
    """ 
    name = character_dict["name"]

    character = ol_classes.character(name)

    if 'race' in character_dict.keys():
        character.race = character_dict["race"]

    # player name 

    # archtype

    # level 

    # experience

    # description

    # attributes

    # feats

    # equipment

    # defences

    # wealth
    
    # speed 

    # hit points

    # initiative

    # perks

    # flaws

    # actions

    return character

def create_character_guide():
    # Initial dictionary
    character_dict = {}

    # Get name and race
    character_dict["name"] = input("Character name: ")
    character_dict["race"] = input("race: ")    

    return create_character(character_dict)
    