TOPIC: 
    
    Hostel Entry System

CONTENT:
    
    Currently, entries in the boy register of the girl’s hostel or the girl register of a boy’s hostel are handwritten. We need a system in which you can show when a particular boy or girl has entered the hostel and left it. Girls cannot enter boy's hostel after 10 and vice versa, so the guards need to know who all are inside at any given time. For now, make it for only one hostel of your choice (but feel free to expand it if you are enthusiastic).

    You are required to make a backend using **Django (RestFramework)** to 

    - Store everyone who has entered or exited
    - Register an entry
    - Register an exit
    - Retrieve who all are currently inside the hostel

DATABASE:

    I have decided to make 9 fields namingly
        - Number                      -> Hostel Number in which registry is going to happen 
        - Entered_boy_girl_name       -> Boy/Girl name who is from another hostel has to go to a room in this hostel
        - Entered_boy_girl_roll_no    -> Boy's/Girl's roll no who is from another hostel has to go to a room in this hostel
        - Host_boy_girl_name          -> Boy/Girl whose room is going to be occupied by the girl/boy from another hostel
        - Host_boy_girl_roll_no       -> Boy's/Girl's roll no whose room is going to be occupied by the girl/boy from another hostel
        - Room_no                     -> Boy's/Girl's room no whose room is going to be occupied by the girl/boy from another hostel
        - Date                        -> Date of register for Entry
        - Entry                       -> Time of Entry to hostel
        - Exit                        -> Time of Exit to hostel

URLS:

    View Class              Link                get/post                   What does the class do?  

    Hostel_Entries          /details            get and post               List all contents of database and ability to write the data. This link should be removed in practice, I will remove it once we use this project to main use.
    Enter_into_Hostel       /api/entry          post                       Link to register Entry. Exit part shouldn't be filled
    Exit_from_Hostel        /api/exit           post                       Link to register Exit. Hostel Number, Roll no of host as well different hostel person, Date, Entry and Exit time details are enough
    Details_of_not_exited   /api/not_exited     get                        Link that lists details of all the users that havent exited from the hostel yet
