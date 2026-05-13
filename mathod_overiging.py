class phone:
   def __init__(self):
      print("This is a constructor of the phone class.")
class samsung (phone):
   def __init__(self):
      super().__init__()
      print("This is a constructor of the samsung class.")

e3 = samsung()
