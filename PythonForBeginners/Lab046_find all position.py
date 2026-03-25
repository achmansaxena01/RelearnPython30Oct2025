s = ("Take up one idea. Make that one idea your life - "
     "think of it, dream of it, live on that idea. Let the brain, "
     "muscles, nerves, every part of your body, be full of that idea, "
     "and just leave every other idea alone. This is the way to success.")
subs = "idea"
found = False
pos = -1
while True:
    pos = s.find(subs, pos + 1, len(s))
    if pos == -1:
        break
    print("Found the sub string at the position : ", pos)
    found = True
if found == False:
    print("Not found")
