from SeaMap import SeaMap, legend

class Game:
  def __init__(self):
    size = 0
    while True:
      print("Enter a number for dimension: (min = 5, max = 50)")
      try:
        size = int(input())
      except ValueError:
        print("enter an integer")
        continue
      if size >= 5 and size <= 50:
        break
      else:
        print('try again')

    self.sea = SeaMap(size)
    self.sea.generateShipCombo()
    self.sea.placeShipsOnMap()
    self.wrecks = []
    self.maxAttack = self.sea.size ** 2 // 3
    self.numAtt = 0

    
  
  def start(self):
    self.overview()
    print('ships arranged in secret, ready to attack')
    self.sea.printMap()
    while True:
      pos = self.getPos()
      while not self.canAttack(pos):
        print("cannot attack the same position again")
        pos = self.getPos()
      self.attack(pos)
      self.sea.printMap()
      if self.getNumShips() == 0:
        print('You won')
        self.summary()
        break
      elif self.numAtt >= self.maxAttack:
        print("out of move")
        self.summary()
        break
      else:
        self.info()
      

  def getPos(self):
    while True:
      print('enter a point to attack (i.e. A1)')
      posInput = input()
      try:
        col = legend.index(posInput[0])
        row = int(posInput[1:]) -1
      except ValueError:
        print("try again")
        continue
      if col == -1 or row >= self.sea.size or col >= self.sea.size or row < 0:
        print("attack out of range, try again")
        continue
      return [row, col]
    
  def getNumShips(self):
    return len(self.sea.ships) - len(self.wrecks)
  
  def getNumAttacks(self):
    return self.maxAttack - self.numAtt

  def canAttack(self, pos):
    return pos not in self.sea.attacks

  def attack(self, pos):
    self.sea.attacks.append(pos)
    self.numAtt += 1
    s = self.sea.secret[pos[0]][pos[1]]
    if s != 0:
      if s in self.wrecks:
        print("hit a wrecked ship...")
      else:
        self.wrecks.append(s)
        print('Hit a ship!')
    else:
      print('attack fails')
    
  def info(self):
    print('number of attacks left: {} \n number of ships left: {}'.format(self.getNumAttacks(), self.getNumShips()))
  
  def summary(self):
    summary = 'You attacked {} ships in {} moves'.format(len(self.wrecks), self.numAtt)
    print(summary)
    print("ships are placed as below")
    self.sea.printMap(True)

  def overview(self):
    print('There are {} ships \nYou have {} attacks in total'.format(len(self.sea.ships), self.maxAttack))
      
    
    
  


g = Game()
g.start()