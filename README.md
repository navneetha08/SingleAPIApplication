# SingleAPIApplication
Built an single API endpoint for a basic problem statement.
The API will take as input items ordered, delivery distance, and offer applied. The response is the total order value.
The input looks like the following below.

# API Input Example
{
  "order_items": [
    {
      "name": "bread",
      "quantity": 2,
      "price": 2200
    },
    {
      "name": "butter",
      "quantity": 1,
      "price": 5900
    }
  ],
  "distance": 1200,
  "offer": {
    "offer_type": "FLAT",
    "offer_val": 1000
  }
}

# API Output Example
The API responds with total order cost.

{'order_cost': 14300 }

 
  # Install all Dependencies and modules using command
    pip install -r requirements.txt
  # Run app.py
    python app.py
  # Test using postman
    The code runs on localhost. Go to postman, send a post request on the localhost url: https://127.0.0.1:5000/
    To check the result for order items, pass the required content in the body in the template above and send a POST request to the URL: https://127.0.0.1:5000/gettotalcost
 
 # Additional Information
requests.py file contains all the corrosponding functionalites. This file is seperated from app.py for maintainability. The slab range is hardcoded for now. It can be made configurable by making it dynamic by sending a request in the required format. Currently the data structure used to represent this is a list of list, where each sublist represents an interval [A,B]. "A" represents the upper bound for that slab. "B" represents the cost value for that slab.

The API returns a response on the following logic:

Final Price = Price Before Offer + Delivery Fee - Discount ( if applicable ) .
 
 # Error Handling
 It is assumed that the user request sent is valid. However, error handling is done for bounds of distance,quantity,price and name. BadRequest response is sent with an appropriate message in such cases.
