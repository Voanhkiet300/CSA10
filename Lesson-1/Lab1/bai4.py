from datetime import datetime

start_date = datetime(2021, 1, 1)
end_date = datetime(2022, 1, 1)

class DateHandler:
    def __init__(self, start_date, end_date) -> None:
        self.start_date = datetime(2021, 1, 1)
        self.end_date = datetime(2022, 1, 1)
    
    @classmethod
    def format_date(cls, date):
        return date.strftime("%Y-%m-%d")
    
    @classmethod
    def get_days_between(cls, start_date, end_date):
        return (end_date - start_date).days
    

start_date = datetime(2021, 1, 1)
end_date = datetime(2022, 1, 1)


print("Start:", DateHandler.format_date(start_date))
print("End:", DateHandler.format_date(end_date))
print("Days between:", DateHandler.get_days_between(start_date, end_date))