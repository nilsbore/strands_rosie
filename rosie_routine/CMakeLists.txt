cmake_minimum_required(VERSION 2.8.3)
project(rosie_routine)

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED COMPONENTS  
  dynamic_reconfigure
  std_msgs message_generation
  routine_behaviours
)

#catkin_python_setup()

## Generate added messages and services with any dependencies listed here
generate_messages(
  DEPENDENCIES
  std_msgs  
)


catkin_package(
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)

install(DIRECTORY scripts/
        DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
        USE_SOURCE_PERMISSIONS)

