execute_process(COMMAND "/home/agilex/autoware.ai/build/autoware_camera_lidar_calibrator/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/agilex/autoware.ai/build/autoware_camera_lidar_calibrator/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
