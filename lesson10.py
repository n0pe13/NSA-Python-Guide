
from datetime import date, timedelta




### Exercise Set 1 ###
 

class Query:
    def __init__(self, classification=None, justification=None, selector=[]):
        self.classification = classification
        self.justification = justification
        self.selector = selector

    def talk(self):
        return f"Classification: {self.classification}, Justification: {self.justification}, Selector: {self.selector}"    

class RangedQuery(Query):
    def __init__(self, classification, justification, selector, begin_date=None, end_date=None):
        self.date_tuples = [("2016-12-01", "2016-12-06"), ("2015-12-01", "2015-12-06"), ("2016-2-01", "2016-2-06"), ("01/03/2014", "02/03/2014"), ("2016-06-01", "2016-10-06")]
        super().__init__(classification, justification, selector)
        #try:
            #datetime.strptime(begin_date, "%Y-%m-%d")
            #datetime.strptime(end_date, "%Y-%m-%d")
            #self.begin_date = begin_date
            #self.end_date = end_date
        #except ValueError:
            #print("Invalid date")


    def range_query(self):
        i = 0
        for i, (start, end) in enumerate(self.date_tuples):
            try:
                datetime.strptime(start, "%Y-%m-%d")
                datetime.strptime(end, "%Y-%m-%d")
                self.begin_date = start
                self.end_date = end
                talk_str = super().talk()
                print(talk_str + f", Begin Date: {self.begin_date}, End Date: {self.end_date}")
                i += 1
            except ValueError:
                print("Invalid format")

        return self.date_tuples   


    def sort_dates(self):
        self.date_tuples.sort(key=lambda x: x[0])
        return self.date_tuples

    #def talk(self):
        #talk_str = super().talk()
        #return talk_str + f", Begin Date: {self.begin_date}, End Date: {self.end_date}"


### Exercise Set 2 ###

class Reverselter:
    def __init__(self, lst=[]):
        self.reverse_iter = lst

    def backwards_iter(self):
        return self.reverse_iter[::-1]
          

### Exercise Set 3 ###

def dates_generator():
    start = date(2020, 1, 1)
    end = date(2020, 12, 31)
    day_increment = timedelta(days=1)

    while start < end:
        yield start.strftime("%A, %B %d")
        start += day_increment


### Exercise Set 4 ###

def dates_generator2(year: int, weekday: int):
    start = date(year, 1, weekday)
    end = date(year, 12, 31)
    day_increment = timedelta(days=1)

    while start < end:
        yield start.strftime("%A, %B %d")
        start += day_increment


if __name__=="__main__":
    #q = Query("Primary email address of Zendian diplomat", "ileona@stato.gov.zd")
    #print(q.talk())
    #q2 = RangedQuery("TS//SI//REL TO USA, FVEY","Primary IP address of Zendian diplomat", "10.254.18.162")
    #q2.sort_dates()
    #q2.range_query()

    #r = Reverselter([1, 2, 3])
    #print(r.backwards_iter())

    #d = dates_generator()
    #print(next(d))
    #print(next(d))
  
    d2 = dates_generator2(2021, 1)
    print(next(d2))
    print(next(d2))
    
    