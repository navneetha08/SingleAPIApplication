from werkzeug.exceptions import BadRequest

# Initialzing base class
class Requests:

    def getEntityObject(self):
        pass

    def __init__(self, json):
        pass
    
class OrderItems(Requests):
    # Initialzing constant variables
    MAXNAMELENGTH = 100000
    MAXPRICE = 100000000
    MAXQUANTITY = 1000
    MAXDISTANCE = 500000
    
    # Delivery slabs input is taken as the upper bound distance(in km) of an interval and its corrosponding cost
    # Assumption that it is stored as increasing order of intervals and is continous
    # This can be made configurable by creating an api to store this information
    # Hardcoded only for assesment purpose
    delivery_slabs = [[10,50],[20,100],[50,500],[500000,1000]]
    
    # Creating basic functions to get key values
    def isOffer(self):
        return self._offerpresent
    
    def getOrderItems(self):
        return self._order_items
    
    def getDistance(self):
        if self._distance < 0 or self._distance > self.MAXDISTANCE:
            raise BadRequest('Distance is invalid')
        return self._distance/1000 #converting to km
    
    def getOffer(self):
        return self._offer
    
    # Validation of values of its corrosponding keys
    def validatename(self,name):
        if len(name) > self.MAXNAMELENGTH:
            raise BadRequest('Name of an item is too long')
        
    def validatequantity(self,quantity):
        if quantity > self.MAXQUANTITY:
            raise BadRequest('Quantity exceeded the max limit')
        
    def validateprice(self,price):
        if price > self.MAXPRICE:
            raise BadRequest('Price of an item exceeded the max limit')
        
    # This function calculates the delivery cost depending on its corrosponding slab
    def getdeliverycost(self):
        distance = self.getDistance()
        for slab in self.delivery_slabs:
            if distance <= slab[0]:
                return slab[1]*100
            
    # Returns the total cost of items by calculating the total sum of items using the formula cost=quantity*price    
    def getitemtotal(self):
        total_price = 0
        for order in self._order_items:
            name = order["name"]
            self.validatename(name)
            quantity = order["quantity"]
            self.validatequantity(quantity)
            price = order["price"]
            self.validateprice(price)
            
            total_price += quantity*price
        return total_price
    
    # Returns the discount applicable on the order request
    def getdiscount(self,delivery_cost):
        type = self._offer["offer_type"]
        if type == "FLAT":
            val = self._offer["offer_val"]
            return val
        elif type == "DELIVERY":
            return delivery_cost
        else:
            raise BadRequest('Order Type is Invalid')
        
    # Calculating the final cost using the formula finalcost = costbeforediscount + deliverycost - discount
    def getfinalprice(self,costbeforediscount,deliverycost,discount):
        return costbeforediscount + deliverycost - discount
    
    #initialising the objects
    def __init__(self, json):
        self._offerpresent = False 
        if 'order_items' not in json:
            raise BadRequest('Order Items not passed in the request')
        if 'distance' not in json:
            raise BadRequest('Distance not passed in the request')
        if 'offer' in json:
            self._offer = json['offer'] #check if offer is appicable
            self._offerpresent = True
        self._order_items = json['order_items']
        self._distance = json['distance']