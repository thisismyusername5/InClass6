
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
        status -- a string of the status of the user referenced in the instance. 
            The following are the statuses currently in use:
                'active' (default)
                'inactive'
        
    The following methods are part of this class:
        __str__ : returns a readable line of text of the current object
        
    There is a class attribute:
        count : the number of instances of the User class
    """
    count = 0
    
    def __init__(self, username, lastname, firstname):
        # Insert your code here
        count += 1
    
    def __str__(self):
        return (f"Username: {self.username} ({self.lastname}, {self.firstname}) [{self.status}]")
        
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
        status -- a string of the status of the user referenced in the instance. 
            The following are the statuses currently in use:
                'active' (default)
                'inactive'
                'needs repair'
        
    The following methods are part of this class:
        __str__ : returns a readable line of text of the current object
        
    There is a class attribute:
        count : the number of instances of the Equipment class
    """
    count = 0
    
    def __init__(self, uuid=None, category=None, device=None, location=None, value = 0.0):
        # Insert you code here
        count += 1
        
    def __str__(self):
        return (f"{self.uuid}, {self.category}, {self.device}, {self.location}, {self.value}, {self.status}")
    
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
         status -- a string of the status of the user referenced in the instance. 
            The following are the statuses currently in use:
                'active' (default)
                'inactive'
                'needs repair'
         os -- the operating system installed on the computer device
         
     The following methods are part of this class:
         __str__ : returns a readable line of text of the current object
         
     There is a class attribute:
         count : the number of instances of the Equipment class    
    """
    count = 0
    def __init__(self, uuid, category, device, location, value = 0.0):
        # insert your code here
        count += 1
        
        def __str__(self):
            return (f"{self.uuid}, {self.category}, {self.device}, {self.os}, {self.location}, {self.value}, {self.status}")