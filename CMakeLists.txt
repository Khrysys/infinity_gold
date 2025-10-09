cmake_minimum_required(VERSION 3.30)

set(CMAKE_CXX_STANDARD 20)
SET(CMAKE_CXX_STANDARD_REQUIRED TRUE)

project(Aleph LANGUAGES CXX)

if(ALEPH_COVERAGE)
    include(cmake/CodeCoverage.cmake)
endif()
