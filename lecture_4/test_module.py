a = (int(input('input number #{}: '.format(x+1))) for x in range(4))
try:
   print(max(x for x in a if not x % 2))
except ValueError:
   print('not found')