current_speed = int(input("please enter current speed"))
average_speed = int(input("please enter average speed"))
calc = current_speed - average_speed
demerit = calc//5
print( "points" , demerit)
if demerit > 12:
    print("time to go to jail")
if (0<= demerit<=12):
    print("ok")



