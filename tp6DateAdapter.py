class dateStandard():
    """"Date en format machine YYYY/MM/DD"""
    def __init__(self,year,month,day):
        self.year = year
        self.month = month
        self.day = day
        self.date = year+ "/"+ month+ "/"+ day

class dateStyle1():
    """Date en format MM/DD/YYYY"""
    def __init__(self,year,month,day):

        self.date = month+"/"+day+"/"+year

class dateStyle2():
    """Date en format DD/MM/YYYY"""
    def __init__(self,year,month,day):
        self.year = year
        self.month = month
        self.day = day

class adapter1(dateStyle1):
    def __init__(self,dateStandard):
        self.date = dateStandard.month+"/"+dateStandard.day+"/"+dateStandard.year

class adapter2(dateStyle2):
    def __init__(self,dateStandard):
        self.date = dateStandard.day+"/"+dateStandard.month+"/"+dateStandard.year

def main():
    Date = dateStandard('2020','2','26')
    ad = adapter2(Date)
    print(ad.date)
    return 0

if __name__ == '__main__':
    main()