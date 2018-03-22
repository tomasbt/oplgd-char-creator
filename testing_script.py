
import ol_classes as ol_c
import ol_functions as ol_f


if __name__ == '__main__':
    print("Starting testing script")

    my_dict = {"name": "Karsten"}

    tmp = ol_f.create_character(my_dict)

    print(tmp.name)

    
    