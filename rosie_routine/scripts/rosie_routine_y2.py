#!/usr/bin/env python

import rospy

from datetime import time, timedelta, datetime
from dateutil.tz import tzutc, tzlocal

from routine_behaviours.marathon_routine import MarathonRoutine
    

if __name__ == '__main__':
    rospy.init_node("rosie_routine")

    # start and end times -- all times should be in a particular timezone - local has stopped working!
    # localtz = tzlocal()
    localtz = tzutc()

    now = datetime.now(localtz).time().replace(tzinfo=localtz)
    # useful for testing
    # start = now

    start = time(9,00, tzinfo=localtz)    
    end = time(19,00, tzinfo=localtz)

    # how long to stand idle before doing something
    idle_duration=rospy.Duration(2)

    # how long do you want it to take to do a tour. this must be greater than the time you think it will take!
    # the number argument is in seconds
    tour_duration_estimate = rospy.Duration(60 * 40 * 2)

    #routine = MarathonRoutine(daily_start=start, daily_end=end, 
    #    idle_duration=idle_duration, tour_duration_estimate=tour_duration_estimate)
    routine = MarathonRoutine(daily_start=start, daily_end=end, 
    idle_duration=idle_duration, tour_duration_estimate=tour_duration_estimate)     


    # choose which nodes are visited at random on idle
    # routine.random_nodes = ['WayPoint2', 'WayPoint3']
    # or
    #routine.random_nodes = routine.all_waypoints_except(['WayPoint2', 'WayPoint3'])
    routine.random_nodes = ['WayPoint4', 'WayPoint16', 'WayPoint22', 'WayPoint21','WayPoint20', 'WayPoint6','WayPoint7','WayPoint13','WayPoint14','WayPoint17']

    # go around every node every tour_duration_estimate
    # routine.create_patrol_routine()

    ten_am = time(10,00, tzinfo=localtz)
    two_pm = time(14,00, tzinfo=localtz)

    fifteen_mins = timedelta(minutes = 15)
    thirty_mins = timedelta(minutes = 30)
    sixty_mins = timedelta(minutes = 60)
    ninety_mins = timedelta(minutes = 90)


    # patrol just these selected waypoints every 30 minutes in the first part of the day
    routine.create_patrol_routine(waypoints=['WayPoint2', 'WayPoint3'], daily_start=start, daily_end=ten_am, repeat_delta=thirty_mins)
    
    # then all but these every 60 minutes in the second part part of the day
    #routine.create_patrol_routine(waypoints=routine.all_waypoints_except(['WayPoint2', 'WayPoint3']), daily_start=ten_am, daily_end=two_pm, repeat_delta=sixty_mins)
    routine.create_patrol_routine(waypoints=['WayPoint7', 'WayPoint21', 'WayPoint5', 'WayPoint16'], daily_start=start, daily_end=end, repeat_delta=thirty_mins)
    
    # then all waypoints these every 90 minutes in the final part of the day
    #routine.create_patrol_routine(waypoints=routine.all_waypoints(), daily_start=two_pm, daily_end=end, repeat_delta=ninety_mins)
 

    # do 3d scans
    scan_waypoints = ['WayPoint16', 'WayPoint19', 'WayPoint5']
    routine.create_3d_scan_routine(waypoints=scan_waypoints, repeat_delta=fifteen_mins)

    # where to stop and what to tweet with the image
    #twitter_waypoints = [['WayPoint6', 'I hope everyone is working hard today #ERW14 #RobotMarathon'],
    #                     ['WayPoint2', 'Knowledge is power for @UoBLibServices #ERW14 #RobotMarathon']]    
    # routine.create_tweet_routine(twitter_waypoints, daily_start=time(23,00, tzinfo=localtz), daily_end=time(00,00, tzinfo=localtz))
    #routine.create_tweet_routine(twitter_waypoints)


    # do rgbd recording for a minute at these places every two hours
    #rgbd_waypoints = ['WayPoint2', 'WayPoint3']
    #routine.create_rgbd_record_routine(waypoints=rgbd_waypoints, duration=rospy.Duration(60), repeat_delta=timedelta(hours=2))


    # the list of collections to be replicated
    #db = 'message_store'
    #collections = ['heads','metric_map_data','rosout_agg','robot_pose','task_events','scheduling_problems','ws_observations','monitored_nav_events', 'people_perception']
    #routine.message_store_entries_to_replicate(collections, db=db)

    #db = 'roslog'
    #collections = ['head_xtion_compressed_depth_libav', 'head_xtion_compressed_rgb_theora', 'head_xtion_compressed_rgb_compressed']
    #routine.message_store_entries_to_replicate(collections, db=db)

    #db = 'metric_maps'
    #collections = ['data', 'summary']
    #routine.message_store_entries_to_replicate(collections, db=db)


    routine.start_routine()

    rospy.spin()

