

### Exercise Set 1-3 ###

class Query:
    def __init__(self, classification=None, justification=None, selector=[]):
        self.classification = classification
        self.justification = justification
        self.selector = selector

    def talk(self):
        return f"Classification: {self.classification} Justification: {self.justification} Selector: {self.selector}"    

class RangedQuery(Query):
    def __init__(self, classification, justification, selector, begin_date=None, end_date=None):
        super().__init__(classification, justification, selector)
        self.begin_date = begin_date
        self.end_date = end_date
    
    def talk(self):
        talk_str = super().talk()
        return talk_str + f" Begin Date: {self.begin_date} End Date: {self.end_date}"

if __name__=="__main__":
    #q = Query("Primary email address of Zendian diplomat", "ileona@stato.gov.zd")

    #print(q.talk())

    q2 = RangedQuery("TS//SI//REL TO USA, FVEY", "Primary IP address of Zendian diplomat", "10.254.18.162", "2016-12-01", "2017-01-01")
    print(q2.talk())