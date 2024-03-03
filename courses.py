rooms = {
    "CSC101": "3004",
    "CSC102": "4501",
    "CSC103": "6755",
    "NET110": "1244",
    "COM241": "1411"
}

instructors = {
    "CSC101": "Haynes",
    "CSC102": "Alvarado",
    "CSC103": "Rich",
    "NET110": "Burke",
    "COM241": "Lee"
}

times = {
    "CSC101": "8:00 am",
    "CSC102": "9:00 am",
    "CSC103": "10:00 am",
    "NET110": "11:00 am",
    "COM241": "1:00 pm"
}



def checkKey(key, rooms, instructors, times): 
    if key in rooms.keys(): 
        print("Room: ", rooms[key])
        print("Instructor: ", instructors[key])
        print("Times: ", times[key]) 
    else: 
        print("Invalid course entry.")

course = input("Enter a course number: ")

checkKey(course, rooms, instructors, times)