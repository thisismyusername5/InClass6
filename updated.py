
class User():
    """
    The User class represents the information that defines the individual users 
    
    To initate: 
        user_var = User(username, lastname, firstname)
        
        where:
            username is the assigned unique name assigned to that user (string)
            lastname is the last name of the user (string)
            firstname is the first name of the user (string)
            
    The following attributes are part of this class:
        username, lastname, firstname -- as defined above
        
    The following methods are part of this class:
        __str__ : returns a readable line of text of the current object
        
    There is a class attribute:
        count : the number of instances of the User class
    """
    
    # you will need to keep track of the number of instances created by the class.
    count = 0
    
    def __init__(self, username, lastname, firstname):
        # Write the script to instantiate the class.
        self.username = username
        self.lastname = lastname
        self.firstname = firstname
        # Set the public class attributes with the values passed 
        # Don't forget to update the class variable keeping track of the number
        # of instances.
        User.count += 1
        
    def __str__(self):
        # Override the default __str__() function.  You should return a string
        # formatted as: "Username: username (lastname, firstname)"
        return f"Username: {username} ({lastname}, {firstname})"
    
        
class Equipment():
    """
    The Equipment class represents the information that defines the equipment
    being tracked and monitored by the IT department
    
    To initate: 
        equip_var = Equipment(uuid, category, device, location, value)
        
        where:
            uuid is the assigned Universally Unique Identifier of the equipment (string)
            category is the category used to identify the type of equipment(string)
            device is the name of the piece of equipment 
                (e.g., "Dell PowerEdge R250") (string)
            location is the current location of the piece of equipment (string)
            value is the monetary value of the piece of equipment (float)
            
            
    The following attributes are part of this class:
        uuid, category, device, location, value -- as defined above
        
    The following methods are part of this class:
        __str__ : returns a readable line of text of the current object
        
    There is a class attribute:
        count : the number of instances of the Equipment class
    """

    count = 0
    
    def __init__(self, uuid, category, device, location, value = 0.0):
        # Write the script to instantiate the class.  
        # Set the public class attributes with the values passed
        self.uuid = uuid
        self.category = category
        self.device = device
        self.location = location
        self.value = value
        # Don't forget to update the class variable keeping track of the number
        # of instances.
        Equipment.count += 1
        
    def __str__(self):
        # Override the default __str__() function.  You should return a string
        # formatted as: "uuid, category, device, location, value"
        return f"{self.uuid}, {self.category}, {self.device}, {self.location}, {self.value}"
    
class Computer(Equipment):
    """
    The Computer class is a sub-class of the Equipment class
    To initate: 
        computer_var = Cmomputer(uuid, category, device, location, value)
        
        where:
            uuid is the assigned Universally Unique Identifier of the equipment (string)
            category is the category used to identify the type of equipment(string)
            device is the name of the piece of equipment 
                (e.g., "Dell PowerEdge R250") (string)
            location is the current location of the piece of equipment (string)
            value is the monetary value of the piece of equipment (float)
            
     The following attributes are part of this class:
         uuid, category, device, location, value -- as defined above
         os -- the operating system installed on the computer device
         
     The following methods are part of this class:
         __str__ : returns a readable line of text of the current object
         
     There is a class attribute:
         count : the number of instances of the Equipment class    
    """
    count = 0
    
    def __init__(self, uuid, category, device, location, value = 0.0):
        # Write the script to instantiate the class.  
        
        # Since the value passed in are inherited from the Equipment class you
        # should call the parent __init__ funtion
        super().__init__(uuid, category, device, location, value)
        # Set the public os attribute to ""
        self.os = ""
        # Don't forget to update the class variable keeping track of the number
        # of instances.
        Computer.count += 1
        
        def __str__(self):
            # Override the default __str__() function.  You should return a string
            # formatted as: "uuid, category, device, os, location, value"
            return f"{self.uuid}, {self.category}, {self.device}, {self.os}, {self.location}, {self.value}"

def print_user_list(user_list):
    """
    This function will print a listing of the objects (of class User) in
    the passed list.
    """
    print('-'*50)
    print("Users")
    print('-'*50)
    for u in user_list:
        print(f"{u.lastname.strip()}, {u.firstname}\t ( {u.username} )")


def print_equipment_list(eq_list):
    """
    This function will print a listing of the objects (of class Equipment or
       class Computer) in the passed list.  
    
    Note: the list should only contain one type of class object
    If the first item in the list is of class Computer, it will process the 
    list as comprised of the Computer class, otherwise it will process the list
    as comprised of the Equipment class
    """
    
    if len(eq_list) > 0:
        if type(eq_list[0]) == Computer:
            print("-"*50)
            print("   Computers")
            print("-"*50)
            print("UUID, Device, Operating System, Location")
            for c in eq_list:
                print(f"{c.uuid}, {c.device}, {c.os}, {c.location}")
        else:
            print("-"*50)
            print("   Other Equipment")
            print("-"*50)
            print("UUID, Category, Device, Location")    
            for e in eq_list:
                print(f"{e.uuid}, {e.category}, {e.device}, {e.location}")
            

if __name__ == "__main__":
    """
    You will use this area to unit test your class definitions
    """
    
    # The lists to create for each class
    user_list = list()
    equipment_list = list()
    computer_list = list()
    
    # populate the user_list here
    input_user_list = [("E1221377", "Gregory", "Cook"),
        ("S15819XX", "Matthew", "Ward"),
        ("S13680XX", "Ian", "Edwards"),
        ("S13009XX", "Quinn", "Bailey"),
        ("S15130XX", "Autumn", "Miller"),
        ("S15081XX", "Luke", "Harris"),
        ("S14982XX", "Victoria", "Young"),
        ("S14212XX", "Mila", "Smith"),
        ("S14678XX", "Samual", "Brooks")]
    
    # if you use a list of users for input, process the list here:
    for username, firstname, lastname in input_user_list:
        # As you loop the input_user_list, create an instance of the
        #   User class and then add that instance to the user_list
        user = User(username, lastname, firstname)
        user_list.append(user)

        
    # populate the equipment_list and computer_list here
    input_equip_list= [('91a7a7c7-56fd-4a28-a953-fd83c759f2ab','PC','Dell Optiplex 7060','Microsoft Windows 10 Pro','BR CC 201'),
                   ('bb33cf03-0721-4adf-93ba-d5474921bcd3','PC','Dell Optiplex 7060','Microsoft Windows 10 Pro','BR CC 201'),
                   ('0e93ca48-8308-421d-907e-c7c861014b93','PC','Dell Optiplex 7060','Microsoft Windows 10 Pro','BR CC 201'),
                   ('dc897b52-9823-4326-8f46-1a5597e80db6','PC','Dell Optiplex 7060','Microsoft Windows 10 Pro','BR CC 201'),
                   ('9f4b171c-69b1-4b99-b997-1f2a7049ae27','PC','Dell Optiplex 7060','Microsoft Windows 10 Pro','BR CC 201'),
                   ('6d209e02-1896-497b-b490-c2eb096d4b4f','Switch','Netgear GS308','BR Comp Room'),
                   ('d6d38b1d-61a2-42aa-b4e7-be541b073d1c','Switch','Tanda GS305','BR Comp Room'),
                   ('73bd442b-ccb2-4646-8500-29acaab88866','Server','Dell PowerEdge R250','Red Hat Linux 9.3','BR CC209'),
                   ('9ed5af33-4ea0-4c76-ae02-8d4988b6c857','Server','Dell PowerEdge R250','Red Hat Linux 9.3','BR CC209')]
    
    #if you use a list of equipment and computers, process the list here:
    for eq in input_equip_list:
    #      Extract the appropriate pieces that are in the same place in the input
    #      list reqgardless of whether they are a computer or not
        try:
            uuid, cat, dev, loc, val = eq
        except ValueError:
            uuid, cat, dev, loc = eq
            val = 0.0
        uuid = eq[0]
        cat = eq[1]
        dev = eq[2]
        val = 0.0
        # Then determine the class you will use and which list you will add
        # the instance to:
        if cat == "PC" or cat == "Server":
            os = eq[3]
            loc = eq[4]
            this = Computer(uuid, cat, dev, loc, val)
            this.os = os
            computer_list.append(this)
        else:
            loc = eq[3]
            this = Equipment(uuid, cat, dev, loc, val)
            equipment_list.append((this))

        
    # report each list
    print_user_list(user_list)
    print_equipment_list(computer_list)
    print_equipment_list(equipment_list)
    
    # print out the counts form the class
    print(User.count)
    print(Equipment.count)
    print(Computer.count)
