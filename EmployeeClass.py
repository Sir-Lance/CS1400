class Erecord:
    def __init__(self, eId, eName, eAddress, eRate, eHour):
        self.id = eId
        self.name = eName
        self.address = eAddress
        self.rate = eRate
        self.hour = eHour

    def __str__(self):
        return "ID: " + str(self.id) + " Name: " + self.name
    
    def calc_salary(self):
        if self.hour <= 40:
            grossPay = self.rate * self.hour
        else:
            grossPay = self.rate*40 + 1.5*self.rate*(self.hour-40)

        stateTax = grossPay * 0.075
        fedTax = grossPay * 0.2
        netPay = grossPay - stateTax - fedTax
        return netPay
