# Author: Yvette Wade 
# Date: 05/18/2021
# Description: 10-1

# This week we will create a program that performs file processing activities.  Your program this week will use the OS library in order to validate that a directory exists before creating a file in that directory.  

import os

# Your program will prompt the user for the directory they would like to save the file in 

while True: # main program loop

    while True: # loop for validating the directory name/existence

        directory_name = input("What directory would you like to save the file in?\n")

        # Make sure the directory exists before proceeding.
        dir_list = os.listdir() # get a list of all things/objects in the current folder
        #print(dir_list)

        if directory_name in dir_list:
            print("Your folder has been located")
            break
        else:
            print(f"{directory_name} was not found in the current directory.")
            print("Current folder contains:",dir_list) 
            print("Please enter an existing directory/folder name.")

    # as well as the name of the file.  

    filename=input("Enter the file name that you would like to use for the new file:\n")

    #print(directory_name,filename)

    # The program should then prompt the user for their name, address, and phone number.

    user_name = input("Please enter your name: ")
    user_phone = input("Please enter you phone number: ")
    user_address = input ("please enter your address: ")

    # Your program will write this data to a comma separated line in a file and store the file in the directory specified by the user.

    filepath = directory_name+'/'+filename
    #print("filepath")
    #print(filepath)

    # open/create the file with "write" permission (means we are going to write data OVER anything presently in the file)
    f = open(filepath,"w")

    # write our data to the file
    f.write(user_name + "," + user_phone + "," + user_address)

    # close the file
    f.close()

    # Once the data has been written your program should read the file you just wrote to the file system and display the file contents to the user for validation purposes. 

    # open the file (again), but this time with READ permission
    f =open(filepath,"r")

    # read the content from the file
    contents = f.read()
    f.close()

    # show the content on the screen
    print("File contents, below:")
    print(contents)

    # ask if the content is correct
    is_correct = input("Are the file contents correct? (yes/no)\n")

    # if correct, then end the program
    if is_correct == "yes":
        break

    # if incorrect, then start the program over
    print("Okay. Let's try again.")
