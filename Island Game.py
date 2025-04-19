print("""
👾👾👾👾👾👾👾👾👾👾👾👾👾
👾👾👾👾👾👾👾👾👾👾👾👾👾
👾👾👾👾👾👾👾👾👾👾👾👾👾
ANASS EL OUALJI (DevAnass), the creator of this game😎🖥️

welcome to my island!""")
# there are 3 doors in front of you.one 🚪 is bule, one🚪 is red.
usr=input("what is your name?\n")
print("Welcome to the island game Mr(s): "+ usr)
age = int(input("How ald are you Mr(s): " + usr + "?\n"))
if age>=10:
  print("you can play the game🎮🎮")
  print("there are 3 doors in front of you.one 🚪 is bule, one🚪 is red.")
  door = input("which door do you wnat to open? (blue/red)\n").lower()
  if door =="red":
    print("""Great! now you entered a room.
    you found three boxes:🎁white,🎁black,🎁green.
    """)
    boxes = input("which box do you opne?(white/black/green\n").lower()
    if boxes=="white":
      print("Oops! You opened a box filled with snakes🐍🐍🐍")
    elif boxes=="blsck":
      print("Oop! You opened a box filled with spiders🕷️🕷️🕷️🕷️")
    elif boxes== "green":
      print("Congratulations! You found the treasure💰💰💰💰")
    else:
      print(f"Check the entry {boxes}.")
      print("Game over!try again🔄")
  elif door=="blue":
     print("""Oops! You chose the crocodile door🐊🐊🐊🐊
        Game over! try again🔄""")
  else:
      print(f"check the entry {door}.")
else:
  print("Unfortunately, this game is only for people aged 10 and above. The game is over.")
  