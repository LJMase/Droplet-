class Paint():
    def __init__(self, brand: str, color: str, sku="0"):
        self.brand = brand 
        self.color = color 
        self.sku = sku 

    def __eq__(self, other):
        return self.brand == other.brand and self.color == other.color and self.sku == other.sku

    def __str__(self):
        if self.sku == "0":
            return f"{self.brand} - {self.color}"
        return f"{self.brand} - {self.color} ({self.sku})"
    
    def __lt__(self, other):
        if self.brand == other.brand:
            return self.color < other.color
        return self.brand < other.brand
