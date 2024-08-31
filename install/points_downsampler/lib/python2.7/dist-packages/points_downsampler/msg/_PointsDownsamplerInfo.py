# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from points_downsampler/PointsDownsamplerInfo.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import std_msgs.msg

class PointsDownsamplerInfo(genpy.Message):
  _md5sum = "a6fc8411fcff551ab66c7910e08a8d14"
  _type = "points_downsampler/PointsDownsamplerInfo"
  _has_header = True  # flag to mark the presence of a Header object
  _full_text = """Header header
string filter_name
float32 measurement_range
int32 original_points_size
int32 filtered_points_size
int32 original_ring_size
int32 filtered_ring_size
float32 exe_time

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
string frame_id
"""
  __slots__ = ['header','filter_name','measurement_range','original_points_size','filtered_points_size','original_ring_size','filtered_ring_size','exe_time']
  _slot_types = ['std_msgs/Header','string','float32','int32','int32','int32','int32','float32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,filter_name,measurement_range,original_points_size,filtered_points_size,original_ring_size,filtered_ring_size,exe_time

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(PointsDownsamplerInfo, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.filter_name is None:
        self.filter_name = ''
      if self.measurement_range is None:
        self.measurement_range = 0.
      if self.original_points_size is None:
        self.original_points_size = 0
      if self.filtered_points_size is None:
        self.filtered_points_size = 0
      if self.original_ring_size is None:
        self.original_ring_size = 0
      if self.filtered_ring_size is None:
        self.filtered_ring_size = 0
      if self.exe_time is None:
        self.exe_time = 0.
    else:
      self.header = std_msgs.msg.Header()
      self.filter_name = ''
      self.measurement_range = 0.
      self.original_points_size = 0
      self.filtered_points_size = 0
      self.original_ring_size = 0
      self.filtered_ring_size = 0
      self.exe_time = 0.

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
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.filter_name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_f4if().pack(_x.measurement_range, _x.original_points_size, _x.filtered_points_size, _x.original_ring_size, _x.filtered_ring_size, _x.exe_time))
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
      if self.header is None:
        self.header = std_msgs.msg.Header()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.filter_name = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.filter_name = str[start:end]
      _x = self
      start = end
      end += 24
      (_x.measurement_range, _x.original_points_size, _x.filtered_points_size, _x.original_ring_size, _x.filtered_ring_size, _x.exe_time,) = _get_struct_f4if().unpack(str[start:end])
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
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.filter_name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_f4if().pack(_x.measurement_range, _x.original_points_size, _x.filtered_points_size, _x.original_ring_size, _x.filtered_ring_size, _x.exe_time))
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
      if self.header is None:
        self.header = std_msgs.msg.Header()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.filter_name = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.filter_name = str[start:end]
      _x = self
      start = end
      end += 24
      (_x.measurement_range, _x.original_points_size, _x.filtered_points_size, _x.original_ring_size, _x.filtered_ring_size, _x.exe_time,) = _get_struct_f4if().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_3I = None
def _get_struct_3I():
    global _struct_3I
    if _struct_3I is None:
        _struct_3I = struct.Struct("<3I")
    return _struct_3I
_struct_f4if = None
def _get_struct_f4if():
    global _struct_f4if
    if _struct_f4if is None:
        _struct_f4if = struct.Struct("<f4if")
    return _struct_f4if
