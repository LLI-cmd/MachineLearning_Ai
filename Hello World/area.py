class Human:
    def __init__(self, name, occupation):
        self.name = name
        self.occupation = occupation

    def do_work(self):
        if self.name == "louis":
            print("doing father's work")
        elif self.name == "faith":
            print("doing mother's work")

louis = Human("louis","nill")
louis.do_work()



