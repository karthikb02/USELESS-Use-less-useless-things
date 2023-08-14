import datetime
class DataBase:
    def __init__(self, filename):
        self.filename = filename
        self.users = None
        self.file = None
        self.load()

    def load(self):
        self.file = open(self.filename, "r")
        self.users = {}

        for line in self.file:
            email, password, name, phone, address, bioDeg,nonBioDeg,metal,electronic,medical, totalWaste,points, created = line.strip().split(";")
            self.users[email] = (password, name, phone, address,bioDeg,nonBioDeg,metal,electronic,medical,totalWaste,points, created)

        self.file.close()

    def get_user(self, email):
        if email in self.users:
            return 1
        else:
            return -1

    def add_user(self, email, password, name, phone, address,bioDeg,nonBioDeg,metal,electronic,medical,totalWaste,points):
        if email.strip() not in self.users:
            self.users[email.strip()] = (password.strip(), name.strip(),str(phone).strip(),str(address).strip(), str(bioDeg),str(nonBioDeg),str(metal),str(electronic),str(medical),str(totalWaste),str(points),DataBase.get_date())
            self.save()
            return 1
        else:
            print("User exists already")
            return -1

    def validate(self, email, password):
        if self.get_user(email) != -1:
            return self.users[email][0] == password
        else:
            return False

    def save(self):
        with open(self.filename, "w") as f:
            for user in self.users:
                f.write(user + ";" + self.users[user][0] + ";" + self.users[user][1] + ";" + self.users[user][2]+";"+self.users[user][3] + ";" + self.users[user][4]+";"+ self.users[user][5]+";" +self.users[user][6]+";" +self.users[user][7]+";" +self.users[user][8]+";" +self.users[user][9]+";"+self.users[user][10]+";"+self.users[user][11]+"\n")

    @staticmethod
    def get_date():
        return str(datetime.datetime.now()).split(" ")[0]
