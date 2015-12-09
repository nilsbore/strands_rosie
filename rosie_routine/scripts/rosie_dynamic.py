#!/usr/bin/env python

import rospy

from datetime import time, timedelta, datetime
from dateutil.tz import tzutc, tzlocal

from routine_behaviours.marathon_routine import MarathonRoutine


if __name__ == '__main__':
    rospy.init_node("rosie_routine")

    # start and end times -- all times should be in a particular timezone - local has stopped working!
    localtz = tzutc()

    now = datetime.now(localtz).time().replace(tzinfo=localtz)

    start = time(9,00, tzinfo=localtz)
    end = time(19,00, tzinfo=localtz)

    # how long to stand idle before doing something
    idle_duration=rospy.Duration(2)

    # how long do you want it to take to do a tour. this must be greater than the time you think it will take!
    # the number argument is in seconds
    tour_duration_estimate = rospy.Duration(60 * 40 * 2)

    routine = MarathonRoutine(daily_start=start, daily_end=end,
    idle_duration=idle_duration, tour_duration_estimate=tour_duration_estimate)

    routine.random_nodes = ['WayPoint3', 'WayPoint15', 'WayPoint22', 'WayPoint31','WayPoint10', 'WayPoint11','WayPoint12','WayPoint32']

    two_hours = timedelta(hours = 3)

    # do 3d scans
    scan_waypoints = ['WayPoint3', 'WayPoint4', 'WayPoint5', 'WayPoint6', 'WayPoint7', 'WayPoint8', 'WayPoint9', 'WayPoint10', 'WayPoint12', 'WayPoint13']
    routine.create_3d_scan_routine(waypoints=scan_waypoints, repeat_delta=two_hours)

    routine.start_routine()

    rospy.spin()
