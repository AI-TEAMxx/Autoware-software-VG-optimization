# CMake generated Testfile for 
# Source directory: /home/agilex/autoware.ai/src/autoware/core_planning/decision_maker
# Build directory: /home/agilex/autoware.ai/build/decision_maker
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(_ctest_decision_maker_rostest_test_test_decision_maker.test "/home/agilex/autoware.ai/build/decision_maker/catkin_generated/env_cached.sh" "/usr/bin/python2" "/opt/ros/melodic/share/catkin/cmake/test/run_tests.py" "/home/agilex/autoware.ai/build/decision_maker/test_results/decision_maker/rostest-test_test_decision_maker.xml" "--return-code" "/usr/bin/python2 /opt/ros/melodic/share/rostest/cmake/../../../bin/rostest --pkgdir=/home/agilex/autoware.ai/src/autoware/core_planning/decision_maker --package=decision_maker --results-filename test_test_decision_maker.xml --results-base-dir \"/home/agilex/autoware.ai/build/decision_maker/test_results\" /home/agilex/autoware.ai/src/autoware/core_planning/decision_maker/test/test_decision_maker.test ")
subdirs("gtest")
