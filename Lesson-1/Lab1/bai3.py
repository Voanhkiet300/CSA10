from datetime import datetime

class CustomDate:
    def __init__(self) -> None:
        self.time = datetime.now()
        
    def get_date(self):
        return self.time.strftime("%d/%m/%Y")

    def get_time(self):
        return self.time.strftime("%H:%M:%S")


customed_date = CustomDate()
print(customed_date.get_date())
print(customed_date.get_time())
