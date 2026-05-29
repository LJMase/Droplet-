class Paint():
    def __init__(self, brand: str, color: str, sku="0"):
        self.brand = brand 
        self.color = color 
        self.sku = sku 

    # Dunder equals is used for finding equivalent paint objects when I compare them in main.
    def __eq__(self, other):
        return self.brand == other.brand and self.color == other.color and self.sku == other.sku

    # Dunder str is used to provide a custom print format for the paint objects. If the SKU is 0 it will not be included in the print. 
    def __str__(self):
        if self.sku == "0":
            return f"{self.brand} - {self.color}"
        return f"{self.brand} - {self.color} ({self.sku})"
    
    # Dunder less than compares objects alphabetically based on brand and then color. This is primarily to use sorted() on a list of paints.
    def __lt__(self, other):
        if self.brand == other.brand:
            return self.color < other.color
        return self.brand < other.brand
