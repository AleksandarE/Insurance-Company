from Customer import *
from Agent import *


class InsuranceCompany:
    def __init__(self, name):
        self.name = name  # Name of the Insurance company
        self.customers = []  # list of customers
        self.agents = []  # list of dealers
        self.claims = [] # list of claims
        self.incoming = []  # list of incoming payments
        self.outgoing = []  # list of outgoing payments

    def getCustomers(self):
        return self.customers

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

    # agent
    def getAgent(self):
        return list(self.agents)

    def getAgents(self):
        return self.agents

    def addAgent(self, name, address):
        c = Agent(name, address)
        self.agents.append(c)
        return c.ID

    def getAgentById(self, id_):
        for d in self.agents:
            if (d.ID == id_):
                return d
        return None

    def deleteAgent(self, agent_id):
        c = self.getAgentById(agent_id)
        agentCustomers = c.getCustomers()
        self.getAgentById(agent_id+1).addCustomer(agentCustomers)
        self.agent.remove(c)

    # claims
    def getClaims(self):
        return self.claims

    def addClaim(self, claim):
        self.claims.append(claim)

    def getClaimById(self, id):
        for d in self.claims:
            if (d.ID == id):
                return d
        return None

    # payments
    def addPayment(self, payments):
        self.incoming.append(payments)

    def addPaymentOut(self, payments):
        self.outgoing.append(payments)

    def getPayments(self):
        return self.incoming, self.outgoing


    def getAllClaims(self):
        claims_per_agent = []
        for agent in self.agents:
            claims_list = []
            for customer in agent:
                claims_list.append(customer.claims)
            claims_per_agent.append(claims_list)
        return claims_per_agent


    def getAllRevenues(self):
        return self.outgoing

    def getAllAgents(self):
        rating = []
        for agent in self.agents:
            rating.append(agent.customers)
        sorted(rating)
        return rating





