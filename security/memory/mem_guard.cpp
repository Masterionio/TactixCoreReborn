#include <iostream>
#include <fstream>
#include <string>
#include <unistd.h>

void checkMemoryUsage() {
    std::ifstream status("/proc/self/status");
    std::string line;
    while (getline(status, line)) {
        if (line.find("VmRSS") != std::string::npos) {
            std::cout << "[C++] Memory Usage (RAM): " << line << std::endl;
        }
    }
}

int main() {
    std::cout << "[C++] Running memory usage scan..." << std::endl;
    checkMemoryUsage();
    return 0;
}
