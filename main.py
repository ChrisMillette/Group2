# doctor class to hold information of particular doctor
class Doctor(object):
    id = 0
    name = ""
    speciality = ""
    timing = ""
    qualification = ""
    roomNumber = 0
    # list to maintain all doctors
    doctor_list = []
    
    def __init__(self, id, name, speciality, timing, qualification, roomNumber):
        self.id = id
        self.name = name
        self.speciality = speciality
        self.timing = timing
        self.qualification = qualification
        self.roomNumber = roomNumber
        self.doctor_list.append(self)       # whenever a constructor is called the doctor is appending the list of doctors

    # function to convert the doctor's information according to the format of doctor.txt file    
    def formatDrInfo(self):
        formatted_data =  str(self.id) + '_' + self.name + '_' + self.speciality + '_' + self.timing + '_' + self.qualification + '_' + str(self.roomNumber)
        return formatted_data


    # this function takes information abput a doctor and returns its object 
    def enterDrInfo(self):
        id = int(input("Enter the doctor's ID: "))
        name = input("Enter the doctor's name: ")
        speciality = input("Enter the doctor's speciality: ")
        timing = input("Enter the doctor's timings (e.g., 7am-10pm): ")
        qualification = input("Enter the doctor's qualifications: ")
        roomNumber = int(input("Enter the doctor's room number: "))
        return Doctor(id, name, speciality, timing, qualification, roomNumber)
        
    # this function reads the doctors' information from the given file
    def readDoctorsFile(self):
        f = open("doctors.txt", "r")
        next(f)  # skips the header of the file 
        lines = f.readlines()
        for line in lines: # reading the file line by line
            id, name, speciality, timing, qualification, roomNumber = line.split('_')   # splitting the contents of the line and saving to variables
            Doctor(int(id), name, speciality, timing, qualification, int(roomNumber))   # creating the doctor's object using the extracted info
        f.close()                                               
        for doc in self.doctor_list:
            if doc.id == self.id:
                print(doc.id, self.id)
                # print("Doctor with the same ID already exists\n")
                self.doctor_list.remove(doc)                                            # removing the doctor with the same id 

    # function to search for a doctor using his/her id 
    def searchDoctorById(self):             
        found = False
        search = int(input("Enter the doctor's ID to search: "))
        f = open("doctors.txt", "r")
        header = (f.readline())
        id, name, speciality, timing, qualification, roomNumber = header.split('_')
        print("{:<4} {:<20} {:<15} {:<15} {:<15} {:<15}".format(id,name,speciality,timing,qualification,roomNumber))    # displaying the header
        
        # searching for doctor in file
        lines = f.readlines()                                                                                            
        for line in lines:
            did, name, speciality, timing, qualification, roomNumber = line.split('_')
            if did == str(search):
                print("{:<4} {:<20} {:<15} {:<15} {:<15} {:<15}".format(did,name,speciality,timing,qualification,roomNumber))   # displaying the doctor's info in a tabular format
                f.close()
                found = True

        # searching for doctor in the list of doctors
        for doc in self.doctor_list:
            if doc.id == id:
                print("{:<4} {:<20} {:<15} {:<15} {:<15} {:<15}".format(doc.id,doc.name,doc.speciality,doc.timing,doc.qualification,doc.roomNumber))
                found = True
        if found == False:
            print("Cant find the doctor with the same ID on the system\n")
        else:
            print("Back to the prevoius menu\n")
        
    # search doctor by name
    def searchDoctorByName(self):
        found = False
        search = input("Enter the doctor's name to search: ")
        f = open("doctors.txt", "r")
        header = (f.readline())
        id, name, speciality, timing, qualification, roomNumber = header.split('_')
        print("{:<4} {:<20} {:<15} {:<15} {:<15} {:<15}".format(id,name,speciality,timing,qualification,roomNumber))
        
        # searching in file
        lines = f.readlines()
        for line in lines:
            id, dname, speciality, timing, qualification, roomNumber = line.split('_')
            if dname == search:
                print("{:<4} {:<20} {:<15} {:<15} {:<15} {:<15}".format(id,dname,speciality,timing,qualification,roomNumber))
                f.close()
                found = True
        

        # searching in doctor's list
        for doc in self.doctor_list:
            if doc.name == name:
                print("{:<4} {:<20} {:<15} {:<15} {:<15} {:<15}".format(doc.id,doc.name,doc.speciality,doc.timing,doc.qualification,doc.roomNumber))
                found = True
        if found == False:   
            print("Cant find the doctor with the same ID on the system\n")
        else:
            print("Back to the prevoius menu\n")

    # display the information of the doctor using its object 
    def displayDoctorInfo(self):
        print(self.id)
        print(self.name)
        print(self.speciality)
        print(self.timing)
        print(self.qualification)
        print(self.roomNumber)
    
    # function to edit the information about a doctor using his/her id
    def editDoctorInfo(self):
        flag = False
        self.readDoctorsFile()  # readint the doctors.txt file and saving all doctors in the list 
        search = int(input("Please enter the id of the doctor that you want to edit their information:  "))
        for doc in self.doctor_list:
            if doc.id == search:        # if the doctor's id is found the program asks for further information to be changed
                flag = True             # set the flag to true 
                print("Enter new Name:")
                name = input("Enter the new name of the doctor: ")
                speciality = input("Enter new Specilist in: ")
                timing = input("Enter new Timing: ")
                qualification = input("Enter new Qualification:  ")
                roomNumber = int(input("Enter new Room number:  "))
                doc.name = name
                doc.speciality = speciality
                doc.timing = timing
                doc.qualification = qualification
                doc.roomNumber = roomNumber
                self.writeListofDoctorsToFile()         # write the changes to the file 
                break
        if flag==False:
            print("Cant find the doctor with the same ID on the system\n")
        else:
            print("Back to the prevoius Menu\n")

    # this function prints all the doctors that are present in the given file
    def displayDoctorsList(self):
        f = open("doctors.txt", "r")
        lines = f.readlines()
        for line in lines:
            id, name, speciality, timing, qualification, roomNumber = line.split('_')
            print("{:<4} {:<20} {:<15} {:<15} {:<15} {:<15}".format(id,name,speciality,timing,qualification,roomNumber))
        f.close()
        print("Back to the prevoius menu\n")

    # this function reads the doctor's list from the program's memory and copy all doctors to file in the same format
    def writeListOfDoctorsToFile(data):
        file = open("files\doctors.txt", "w")
        for i in data:
            file.write(i)
        file.close()
    
    # add a single doctor's information to the txt file
    def addDrToFile(self):
        new = self.enterDrInfo()
        f = open("doctors.txt", "a")
        f.write("\n"+new.formatDrInfo())
        f.close()
        print("Back to the prevoius menu\n")
                
class Facility(object):
    tfile = open ("files/facilities.txt", "r")
    global fac
    fac = tfile.read()
    tfile.close
    global facl 
    facl = fac
    global facu
    facu = fac

    def addFacility():
        global facu
        nfac = input ("Add a New Facility:\n")
        facu = fac+"\n"+nfac


    def displayFacilities():
        print (facu)

    def writeListOffacilitiestoFile():
        wl = open ("files/facilities.txt", "w")
        wl.write(facu)
        wl.close

class Patient(object):

    global patients
    patients = {}

    def __init__(self):
        self.Patient = Patient()
        
    def formatPatientInfo():
        data = ''
        count = 0
        for i in patients:
            for x in patients[i]:
                if count == 0 or count % 5 == 0:
                    data = data + '\n' + x
                    count += 1
                else:
                    data = data + '_' + x
                    count += 1
        return data
    
    def enterPatientInfo():
        data = []
        data.append(input("Enter the patient's ID:\n\n\t"))
        data.append(input("Enter the patient's name:\n\n\t"))
        data.append(input("Enter the patient's specialty:\n\n\t"))
        data.append(input("Enter the patient's timing (e.g., 7am-10pm):\n\n\t"))
        data.append(input("Enter the patient's qualification:\n\n\t"))
        data.append(input("Enter the patient's room number:\n\n\t"))
        patients[data[0]] = data
        print("\nBack to the previous menu\n")

    def readPatientFile():
        data = {}
        count = 0
        file = open("files\patients.txt", "r")
        for i in file.readlines():
            i = i.replace(' ', '')
            i = i.replace('\n','')
            data[count] = i.split('_', 4)
            count += 1
        for i in data:
            if i == 0:
                patients['0'] = data[i]
            else:
                patients[data[i][0]] = data[i]
        file.close()

    def searchPatientById(entry):
        for i in patients:
            if i == entry:
                result = True
                break
            else:
                result = False
        if result == True:
            return True
        else:
            return False

    def displayPatientInfo(id):
        print("\n{:<8} {:<15} {:<15} {:<10} {:<20}\n".format('ID', 'Name', 'Disease', 'Gender', 'Age'))
        print("{:<8} {:<15} {:<15} {:<10} {:<20}".format(id, patients[id][1], patients[id][2], patients[id][3], patients[id][4]))

    def editPatientInfo():
        id = input("Please enter the ID of the patient that you want to edit their information:\n\n")
        patients[id][1] = input("Enter new Name:\n\n")
        patients[id][2] = input("Enter new Disease:\n\n")
        patients[id][3] = input("Enter new Gender:\n\n")
        patients[id][4] = input("Enter new Age:\n\n")
        print("\nBack to the previous menu\n")

    def displayPatientsList():
        print("\n{:<8} {:<15} {:<15} {:<10} {:<20}\n".format('ID', 'Name', 'Disease', 'Gender', 'Age'))
        for i in patients:
            if i != '0':
                print("{:<8} {:<15} {:<15} {:<10} {:<20}".format(i, patients[i][1], patients[i][2], patients[i][3], patients[i][4]))
        print("\nBack to the previous menu\n")

    def writeListOfPatientsToFile(data):
        file = open("files\patients.txt", "w")
        for i in data:
            file.write(i)
        file.close()

    def addPatientToFile():
        data = ''
        file = open("files\patients.txt", "a")
        data += '\n' + input("Enter the patient's ID:\n\n") + '_'
        data += input("Enter the patient's Name:\n\n") + '_'
        data += input("Enter the patient's Disease:\n\n") + '_'
        data += input("Enter the patient's Gender:n\n") + '_'
        data += input("Enter the patient's Age:\n\n") + '_'
        file.write(data)
        file.close()
        print("\nBack to the previous menu\n")
        
class Laboratory:
    name = ""
    cost = 0
    # list to maintain all laboratories
    laboratory_list = []
    
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost
        self.laboratory_list.append(self)
    
    def list_laboratories(self):
        f = open("laboratories.txt", "r")
        lines = f.readlines()
        for line in lines:
            name, cost = line.split('_')
            print("{:<20} {:<15}".format(name,cost))
        f.close()
        print("\nBack to the prevoius menu\n")
    
    def add_laboratory(self):  
        name = input("Enter the name of the laboratory: ")
        cost = int(input("Enter the cost of the laboratory: "))
        self.laboratory_list.append(Laboratory(name, cost))
        f = open("laboratories.txt", "a")
        if f.read() == "\n":
            f.write(name + "_" + str(cost))
            f.close()
        else:
            f.write("\n" + name + "_" + str(cost))
            f.close()
        print("\nBack to the prevoius menu\n")    
    
    def writeListOfLaboratories(self):
        f = open("laboratories.txt", "w")
        f.write("Laboratories List:")
        for lab in self.laboratory_list:
            if lab.name == self.name:
                self.laboratory_list.remove(lab)
            else:
                f.write("\n" + lab.formatLabInfo())
        f.close()
    
    def formatLabInfo(self):
        return self.name + "_" + str(self.cost)
        
    
    def enterLaboratoryInfo(self):
        name = input("Enter the name of the laboratory: ")
        cost = int(input("Enter the cost of the laboratory: "))
        Laboratory(name, cost)
        print("Laboratory oject created successfully")
    
    def readLaboratorieFile(self):
        f = open("laboratories.txt", "r")
        lines = f.readlines()
        for line in lines:
            name, cost = line.split('_')
            Laboratory(name, cost)
        f.close()
        print("\nBack to the prevoius menu\n")
    
    def lab_menu(self):
        while 1:
            print("Laboratory Menu")
            print("1 - Display laboratories list")
            print("2 - Add laboratory")
            print("3 - Go back to main menu")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                self.list_laboratories()
            elif choice == 2:
                self.add_laboratory()
            elif choice == 3:
                exit()
            else:
                print("Invalid choice")
                self.lab_menu()

class Management:
# DisplayMenu to display the menu shown in the Sample Run section.     
    def displayMenu():
        while True:
            mainEntry = input("""\nWelcome to Alberta Hospital (AH) Management system 
Select from the following options, or select 0 to stop: 
1 - 	Doctors
2 - 	Facilities
3 - 	Laboratories
4 - 	Patients\n\n""")
# This Entry[1] will run through the Doctor's Menu.
            if mainEntry == '1':
                doctor = Doctor()
                while True:
                    Doctor.readDoctorsFile()
                    doctorEntry = input("""\nDoctors Menu:
1 - Display Doctors list
2 - Search for doctor by ID
3 - Search for doctor by name
4 - Add doctor
5 - Edit doctor info
6 - Back to the Main Menu\n\n""")
                    if doctorEntry == '1':
                        Doctor.displayDoctorsList(doctor)
                    elif doctorEntry == '2':
                        Doctor.searchDoctorById(doctor)
                    elif doctorEntry == '3':
                        Doctor.searchDoctorByName(doctor)
                    elif doctorEntry == '4':
                        Doctor.addDrToFile(doctor)
                        Doctor.writeListOfDoctorsToFile(Doctor.formatDrInfo(doctor))
                    elif doctorEntry == '5':
                        Doctor.editDoctorInfo(doctor)
                        Doctor.writeListOfDoctorsToFile(Doctor.formatDrInfo(doctor))
                    elif doctorEntry == '6':
                        break
# This Entry[2] will run through the Facilities Menu.
            elif mainEntry == '2':
                while True:
                    facilityEntry = input("""\nFacilities Menu:
1 - Display Facilities list
2 - Add Facility
3 - Back to the Main Menu\n\n""")
                    if facilityEntry == '1':
                        Facility.displayFacilities()
                    elif facilityEntry == '2':
                        Facility.addFacility()
                        Facility.writeListOffacilitiestoFile()
                    elif facilityEntry == '3':
                        break
# This Entry[3] will run through the Laboratory Menu.  

            elif mainEntry == '3':
                while True:
                    laboratoryEntry = input("""Laboratories Menu:
1 - Display laboratories list
2 - Add laboratory
3 - Back to the Main Menu\n\n""")
                    if laboratoryEntry == '1':
                        pass
                    elif laboratoryEntry == '2':
                        pass
# This Entry[4] will run through the Patient Menu.

            elif mainEntry == '4':
                while True:
                    Patient.readPatientFile()
                    patientsEntry = input("""Patients Menu:
    1 - Display patients list
    2 - Search for patient by ID
    3 - Add patient
    4 - Edit patient info
    5 - Back to the Main Menu\n\n""")
                    if patientsEntry == '1':
                        Patient.displayPatientsList()
                        print("\nBack to the previous menu\n")
                    elif patientsEntry == '2':
                        entry = input("\n Enter the Patient ID:\n\n")
                        Patient.searchPatientById(entry)
                        Patient.displayPatientInfo(entry)
                        print("\nBack to the previous menu\n")
                    elif patientsEntry == '3':
                        Patient.addPatientToFile()
                        Patient.writeListOfPatientsToFile(Patient.formatPatientInfo())
                        print("\nBack to the previous menu\n")
                    elif patientsEntry == '4':
                        Patient.editPatientInfo()
                        Patient.writeListOfPatientsToFile()
                        print("\nBack to the previous menu\n")
                    elif patientsEntry == '5':
                        print("\nBack to the previous menu\n")
                        break

            elif mainEntry == '0':
                break


    while True:
        if displayMenu() == True:
            continue
        else:
            break  
