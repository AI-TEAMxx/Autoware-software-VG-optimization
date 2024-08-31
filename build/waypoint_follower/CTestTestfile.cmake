# CMake generated Testfile for 
# Source directory: /home/agilex/autoware.ai/src/autoware/common/waypoint_follower
# Build directory: /home/agilex/autoware.ai/build/waypoint_follower
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(_ctest_waypoint_follower_rostest_test_test_twist_gate.test "/home/agilex/autoware.ai/build/waypoint_follower/catkin_generated/env_cached.sh" "/usr/bin/python2" "/opt/ros/melodic/share/catkin/cmake/test/run_tests.py" "/home/agilex/autoware.ai/build/waypoint_follower/test_results/waypoint_follower/rostest-test_test_twist_gate.xml" "--return-code" "/usr/bin/python2 /opt/ros/melodic/share/rostest/cmake/../../../bin/rostest --pkgdir=/home/agilex/autoware.ai/src/autoware/common/waypoint_follower --package=waypoint_follower --results-filename test_test_twist_gate.xml --results-base-dir \"/home/agilex/autoware.ai/build/waypoint_follower/test_results\" /home/agilex/autoware.ai/src/autoware/common/waypoint_follower/test/test_twist_gate.test ")
add_test(_ctest_waypoint_follower_rostest_test_test_mpc_utils.test "/home/agilex/autoware.ai/build/waypoint_follower/catkin_generated/env_cached.sh" "/usr/bin/python2" "/opt/ros/melodic/share/catkin/cmake/test/run_tests.py" "/home/agilex/autoware.ai/build/waypoint_follower/test_results/waypoint_follower/rostest-test_test_mpc_utils.xml" "--return-code" "/usr/bin/python2 /opt/ros/melodic/share/rostest/cmake/../../../bin/rostest --pkgdir=/home/agilex/autoware.ai/src/autoware/common/waypoint_follower --package=waypoint_follower --results-filename test_test_mpc_utils.xml --results-base-dir \"/home/agilex/autoware.ai/build/waypoint_follower/test_results\" /home/agilex/autoware.ai/src/autoware/common/waypoint_follower/test/test_mpc_utils.test ")
add_test(_ctest_waypoint_follower_rostest_test_test_mpc_follower.test "/home/agilex/autoware.ai/build/waypoint_follower/catkin_generated/env_cached.sh" "/usr/bin/python2" "/opt/ros/melodic/share/catkin/cmake/test/run_tests.py" "/home/agilex/autoware.ai/build/waypoint_follower/test_results/waypoint_follower/rostest-test_test_mpc_follower.xml" "--return-code" "/usr/bin/python2 /opt/ros/melodic/share/rostest/cmake/../../../bin/rostest --pkgdir=/home/agilex/autoware.ai/src/autoware/common/waypoint_follower --package=waypoint_follower --results-filename test_test_mpc_follower.xml --results-base-dir \"/home/agilex/autoware.ai/build/waypoint_follower/test_results\" /home/agilex/autoware.ai/src/autoware/common/waypoint_follower/test/test_mpc_follower.test ")
add_test(_ctest_waypoint_follower_rostest_test_test_mpc_lowpass_filter.test "/home/agilex/autoware.ai/build/waypoint_follower/catkin_generated/env_cached.sh" "/usr/bin/python2" "/opt/ros/melodic/share/catkin/cmake/test/run_tests.py" "/home/agilex/autoware.ai/build/waypoint_follower/test_results/waypoint_follower/rostest-test_test_mpc_lowpass_filter.xml" "--return-code" "/usr/bin/python2 /opt/ros/melodic/share/rostest/cmake/../../../bin/rostest --pkgdir=/home/agilex/autoware.ai/src/autoware/common/waypoint_follower --package=waypoint_follower --results-filename test_test_mpc_lowpass_filter.xml --results-base-dir \"/home/agilex/autoware.ai/build/waypoint_follower/test_results\" /home/agilex/autoware.ai/src/autoware/common/waypoint_follower/test/test_mpc_lowpass_filter.test ")
subdirs("gtest")
