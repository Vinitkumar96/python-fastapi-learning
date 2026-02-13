from datetime import date

class ExpenseModel:
    def __init__(self,title:str,amount:float,type:str,category:str,record_date:date):
        self.title = title
        self.amount = amount
        self.type = type
        self.category = category
        self.record_date =  record_date

    def to_dict(self):
        return{
            "title": self.title,
            "amount":self.amount,
            "type":self.type,
            "category":self.category,
            "date":str(self.record_date)
        }