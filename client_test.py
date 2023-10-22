import unittest
from client3 import getDataPoint
from client3 import getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    self.assertEquals(getDataPoint(quotes[0]),('ABC',120.48,121.2,120.84))
    self.assertEquals(getDataPoint(quotes[1]),('DEF',117.87,121.68,119.775))

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 107.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    self.assertEquals(getDataPoint(quotes[0]),('ABC',120.48,119.2,119.84))
    self.assertEquals(getDataPoint(quotes[1]),('DEF',107.87,121.68,114.775))


  """ ------------ Add more unit tests ------------ """
  def test_getDataPoint_calculatePriceAskGreaterThanBid(self):
    quotes = [
      {'top_ask': {'price': 120.48, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 119.2, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 117.87, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 121.68, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    self.assertEquals(getDataPoint(quotes[0]),('ABC',119.2,120.48,119.84))
    self.assertEquals(getDataPoint(quotes[1]),('DEF',121.68,117.87,119.775))

  def test_getRatio_calculatePriceAGreaterThanB(self):
    prices = [
      {'a':114.78 , 'b':130.56},
      {'a':90.78 , 'b':230.56},
    ]
    """ ------------ Add the assertion below ------------ """
    self.assertEquals(getRatio(prices[0]['a'],prices[0]['b']),0.87913602941176470588235294117647)
    self.assertEquals(getRatio(prices[1]['a'],prices[1]['b']),0.39373698820263705759888965995836)

  def test_getRatio_priceAIsZero(self):
    prices = [
      {'a':0, 'b':130.56},
      {'a':0 , 'b':230.56},
    ]
    """ ------------ Add the assertion below ------------ """
    self.assertEquals(getRatio(prices[0]['a'],prices[0]['b']),0)
    self.assertEquals(getRatio(prices[1]['a'],prices[1]['b']),0)

  def test_getRatio_priceBIsZero(self):
    prices = [
      {'a':130.56, 'b':0},
      {'a':230.56 , 'b':0},
    ]
    """ ------------ Add the assertion below ------------ """
    self.assertEquals(getRatio(prices[0]['a'],prices[0]['b']),0)
    self.assertEquals(getRatio(prices[1]['a'],prices[1]['b']),0)

if __name__ == '__main__':
    unittest.main()
