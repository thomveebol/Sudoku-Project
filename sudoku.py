class Cell:
  def __init__(self, value, row, col, screen):
    self.value = set_cell_value(value)

  def set_cell_value(self, value):
    self.value = value
    return self.value