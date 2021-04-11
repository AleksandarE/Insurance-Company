from flask import Flask, request, jsonify
from InsurenceCompany import *
from Customer import *

app = Flask(__name__)

# Root object for the insurance company
company = InsuranceCompany("Be-Safe Insurance Company")


# Add a new customer (parameters: name, address).
@app.route("/customer", methods=["POST"])
def addCustomer():
    # parameters are passed in the body of the request
    cid = company.addCustomer(request.args.get('name'), request.args.get('address'))
    return jsonify(f"Added a new customer with ID {cid}")



# Return the details of a customer of the given customer_id.
@app.route("/customer/<customer_id>", methods=["GET"])
def customerInfo(customer_id):
    c = company.getCustomerById(customer_id)
    if (c != None):
        return jsonify(c.serialize())
    return jsonify(
        success=False,
        message="Customer not found")


# Add a new car (parameters: model, numberplate, motor power).
@app.route("/customer/<customer_id>/car", methods=["POST"])
def addCar(customer_id):
    c = company.getCustomerById(customer_id)
    if (c != None):
        car = Car(request.args.get(',model'), request.args.get('number_plate'), request.args.get('motor_power'), request.args.get("year"))
        c.addCar(car)
    return jsonify(
        success=c != None,
        message="Customer not found")

# deleting a customer with a given customer_id
@app.route("/customer/<customer_id>", methods=["DELETE"])
def deleteCustomer(customer_id):
    result = company.deleteCustomer(customer_id)
    if (result):
        message = f"Customer with id{customer_id} was deleted"
    else:
        message = "Customer not found"
    return jsonify(
        success=result,
        message=message)


# return list of all customers
@app.route("/customers", methods=["GET"])
def allCustomers():
    return jsonify(customers=[h.serialize() for h in company.getCustomers()])

##################################################################################

# Add a new agent with parameters: name, address
@app.route("/agent", methods=["POST"])
def addAgent():
    cid = company.addAgent(request.args.get('name'), request.args.get('address'))
    return jsonify(f"Added a new agent with ID {cid}")


# Return the details of an agent of the given agent_id.
@app.route("/agent/<agent_id>", methods=["GET"])
def agentInfo(agent_id):
    c = company.getAgentById(agent_id)
    if (c != None):
        return jsonify(c.serialize())
    return jsonify(
        success=False,
        message="Agent not found")


# assigning a new customer with a provided customer_id
@app.route("/agent/<agent_id>/<customer_id>", methods=["POST"])
def assignCustomer(agent_id):
    c = company.getAgentById(agent_id)
    if (c != None):
        list_customers = company.getCustomerById(request.args.get(',customer_id'))
        if (list_customers != None):
            c.customers.append(list_customers)
        else:
            return jsonify(
                success=list_customers != None,
                message="Customer not found")
    return jsonify(
        success=c != None,
        message="Agent not found")

# deleting agent
@app.route("/agent/<agent_id>", methods=["DELETE"])
def deleteAgent(agent_id):
    result = company.deleteAgent(agent_id)
    if (result):
        message = f"Agent with id{agent_id} was deleted"
    else:
        message = "Agent not found"
    return jsonify(
        success=result,
        message=message)

# returning a list of all agents
@app.route("/agents", methods=["GET"])
def allAgents():
    return jsonify(agents=[h.serialize() for h in company.getAgents()])


##################################################################################

# Add a new CLAIM (parameters: date,
# incident_description, claim_amount).
@app.route("/claims/<customer_id>/file", methods=["POST"])
def addClaim(customer_id):
    c = company.getCustomerById(customer_id)
    if (c != None):
        file = Claims(request.args.get(',date'), request.args.get('incident_description'), request.args.get('claim_amount'))
        c.addClaim(file)
    return jsonify(
        success=c != None,
        message="Customer not found")


# Return details about the claim
@app.route("/claims/<customer_id>", methods=["GET"])
def getClaim(claim_id):
    claim = company.getClaimById(claim_id)
    if (claim != None):
        return jsonify(claim.serialize())
    return jsonify(
        success=False,
        message="Claim not found")

# Change status
@app.route("/claims/<claim_id>/status", methods=["PUT"])
def changeStatus(claim_id):
    claim = company.getClaimById(claim_id)
    if (claim != None):
        claim.updateStatus(request.args.get('value'))
    return jsonify(
        success=claim != None,
        message="Claim not found")


# return a list of all claims
@app.route("/claims", methods=["GET"])
def allClaims():
    return jsonify(claims=[h.serialize() for h in company.getClaims()])

##################################################################################

# Adding a new payment in with parameters: date, customer_id,
# amount_received
@app.route("/payment/in", methods=["POST"])
def incomingPayment():
    c = company.getCustomerById(request.args.get('customer_id'))
    if (c != None):
        payment = Payment(request.args.get(',date'), request.args.get('amount_received'), request.args.get('customer_id'))
        c.addPayment(payment)
    return jsonify(
        success=c != None,
        message="Customer not found")


# Adding a new payment out with parameters :date, agent_id, amount_sent
@app.route("/payment/out", methods=["POST"])
def outgoingPayment():
    c = company.getAgentById(request.args.get('agent_id'))
    if (c != None):
        payment = Payment(request.args.get(',date'), request.args.get('amount_sent'), request.args.get('agent_id'))
        c.addPaymentOut(payment)
    return jsonify(
        success=c != None,
        message="Agent not found")

##################################################################################

# Return a list of all payments
@app.route("/payments", methods=["GET"])
def allPayments():
    return jsonify(payments=[h.serialize() for h in company.getPayments()])



# Return list of all claims
@app.route("/stats/claims", methods=["GET"])
def getClaimsByAgent():
    return jsonify(payments=[h.serialize() for h in company.getAllClaims()])

# Return list of all revenues
@app.route("/stats/revenues", methods=["GET"])
def getRevenuesByAgent():
    return jsonify(revenues=[h.serialize() for h in company.getAllRevenues()])

# Return sorted list with the agents
@app.route("/stats/agents", methods=["GET"])
def agentByPerformance():
    return jsonify(agents=[h.serialize() for h in company.getAllAgents()])

##################################################################################


###DO NOT CHANGE CODE BELOW THIS LINE ##############################
@app.route("/")
def index():
    return jsonify(
        success=True,
        message="Your server is running! Welcome to the Insurance Company API.")


@app.after_request
def add_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers[
        'Access-Control-Allow-Headers'] = "Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With"
    response.headers['Access-Control-Allow-Methods'] = "POST, GET, PUT, DELETE"
    return response


if __name__ == "__main__":
    app.run(debug=True, port=8888)