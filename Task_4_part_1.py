class Property:
    """
    The class stores the property information
    """
    def __init__(self, square_feet='', beds='',
                 baths='', **kwargs):
        """
         I  added the extra **kwargs parameter to __init__ because
         I know it's going to be used in a multiple inheritance situation.
         I also included a call to super().__init__ in case I am not the last
         call in the multiple inheritance chain.
        """
        super().__init__(**kwargs)
        self.square_feet = square_feet
        self.num_bedrooms = beds
        self.num_baths = baths

    def display(self):
        """
        This function displaying property details
        """
        print("PROPERTY DETAILS")
        print("================")
        print("square footage: {}".format(self.square_feet))
        print("bedrooms: {}".format(self.num_bedrooms))
        print("bathrooms: {}".format(self.num_baths))
        print()

    def prompt_init():
        """
        This function return dictionary with information about the count of
        square feet, beds, baths
        """
        return dict(square_feet=input("Enter the square feet: "),
                    beds=input("Enter number of bedrooms: "),
                    baths=input("Enter number of baths: "))

    prompt_init = staticmethod(prompt_init)


class Apartment(Property):
    """
    The class stores the Apartment information
    """
    valid_laundries = ("coin", "ensuite", "none")
    valid_balconies = ("yes", "no", "solarium")


    def __init__(self, balcony='', laundry='', **kwargs):
        """
        Initialing the  apartment attributes by calling super init and adding
        2 attributes
        """
        super().__init__(**kwargs)
        self.balcony = balcony
        self.laundry = laundry

    def display(self):
        """
        This function displaying property details
        """
        super().display()
        print("APARTMENT DETAILS")
        print("laundry: %s" % self.laundry)
        print("has balcony: %s" % self.balcony)

    def prompt_init():
        """
        This function return dictionary with information about apartment

        """
        parent_init = Property.prompt_init()
        laundry = ''
        while laundry.lower() not in \
                Apartment.valid_laundries:
            laundry = input("What laundry facilities does "
                            "the property have? ({})".format(
                                ", ".join(Apartment.valid_laundries)))
        balcony = ''
        while balcony.lower() not in \
                Apartment.valid_balconies:
            balcony = input(
                "Does the property have a balcony? "
                "({})".format(
                    ", ".join(Apartment.valid_balconies)))
        parent_init.update({
            "laundry": laundry,
            "balcony": balcony
        })
        return parent_init

    prompt_init = staticmethod(prompt_init)


def get_valid_input(input_string, valid_options):
    """
    This function checking our input
    """
    input_string += " ({}) ".format(", ".join(valid_options))
    response = input(input_string)
    while response.lower() not in valid_options:
        response = input(input_string)
    return response


def prompt_init():
    """
    Updating our input information
    """
    parent_init = Property.prompt_init()
    laundry = get_valid_input(
        "What laundry facilities does "
        "the property have? ",
        Apartment.valid_laundries)
    balcony = get_valid_input(
               "Does the property have a balcony? ",
               Apartment.valid_balconies)
    parent_init.update({
               "laundry": laundry,
               "balcony": balcony
               })
    return parent_init
prompt_init = staticmethod(prompt_init)


class House(Property):
        """
        The class stores the House information
        This class employs class methods and attributes from class Property
        """
    valid_garage = ("attached", "detached", "none")
    valid_fenced = ("yes", "no")
       
       
    def __init__(self, num_stories='',garage='', fenced='', **kwargs):
           """
        Initialing the  House attributes by calling super init and adding 3 attributes

           """
           super().__init__(**kwargs)
           self.garage = garage
           self.fenced = fenced
           self.num_stories = num_stories

       def display(self):
           """
            This function displaying our house information
           """
           super().display()
           print("HOUSE DETAILS")
           print("# of stories: {}".format(self.num_stories))
           print("garage: {}".format(self.garage))
           print("fenced yard: {}".format(self.fenced))
       def prompt_init():
           """
            This function convert  our input in dictionary
           """
           parent_init = Property.prompt_init()
           fenced = get_valid_input("Is the yard fenced? ",
                       House.valid_fenced)
           garage = get_valid_input("Is there a garage? ",
                   House.valid_garage)
           num_stories = input("How many stories? ")
           parent_init.update({
                    "fenced": fenced,
                    "garage": garage,
                    "num_stories": num_stories
            })
           return parent_init
prompt_init = staticmethod(prompt_init)
class Purchase:
    """
    This class holds information about buying a property
    """
    def __init__(self, price='', taxes='', **kwargs):
       """
        Initialing the  Purchase attributes by calling super init and adding 2 attributes
       """
       super().__init__(**kwargs)
       self.price = price
       self.taxes = taxes
    def display(self):
        """
        This function displaying our Purchase information
        """
        super().display()
        print("PURCHASE DETAILS")
        print("selling price: {}".format(self.price))
        print("estimated taxes: {}".format(self.taxes))
    def prompt_init():
        """
        This function convert  our input in dictionary
        """
        return dict(
           price=input("What is the selling price? "),
           taxes=input("What are the estimated taxes? "))
    prompt_init = staticmethod(prompt_init)
class Rental:
   """
    This class holds information about renting a property
   """

   def __init__(self, furnished='', utilities='',rent='', **kwargs):
    """
    Initialing the  Rental attributes by calling super init and adding 3 attributes
    """
    super().__init__(**kwargs)
    self.furnished = furnished
    self.rent = rent
    self.utilities = utilities
   def display(self):
        """
        This function displaying our Rental information
       """
        super().display()
        print("RENTAL DETAILS")
        print("rent: {}".format(self.rent))
        print("estimated utilities: {}".format(
            self.utilities))
        print("furnished: {}".format(self.furnished))

   def prompt_init():
        """
        This function convert  our input in dictionary
       """
        return dict(
            rent=input("What is the monthly rent? "),
            utilities=input(
                "What are the estimated utilities? "),
            furnished = get_valid_input(
                "Is the property furnished? ",
                    ("yes", "no")))
prompt_init = staticmethod(prompt_init)

class HouseRental(Rental, House):
    """
    This class contains information about house rental
    This class inherits methods and attributes from classes Rental and House
    """
    def prompt_init():
        """
        This function return information about rental of the house
        """
        init = House.prompt_init()
        init.update(Rental.prompt_init())
        return init
prompt_init = staticmethod(prompt_init)
init = HouseRental.prompt_init()

class ApartmentRental(Rental, Apartment):
    """
    This class contains information about apartment rental
    This class inherits methods and attributes from classes Rental and Apartment
    """
    def prompt_init():
        """
        This function return information about rental of the apartment
        """
        init = Apartment.prompt_init()
        init.update(Rental.prompt_init())
        return init
prompt_init = staticmethod(prompt_init)

class ApartmentPurchase(Purchase):
    """
    This class contains information about apartment purchase
    This class inherits methods and attributes from class Purchase

    In this class I have avoided the imitation of two classes with the composition
    """
    def prompt_init():
        """
         This function return information about purchase of the apartment
        """
        init = Apartment.prompt_init()
        init.update(Purchase.prompt_init())
        return init
prompt_init = staticmethod(prompt_init)

class HousePurchase(Purchase):
    """
    This class contains information about house purchase
    This class inherits methods and attributes from class Purchase

    In this class I have avoided the imitation of two classes with the composition
    """
    def prompt_init():
        """
        This function return information about purchase of the house
        """
        init = House.prompt_init()
        init.update(Purchase.prompt_init())
        return init
prompt_init = staticmethod(prompt_init)

class Agent:
    """
    This class contain information about about all properties
    """
    def __init__(self):
        """
        Initializes a list from all of ours properties
        """
        self.property_list = []
        self.count_apartments = 1
        self.count_houses = 1


    def display_properties(self):
        """
        This function display our properties
        """
        for property in self.property_list:
            property.display()
    type_map = {
        ("house", "rental"): HouseRental,
        ("house", "purchase"): HousePurchase,
        ("apartment", "rental"): ApartmentRental,
        ("apartment", "purchase"): ApartmentPurchase
        }
    def add_property(self):
        """
        This function adding new property
        """
        property_type = get_valid_input(
            "What type of property? ",
                ("house", "apartment")).lower()
        if property_type == "apartment":
            self.count_apartments += 1
        else:
            self.count_houses += 1
        payment_type = get_valid_input(
               "What payment type? ",
               ("purchase", "rental")).lower()
        PropertyClass = self.type_map[
            (property_type, payment_type)]
        init_args = PropertyClass.prompt_init()
        self.property_list.append(PropertyClass(**init_args))

    def count_properties(self):
        """
        This function add to attribute count count of properties
        """
        self.count = len(self.property_list)

    def relation(self):
        """
        This function display relation between house and apartment
        """
        print("Relation between house and apartment", self.count_houses / self.count_apartments)
        
    """
    I have avoided the imitation of two classes with the composition in classes ApartmentPurchase and  HousePurchase
    """
