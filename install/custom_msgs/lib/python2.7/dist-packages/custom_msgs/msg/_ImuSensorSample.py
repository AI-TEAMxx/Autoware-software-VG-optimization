# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from custom_msgs/ImuSensorSample.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import custom_msgs.msg
import geometry_msgs.msg

class ImuSensorSample(genpy.Message):
  _md5sum = "4cafe678792d03390e2d87979096a4f3"
  _type = "custom_msgs/ImuSensorSample"
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
float64 z"""
  __slots__ = ['dq','dv','bGyr']
  _slot_types = ['custom_msgs/XsensQuaternion','geometry_msgs/Vector3','geometry_msgs/Vector3']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       dq,dv,bGyr

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(ImuSensorSample, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.dq is None:
        self.dq = custom_msgs.msg.XsensQuaternion()
      if self.dv is None:
        self.dv = geometry_msgs.msg.Vector3()
      if self.bGyr is None:
        self.bGyr = geometry_msgs.msg.Vector3()
    else:
      self.dq = custom_msgs.msg.XsensQuaternion()
      self.dv = geometry_msgs.msg.Vector3()
      self.bGyr = geometry_msgs.msg.Vector3()

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
      buff.write(_get_struct_10d().pack(_x.dq.w, _x.dq.x, _x.dq.y, _x.dq.z, _x.dv.x, _x.dv.y, _x.dv.z, _x.bGyr.x, _x.bGyr.y, _x.bGyr.z))
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
      if self.dq is None:
        self.dq = custom_msgs.msg.XsensQuaternion()
      if self.dv is None:
        self.dv = geometry_msgs.msg.Vector3()
      if self.bGyr is None:
        self.bGyr = geometry_msgs.msg.Vector3()
      end = 0
      _x = self
      start = end
      end += 80
      (_x.dq.w, _x.dq.x, _x.dq.y, _x.dq.z, _x.dv.x, _x.dv.y, _x.dv.z, _x.bGyr.x, _x.bGyr.y, _x.bGyr.z,) = _get_struct_10d().unpack(str[start:end])
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
      buff.write(_get_struct_10d().pack(_x.dq.w, _x.dq.x, _x.dq.y, _x.dq.z, _x.dv.x, _x.dv.y, _x.dv.z, _x.bGyr.x, _x.bGyr.y, _x.bGyr.z))
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
      if self.dq is None:
        self.dq = custom_msgs.msg.XsensQuaternion()
      if self.dv is None:
        self.dv = geometry_msgs.msg.Vector3()
      if self.bGyr is None:
        self.bGyr = geometry_msgs.msg.Vector3()
      end = 0
      _x = self
      start = end
      end += 80
      (_x.dq.w, _x.dq.x, _x.dq.y, _x.dq.z, _x.dv.x, _x.dv.y, _x.dv.z, _x.bGyr.x, _x.bGyr.y, _x.bGyr.z,) = _get_struct_10d().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_10d = None
def _get_struct_10d():
    global _struct_10d
    if _struct_10d is None:
        _struct_10d = struct.Struct("<10d")
    return _struct_10d
