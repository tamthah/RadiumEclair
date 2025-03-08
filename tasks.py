from robocorp.tasks import task
from line_follower import LineFollowerRobot

@task
def line_following_task():
    robot = LineFollowerRobot()
    robot.follow_line()
