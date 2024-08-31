# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from custom_msgs/Internal.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import custom_msgs.msg
import geometry_msgs.msg
import std_msgs.msg

class Internal(genpy.Message):
  _md5sum = "e17159f7355766bfcea833fefb15620b"
  _type = "custom_msgs/Internal"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """# This is a message to hold data from an IMU (Inertial Measurement Unit)
#
# Accelerations should be in m/s^2 (not in g's), and rotational velocity should be in rad/sec
#
# If the covariance of the measurement is known, it should be filled in (if all you know is the 
# variance of each measurement, e.g. from the datasheet, just put those along the diagonal)
# A covariance matrix of all zeros will be interpreted as "covariance unknown", and to use the
# data a covariance will have to be assumed or gotten from some other source
#
# If you have no estimate for one of the data elements (e.g. your IMU doesn't produce an orientation 
# estimate), please set element 0 of the associated covariance matrix to -1
# If you are interpreting this message, please check for a value of -1 in the first element of each 
# covariance matrix, and disregard the associated estimate.

ImuSensorSample imu

geometry_msgs/Vector3 mag

BaroSensorSample baro

GnssSensorSample gnss


================================================================================
MSG: custom_msgs/ImuSensorSample
# This is a message to hold data from an IMU (Inertial Measurement Unit)
#
# Accelerations should be in m/s^2 (not in g's), and rotational velocity should be in rad/sec
#
# If the covariance of the measurement is known, it should be filled in (if all you know is the 
# variance of each measurement, e.g. from the datasheet, just put those along the diagonal)
# A covariance matrix of all zeros will be interpreted as "covariance unknown", and to use the
# data a covariance will have to be assumed or gotten from some other source
#
# If you have no estimate for one of the data elements (e.g. your IMU doesn't produce an orientation 
# estimate), please set element 0 of the associated covariance matrix to -1
# If you are interpreting this message, please check for a value of -1 in the first element of each 
# covariance matrix, and disregard the associated estimate.

XsensQuaternion dq

geometry_msgs/Vector3 dv

geometry_msgs/Vector3 bGyr




================================================================================
MSG: custom_msgs/XsensQuaternion
# This represents an orientation in free space in quaternion form.

float64 w
float64 x
float64 y
float64 z


================================================================================
MSG: geometry_msgs/Vector3
# This represents a vector in free space. 
# It is only meant to represent a direction. Therefore, it does not
# make sense to apply a translation to it (e.g., when applying a 
# generic rigid transformation to a Vector3, tf2 will only apply the
# rotation). If you want your data to be translatable too, use the
# geometry_msgs/Point message instead.

float64 x
float64 y
float64 z
================================================================================
MSG: custom_msgs/BaroSensorSample
# This is a message to hold data from a baro 

float64 height




================================================================================
MSG: custom_msgs/GnssSensorSample
# This is a message to hold data a GNSS unit
# Supported for MTi Devices with FW 1.4 and above.

std_msgs/Float64 itow
std_msgs/Float64 fix

float64 latitude
float64 longitude
float64 hEll
float64 hMsl

# ENU velocity
geometry_msgs/Vector3 vel

float64 hAcc
float64 vAcc
float64 sAcc

float64 pDop
float64 hDop
float64 vDop

float64 numSat
float64 heading
float64 headingAcc




================================================================================
MSG: std_msgs/Float64
float64 data"""
  __slots__ = ['imu','mag','baro','gnss']
  _slot_types = ['custom_msgs/ImuSensorSample','geometry_msgs/Vector3','custom_msgs/BaroSensorSample','custom_msgs/GnssSensorSample']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       imu,mag,baro,gnss

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(Internal, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.imu is None:
        self.imu = custom_msgs.msg.ImuSensorSample()
      if self.mag is None:
        self.mag = geometry_msgs.msg.Vector3()
      if self.baro is None:
        self.baro = custom_msgs.msg.BaroSensorSample()
      if self.gnss is None:
        self.gnss = custom_msgs.msg.GnssSensorSample()
    else:
      self.imu = custom_msgs.msg.ImuSensorSample()
      self.mag = geometry_msgs.msg.Vector3()
      self.baro = custom_msgs.msg.BaroSensorSample()
      self.gnss = custom_msgs.msg.GnssSensorSample()

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_32d().pack(_x.imu.dq.w, _x.imu.dq.x, _x.imu.dq.y, _x.imu.dq.z, _x.imu.dv.x, _x.imu.dv.y, _x.imu.dv.z, _x.imu.bGyr.x, _x.imu.bGyr.y, _x.imu.bGyr.z, _x.mag.x, _x.mag.y, _x.mag.z, _x.baro.height, _x.gnss.itow.data, _x.gnss.fix.data, _x.gnss.latitude, _x.gnss.longitude, _x.gnss.hEll, _x.gnss.hMsl, _x.gnss.vel.x, _x.gnss.vel.y, _x.gnss.vel.z, _x.gnss.hAcc, _x.gnss.vAcc, _x.gnss.sAcc, _x.gnss.pDop, _x.gnss.hDop, _x.gnss.vDop, _x.gnss.numSat, _x.gnss.heading, _x.gnss.headingAcc))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.imu is None:
        self.imu = custom_msgs.msg.ImuSensorSample()
      if self.mag is None:
        self.mag = geometry_msgs.msg.Vector3()
      if self.baro is None:
        self.baro = custom_msgs.msg.BaroSensorSample()
      if self.gnss is None:
        self.gnss = custom_msgs.msg.GnssSensorSample()
      end = 0
      _x = self
      start = end
      end += 256
      (_x.imu.dq.w, _x.imu.dq.x, _x.imu.dq.y, _x.imu.dq.z, _x.imu.dv.x, _x.imu.dv.y, _x.imu.dv.z, _x.imu.bGyr.x, _x.imu.bGyr.y, _x.imu.bGyr.z, _x.mag.x, _x.mag.y, _x.mag.z, _x.baro.height, _x.gnss.itow.data, _x.gnss.fix.data, _x.gnss.latitude, _x.gnss.longitude, _x.gnss.hEll, _x.gnss.hMsl, _x.gnss.vel.x, _x.gnss.vel.y, _x.gnss.vel.z, _x.gnss.hAcc, _x.gnss.vAcc, _x.gnss.sAcc, _x.gnss.pDop, _x.gnss.hDop, _x.gnss.vDop, _x.gnss.numSat, _x.gnss.heading, _x.gnss.headingAcc,) = _get_struct_32d().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_32d().pack(_x.imu.dq.w, _x.imu.dq.x, _x.imu.dq.y, _x.imu.dq.z, _x.imu.dv.x, _x.imu.dv.y, _x.imu.dv.z, _x.imu.bGyr.x, _x.imu.bGyr.y, _x.imu.bGyr.z, _x.mag.x, _x.mag.y, _x.mag.z, _x.baro.height, _x.gnss.itow.data, _x.gnss.fix.data, _x.gnss.latitude, _x.gnss.longitude, _x.gnss.hEll, _x.gnss.hMsl, _x.gnss.vel.x, _x.gnss.vel.y, _x.gnss.vel.z, _x.gnss.hAcc, _x.gnss.vAcc, _x.gnss.sAcc, _x.gnss.pDop, _x.gnss.hDop, _x.gnss.vDop, _x.gnss.numSat, _x.gnss.heading, _x.gnss.headingAcc))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.imu is None:
        self.imu = custom_msgs.msg.ImuSensorSample()
      if self.mag is None:
        self.mag = geometry_msgs.msg.Vector3()
      if self.baro is None:
        self.baro = custom_msgs.msg.BaroSensorSample()
      if self.gnss is None:
        self.gnss = custom_msgs.msg.GnssSensorSample()
      end = 0
      _x = self
      start = end
      end += 256
      (_x.imu.dq.w, _x.imu.dq.x, _x.imu.dq.y, _x.imu.dq.z, _x.imu.dv.x, _x.imu.dv.y, _x.imu.dv.z, _x.imu.bGyr.x, _x.imu.bGyr.y, _x.imu.bGyr.z, _x.mag.x, _x.mag.y, _x.mag.z, _x.baro.height, _x.gnss.itow.data, _x.gnss.fix.data, _x.gnss.latitude, _x.gnss.longitude, _x.gnss.hEll, _x.gnss.hMsl, _x.gnss.vel.x, _x.gnss.vel.y, _x.gnss.vel.z, _x.gnss.hAcc, _x.gnss.vAcc, _x.gnss.sAcc, _x.gnss.pDop, _x.gnss.hDop, _x.gnss.vDop, _x.gnss.numSat, _x.gnss.heading, _x.gnss.headingAcc,) = _get_struct_32d().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_32d = None
def _get_struct_32d():
    global _struct_32d
    if _struct_32d is None:
        _struct_32d = struct.Struct("<32d")
    return _struct_32d
