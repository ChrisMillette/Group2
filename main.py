class Doctor:
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
        self.doctor_list.append(self)
    
    def formatDrInfo(self):
        formatted_data =  str(self.id) + '_' + self.name + '_' + self.speciality + '_' + self.timing + '_' + self.qualification + '_' + str(self.roomNumber)
        return formatted_data

    def enterDrInfo(self):
        id = int(input("Enter the doctor's ID: "))
        name = input("Enter the doctor's name: ")
        speciality = input("Enter the doctor's speciality: ")
        timing = input("Enter the doctor's timings (e.g., 7am-10pm): ")
        qualification = input("Enter the doctor's qualifications: ")
        roomNumber = int(input("Enter the doctor's room number: "))
        return Doctor(id, name, speciality, timing, qualification, roomNumber)
        

    def readDoctorsFile(self):
        f = open("doctors.txt", "r")
        next(f)
        lines = f.readlines()
        for line in lines:
            id, name, speciality, timing, qualification, roomNumber = line.split('_')
            Doctor(int(id), name, speciality, timing, qualification, int(roomNumber))
        f.close()
        for doc in self.doctor_list:
            if doc.id == self.id:
                print(doc.id, self.id)
                print("Doctor with the same ID already exists\n")
                self.doctor_list.remove(doc)


    def search_doctor_id(self):
        found = False
        search = int(input("Enter the doctor's ID to search: "))
        f = open("doctors.txt", "r")
        header = (f.readline())
        id, name, speciality, timing, qualification, roomNumber = header.split('_')
        print("{:<4} {:<20} {:<15} {:<15} {:<15} {:<15}".format(id,name,speciality,timing,qualification,roomNumber))

        lines = f.readlines()
        for line in lines:
            did, name, speciality, timing, qualification, roomNumber = line.split('_')
            if did == str(search):
                print("{:<4} {:<20} {:<15} {:<15} {:<15} {:<15}".format(did,name,speciality,timing,qualification,roomNumber))
                f.close()
                found = True

        for doc in self.doctor_list:
            if doc.id == id:
                print("{:<4} {:<20} {:<15} {:<15} {:<15} {:<15}".format(doc.id,doc.name,doc.speciality,doc.timing,doc.qualification,doc.roomNumber))
                found = True
        if found == False:
            print("Cant find the doctor with the same ID on the system\n")
        else:
            print("Back to the prevoius menu\n")
        

    def search_doctor_name(self):
        found = False
        search = input("Enter the doctor's name to search: ")
        f = open("doctors.txt", "r")
        header = (f.readline())
        id, name, speciality, timing, qualification, roomNumber = header.split('_')
        print("{:<4} {:<20} {:<15} {:<15} {:<15} {:<15}".format(id,name,speciality,timing,qualification,roomNumber))
        
        lines = f.readlines()
        for line in lines:
            id, dname, speciality, timing, qualification, roomNumber = line.split('_')
            if dname == search:
                print("{:<4} {:<20} {:<15} {:<15} {:<15} {:<15}".format(id,dname,speciality,timing,qualification,roomNumber))
                f.close()
                found = True
        
        for doc in self.doctor_list:
            if doc.name == name:
                print("{:<4} {:<20} {:<15} {:<15} {:<15} {:<15}".format(doc.id,doc.name,doc.speciality,doc.timing,doc.qualification,doc.roomNumber))
                found = True
        if found == False:   
            print("Cant find the doctor with the same ID on the system\n")
        else:
            print("Back to the prevoius menu\n")


    def displayDoctorInfo(self):
        print(self.id)
        print(self.name)
        print(self.speciality)
        print(self.timing)
        print(self.qualification)
        print(self.roomNumber)
    
    def edit_doctor(self):
        flag = False
        self.readDoctorsFile()
        search = int(input("Please enter the id of the doctor that you want to edit their information:  "))
        for doc in self.doctor_list:
            if doc.id == search:
                flag = True
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
                self.writeListofDoctorsToFile()
                break
        if flag==False:
            print("Cant find the doctor with the same ID on the system\n")
        else:
            print("Back to the prevoius Menu\n")

    def list_doctors(self):
        f = open("doctors.txt", "r")
        lines = f.readlines()
        for line in lines:
            id, name, speciality, timing, qualification, roomNumber = line.split('_')
            print("{:<4} {:<20} {:<15} {:<15} {:<15} {:<15}".format(id,name,speciality,timing,qualification,roomNumber))
        f.close()
        print("Back to the prevoius menu\n")

    def writeListofDoctorsToFile(self):
        # remove duplicates from list
        f = open("doctors.txt", "w")
        f.write("id_name_speciality_timing_qualification_roomNumber")
        for doc in self.doctor_list:    
            f.write("\n"+doc.formatDrInfo())
        f.close()
    
    def addDrToFile(self):
        new = self.enterDrInfo()
        f = open("doctors.txt", "a")
        f.write("\n"+new.formatDrInfo())
        f.close()
        print("Back to the prevoius menu\n")

    def doctor_menu(self):
        while 1:
            print("\nDoctors Menu:")
            print("1 - Display Doctors list")
            print("2 - Search for doctor by ID")
            print("3 - Search for doctor by name")
            print("4 - Add doctor")
            print("5 - Edit doctor info")
            print("6 - Back to the Main Menu")
        
            choice = int(input("Enter your choice: "))
            if choice == 1:
                self.list_doctors()
            elif choice == 2:
                self.search_doctor_id()
            elif choice == 3:
                self.search_doctor_name()
            elif choice == 4:
                self.addDrToFile()
            elif choice == 5:
                self.edit_doctor()
            elif choice == 6:
                exit()
               
            else:
                print("Invalid choice")
                self.doctor_menu()
    
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
        print("\nBack to the previous menu\n")

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
        file = open("files\doctors.txt", "a")
        data += '\n' + input("Enter the patient's ID:\n\n") + '_'
        data += input("Enter the patient's Name:\n\n") + '_'
        data += input("Enter the patient's Disease:\n\n") + '_'
        data += input("Enter the patient's Gender:n\n") + '_'
        data += input("Enter the patient's Age:\n\n") + '_'
        file.write(data)
        file.close()
        print("\nBack to the previous menu\n")
