class DriveBot:
    all_disabled = False
    latitude = -999999
    longitude = -999999
    robot_count = 0

    def __init__(self, motor_speed = 0, sensor_range = 10, direction = 180):
        self.motor_speed = motor_speed
        self.sensor_range = sensor_range
        self.direction = direction
        DriveBot.robot_count += 1
        self.id = DriveBot.robot_count

    def control_bot(self, new_speed, new_dirction):
        self.motor_speed = new_speed
        self.direction = new_dirction

    def adjust_sensor(self, new_sensor_range):
        self.sensor_range = new_sensor_range


# Testing functions
robot_1 = DriveBot(5, 10, 90)
print(robot_1.motor_speed)
print(robot_1.direction)
print(robot_1.sensor_range)

robot_1.control_bot(10, 180)
robot_1.adjust_sensor(20)

print(robot_1.motor_speed)
print(robot_1.direction)
print(robot_1.sensor_range)

robot_2 = DriveBot(35,25, 75)
print(robot_2.motor_speed)
print(robot_2.direction)
print(robot_2.sensor_range)

DriveBot.latitude = -50.0
DriveBot.longitude = 50.0
DriveBot.all_disabled = True
robot_3 = DriveBot(20, 60, 10)

print(robot_1.latitude)
print(robot_2.longitude)
print(robot_3.all_disabled)
print(DriveBot.robot_count)
print(robot_1.id)
print(robot_2.id)
print(robot_3.id)