class User:
    def __init__(self, name, age, mail):
        self.name = name
        self.age = age
        self.mail = mail

    def serialize(self):
        return {
            "name": self.name,
            "age": self.age,
            "mail": self.mail
        }
