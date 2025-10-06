from conan import ConanFile
from conan.tools.cmake import CMake, cmake_layout, CMakeToolchain
from conan.tools.scm import Git


class CinfinityConan(ConanFile):
    name = "cinfinity"
    version = "0.1.0"
    license = "GNU GPLv3"   # or your license
    url = "https://github.com/yourorg/cinfinity"
    description = "MCTS/Chess project with ONNXRuntime, fuzzing, and bindings"
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeDeps", "CMakeToolchain"
    exports_sources = "CMakeLists.txt", "bindings/**", "core/**", "nn/**"
    
    def requirements(self):
        self.settings.compiler.cppstd = "20"

        self.requires("abseil/20240116.1") 
        self.requires("onnxruntime/1.18.1")
        self.requires("pybind11/3.0.1")

    def layout(self):
        cmake_layout(self)

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()