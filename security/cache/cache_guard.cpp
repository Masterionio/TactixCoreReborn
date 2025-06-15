#include <iostream>
#include <filesystem>
#include <fstream>

namespace fs = std::filesystem;

bool isSafeExtension(const std::string& file) {
    return file.ends_with(".tmp") || file.ends_with(".cache") ||
           file.ends_with(".log") || file.ends_with(".txt");
}

int main() {
    std::string cacheDir = "./cache";

    if (!fs::exists(cacheDir)) {
        std::cout << "Cache folder missing." << std::endl;
        return 1;
    }

    for (const auto& entry : fs::directory_iterator(cacheDir)) {
        std::string filename = entry.path().string();
        if (!isSafeExtension(filename)) {
            std::cout << "[!] Suspicious: " << filename << " → Quarantine." << std::endl;
            fs::rename(filename, "./quarantine/" + entry.path().filename().string());
        } else {
            std::cout << "[✓] Safe: " << filename << std::endl;
        }
    }

    return 0;
}
