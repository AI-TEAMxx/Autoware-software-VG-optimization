# generated from catkin/cmake/template/pkg.context.pc.in
CATKIN_PACKAGE_PREFIX = ""
PROJECT_PKG_CONFIG_INCLUDE_DIRS = "${prefix}/include".split(';') if "${prefix}/include" != "" else []
PROJECT_CATKIN_DEPENDS = "geometry_msgs;vector_map_msgs;roscpp;rospy;std_msgs;waypoint_follower;op_utility;op_planner;op_simu".replace(';', ' ')
PKG_CONFIG_LIBRARIES_WITH_PREFIX = "-lway_planner".split(';') if "-lway_planner" != "" else []
PROJECT_NAME = "way_planner"
PROJECT_SPACE_DIR = "/home/agilex/autoware.ai/install/way_planner"
PROJECT_VERSION = "1.11.0"
