from random import randint

legend = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'


class SeaMap:
  def __init__(self, size):
    self.size = size
    self.secret = [[0 for i in range(size)] for i in range(size)]
    self.attacks = []
    self.ships = []

  def generateShipCombo(self):
    longest = self.size // 2
    shortest = self.size // 5
    if shortest < 2:
      shortest = 2
    total = self.size ** 2 * 3 // 10
    leftover = total
    while leftover > longest:
      s = randint(shortest, longest)
      leftover -= s
      self.ships.append(s)
    if leftover >= 2:
      self.ships.append(leftover)
    self.ships.sort(reverse = True)
  
  def placeShipsOnMap(self):
    o = ['H', 'V']
    for i in range(len(self.ships)):
      ship = self.ships[i]
      orientation = o[randint(0,1)]
      startPos = self.getStartPos(ship, orientation)
      self.updateSecret(ship, orientation, startPos, i)

  def getStartPos(self, ship, orientation):
    startPos = (0, 0)
    while True:
      startPos = self.helperPos(ship, orientation)
      canPlaceHere = self.checkPos(ship, orientation, startPos)
      if canPlaceHere:
        break
    return startPos

  def helperPos(self, ship, orientation):
    col = 0
    row = 0
    if orientation == 'H':
      col = randint(0, self.size - ship)
      row = randint(0, self.size - 1)
    elif orientation == 'V':
      row = randint(0, self.size - ship)
      col = randint(0, self.size - 1)
    else:
      return False
    return (row, col)
  
  def checkPos(self, ship, orientation, startPos):
    placed = 0
    (row, col) = startPos
    if orientation == 'H':
      for i in range(ship):
        if self.secret[row][col+i] == 0:
          placed += 1
    if orientation == 'V':
      for i in range(ship):
        if self.secret[row + i][col] == 0:
          placed += 1
    return placed == ship

  def printMap(self, secretPr = False):
    mapStr = '    '
    for i in range(self.size):
      mapStr += legend[i] + ' '
    mapStr += '\n' + '    '
    for i in range(self.size):
      mapStr += '- '

    for i in range(self.size):
      if i + 1 < 10:
        mapStr += '\n' + str(i+1) +' | '
      else:
        mapStr += '\n' + str(i+1)+'| '
      for j in range(self.size):
        if not secretPr:
          if [i, j] in self.attacks:
            if self.secret[i][j] != 0:
              mapStr += 'X '
            else: 
              mapStr += 'O '
          else:
            mapStr += '^ '
        else:
          if self.secret[i][j] != 0:
            mapStr += str(self.secret[i][j]) + ' '
          else:
            mapStr += '^ '
    print(mapStr)

  def updateSecret(self, ship, orientation, startPos, i):
    if orientation == 'H':
      for k in range(ship):
        self.secret[startPos[0]][startPos[1] + k] = i + 1
    else:
      for k in range(ship):
        self.secret[startPos[0] + k][startPos[1]] = i + 1
      

      
    





