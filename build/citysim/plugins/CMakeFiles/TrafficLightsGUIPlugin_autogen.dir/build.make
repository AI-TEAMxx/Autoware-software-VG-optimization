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
CMAKE_SOURCE_DIR = /home/agilex/autoware.ai/src/citysim

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/agilex/autoware.ai/build/citysim

# Utility rule file for TrafficLightsGUIPlugin_autogen.

# Include the progress variables for this target.
include plugins/CMakeFiles/TrafficLightsGUIPlugin_autogen.dir/progress.make

plugins/CMakeFiles/TrafficLightsGUIPlugin_autogen:
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/home/agilex/autoware.ai/build/citysim/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Automatic MOC for target TrafficLightsGUIPlugin"
	cd /home/agilex/autoware.ai/build/citysim/plugins && /usr/bin/cmake -E cmake_autogen /home/agilex/autoware.ai/build/citysim/plugins/CMakeFiles/TrafficLightsGUIPlugin_autogen.dir Release

TrafficLightsGUIPlugin_autogen: plugins/CMakeFiles/TrafficLightsGUIPlugin_autogen
TrafficLightsGUIPlugin_autogen: plugins/CMakeFiles/TrafficLightsGUIPlugin_autogen.dir/build.make

.PHONY : TrafficLightsGUIPlugin_autogen

# Rule to build all files generated by this target.
plugins/CMakeFiles/TrafficLightsGUIPlugin_autogen.dir/build: TrafficLightsGUIPlugin_autogen

.PHONY : plugins/CMakeFiles/TrafficLightsGUIPlugin_autogen.dir/build

plugins/CMakeFiles/TrafficLightsGUIPlugin_autogen.dir/clean:
	cd /home/agilex/autoware.ai/build/citysim/plugins && $(CMAKE_COMMAND) -P CMakeFiles/TrafficLightsGUIPlugin_autogen.dir/cmake_clean.cmake
.PHONY : plugins/CMakeFiles/TrafficLightsGUIPlugin_autogen.dir/clean

plugins/CMakeFiles/TrafficLightsGUIPlugin_autogen.dir/depend:
	cd /home/agilex/autoware.ai/build/citysim && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/agilex/autoware.ai/src/citysim /home/agilex/autoware.ai/src/citysim/plugins /home/agilex/autoware.ai/build/citysim /home/agilex/autoware.ai/build/citysim/plugins /home/agilex/autoware.ai/build/citysim/plugins/CMakeFiles/TrafficLightsGUIPlugin_autogen.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : plugins/CMakeFiles/TrafficLightsGUIPlugin_autogen.dir/depend

