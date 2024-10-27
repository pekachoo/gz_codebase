# generated from ament/cmake/core/templates/nameConfig.cmake.in

# prevent multiple inclusion
if(_gz_codebase_CONFIG_INCLUDED)
  # ensure to keep the found flag the same
  if(NOT DEFINED gz_codebase_FOUND)
    # explicitly set it to FALSE, otherwise CMake will set it to TRUE
    set(gz_codebase_FOUND FALSE)
  elseif(NOT gz_codebase_FOUND)
    # use separate condition to avoid uninitialized variable warning
    set(gz_codebase_FOUND FALSE)
  endif()
  return()
endif()
set(_gz_codebase_CONFIG_INCLUDED TRUE)

# output package information
if(NOT gz_codebase_FIND_QUIETLY)
  message(STATUS "Found gz_codebase: 0.0.0 (${gz_codebase_DIR})")
endif()

# warn when using a deprecated package
if(NOT "" STREQUAL "")
  set(_msg "Package 'gz_codebase' is deprecated")
  # append custom deprecation text if available
  if(NOT "" STREQUAL "TRUE")
    set(_msg "${_msg} ()")
  endif()
  # optionally quiet the deprecation message
  if(NOT ${gz_codebase_DEPRECATED_QUIET})
    message(DEPRECATION "${_msg}")
  endif()
endif()

# flag package as ament-based to distinguish it after being find_package()-ed
set(gz_codebase_FOUND_AMENT_PACKAGE TRUE)

# include all config extra files
set(_extras "")
foreach(_extra ${_extras})
  include("${gz_codebase_DIR}/${_extra}")
endforeach()
