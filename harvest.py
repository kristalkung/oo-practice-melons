############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name):
        """Initialize a melon."""

        self.pairings = []

        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name


    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    melon_type_1 = MelonType("musk", "First harvest in 1988", "green", True, True, 
                 "Muskmelon")
    all_melon_types.append(melon_type_1)
    melon_type_1.add_pairing("mint")

    melon_type_2 = MelonType("cas", "First harvest in 2003", "orange", False, False, 
                 "Casaba")
    all_melon_types.append(melon_type_2)
    melon_type_2.add_pairing("mint")
    melon_type_2.add_pairing("strawberries")

    melon_type_3 = MelonType("cren", "First harvest in 1996", "green", False, False, 
                 "Crenshaw")
    all_melon_types.append(melon_type_3)
    melon_type_3.add_pairing("proscuitto")

    melon_type_4 = MelonType("yw", "First harvest in 2013", "yellow", False, True, 
                 "Yellow Watermelon")
    all_melon_types.append(melon_type_4)
    melon_type_4.add_pairing("ice cream")

    return all_melon_types

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""
    melon_types = make_melon_types()

    for melon in melon_types:
        print(f'{melon.name} pairs with')
        for pairing in melon.pairings:
            print(f'- {pairing}')
        print("")

# print_pairing_info(make_melon_types)

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""
    melon_types = make_melon_types()
    melon_dict = {}

    for melon in melon_types:
        melon_dict[melon.code] = melon
    
    return melon_dict

print(make_melon_type_lookup(make_melon_types))

############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods

    def __init__(self, melon_type)

def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest 



