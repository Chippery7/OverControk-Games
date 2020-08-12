def example():
    example.has_been_called = True
    pass
example.has_been_called = False



#Actual Code!:
if example.has_been_called:
   print("foo bar")
else:
    print('As not been used...Yet')
