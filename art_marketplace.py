class Art:
  def __init__(self, artist, title, medium, year, owner):
    self.artist = artist
    self.title = title
    self.medium = medium
    self.year = year
    self.owner = owner
    
  def __repr__(self):
    return "{}. {}. {}. {}. {}, {}.".format(self.artist, self.title, self.year, self.medium, self.owner.name, self.owner.location)
  
class Marketplace:
  def __init__(self):
    self.listings = []
    
  def __repr__(self):
    return "The mARTetplace"
  
  def add_listing(self, new_listing):
    self.listings.append(new_listing)
    
  def remove_listing(self, tbr_listing):
    self.listings.remove(tbr_listing)
    
  def show_listing(self):
    for each in self.listings:
      print(each)
    
class Client:
  def __init__(self, name, location, is_museum):
    self.name = name
    self.is_museum = is_museum
    if not is_museum:
      self.location = "Private Collector"
    else:
      self.location = location
    
  def sell_artwork(self, artwork, price):
    if(self.name == artwork.owner.name):
      veneer.add_listing(Listing(artwork.title, price, self.name))
      
  def buy_artwork(self, artwork):
    if artwork.owner != self.name:
      print(artwork)
      for each in veneer.listings:
        if each.art == artwork.title:
          artwork.owner = self
          veneer.remove_listing(each)
                  
class Listing:
  def __init__(self, art, price, seller):
    self.art = art
    self.price = price
    self.seller = seller
    
  def __repr__(self):
    return "{}: {}".format(self.art, self.price)

veneer = Marketplace()
veneer.show_listing()

edytta = Client("Edytta Halpirt", "pc", False)
moma = Client("The MOMA", "New York", True)

girl_with_mandolin = Art("Picasso, Pablo", "Girl with a Mandolin", "oil on canvas", 1910, edytta)

edytta.sell_artwork(girl_with_mandolin, "$6M (USD)")

veneer.show_listing()
moma.buy_artwork(girl_with_mandolin)
print(girl_with_mandolin)