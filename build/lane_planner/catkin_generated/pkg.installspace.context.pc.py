# generated from catkin/cmake/template/pkg.context.pc.in
CATKIN_PACKAGE_PREFIX = ""
PROJECT_PKG_CONFIG_INCLUDE_DIRS = "${prefix}/include".split(';') if "${prefix}/include" != "" else []
PROJECT_CATKIN_DEPENDS = "roscpp;std_msgs;waypoint_follower;vector_map;gnss;autoware_msgs".replace(';', ' ')
PKG_CONFIG_LIBRARIES_WITH_PREFIX = "-llane_planner".split(';') if "-llane_planner" != "" else []
PROJECT_NAME = "lane_planner"
PROJECT_SPACE_DIR = "/home/agilex/autoware.ai/install/lane_planner"
PROJECT_VERSION = "1.11.0"
