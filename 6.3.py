# House lighting with three bulbs and two switches
light_switch1 = False  
light_switch2 = False  
bulbs_on = 0

if light_switch1:
    bulbs_on += 1
if light_switch2:
    bulbs_on += 2  

print(f"Number of bulbs lit: {bulbs_on}")
