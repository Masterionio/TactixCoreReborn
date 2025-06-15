#include <iostream>
#include <fstream>
#include <string>

bool isHiddenOrSuspicious(const std::string& name) {
    return name.find("nc") != std::string::npos ||
           name.find("netcat") != std::string::npos ||
           name.find("reverse") != std::string::npos;
}

int main() {
    std::ifstream proc("/proc");
    if (!proc.good()) {
        std::cerr << "Cannot access /proc - skipping process check." << std::endl;
        return 1;
    }

    std::cout << "[SECURITY] Scanning for suspicious processes..." << std::endl;
    system("ps -e > process.txt");

    std::ifstream pfile("process.txt");
    std::string line;
    while (getline(pfile, line)) {
        if (isHiddenOrSuspicious(line)) {
            std::cout << "[!] Suspicious Process: " << line << std::endl;
        }
    }

    return 0;
}
