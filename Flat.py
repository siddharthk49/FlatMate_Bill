class Bill:
    """
    This class contains information about the Bill. The Bill comes with Amount and Time Period.
    """
    def __init__(self,amount,period):
        self.period = period
        self.amount = amount


class Flatmate:
    """
    This class is for the flatmate who lives in flat for a certain days of time and has to pay the amount based on Bill Amount

    """


    def __init__(self, name, no_of_days):
        self.name = name
        self.no_of_days= no_of_days

    def pays(self, Bill,flatmate2):
        weight =  float(self.no_of_days)/(float(self.no_of_days) + float(flatmate2.no_of_days))
        to_pay = weight * float(Bill.amount)
        return to_pay