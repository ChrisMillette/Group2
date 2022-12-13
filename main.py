class Doctor:
    id = 0
    name = ""
    speciality = ""
    timing = ""
    qualification = ""
    roomNumber = 0
    
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
        
# Import files from, Doctor, Facility and Patient
from Doctor import Doctor
from Facility import Facility
from Patient import Patient

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
            if mainEntry == '1':
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
                        Doctor.displayDoctorsList()
                    elif doctorEntry == '2':
                        Doctor.searchDoctorById(input("\n Enter the doctor ID:\n\n"))
                    elif doctorEntry == '3':
                        Doctor.searchDoctorByName(input("\n Enter the doctor name:\n\n"))
                    elif doctorEntry == '4':
                        Doctor.addDrToFile()
                        Doctor.writeListOfDoctorsToFile(Doctor.formatDrInfo())
                    elif doctorEntry == '5':
                        Doctor.editDoctorInfo()
                        Doctor.writeListOfDoctorsToFile(Doctor.formatDrInfo())
                    elif doctorEntry == '6':
                        break
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
                    elif facilityEntry == '3':
                        break
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
                    elif patientsEntry == '4':
                        Patient.editPatientInfo()
                        Patient.writeListOfPatientsToFile()
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
