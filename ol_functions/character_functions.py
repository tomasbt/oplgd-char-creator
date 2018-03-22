
import ol_classes

def create_character(character_dict):
    """
    Generate a character
    """ 
    name = character_dict["name"]

    character = ol_classes.character(name)

    if 'race' in character_dict.keys():
        1

    return character