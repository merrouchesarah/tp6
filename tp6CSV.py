import csv

class OpenFile():
    def __init__(self):
        pass
    def open(self):
        file = open('fichier.csv')
        reader = csv.reader(file)
        data = list(reader)
        for d in data:
            print(d)
        file.close()
def main():
    file = OpenFile()
    file.open()

if __name__ == '__main__':
    main()