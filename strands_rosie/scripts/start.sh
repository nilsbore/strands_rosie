#!/bin/bash

SESSION=$USER

tmux -2 new-session -d -s $SESSION
# Setup a window for tailing log files
tmux new-window -t $SESSION:0 -n 'roscore'
tmux new-window -t $SESSION:1 -n 'rosie_core'
tmux new-window -t $SESSION:2 -n 'rosie_robot'
tmux new-window -t $SESSION:3 -n 'rosie_cameras'
tmux new-window -t $SESSION:4 -n 'strands_ui'
tmux new-window -t $SESSION:5 -n 'rosie_navigation'
tmux new-window -t $SESSION:6 -n 'rosie_head_camera'
tmux new-window -t $SESSION:7 -n 'RViz'
tmux new-window -t $SESSION:8 -n 'rosie_mapping'
tmux new-window -t $SESSION:9 -n 'record_server'
tmux new-window -t $SESSION:10 -n 'rosie_scheduler'
tmux new-window -t $SESSION:11 -n 'rosie_routine'



tmux select-window -t $SESSION:0
tmux split-window -v
tmux select-pane -t 0
tmux send-keys "roscore" C-m
tmux resize-pane -U 30
tmux select-pane -t 1
tmux send-keys "htop" C-m

tmux select-window -t $SESSION:1
tmux send-keys "roslaunch strands_rosie rosie_core.launch"

tmux select-window -t $SESSION:2
tmux send-keys "roslaunch strands_rosie rosie_robot.launch"

tmux select-window -t $SESSION:3
tmux send-keys "roslaunch strands_rosie rosie_cameras.launch"

tmux select-window -t $SESSION:4
tmux send-keys "roslaunch strands_ui strands_ui.launch"

tmux select-window -t $SESSION:5
tmux send-keys "roslaunch strands_rosie rosie_navigation.launch"

tmux select-window -t $SESSION:6
tmux send-keys "ssh hydro-default@strands-sidekick" C-m
tmux send-keys "roslaunch openni_wrapper main.launch camera:=head_xtion"

tmux select-window -t $SESSION:7
tmux send-keys "rosrun rviz rviz"

tmux select-window -t $SESSION:8
tmux send-keys "ssh hydro-default@strands-sidekick" C-m
tmux send-keys "roslaunch strands_rosie rosie_mapping.launch"

tmux select-window -t $SESSION:9
tmux send-keys "ssh hydro-default@strands-sidekick" C-m
tmux send-keys "roslaunch mongodb_openni_compression record_server.launch"

tmux select-window -t $SESSION:10
tmux send-keys "roslaunch strands_rosie strands_scheduler.launch"

tmux select-window -t $SESSION:11
tmux send-keys "rosrun rosie_routine marathon_y2_rosie_routine.py"

# Set default window
tmux select-window -t $SESSION:0

# Attach to session
tmux -2 attach-session -t $SESSION

tmux setw -g mode-mouse on
