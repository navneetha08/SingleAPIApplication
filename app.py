from flask import Flask,request,Response
import json
import requests
from werkzeug.exceptions import BadRequest

app = Flask(__name__)

@app.before_request
def before_request():
    if request.method == 'PUT' or request.method == 'POST':
        if not request.is_json:
            raise BadRequest('Content-Type unrecognized')

# Hello World, Basic Route
@app.route("/", methods=["GET"])
def hello_word():
    return Response("Hello World")


# End point for the use case
@app.route("/gettotalcost",methods=["POST"])
def class_cost():
    total_data = request.get_json()
    
    user_request = requests.OrderItems(total_data) # Get the json Body
    item_cost = user_request.getitemtotal() # Calculate the item cost
    d_cost = user_request.getdeliverycost() # Calculate the delivery cost
    print(item_cost,d_cost)
    ifoffer = user_request.isOffer() # Check for offer
    discount = 0
    if ifoffer:
        discount = user_request.getdiscount(d_cost)
        discount = min(discount,item_cost) # Max discount available is the item cost
    print(discount)  
    finalprice = user_request.getfinalprice(item_cost,d_cost,discount) # Calculate the final price
    res = {}
    res["order_total"] = finalprice
    return Response(json.dumps(res),status=200, mimetype='application/json')





if __name__ == "__main__":
    app.debug = True
    app.run()
    
