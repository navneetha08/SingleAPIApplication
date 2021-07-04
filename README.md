# SingleAPIApplication
Built an single API endpoint for a basic problem statement.
The API will take as input items ordered, delivery distance, and offer applied. The response is the total order value.
The input looks like the following below.

# API Input
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

# API Output
The API responds with total order cost.

 
  # Install all Dependencies and modules using command
    pip install -r requirements.txt
  # Run app.py
    python app.py
  # Test using postman
    The code runs on localhost. Go to postman, send a post request on the localhost url: https://127.0.0.1:5000/
    To check the result for order items, pass the required content in the body in the template above and send a POST request to the URL: https://127.0.0.1:5000/gettotalcost
 
