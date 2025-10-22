text = "It's probably pining for the fjords!"

print(text[21:35].rfind('f'))     # 8 - finds the f in fjords but relative to the start at 21
print(text.rfind('f', 21, 35))    # 29 - finds the f in fjords