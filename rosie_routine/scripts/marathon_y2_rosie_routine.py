#!/usr/bin/env python

import rospy

from datetime import time, timedelta
from dateutil.tz import tzutc, tzlocal

from routine_behaviours.marathon_routine import MarathonRoutine
    

if __name__ == '__main__':
    rospy.init_node("rosie_marathon_routine")

    # start and end times -- all times should be in a particular timezone - local has stopped working!
    # localtz = tzlocal()
    localtz = tzutc()
    start = time(8,00, tzinfo=localtz)
    end = time(00,00, tzinfo=localtz)

    thirty_mins = timedelta(minutes = 30)
    sixty_mins = timedelta(minutes = 60)
    ninety_mins = timedelta(minutes = 90)

  # how long to stand idle before doing something
    idle_duration=rospy.Duration(20)

    # how long do you want it to take to do a tour. this must be greater than the time you think it will take!
    # the number argument is in seconds
    tour_duration_estimate = rospy.Duration(60 * 40 * 2)

    routine = MarathonRoutine(daily_start=start, daily_end=end, 
    idle_duration=idle_duration, tour_duration_estimate=tour_duration_estimate)    

    # go around every node every tour_duration_estimate
    #routine.create_patrol_routine()

    # patrol just these selected waypoints every 30 minutes in the first part of the day
    routine.create_patrol_routine(waypoints=['WayPoint7', 'WayPoint21'], daily_start=start, daily_end=end, repeat_delta=thirty_mins)

    # do 3d scans
    scan_waypoints = ['WayPoint16', 'WayPoint19', 'WayPoint5']
    routine.create_3d_scan_routine(waypoints=scan_waypoints, repeat_delta=timedelta(hours=1))
 
    # do rgbd recording for a minute at these places every two hours
    rgbd_waypoints = ['WayPoint4', 'WayPoint1']
    routine.create_rgbd_record_routine(waypoints=rgbd_waypoints, duration=rospy.Duration(60), repeat_delta=timedelta(hours=1))

    #following_task = Task(start_node_id=self.waypoint,max_duration=rospy.Duration(300),action='simple_follow')
    #task_utils.add_int_argument(following_task, 270)
    #routine.repeat_every_hour(following_task, hours=1, times=1)



    # where to stop and what to tweet with the image
    # twitter_waypoints = [['WayPoint6', 'I hope everyone is working hard today #ERW14 #RobotMarathon'],
    #                    ['WayPoint2', 'Knowledge is power for @UoBLibServices #ERW14 #RobotMarathon']]    
    # routine.create_tweet_routine(twitter_waypoints, daily_start=time(23,00, tzinfo=localtz), daily_end=time(00,00, tzinfo=localtz))
    # routine.create_tweet_routine(twitter_waypoints)

    # the list of collections from the message_store db to be replicated
    db = 'message_store'
    collections = ['heads','metric_map_data','rosout_agg','robot_pose','task_events','scheduling_problems','ws_observations','monitored_nav_events', 'people_perception']
    routine.message_store_entries_to_replicate(collections)

    db = 'roslog'
    collections = ['head_xtion_compressed_depth_libav', 'head_xtion_compressed_rgb_theora', 'head_xtion_compressed_rgb_compressed']
    routine.message_store_entries_to_replicate(collections)

    db = 'metric_maps'
    collections = ['data', 'summary']
    routine.message_store_entries_to_replicate(collections)


    routine.start_routine()

    rospy.spin()

