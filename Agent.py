import uuid
from Customer import *


# Represents the insurance agent
class Agent:
    def __init__(self, name, address):
        self.ID = str(uuid.uuid1())
        self.name = name
        self.address = address
        self.customers = []


    # convert object o JSON
    def serialize(self):
        return {
            'id': self.ID,
            'name': self.name,
            'address': self.address
        }

    def getCustomers(self):
        return list(self.customers)

    def addCustomer(self, name, address):
        c = Customer(name, address)
        self.customers.append(c)
        return c.ID

    def getCustomerById(self, id_):
        for d in self.customers:
            if (d.ID == id_):
                return d
        return None

    def deleteCustomer(self, agent_id):
        c = self.getAgentById(agent_id)
        self.agents.remove(c)

