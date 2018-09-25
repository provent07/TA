velocity=0
time=0
dis=0
time1=int(input("Input time spent on road: "))
acc=int(input("Input acceleration: "))
dis1=int(input("Input distance: "))
while time<=time1:
    velocity1 = int(velocity + acc * time)
    dis=(time*velocity1+time*velocity)//2
    print("Duration: ",time,"Distance: ","*"*(dis//10))
    time=time+1

if velocity1>=60:
    print("The person went over the speed limit")
    print("Max speed: ", velocity1)
else:
    print("The person did not go over the speed limit")
    print("Max speed: ", velocity1)
if dis<dis1:
    print("The person did not reach destination")
    print("Reached: ",dis)
else:
    print("The person reach destination")
    print("Reached: ", dis)



