from dealership.vehicles import Car, Truck, Motorcycle

class Contract(object):
    def __init__(self,vehicle, customer):
        self.vehicle = vehicle
        self.customer = customer      


class BuyContract(Contract):
    INTEREST_MULTIPLIERS = {
            Car : 1.07,
            Motorcycle : 1.03,
            Truck : 1.11
    }
    def __init__(self, vehicle, customer, monthly_payments):
        super(BuyContract, self).__init__(vehicle, customer)
        self.monthly_payments = monthly_payments

    def total_value(self):
        Discount = 1
        if self.customer.is_employee():
            Discount = 0.9
        return (self.vehicle.sale_price() + (self.INTEREST_MULTIPLIERS[self.vehicle.__class__] * self.monthly_payments * self.vehicle.sale_price() / 100)) * Discount
    
    def monthly_value(self):
        return self.total_value() / self.monthly_payments

class LeaseContract(Contract):
    
    LEASE_MULTIPLIERS = {
            Car : 1.2,
            Motorcycle : 1,
            Truck : 1.7,
    }
    
    def __init__(self, vehicle, customer, length_in_months):
        super(LeaseContract, self).__init__(vehicle, customer)
        self.length_in_months = length_in_months
    
    def total_value(self):
        Discount = 1
        if self.customer.is_employee():
            Discount = 0.9
        return (self.vehicle.sale_price() + (self.vehicle.sale_price() * self.LEASE_MULTIPLIERS[self.vehicle.__class__] / self.length_in_months)) * Discount

    def monthly_value(self):
        return self.total_value() / self.length_in_months