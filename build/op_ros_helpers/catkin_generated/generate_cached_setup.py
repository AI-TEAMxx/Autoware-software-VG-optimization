# -*- coding: utf-8 -*-
from __future__ import print_function

import os
import stat
import sys

# find the import for catkin's python package - either from source space or from an installed underlay
if os.path.exists(os.path.join('/opt/ros/melodic/share/catkin/cmake', 'catkinConfig.cmake.in')):
    sys.path.insert(0, os.path.join('/opt/ros/melodic/share/catkin/cmake', '..', 'python'))
try:
    from catkin.environment_cache import generate_environment_script
except ImportError:
    # search for catkin package in all workspaces and prepend to path
    for workspace in '/home/agilex/autoware.ai/install/op_simu;/home/agilex/autoware.ai/install/op_planner;/home/agilex/autoware.ai/install/op_utility;/home/agilex/autoware.ai/install/waypoint_follower;/home/agilex/autoware.ai/install/vector_map_server;/home/agilex/autoware.ai/install/map_file;/home/agilex/autoware.ai/install/vector_map;/home/agilex/autoware.ai/install/autoware_health_checker;/home/agilex/autoware.ai/install/amathutils_lib;/home/agilex/autoware.ai/install/vector_map_msgs;/home/agilex/autoware.ai/install/tablet_socket_msgs;/home/agilex/autoware.ai/install/autoware_system_msgs;/home/agilex/autoware.ai/install/autoware_msgs;/home/agilex/autoware.ai/install/autoware_config_msgs;/home/agilex/autoware.ai/install/autoware_build_flags;/opt/ros/melodic'.split(';'):
        python_path = os.path.join(workspace, 'lib/python2.7/dist-packages')
        if os.path.isdir(os.path.join(python_path, 'catkin')):
            sys.path.insert(0, python_path)
            break
    from catkin.environment_cache import generate_environment_script

code = generate_environment_script('/home/agilex/autoware.ai/build/op_ros_helpers/devel/env.sh')

output_filename = '/home/agilex/autoware.ai/build/op_ros_helpers/catkin_generated/setup_cached.sh'
with open(output_filename, 'w') as f:
    # print('Generate script for cached setup "%s"' % output_filename)
    f.write('\n'.join(code))

mode = os.stat(output_filename).st_mode
os.chmod(output_filename, mode | stat.S_IXUSR)
