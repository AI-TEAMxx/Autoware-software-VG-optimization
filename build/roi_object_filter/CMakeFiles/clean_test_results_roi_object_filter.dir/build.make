# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.10

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/agilex/autoware.ai/src/autoware/core_perception/roi_object_filter

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/agilex/autoware.ai/build/roi_object_filter

# Utility rule file for clean_test_results_roi_object_filter.

# Include the progress variables for this target.
include CMakeFiles/clean_test_results_roi_object_filter.dir/progress.make

CMakeFiles/clean_test_results_roi_object_filter:
	/usr/bin/python2 /opt/ros/melodic/share/catkin/cmake/test/remove_test_results.py /home/agilex/autoware.ai/build/roi_object_filter/test_results/roi_object_filter

clean_test_results_roi_object_filter: CMakeFiles/clean_test_results_roi_object_filter
clean_test_results_roi_object_filter: CMakeFiles/clean_test_results_roi_object_filter.dir/build.make

.PHONY : clean_test_results_roi_object_filter

# Rule to build all files generated by this target.
CMakeFiles/clean_test_results_roi_object_filter.dir/build: clean_test_results_roi_object_filter

.PHONY : CMakeFiles/clean_test_results_roi_object_filter.dir/build

CMakeFiles/clean_test_results_roi_object_filter.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/clean_test_results_roi_object_filter.dir/cmake_clean.cmake
.PHONY : CMakeFiles/clean_test_results_roi_object_filter.dir/clean

CMakeFiles/clean_test_results_roi_object_filter.dir/depend:
	cd /home/agilex/autoware.ai/build/roi_object_filter && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/agilex/autoware.ai/src/autoware/core_perception/roi_object_filter /home/agilex/autoware.ai/src/autoware/core_perception/roi_object_filter /home/agilex/autoware.ai/build/roi_object_filter /home/agilex/autoware.ai/build/roi_object_filter /home/agilex/autoware.ai/build/roi_object_filter/CMakeFiles/clean_test_results_roi_object_filter.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/clean_test_results_roi_object_filter.dir/depend

