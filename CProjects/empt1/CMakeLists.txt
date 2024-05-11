cmake_minimum_required(VERSION 3.28)
project(empt1)

set(CMAKE_CXX_STANDARD 17)

add_executable(empt1 main.cpp
        cmake-build-debug/nose.cpp
        cmake-build-debug/nose.h)
