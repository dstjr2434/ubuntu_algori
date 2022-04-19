input=78

arr=list(filter((lambda x : input % x == 0),range(1,input+1)))

print(arr)

# filter( (원하는 함수),열거가능한 범위(ex:range, list , tuple)

# 열거가능한 범위 처음부터 함수를 돌린후에 조건을 만족하는(true) 값을 arr에 넣어준다.
catkin_create_pkg yh_tutorial_8 roscpp std_msgs message_generation rospy
catkin_create_pkg yh_tutorial_9 roscpp std_msgs message_generation rospy
catkin_create_pkg yh_tutorial_10 roscpp std_msgs message_generation rospy
