## *********************************************************
##
## File autogenerated for the sick_ldmrs_driver package
## by the dynamic_reconfigure package.
## Please do not edit.
##
## ********************************************************/

from dynamic_reconfigure.encoding import extract_params

inf = float('inf')

config_description = {'upper': 'DEFAULT', 'lower': 'groups', 'srcline': 246, 'name': 'Default', 'parent': 0, 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'cstate': 'true', 'parentname': 'Default', 'class': 'DEFAULT', 'field': 'default', 'state': True, 'parentclass': '', 'groups': [], 'parameters': [{'srcline': 291, 'description': 'The TF frame in which point clouds will be returned.', 'max': '', 'cconsttype': 'const char * const', 'ctype': 'std::string', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'frame_id', 'edit_method': '', 'default': 'ldmrs', 'level': 0, 'min': '', 'type': 'str'}, {'srcline': 291, 'description': 'The angle of the first range measurement [rad].', 'max': 0.8726646259971648, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'start_angle', 'edit_method': '', 'default': 0.8726646259971648, 'level': 0, 'min': -1.0461067204141012, 'type': 'double'}, {'srcline': 291, 'description': 'The angle of the last range measurement [rad].', 'max': 0.8715737952146683, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'end_angle', 'edit_method': '', 'default': -1.0471975511965976, 'level': 0, 'min': -1.0471975511965976, 'type': 'double'}, {'srcline': 291, 'description': 'Scan frequency, 0 = 12.5Hz, 1 = 25 Hz, 2 = 50 Hz', 'max': 2, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'scan_frequency', 'edit_method': "{'enum_description': 'Available scan frequencies', 'enum': [{'srcline': 44, 'description': 'Scan frequency 12.5 Hz', 'srcfile': '/home/agilex/autoware.ai/src/drivers/awf_drivers/sick_ldmrs_driver/cfg/SickLDMRSDriver.cfg', 'cconsttype': 'const int', 'value': 0, 'ctype': 'int', 'type': 'int', 'name': 'ScanFreq1250'}, {'srcline': 45, 'description': 'Scan frequency 25.0 Hz', 'srcfile': '/home/agilex/autoware.ai/src/drivers/awf_drivers/sick_ldmrs_driver/cfg/SickLDMRSDriver.cfg', 'cconsttype': 'const int', 'value': 1, 'ctype': 'int', 'type': 'int', 'name': 'ScanFreq2500'}, {'srcline': 46, 'description': 'Scan frequency 50.0 Hz', 'srcfile': '/home/agilex/autoware.ai/src/drivers/awf_drivers/sick_ldmrs_driver/cfg/SickLDMRSDriver.cfg', 'cconsttype': 'const int', 'value': 2, 'ctype': 'int', 'type': 'int', 'name': 'ScanFreq5000'}]}", 'default': 0, 'level': 0, 'min': 0, 'type': 'int'}, {'srcline': 291, 'description': 'Angle under which the LD-MRS measures at the time of the sync pulse [rad].', 'max': 3.141047238198545, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'sync_angle_offset', 'edit_method': '', 'default': 0.0, 'level': 0, 'min': -3.141592653589793, 'type': 'double'}, {'srcline': 291, 'description': 'Angular resolution type: 0 = focused, 1 = constant, 2 = flexible', 'max': 2, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'angular_resolution_type', 'edit_method': "{'enum_description': 'Angular resolution type', 'enum': [{'srcline': 54, 'description': 'Focused resolution', 'srcfile': '/home/agilex/autoware.ai/src/drivers/awf_drivers/sick_ldmrs_driver/cfg/SickLDMRSDriver.cfg', 'cconsttype': 'const int', 'value': 0, 'ctype': 'int', 'type': 'int', 'name': 'FocusedRes'}, {'srcline': 55, 'description': 'Constant resolution', 'srcfile': '/home/agilex/autoware.ai/src/drivers/awf_drivers/sick_ldmrs_driver/cfg/SickLDMRSDriver.cfg', 'cconsttype': 'const int', 'value': 1, 'ctype': 'int', 'type': 'int', 'name': 'ConstantRes'}, {'srcline': 56, 'description': 'Flexible resolution', 'srcfile': '/home/agilex/autoware.ai/src/drivers/awf_drivers/sick_ldmrs_driver/cfg/SickLDMRSDriver.cfg', 'cconsttype': 'const int', 'value': 2, 'ctype': 'int', 'type': 'int', 'name': 'FlexRes'}]}", 'default': 1, 'level': 0, 'min': 0, 'type': 'int'}, {'srcline': 291, 'description': '0: Full range, 1: lower 4 reduced, 2: upper 4 reduced, 3: all reduced', 'max': 3, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'layer_range_reduction', 'edit_method': "{'enum_description': 'Layer range reduction', 'enum': [{'srcline': 59, 'description': 'All layers full range', 'srcfile': '/home/agilex/autoware.ai/src/drivers/awf_drivers/sick_ldmrs_driver/cfg/SickLDMRSDriver.cfg', 'cconsttype': 'const int', 'value': 0, 'ctype': 'int', 'type': 'int', 'name': 'RangeFull'}, {'srcline': 60, 'description': 'Lower 4 layers reduced range', 'srcfile': '/home/agilex/autoware.ai/src/drivers/awf_drivers/sick_ldmrs_driver/cfg/SickLDMRSDriver.cfg', 'cconsttype': 'const int', 'value': 1, 'ctype': 'int', 'type': 'int', 'name': 'RangeLowerReduced'}, {'srcline': 61, 'description': 'Upper 4 layers reduced range', 'srcfile': '/home/agilex/autoware.ai/src/drivers/awf_drivers/sick_ldmrs_driver/cfg/SickLDMRSDriver.cfg', 'cconsttype': 'const int', 'value': 2, 'ctype': 'int', 'type': 'int', 'name': 'RangeUpperReduced'}, {'srcline': 62, 'description': 'All 8 layers reduced range', 'srcfile': '/home/agilex/autoware.ai/src/drivers/awf_drivers/sick_ldmrs_driver/cfg/SickLDMRSDriver.cfg', 'cconsttype': 'const int', 'value': 3, 'ctype': 'int', 'type': 'int', 'name': 'RangeAllReduced'}]}", 'default': 0, 'level': 0, 'min': 0, 'type': 'int'}, {'srcline': 291, 'description': 'Ignore scan points up to 15m. Requires layer_range_reduction = lower 4 reduced.', 'max': True, 'cconsttype': 'const bool', 'ctype': 'bool', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'ignore_near_range', 'edit_method': '', 'default': False, 'level': 0, 'min': False, 'type': 'bool'}, {'srcline': 291, 'description': 'Reduce the sensitivity automatically in case of extraneous light.', 'max': True, 'cconsttype': 'const bool', 'ctype': 'bool', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'sensitivity_control', 'edit_method': '', 'default': False, 'level': 0, 'min': False, 'type': 'bool'}, {'srcline': 291, 'description': 'FlexRes: start angle of sector 1.', 'max': 0.8726646259971648, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'flexres_start_angle1', 'edit_method': '', 'default': 0.8726646259971648, 'level': 0, 'min': -1.0461067204141012, 'type': 'double'}, {'srcline': 291, 'description': 'FlexRes: start angle of sector 2.', 'max': 0.8726646259971648, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'flexres_start_angle2', 'edit_method': '', 'default': 0.6108652381980153, 'level': 0, 'min': -1.0461067204141012, 'type': 'double'}, {'srcline': 291, 'description': 'FlexRes: start angle of sector 3.', 'max': 0.8726646259971648, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'flexres_start_angle3', 'edit_method': '', 'default': 0.5235987755982988, 'level': 0, 'min': -1.0461067204141012, 'type': 'double'}, {'srcline': 291, 'description': 'FlexRes: start angle of sector 4.', 'max': 0.8726646259971648, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'flexres_start_angle4', 'edit_method': '', 'default': 0.3490658503988659, 'level': 0, 'min': -1.0461067204141012, 'type': 'double'}, {'srcline': 291, 'description': 'FlexRes: start angle of sector 5.', 'max': 0.8726646259971648, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'flexres_start_angle5', 'edit_method': '', 'default': 0.0, 'level': 0, 'min': -1.0461067204141012, 'type': 'double'}, {'srcline': 291, 'description': 'FlexRes: start angle of sector 6.', 'max': 0.8726646259971648, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'flexres_start_angle6', 'edit_method': '', 'default': -0.3490658503988659, 'level': 0, 'min': -1.0461067204141012, 'type': 'double'}, {'srcline': 291, 'description': 'FlexRes: start angle of sector 7.', 'max': 0.8726646259971648, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'flexres_start_angle7', 'edit_method': '', 'default': -0.5235987755982988, 'level': 0, 'min': -1.0461067204141012, 'type': 'double'}, {'srcline': 291, 'description': 'FlexRes: start angle of sector 8.', 'max': 0.8726646259971648, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'flexres_start_angle8', 'edit_method': '', 'default': -0.6981317007977318, 'level': 0, 'min': -1.0461067204141012, 'type': 'double'}, {'srcline': 291, 'description': 'FlexRes: angular resolution of sector 1.', 'max': 32, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'flexres_resolution1', 'edit_method': "{'enum_description': 'FlexRes angular resolution', 'enum': [{'srcline': 65, 'description': 'Angular resolution 0.125 degrees', 'srcfile': '/home/agilex/autoware.ai/src/drivers/awf_drivers/sick_ldmrs_driver/cfg/SickLDMRSDriver.cfg', 'cconsttype': 'const int', 'value': 4, 'ctype': 'int', 'type': 'int', 'name': 'Res0125'}, {'srcline': 66, 'description': 'Angular resolution 0.25 degrees', 'srcfile': '/home/agilex/autoware.ai/src/drivers/awf_drivers/sick_ldmrs_driver/cfg/SickLDMRSDriver.cfg', 'cconsttype': 'const int', 'value': 8, 'ctype': 'int', 'type': 'int', 'name': 'Res0250'}, {'srcline': 67, 'description': 'Angular resolution 0.5 degrees', 'srcfile': '/home/agilex/autoware.ai/src/drivers/awf_drivers/sick_ldmrs_driver/cfg/SickLDMRSDriver.cfg', 'cconsttype': 'const int', 'value': 16, 'ctype': 'int', 'type': 'int', 'name': 'Res0500'}, {'srcline': 68, 'description': 'Angular resolution 1.0 degrees', 'srcfile': '/home/agilex/autoware.ai/src/drivers/awf_drivers/sick_ldmrs_driver/cfg/SickLDMRSDriver.cfg', 'cconsttype': 'const int', 'value': 32, 'ctype': 'int', 'type': 'int', 'name': 'Res1000'}]}", 'default': 32, 'level': 0, 'min': 4, 'type': 'int'}, {'srcline': 291, 'description': 'FlexRes: angular resolution of sector 2.', 'max': 32, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'flexres_resolution2', 'edit_method': "{'enum_description': 'FlexRes angular resolution', 'enum': [{'srcline': 65, 'description': 'Angular resolution 0.125 degrees', 'srcfile': '/home/agilex/autoware.ai/src/drivers/awf_drivers/sick_ldmrs_driver/cfg/SickLDMRSDriver.cfg', 'cconsttype': 'const int', 'value': 4, 'ctype': 'int', 'type': 'int', 'name': 'Res0125'}, {'srcline': 66, 'description': 'Angular resolution 0.25 degrees', 'srcfile': '/home/agilex/autoware.ai/src/drivers/awf_drivers/sick_ldmrs_driver/cfg/SickLDMRSDriver.cfg', 'cconsttype': 'const int', 'value': 8, 'ctype': 'int', 'type': 'int', 'name': 'Res0250'}, {'srcline': 67, 'description': 'Angular resolution 0.5 degrees', 'srcfile': '/home/agilex/autoware.ai/src/drivers/awf_drivers/sick_ldmrs_driver/cfg/SickLDMRSDriver.cfg', 'cconsttype': 'const int', 'value': 16, 'ctype': 'int', 'type': 'int', 'name': 'Res0500'}, {'srcline': 68, 'description': 'Angular resolution 1.0 degrees', 'srcfile': '/home/agilex/autoware.ai/src/drivers/awf_drivers/sick_ldmrs_driver/cfg/SickLDMRSDriver.cfg', 'cconsttype': 'const int', 'value': 32, 'ctype': 'int', 'type': 'int', 'name': 'Res1000'}]}", 'default': 16, 'level': 0, 'min': 4, 'type': 'int'}, {'srcline': 291, 'description': 'FlexRes: angular resolution of sector 3.', 'max': 32, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'flexres_resolution3', 'edit_method': "{'enum_description': 'FlexRes angular resolution', 'enum': [{'srcline': 65, 'description': 'Angular resolution 0.125 degrees', 'srcfile': '/home/agilex/autoware.ai/src/drivers/awf_drivers/sick_ldmrs_driver/cfg/SickLDMRSDriver.cfg', 'cconsttype': 'const int', 'value': 4, 'ctype': 'int', 'type': 'int', 'name': 'Res0125'}, {'srcline': 66, 'description': 'Angular resolution 0.25 degrees', 'srcfile': '/home/agilex/autoware.ai/src/drivers/awf_drivers/sick_ldmrs_driver/cfg/SickLDMRSDriver.cfg', 'cconsttype': 'const int', 'value': 8, 'ctype': 'int', 'type': 'int', 'name': 'Res0250'}, {'srcline': 67, 'description': 'Angular resolution 0.5 degrees', 'srcfile': '/home/agilex/autoware.ai/src/drivers/awf_drivers/sick_ldmrs_driver/cfg/SickLDMRSDriver.cfg', 'cconsttype': 'const int', 'value': 16, 'ctype': 'int', 'type': 'int', 'name': 'Res0500'}, {'srcline': 68, 'description': 'Angular resolution 1.0 degrees', 'srcfile': '/home/agilex/autoware.ai/src/drivers/awf_drivers/sick_ldmrs_driver/cfg/SickLDMRSDriver.cfg', 'cconsttype': 'const int', 'value': 32, 'ctype': 'int', 'type': 'int', 'name': 'Res1000'}]}", 'default': 8, 'level': 0, 'min': 4, 'type': 'int'}, {'srcline': 291, 'description': 'FlexRes: angular resolution of sector 4.', 'max': 32, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'flexres_resolution4', 'edit_method': "{'enum_description': 'FlexRes angular resolution', 'enum': [{'srcline': 65, 'description': 'Angular resolution 0.125 degrees', 'srcfile': '/home/agilex/autoware.ai/src/drivers/awf_drivers/sick_ldmrs_driver/cfg/SickLDMRSDriver.cfg', 'cconsttype': 'const int', 'value': 4, 'ctype': 'int', 'type': 'int', 'name': 'Res0125'}, {'srcline': 66, 'description': 'Angular resolution 0.25 degrees', 'srcfile': '/home/agilex/autoware.ai/src/drivers/awf_drivers/sick_ldmrs_driver/cfg/SickLDMRSDriver.cfg', 'cconsttype': 'const int', 'value': 8, 'ctype': 'int', 'type': 'int', 'name': 'Res0250'}, {'srcline': 67, 'description': 'Angular resolution 0.5 degrees', 'srcfile': '/home/agilex/autoware.ai/src/drivers/awf_drivers/sick_ldmrs_driver/cfg/SickLDMRSDriver.cfg', 'cconsttype': 'const int', 'value': 16, 'ctype': 'int', 'type': 'int', 'name': 'Res0500'}, {'srcline': 68, 'description': 'Angular resolution 1.0 degrees', 'srcfile': '/home/agilex/autoware.ai/src/drivers/awf_drivers/sick_ldmrs_driver/cfg/SickLDMRSDriver.cfg', 'cconsttype': 'const int', 'value': 32, 'ctype': 'int', 'type': 'int', 'name': 'Res1000'}]}", 'default': 4, 'level': 0, 'min': 4, 'type': 'int'}, {'srcline': 291, 'description': 'FlexRes: angular resolution of sector 5.', 'max': 32, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'flexres_resolution5', 'edit_method': "{'enum_description': 'FlexRes angular resolution', 'enum': [{'srcline': 65, 'description': 'Angular resolution 0.125 degrees', 'srcfile': '/home/agilex/autoware.ai/src/drivers/awf_drivers/sick_ldmrs_driver/cfg/SickLDMRSDriver.cfg', 'cconsttype': 'const int', 'value': 4, 'ctype': 'int', 'type': 'int', 'name': 'Res0125'}, {'srcline': 66, 'description': 'Angular resolution 0.25 degrees', 'srcfile': '/home/agilex/autoware.ai/src/drivers/awf_drivers/sick_ldmrs_driver/cfg/SickLDMRSDriver.cfg', 'cconsttype': 'const int', 'value': 8, 'ctype': 'int', 'type': 'int', 'name': 'Res0250'}, {'srcline': 67, 'description': 'Angular resolution 0.5 degrees', 'srcfile': '/home/agilex/autoware.ai/src/drivers/awf_drivers/sick_ldmrs_driver/cfg/SickLDMRSDriver.cfg', 'cconsttype': 'const int', 'value': 16, 'ctype': 'int', 'type': 'int', 'name': 'Res0500'}, {'srcline': 68, 'description': 'Angular resolution 1.0 degrees', 'srcfile': '/home/agilex/autoware.ai/src/drivers/awf_drivers/sick_ldmrs_driver/cfg/SickLDMRSDriver.cfg', 'cconsttype': 'const int', 'value': 32, 'ctype': 'int', 'type': 'int', 'name': 'Res1000'}]}", 'default': 8, 'level': 0, 'min': 4, 'type': 'int'}, {'srcline': 291, 'description': 'FlexRes: angular resolution of sector 6.', 'max': 32, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'flexres_resolution6', 'edit_method': "{'enum_description': 'FlexRes angular resolution', 'enum': [{'srcline': 65, 'description': 'Angular resolution 0.125 degrees', 'srcfile': '/home/agilex/autoware.ai/src/drivers/awf_drivers/sick_ldmrs_driver/cfg/SickLDMRSDriver.cfg', 'cconsttype': 'const int', 'value': 4, 'ctype': 'int', 'type': 'int', 'name': 'Res0125'}, {'srcline': 66, 'description': 'Angular resolution 0.25 degrees', 'srcfile': '/home/agilex/autoware.ai/src/drivers/awf_drivers/sick_ldmrs_driver/cfg/SickLDMRSDriver.cfg', 'cconsttype': 'const int', 'value': 8, 'ctype': 'int', 'type': 'int', 'name': 'Res0250'}, {'srcline': 67, 'description': 'Angular resolution 0.5 degrees', 'srcfile': '/home/agilex/autoware.ai/src/drivers/awf_drivers/sick_ldmrs_driver/cfg/SickLDMRSDriver.cfg', 'cconsttype': 'const int', 'value': 16, 'ctype': 'int', 'type': 'int', 'name': 'Res0500'}, {'srcline': 68, 'description': 'Angular resolution 1.0 degrees', 'srcfile': '/home/agilex/autoware.ai/src/drivers/awf_drivers/sick_ldmrs_driver/cfg/SickLDMRSDriver.cfg', 'cconsttype': 'const int', 'value': 32, 'ctype': 'int', 'type': 'int', 'name': 'Res1000'}]}", 'default': 16, 'level': 0, 'min': 4, 'type': 'int'}, {'srcline': 291, 'description': 'FlexRes: angular resolution of sector 7.', 'max': 32, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'flexres_resolution7', 'edit_method': "{'enum_description': 'FlexRes angular resolution', 'enum': [{'srcline': 65, 'description': 'Angular resolution 0.125 degrees', 'srcfile': '/home/agilex/autoware.ai/src/drivers/awf_drivers/sick_ldmrs_driver/cfg/SickLDMRSDriver.cfg', 'cconsttype': 'const int', 'value': 4, 'ctype': 'int', 'type': 'int', 'name': 'Res0125'}, {'srcline': 66, 'description': 'Angular resolution 0.25 degrees', 'srcfile': '/home/agilex/autoware.ai/src/drivers/awf_drivers/sick_ldmrs_driver/cfg/SickLDMRSDriver.cfg', 'cconsttype': 'const int', 'value': 8, 'ctype': 'int', 'type': 'int', 'name': 'Res0250'}, {'srcline': 67, 'description': 'Angular resolution 0.5 degrees', 'srcfile': '/home/agilex/autoware.ai/src/drivers/awf_drivers/sick_ldmrs_driver/cfg/SickLDMRSDriver.cfg', 'cconsttype': 'const int', 'value': 16, 'ctype': 'int', 'type': 'int', 'name': 'Res0500'}, {'srcline': 68, 'description': 'Angular resolution 1.0 degrees', 'srcfile': '/home/agilex/autoware.ai/src/drivers/awf_drivers/sick_ldmrs_driver/cfg/SickLDMRSDriver.cfg', 'cconsttype': 'const int', 'value': 32, 'ctype': 'int', 'type': 'int', 'name': 'Res1000'}]}", 'default': 32, 'level': 0, 'min': 4, 'type': 'int'}, {'srcline': 291, 'description': 'FlexRes: angular resolution of sector 8.', 'max': 32, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'flexres_resolution8', 'edit_method': "{'enum_description': 'FlexRes angular resolution', 'enum': [{'srcline': 65, 'description': 'Angular resolution 0.125 degrees', 'srcfile': '/home/agilex/autoware.ai/src/drivers/awf_drivers/sick_ldmrs_driver/cfg/SickLDMRSDriver.cfg', 'cconsttype': 'const int', 'value': 4, 'ctype': 'int', 'type': 'int', 'name': 'Res0125'}, {'srcline': 66, 'description': 'Angular resolution 0.25 degrees', 'srcfile': '/home/agilex/autoware.ai/src/drivers/awf_drivers/sick_ldmrs_driver/cfg/SickLDMRSDriver.cfg', 'cconsttype': 'const int', 'value': 8, 'ctype': 'int', 'type': 'int', 'name': 'Res0250'}, {'srcline': 67, 'description': 'Angular resolution 0.5 degrees', 'srcfile': '/home/agilex/autoware.ai/src/drivers/awf_drivers/sick_ldmrs_driver/cfg/SickLDMRSDriver.cfg', 'cconsttype': 'const int', 'value': 16, 'ctype': 'int', 'type': 'int', 'name': 'Res0500'}, {'srcline': 68, 'description': 'Angular resolution 1.0 degrees', 'srcfile': '/home/agilex/autoware.ai/src/drivers/awf_drivers/sick_ldmrs_driver/cfg/SickLDMRSDriver.cfg', 'cconsttype': 'const int', 'value': 32, 'ctype': 'int', 'type': 'int', 'name': 'Res1000'}]}", 'default': 16, 'level': 0, 'min': 4, 'type': 'int'}, {'srcline': 291, 'description': 'Contour point density, 0: closest point only, 1: low density, 2: high density', 'max': 2, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'contour_point_density', 'edit_method': "{'enum_description': 'Contour point density', 'enum': [{'srcline': 49, 'description': 'Closest point only', 'srcfile': '/home/agilex/autoware.ai/src/drivers/awf_drivers/sick_ldmrs_driver/cfg/SickLDMRSDriver.cfg', 'cconsttype': 'const int', 'value': 0, 'ctype': 'int', 'type': 'int', 'name': 'ClosestPointOnly'}, {'srcline': 50, 'description': 'Low density', 'srcfile': '/home/agilex/autoware.ai/src/drivers/awf_drivers/sick_ldmrs_driver/cfg/SickLDMRSDriver.cfg', 'cconsttype': 'const int', 'value': 1, 'ctype': 'int', 'type': 'int', 'name': 'LowDensity'}, {'srcline': 51, 'description': 'High density', 'srcfile': '/home/agilex/autoware.ai/src/drivers/awf_drivers/sick_ldmrs_driver/cfg/SickLDMRSDriver.cfg', 'cconsttype': 'const int', 'value': 2, 'ctype': 'int', 'type': 'int', 'name': 'HighDensity'}]}", 'default': 2, 'level': 0, 'min': 0, 'type': 'int'}, {'srcline': 291, 'description': 'Minimum tracking age (number of scans) of an object to be transmitted.', 'max': 65535, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'min_object_age', 'edit_method': '', 'default': 0, 'level': 0, 'min': 0, 'type': 'int'}, {'srcline': 291, 'description': 'Maximum prediction age (number of scans) of an object to be transmitted.', 'max': 65535, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'max_prediction_age', 'edit_method': '', 'default': 0, 'level': 0, 'min': 0, 'type': 'int'}], 'type': '', 'id': 0}

min = {}
max = {}
defaults = {}
level = {}
type = {}
all_level = 0

#def extract_params(config):
#    params = []
#    params.extend(config['parameters'])
#    for group in config['groups']:
#        params.extend(extract_params(group))
#    return params

for param in extract_params(config_description):
    min[param['name']] = param['min']
    max[param['name']] = param['max']
    defaults[param['name']] = param['default']
    level[param['name']] = param['level']
    type[param['name']] = param['type']
    all_level = all_level | param['level']

SickLDMRSDriver_ScanFreq1250 = 0
SickLDMRSDriver_ScanFreq2500 = 1
SickLDMRSDriver_ScanFreq5000 = 2
SickLDMRSDriver_ClosestPointOnly = 0
SickLDMRSDriver_LowDensity = 1
SickLDMRSDriver_HighDensity = 2
SickLDMRSDriver_FocusedRes = 0
SickLDMRSDriver_ConstantRes = 1
SickLDMRSDriver_FlexRes = 2
SickLDMRSDriver_RangeFull = 0
SickLDMRSDriver_RangeLowerReduced = 1
SickLDMRSDriver_RangeUpperReduced = 2
SickLDMRSDriver_RangeAllReduced = 3
SickLDMRSDriver_Res0125 = 4
SickLDMRSDriver_Res0250 = 8
SickLDMRSDriver_Res0500 = 16
SickLDMRSDriver_Res1000 = 32
