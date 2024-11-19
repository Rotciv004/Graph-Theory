from REPOSITORY import Repository
from FUNCTIONS import Functions
from MENU import Menu

def start():

    file = str(input("Input a file -> "))

    repository = Repository(file)
    functions = Functions(repository)
    menu = Menu(repository,functions)

    menu.ShowMenu()

if __name__ == "__main__":
    start()