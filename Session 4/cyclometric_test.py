def get_speed(extinct, flightless, name):
    if extinct:
      return -1
    else:
      if flightless:
        if name == 'Ostrich':
          return 15
        elif name == 'Chicken':
          return 7
        elif name == 'Flamingo':
          return 8
        else:
          return -1
      else:
        if name == 'Gold Finch':
          return 12
        elif name == 'Bluejay':
          return 10
        elif name == 'Robin':
          return 14
        elif name == 'Hummingbird':
          return 16
        else:
          return -1
res = get_speed(flightless=True, extinct=False, name='Ostrich1')
print(res)
