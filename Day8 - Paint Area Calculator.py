import math

def paint_calc(height, width, cover):
  can_qty = (height*width)/cover
  can_roundup = math.ceil(can_qty)
  print(f"You'll need {can_roundup} cans of paint.") 

test_h = int(input("Height of wall (m): "))
test_w = int(input("Width of wall (m): "))
coverage = 5

paint_calc(height=test_h, width=test_w, cover=coverage)
