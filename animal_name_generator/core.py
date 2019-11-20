import random

first_names = ['toby',
               'molly',
               'peter',
               'kelsey',
               'lauren',
               'robert']

animals = ['frog',
           'pony',
           'bird',
           'zebra',
           'hamster',
           'fish']


def generate_name() -> str:
    """Generate a random animal name
    """
    first_name = random.choice(first_names).capitalize()
    animal = random.choice(animals).capitalize()
    name = '{} the {}'.format(first_name, animal)
    return name
