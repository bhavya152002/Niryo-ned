from pyniryo import *

# -- Setting variables
sensor_pin_id = PinID.GPIO_1A

catch_nb = 5
cab=0.1
# The pick pose
pick_pose = PoseObject(
    x=0.27, y=-.05, z=0.125,
    roll=-0., pitch=1.57, yaw=0.0,
)
# The Place pose
place_pose = PoseObject(
                     x=0., y=-0.25, z=0.1,
                      roll=0., pitch=1.57, yaw=-1.57)

# -- MAIN PROGRAM

# Connecting to the robot
robot = NiryoRobot("169.254.200.200")

# Activating connexion with the Conveyor Belt
conveyor_id = robot.set_conveyor()

robot.run_conveyor(conveyor_id)
while robot.digital_read(sensor_pin_id) == PinState.LOW:
    robot.wait(0.1)

    # Stopping robot's motor
robot.stop_conveyor(conveyor_id)
    # Making a pick & place
robot.pick_and_place(pick_pose, place_pose)

# Deactivating connexion with the Conveyor Belt
robot.unset_conveyor(conveyor_id)

#second
pick_pose = PoseObject(
    x=0.27, y=-.05, z=0.125,
    roll=-0., pitch=1.57, yaw=0.0,
)
# The Place pose

place_pose = PoseObject(
                      x=-0, y=-0.2501, z=0.11,
                      roll=0., pitch=1.57, yaw=-1.57)

# -- MAIN PROGRAM


# Activating connexion with the Conveyor Belt
conveyor_id = robot.set_conveyor()

robot.run_conveyor(conveyor_id)
while robot.digital_read(sensor_pin_id) == PinState.LOW:
    robot.wait(0.1)

    # Stopping robot's motor
robot.stop_conveyor(conveyor_id)
    # Making a pick & place
robot.pick_and_place(pick_pose, place_pose)

# Deactivating connexion with the Conveyor Belt
robot.unset_conveyor(conveyor_id)

pick_pose = PoseObject(
    x=0.27, y=-.05, z=0.125,
    roll=-0., pitch=1.57, yaw=0.0,
)
# The Place pose

place_pose = PoseObject(
                      x=0, y=-0.2502, z=0.12,
                      roll=0., pitch=1.57, yaw=-1.57)

# -- MAIN PROGRAM


# Activating connexion with the Conveyor Belt
conveyor_id = robot.set_conveyor()

robot.run_conveyor(conveyor_id)
while robot.digital_read(sensor_pin_id) == PinState.LOW:
    robot.wait(0.1)

    # Stopping robot's motor
robot.stop_conveyor(conveyor_id)
    # Making a pick & place
robot.pick_and_place(pick_pose, place_pose)

# Deactivating connexion with the Conveyor Belt
robot.unset_conveyor(conveyor_id)