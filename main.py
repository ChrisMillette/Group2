class Doctor(object):
    
    global doctors
    doctors = {}

    def __init__(self):
        self.Doctor = Doctor()
    
    def formatDrInfo():
        data = ''
        count = 0
        for i in doctors:
            for x in doctors[i]:
                if count == 0 or count % 6 == 0:
                    data = data + '\n' + x
                    count += 1
                else:
                    data = data + '_' + x
                    count += 1
        return data
            
    def enterDrInfo():
        data = []
        data.append(input("Enter the doctor's ID:\n\n\t"))
        data.append(input("Enter the doctor's name:\n\n\t"))
        data.append(input("Enter the doctor's specialty:\n\n\t"))
        data.append(input("Enter the doctor's timing (e.g., 7am-10pm):\n\n\t"))
        data.append(input("Enter the doctor's qualification:\n\n\t"))
        data.append(input("Enter the doctor's room number:\n\n\t"))
        doctors[data[0]] = data
        print("\nBack to the previous menu\n")

    def readDoctorsFile():
        data = {}
        count = 0
        file = open("files\doctors.txt", "r")
        for i in file.readlines():
            i = i.replace(' ', '')
            i = i.replace('\n','')
            data[count] = i.split('_', 5)
            count += 1
        for i in data:
            if i == 0:
                doctors['0'] = data[i]
            else:
                doctors[data[i][0]] = data[i]
        file.close()

    def searchDoctorById():
        
        for i in doctors:
            if i == entry:
                result = True
                break
            else:
                result = False
        if result == True:
            return True
        else:
            return False       

    def searchDoctorByName():
        name = input(" Enter the doctor name:")
        for i in doctors:
            if doctors[i][1] == name:
                loc = i
                result = True
                break
            else:
                result = False
        if result == True:
            return True, loc
        else:
            return False

    def displayDoctorInfo(id):
        print("\n{:<8} {:<25} {:<15} {:<10} {:<20} {:<20}\n".format('ID', 'Name', 'Specialty', 'Timing', 'Qualification', 'Room Number'))
        print("{:<8} {:<25} {:<15} {:<10} {:<20} {:<20}".format(id, doctors[id][1], doctors[id][2], doctors[id][3], doctors[id][4], doctors[id][5]))        

    def editDoctorInfo():
        id = input("Please enter the ID of the doctor that you want to edit their information:\n\n")
        doctors[id][1] = input("Enter new Name:\n\n")
        doctors[id][2] = input("Enter new Specialty:\n\n")
        doctors[id][3] = input("Enter new Timing:\n\n")
        doctors[id][4] = input("Enter new Qualification\n\n")
        doctors[id][5] = input("Enter new Room number:\n\n")
        print("\nBack to the previous menu\n")

    def displayDoctorsList():
        print("\n{:<8} {:<25} {:<15} {:<10} {:<20} {:<20}\n".format('ID', 'Name', 'Specialty', 'Timing', 'Qualification', 'Room Number'))
        for i in doctors:
            if i != '0':
                print("{:<8} {:<25} {:<15} {:<10} {:<20} {:<20}".format(i, doctors[i][1], doctors[i][2], doctors[i][3], doctors[i][4], doctors[i][5]))
        print("\nBack to the previous menu\n")

    def writeListOfDoctorsToFile(data):
        file = open("files\doctors.txt", "w")
        for i in data:
            file.write(i)
        file.close()

    def addDrToFile():
        data = ''
        file = open("files\doctors.txt", "a")
        data += '\n' + input("Enter the doctor's ID:\n\n") + '_'
        data += input("Enter the doctor's name:\n\n") + '_'
        data += input("Enter the doctor's specialty:\n\n") + '_'
        data += input("Enter the doctor's timing (e.g., 7am-11pm):\n\n") + '_'
        data += input("Enter the doctor's qualification:\n\n") + '_'
        data += input("Enter the doctor's room number:\n\n")
        file.write(data)
        file.close()
        print("\nBack to the previous menu\n")




