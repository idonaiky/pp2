class MyNumbers:
  def __iter__(self):
    self.a = int(input())
    return self

  def __next__(self):
    if self.a >= 0:
      x = self.a
      self.a -= 1
      return x
    else:
      raise StopIteration


myiter = iter(MyNumbers())

for x in myiter:
  print(x)
