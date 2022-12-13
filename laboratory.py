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

if __name__ == "__main__":
    Lab = Laboratory("Main")
    lab.lab_menu()