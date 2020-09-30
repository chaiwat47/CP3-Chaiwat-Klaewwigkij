# version 2
class Player1():
    def __init__(self, firstname, lastname, number):
        self.firstname = firstname
        self.lastname = lastname
        self.number = number

if __name__ == '__main__':
    p1 = Player1()
    p1.firstname = "Loris"
    p1.lastname = "Karius"
    p1.number = 1
    
    p2 = Player1()
    p2.firstname = "Alex"
    p2.lastname = "Manniger"
    p2.number = 13
