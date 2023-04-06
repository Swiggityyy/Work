from . import Automation
from Scripts import WorkWeek, Mileage

def main():
    print('HelloWorld!')

if __name__ == "__main__":
    main()

def clean():
    WorkWeek()
    Mileage()

def Selen():
    Automation()