# If it’s raining and the temperature is less than 15 degrees ---------->“It’s wet and cold”
# if it's not raining and temperature is less than 15 degrees ---------->“It’s not raining but cold”. 
# If it’s greater than or equal to 15 but not raining------------------->“It’s warm but not raining” 
# otherwise tell them--------------------------------------------------->“It’s warm and raining”.

# You have access to two variables: raining (boolean) and temperature (integer). If it’s raining and the temperature is less than 15 degrees, print to the screen “It’s wet and cold”, if it is less than 15 but not raining print “It’s not raining but cold”. If it’s greater than or equal to 15 but not raining print “It’s warm but not raining”, and otherwise tell them “It’s warm and raining”.

raining = False
temp = round(float(15),1)

if raining and temp < 15:
    print("It's wet and cold")
elif not raining and temp < 15:
    print("It's not raining but cold")
elif not raining and temp >= 15:
    print("It's warm but not raining")
else:
    print("It's warm and raining")