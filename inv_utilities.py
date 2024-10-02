import csv
from inv_classes import User, Equipment, Computer

def load_user_file(infile):
    """
    The load_user_file() function will process a .csv file and return a 
    list of class User
    
    Parameters:
    ------------
        infile:
            the name of the csv file to be processed
        
    An example csv file shows the structure of the csv:
        UserID,FirstName,LastName,Status
        E1221377,Gregory,Cook,active
        S1113954,Emelia,Hayes,active
        S1137091,Louis,Mejia,active
        
    Returns
    -------
        a list of tuples containing the data from class User
    """
    
    #create an empty list to hold each row in the file
    proc_list = ??
    
    with open(infile, 'r') as f:
        # create a csv.reader()
        user_reader = ??
        
        # keep track of the number of lines read
        line_count = 0
        for row in user_reader:
            # loop through the file.  Do not process the header row
            if line_count > 0:
                # create a new User instance using the data from the file
                new_user = ??
                new_user.status = ??
                
                # add the new user instance to the list
                ??
            line_count += 1
            
    # return the populated list of User instances      
    return proc_list

def load_equipment_file(infile):
    """
    Parameters
    ----------
    infile :
        A .csv file containing equipment information
        
    An example csv file shows the structure of the csv:
        UUID,Category,Device,OS,Location,Value,Status
        64e3e407-7700-4d6a-8964-1991a0535f51,PC,Dell Optiplex 7060,Microsoft Windows 10 Pro,BR CC 209,0,active
        0f3e9be6-4e72-4d96-a70b-0e80858b47c6,PC,Dell Optiplex 7060,Microsoft Windows 10 Pro,BR CC 209,0,active
        7ecb22b2-ddc4-49fd-a1ad-8fdbb280526d,PC,Dell Optiplex 7060,Microsoft Windows 10 Pro,BR CC 209,0,active

    Returns
    -------
    a list of tuples containing the data from classes Equipment and sub-classes

    """
    
    #create an empty list to hold each row in the file
    equip_list = ??
    
    with open(infile, 'r') as f:
        # create a csv.reader()
        e_reader = ??
        
        # keep track of the number of lines read        
        line_count = 0
        for row in e_reader:
            # loop through the file.  Do not process the header row
            if line_count > 0:
                # determine the category of the piece of equipment from the row
                cat = ??
                
                # depending on the category, you will create an instance of type Computer or type Equipment
                if cat == 'PC' or cat == 'Server':
                    # create a new Computer instance using the data from the file
                    comp = ?
                    comp.os = ??
                    comp.status = ??
                    # add the new Computer instance to the list
                    ??
                else:
                    # create a new Computer instance using the data from the file
                    eq = ??
                    eq.status = ??
                    # add the new Equipment instance to the list
                    ??
            line_count += 1
    
    return(equip_list)

def print_user_listing(user_list, show_active_only = False):
    """
    The print_uers_listing() displays formatted list of users to the screen
    
    Parameters
    ----------
    user_list:
        a list of tuples containing the: (username, lastname, firstname, status)
    show_active_only:
        if this is set to True, then only those user records with a status of 'active' is displayed
        
    An example csv file shows the structure of the csv:
        UUID,Category,Device,OS,Location,Value,Status
        64e3e407-7700-4d6a-8964-1991a0535f51,PC,Dell Optiplex 7060,Microsoft Windows 10 Pro,BR CC 209,0,active
        0f3e9be6-4e72-4d96-a70b-0e80858b47c6,PC,Dell Optiplex 7060,Microsoft Windows 10 Pro,BR CC 209,0,active
        7ecb22b2-ddc4-49fd-a1ad-8fdbb280526d,PC,Dell Optiplex 7060,Microsoft Windows 10 Pro,BR CC 209,0,active

    Returns
    -------
    print_user_function returns Nothing.  
    """
    
    # print a header row:
        
    # loop throught the list and display the information in each tuple in the list. 
    # if the show_active_only attribute is True, only display the user information that has a status of 'active'
    pass

def print_equipment_listing(equipment_list, show_active_only = False):
    """
    The print_equipment_listing() displays formatted list of computers and other quipment to the screen
    
    Parameters
    ----------
    equipment_list:
        a list of tuples containing the: (uuid, category, device, os, location, value, status) if it represents 
          a computer or (uuid, category, device, location, value, status) if it represents other equipment
        
    show_active_only:
        if this is set to True, then only those user records with a status of 'active' is displayed
        
    An example csv file shows the structure of the csv:
        UUID,Category,Device,OS,Location,Value,Status
        64e3e407-7700-4d6a-8964-1991a0535f51,PC,Dell Optiplex 7060,Microsoft Windows 10 Pro,BR CC 209,0,active
        0f3e9be6-4e72-4d96-a70b-0e80858b47c6,PC,Dell Optiplex 7060,Microsoft Windows 10 Pro,BR CC 209,0,active
        7ecb22b2-ddc4-49fd-a1ad-8fdbb280526d,PC,Dell Optiplex 7060,Microsoft Windows 10 Pro,BR CC 209,0,active

    Returns
    -------
    print_equipment_listing_function returns Nothing.  
    """
    
    # print a header row:
        
    # first loop through the list and display the information about computers in the tuples in the list. 
    # Then loop through the list and display the information about other equipment in the tuples in the list
    # if the show_active_only attribute is True, only display the user information that has a status of 'active'
    pass

                              
                
