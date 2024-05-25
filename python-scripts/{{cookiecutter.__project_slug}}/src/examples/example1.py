# You can run this script by executing `python example1.py` in the terminal or import it in another script

dog_name = "Rex"


def get_cat_name():
    return "Fluffy"


# This part will only run if you execute this script directly, not if you import it in another script
if __name__ == "__main__":
    print(f"Dog name: {dog_name}")
    print(f"Cat name: {get_cat_name()}")
