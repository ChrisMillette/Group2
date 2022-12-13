
class Patient(object):

    global patients
    patients = {}
#Constructor
    def __init__(self):
        self.Patient = Patient()
#Formats current patient list to that of the patient file
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
#Asks the user to enter new patient info and adds it to the patient list    
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
#Reads the patient file and populates the patient dictionary
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
#Searches for patient by ID
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
#Displays specific patient info in terminal
    def displayPatientInfo(id):
        print("\n{:<8} {:<15} {:<15} {:<10} {:<20}\n".format('ID', 'Name', 'Disease', 'Gender', 'Age'))
        print("{:<8} {:<15} {:<15} {:<10} {:<20}".format(id, patients[id][1], patients[id][2], patients[id][3], patients[id][4]))
        print("\nBack to the previous menu\n")
#Edits current patient info after user prompts
    def editPatientInfo():
        id = input("Please enter the ID of the patient that you want to edit their information:\n\n")
        patients[id][1] = input("Enter new Name:\n\n")
        patients[id][2] = input("Enter new Disease:\n\n")
        patients[id][3] = input("Enter new Gender:\n\n")
        patients[id][4] = input("Enter new Age:\n\n")
        print("\nBack to the previous menu\n")
#Displays table of all of the patients present in dictionary
    def displayPatientsList():
        print("\n{:<8} {:<15} {:<15} {:<10} {:<20}\n".format('ID', 'Name', 'Disease', 'Gender', 'Age'))
        for i in patients:
            if i != '0':
                print("{:<8} {:<15} {:<15} {:<10} {:<20}".format(i, patients[i][1], patients[i][2], patients[i][3], patients[i][4]))
        print("\nBack to the previous menu\n")
#Writes the formatted patient list to the patients file
    def writeListOfPatientsToFile(data):
        file = open("files\patients.txt", "w")
        for i in data:
            file.write(i)
        file.close()
#Add's a single patient to the file
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
