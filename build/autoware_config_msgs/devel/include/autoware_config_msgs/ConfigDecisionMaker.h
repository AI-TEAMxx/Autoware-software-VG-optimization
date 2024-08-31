// Generated by gencpp from file autoware_config_msgs/ConfigDecisionMaker.msg
// DO NOT EDIT!


#ifndef AUTOWARE_CONFIG_MSGS_MESSAGE_CONFIGDECISIONMAKER_H
#define AUTOWARE_CONFIG_MSGS_MESSAGE_CONFIGDECISIONMAKER_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <std_msgs/Header.h>

namespace autoware_config_msgs
{
template <class ContainerAllocator>
struct ConfigDecisionMaker_
{
  typedef ConfigDecisionMaker_<ContainerAllocator> Type;

  ConfigDecisionMaker_()
    : header()
    , auto_mission_reload(false)
    , auto_engage(false)
    , auto_mission_change(false)
    , use_fms(false)
    , disuse_vector_map(false)
    , num_of_steer_behind(0)
    , change_threshold_dist(0.0)
    , change_threshold_angle(0.0)
    , goal_threshold_dist(0.0)
    , goal_threshold_vel(0.0)
    , stopped_vel(0.0)  {
    }
  ConfigDecisionMaker_(const ContainerAllocator& _alloc)
    : header(_alloc)
    , auto_mission_reload(false)
    , auto_engage(false)
    , auto_mission_change(false)
    , use_fms(false)
    , disuse_vector_map(false)
    , num_of_steer_behind(0)
    , change_threshold_dist(0.0)
    , change_threshold_angle(0.0)
    , goal_threshold_dist(0.0)
    , goal_threshold_vel(0.0)
    , stopped_vel(0.0)  {
  (void)_alloc;
    }



   typedef  ::std_msgs::Header_<ContainerAllocator>  _header_type;
  _header_type header;

   typedef uint8_t _auto_mission_reload_type;
  _auto_mission_reload_type auto_mission_reload;

   typedef uint8_t _auto_engage_type;
  _auto_engage_type auto_engage;

   typedef uint8_t _auto_mission_change_type;
  _auto_mission_change_type auto_mission_change;

   typedef uint8_t _use_fms_type;
  _use_fms_type use_fms;

   typedef uint8_t _disuse_vector_map_type;
  _disuse_vector_map_type disuse_vector_map;

   typedef uint32_t _num_of_steer_behind_type;
  _num_of_steer_behind_type num_of_steer_behind;

   typedef double _change_threshold_dist_type;
  _change_threshold_dist_type change_threshold_dist;

   typedef double _change_threshold_angle_type;
  _change_threshold_angle_type change_threshold_angle;

   typedef double _goal_threshold_dist_type;
  _goal_threshold_dist_type goal_threshold_dist;

   typedef double _goal_threshold_vel_type;
  _goal_threshold_vel_type goal_threshold_vel;

   typedef double _stopped_vel_type;
  _stopped_vel_type stopped_vel;





  typedef boost::shared_ptr< ::autoware_config_msgs::ConfigDecisionMaker_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::autoware_config_msgs::ConfigDecisionMaker_<ContainerAllocator> const> ConstPtr;

}; // struct ConfigDecisionMaker_

typedef ::autoware_config_msgs::ConfigDecisionMaker_<std::allocator<void> > ConfigDecisionMaker;

typedef boost::shared_ptr< ::autoware_config_msgs::ConfigDecisionMaker > ConfigDecisionMakerPtr;
typedef boost::shared_ptr< ::autoware_config_msgs::ConfigDecisionMaker const> ConfigDecisionMakerConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::autoware_config_msgs::ConfigDecisionMaker_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::autoware_config_msgs::ConfigDecisionMaker_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::autoware_config_msgs::ConfigDecisionMaker_<ContainerAllocator1> & lhs, const ::autoware_config_msgs::ConfigDecisionMaker_<ContainerAllocator2> & rhs)
{
  return lhs.header == rhs.header &&
    lhs.auto_mission_reload == rhs.auto_mission_reload &&
    lhs.auto_engage == rhs.auto_engage &&
    lhs.auto_mission_change == rhs.auto_mission_change &&
    lhs.use_fms == rhs.use_fms &&
    lhs.disuse_vector_map == rhs.disuse_vector_map &&
    lhs.num_of_steer_behind == rhs.num_of_steer_behind &&
    lhs.change_threshold_dist == rhs.change_threshold_dist &&
    lhs.change_threshold_angle == rhs.change_threshold_angle &&
    lhs.goal_threshold_dist == rhs.goal_threshold_dist &&
    lhs.goal_threshold_vel == rhs.goal_threshold_vel &&
    lhs.stopped_vel == rhs.stopped_vel;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::autoware_config_msgs::ConfigDecisionMaker_<ContainerAllocator1> & lhs, const ::autoware_config_msgs::ConfigDecisionMaker_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace autoware_config_msgs

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::autoware_config_msgs::ConfigDecisionMaker_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::autoware_config_msgs::ConfigDecisionMaker_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::autoware_config_msgs::ConfigDecisionMaker_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::autoware_config_msgs::ConfigDecisionMaker_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::autoware_config_msgs::ConfigDecisionMaker_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::autoware_config_msgs::ConfigDecisionMaker_<ContainerAllocator> const>
  : TrueType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::autoware_config_msgs::ConfigDecisionMaker_<ContainerAllocator> >
{
  static const char* value()
  {
    return "adfaf802f5ca35bf03b4eb5191ba9782";
  }

  static const char* value(const ::autoware_config_msgs::ConfigDecisionMaker_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xadfaf802f5ca35bfULL;
  static const uint64_t static_value2 = 0x03b4eb5191ba9782ULL;
};

template<class ContainerAllocator>
struct DataType< ::autoware_config_msgs::ConfigDecisionMaker_<ContainerAllocator> >
{
  static const char* value()
  {
    return "autoware_config_msgs/ConfigDecisionMaker";
  }

  static const char* value(const ::autoware_config_msgs::ConfigDecisionMaker_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::autoware_config_msgs::ConfigDecisionMaker_<ContainerAllocator> >
{
  static const char* value()
  {
    return "Header header\n"
"bool auto_mission_reload\n"
"bool auto_engage\n"
"bool auto_mission_change\n"
"bool use_fms\n"
"bool disuse_vector_map\n"
"uint32 num_of_steer_behind\n"
"float64 change_threshold_dist\n"
"float64 change_threshold_angle\n"
"float64 goal_threshold_dist\n"
"float64 goal_threshold_vel\n"
"float64 stopped_vel\n"
"\n"
"================================================================================\n"
"MSG: std_msgs/Header\n"
"# Standard metadata for higher-level stamped data types.\n"
"# This is generally used to communicate timestamped data \n"
"# in a particular coordinate frame.\n"
"# \n"
"# sequence ID: consecutively increasing ID \n"
"uint32 seq\n"
"#Two-integer timestamp that is expressed as:\n"
"# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')\n"
"# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')\n"
"# time-handling sugar is provided by the client library\n"
"time stamp\n"
"#Frame this data is associated with\n"
"string frame_id\n"
;
  }

  static const char* value(const ::autoware_config_msgs::ConfigDecisionMaker_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::autoware_config_msgs::ConfigDecisionMaker_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.header);
      stream.next(m.auto_mission_reload);
      stream.next(m.auto_engage);
      stream.next(m.auto_mission_change);
      stream.next(m.use_fms);
      stream.next(m.disuse_vector_map);
      stream.next(m.num_of_steer_behind);
      stream.next(m.change_threshold_dist);
      stream.next(m.change_threshold_angle);
      stream.next(m.goal_threshold_dist);
      stream.next(m.goal_threshold_vel);
      stream.next(m.stopped_vel);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct ConfigDecisionMaker_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::autoware_config_msgs::ConfigDecisionMaker_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::autoware_config_msgs::ConfigDecisionMaker_<ContainerAllocator>& v)
  {
    s << indent << "header: ";
    s << std::endl;
    Printer< ::std_msgs::Header_<ContainerAllocator> >::stream(s, indent + "  ", v.header);
    s << indent << "auto_mission_reload: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.auto_mission_reload);
    s << indent << "auto_engage: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.auto_engage);
    s << indent << "auto_mission_change: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.auto_mission_change);
    s << indent << "use_fms: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.use_fms);
    s << indent << "disuse_vector_map: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.disuse_vector_map);
    s << indent << "num_of_steer_behind: ";
    Printer<uint32_t>::stream(s, indent + "  ", v.num_of_steer_behind);
    s << indent << "change_threshold_dist: ";
    Printer<double>::stream(s, indent + "  ", v.change_threshold_dist);
    s << indent << "change_threshold_angle: ";
    Printer<double>::stream(s, indent + "  ", v.change_threshold_angle);
    s << indent << "goal_threshold_dist: ";
    Printer<double>::stream(s, indent + "  ", v.goal_threshold_dist);
    s << indent << "goal_threshold_vel: ";
    Printer<double>::stream(s, indent + "  ", v.goal_threshold_vel);
    s << indent << "stopped_vel: ";
    Printer<double>::stream(s, indent + "  ", v.stopped_vel);
  }
};

} // namespace message_operations
} // namespace ros

#endif // AUTOWARE_CONFIG_MSGS_MESSAGE_CONFIGDECISIONMAKER_H
