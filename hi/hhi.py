
def my_function(greeting, room, *names):
  for name in names:
    print(f"{greeting}, {name}! You are currently in the {room} room.")

my_function("Hello", "Living", "Emil", "Tobias", "Linus")