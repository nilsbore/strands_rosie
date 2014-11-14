#!/bin/bash

SESSION=$USER

tmux -2 new-session -d -s $SESSION
# Setup a window for tailing log files
tmux new-window -t $SESSION:0 -n 'roscore'
tmux new-window -t $SESSION:1 -n 'rosie_core'
tmux new-window -t $SESSION:2 -n 'rosie_robot'
tmux new-window -t $SESSION:3 -n 'strands_ui'
tmux new-window -t $SESSION:4 -n 'rosie_navigation'
tmux new-window -t $SESSION:5 -n 'rosie_head_camera'
tmux new-window -t $SESSION:6 -n 'door_pass'
tmux new-window -t $SESSION:7 -n 'RViz'



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
tmux send-keys "roslaunch strands_ui strands_ui.launch"

tmux select-window -t $SESSION:4
tmux send-keys "roslaunch strands_rosie rosie_navigation.launch"

tmux select-window -t $SESSION:5
tmux send-keys "ssh hydro-default@strands-sidekick" C-m
tmux send-keys "source release_ws/devel/setup.bash" C-m
tmux send-keys "roslaunch openni_wrapper main.launch camera:=head_xtion"

tmux select-window -t $SESSION:6
tmux send-keys "rosrun door_pass door_pass.py"

tmux select-window -t $SESSION:7
tmux send-keys "rosrun rviz rviz"

# Set default window
tmux select-window -t $SESSION:0

# Attach to session
tmux -2 attach-session -t $SESSION

tmux setw -g mode-mouse on
