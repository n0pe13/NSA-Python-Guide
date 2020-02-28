### Exercise Set 1-2 ###
from datetime import datetime


class Query:
    def __init__(self, classification=None, justification=None, selector=[]):
        self.classification = classification
        self.justification = justification
        self.selector = selector

    def talk(self):
        return f"Classification: {self.classification}, Justification: {self.justification}, Selector: {self.selector}"    

class RangedQuery(Query):
    def __init__(self, classification, justification, selector, begin_date=None, end_date=None):
        super().__init__(classification, justification, selector)
        #try:
            #datetime.strptime(begin_date, "%Y-%m-%d")
            #datetime.strptime(end_date, "%Y-%m-%d")
            #self.begin_date = begin_date
            #self.end_date = end_date
        #except ValueError:
            #print("Invalid date")

    def range_query(self):
        date_tuples = [("2016-12-01", "2016-12-06"), ("2015-12-01", "2015-12-06"), ("2016-2-01", "2016-2-06"), ("01/03/2014", "02/03/2014"), ("2016-06-01", "2016-10-06")]
        i = 0
        for i, (start, end) in enumerate(date_tuples):
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
              
                

    #def talk(self):
        #talk_str = super().talk()
        #return talk_str + f", Begin Date: {self.begin_date}, End Date: {self.end_date}"



if __name__=="__main__":
    #q = Query("Primary email address of Zendian diplomat", "ileona@stato.gov.zd")

    #print(q.talk())

    q2 = RangedQuery("TS//SI//REL TO USA, FVEY","Primary IP address of Zendian diplomat", "10.254.18.162", "2016-12-01", "2017-01-01")
    
    q2.range_query()
    