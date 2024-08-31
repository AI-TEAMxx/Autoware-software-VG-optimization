#!/bin/sh

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
fi

echo_and_run() { echo "+ $@" ; "$@" ; }

echo_and_run cd "/home/agilex/autoware.ai/src/autoware/simulation/lgsvl_simulator_bridge"

# ensure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/agilex/autoware.ai/install/lgsvl_simulator_bridge/lib/python2.7/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/agilex/autoware.ai/install/lgsvl_simulator_bridge/lib/python2.7/dist-packages:/home/agilex/autoware.ai/build/lgsvl_simulator_bridge/lib/python2.7/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/agilex/autoware.ai/build/lgsvl_simulator_bridge" \
    "/usr/bin/python2" \
    "/home/agilex/autoware.ai/src/autoware/simulation/lgsvl_simulator_bridge/setup.py" \
     \
    build --build-base "/home/agilex/autoware.ai/build/lgsvl_simulator_bridge" \
    install \
    --root="${DESTDIR-/}" \
    --install-layout=deb --prefix="/home/agilex/autoware.ai/install/lgsvl_simulator_bridge" --install-scripts="/home/agilex/autoware.ai/install/lgsvl_simulator_bridge/bin"
