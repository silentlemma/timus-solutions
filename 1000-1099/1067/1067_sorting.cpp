#include <algorithm>
#include <cstdio>
#include <iostream>
#include <string>
#include <vector>

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int count;
    if (!(std::cin >> count))
        return 0;
    std::vector<std::string> paths(count);
    for (auto &path : paths) {
        std::cin >> path;
        // A component terminator sorts before every legal name character.
        std::replace(path.begin(), path.end(), '\\', '\0');
    }
    std::sort(paths.begin(), paths.end());
    const std::string empty;
    const auto *previous = &empty;
    for (const auto &path : paths) {
        const auto shared = static_cast<std::size_t>(
            std::mismatch(path.begin(), path.end(), previous->begin(), previous->end()).first -
            path.begin());
        for (std::size_t begin = 0, depth = 0; begin < path.size(); ++depth) {
            const auto separator = path.find('\0', begin);
            const auto end = separator == std::string::npos ? path.size() : separator;
            if (end > shared || (end < previous->size() && (*previous)[end] != '\0')) {
                for (std::size_t i = 0; i < depth; ++i)
                    std::putchar(' ');
                std::fwrite(path.data() + begin, 1, end - begin, stdout);
                std::putchar('\n');
            }
            begin = end + 1;
        }
        previous = &path;
    }
}
