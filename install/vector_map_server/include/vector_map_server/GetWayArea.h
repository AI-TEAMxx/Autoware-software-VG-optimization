// Generated by gencpp from file vector_map_server/GetWayArea.msg
// DO NOT EDIT!


#ifndef VECTOR_MAP_SERVER_MESSAGE_GETWAYAREA_H
#define VECTOR_MAP_SERVER_MESSAGE_GETWAYAREA_H

#include <ros/service_traits.h>


#include <vector_map_server/GetWayAreaRequest.h>
#include <vector_map_server/GetWayAreaResponse.h>


namespace vector_map_server
{

struct GetWayArea
{

typedef GetWayAreaRequest Request;
typedef GetWayAreaResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct GetWayArea
} // namespace vector_map_server


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::vector_map_server::GetWayArea > {
  static const char* value()
  {
    return "4b13302b5044d109c446dcf59901a39f";
  }

  static const char* value(const ::vector_map_server::GetWayArea&) { return value(); }
};

template<>
struct DataType< ::vector_map_server::GetWayArea > {
  static const char* value()
  {
    return "vector_map_server/GetWayArea";
  }

  static const char* value(const ::vector_map_server::GetWayArea&) { return value(); }
};


// service_traits::MD5Sum< ::vector_map_server::GetWayAreaRequest> should match
// service_traits::MD5Sum< ::vector_map_server::GetWayArea >
template<>
struct MD5Sum< ::vector_map_server::GetWayAreaRequest>
{
  static const char* value()
  {
    return MD5Sum< ::vector_map_server::GetWayArea >::value();
  }
  static const char* value(const ::vector_map_server::GetWayAreaRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::vector_map_server::GetWayAreaRequest> should match
// service_traits::DataType< ::vector_map_server::GetWayArea >
template<>
struct DataType< ::vector_map_server::GetWayAreaRequest>
{
  static const char* value()
  {
    return DataType< ::vector_map_server::GetWayArea >::value();
  }
  static const char* value(const ::vector_map_server::GetWayAreaRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::vector_map_server::GetWayAreaResponse> should match
// service_traits::MD5Sum< ::vector_map_server::GetWayArea >
template<>
struct MD5Sum< ::vector_map_server::GetWayAreaResponse>
{
  static const char* value()
  {
    return MD5Sum< ::vector_map_server::GetWayArea >::value();
  }
  static const char* value(const ::vector_map_server::GetWayAreaResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::vector_map_server::GetWayAreaResponse> should match
// service_traits::DataType< ::vector_map_server::GetWayArea >
template<>
struct DataType< ::vector_map_server::GetWayAreaResponse>
{
  static const char* value()
  {
    return DataType< ::vector_map_server::GetWayArea >::value();
  }
  static const char* value(const ::vector_map_server::GetWayAreaResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // VECTOR_MAP_SERVER_MESSAGE_GETWAYAREA_H
