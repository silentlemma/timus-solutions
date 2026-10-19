#include <cstdint>
#include <iostream>
#include <sstream>
#include <string>
#include <unordered_map>
#include <vector>

constexpr int INTEGER = -1;
constexpr int STRING = -2;
constexpr int HEX_BASE = 16;
constexpr int BYTE_BITS = 8;
constexpr int WORD_BYTES = 4;

struct Schema {
    std::string name;
    std::vector<int> fields;
};

struct Frame {
    int type;
    std::size_t next;
};

int hex_digit(char ch) { return ch <= '9' ? ch - '0' : ch - 'A' + 10; }

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int count, lines;
    std::cin >> count >> lines;
    std::string line;
    std::getline(std::cin, line);
    std::vector<Schema> schemas;
    schemas.reserve(count);
    std::unordered_map<std::string, int> types = {{"int", INTEGER}, {"string", STRING}};
    for (int i = 0; i < lines; ++i) {
        std::getline(std::cin, line);
        std::istringstream description(line);
        std::string type;
        description >> type;
        if (type == "struct") {
            std::string name;
            description >> name;
            types[name] = static_cast<int>(schemas.size());
            schemas.push_back({name, {}});
        } else {
            schemas.back().fields.push_back(types.at(type));
        }
    }

    std::string hex;
    std::cin >> hex;
    std::string data;
    data.reserve(hex.size() / 2);
    for (std::size_t i = 0; i < hex.size(); i += 2) {
        data.push_back(static_cast<char>(hex_digit(hex[i]) * HEX_BASE + hex_digit(hex[i + 1])));
    }
    std::size_t position = 0;
    auto read_word = [&]() {
        std::uint32_t value = 0;
        for (int i = 0; i < WORD_BYTES; ++i) {
            value = (value << BYTE_BITS) | static_cast<unsigned char>(data[position++]);
        }
        return value;
    };

    std::vector<Frame> stack;
    stack.reserve(count);
    while (position < data.size()) {
        int root = static_cast<int>(read_word()) - 1;
        std::cout << schemas[root].name << '\n';
        stack.push_back({root, 0});
        while (!stack.empty()) {
            Frame &frame = stack.back();
            const auto &fields = schemas[frame.type].fields;
            if (frame.next == fields.size()) {
                stack.pop_back();
                continue;
            }
            int type = fields[frame.next++];
            std::cout << std::string(stack.size(), ' ');
            if (type == INTEGER) {
                std::cout << "int " << read_word() << '\n';
            } else if (type == STRING) {
                std::size_t length = read_word();
                std::cout << "string " << data.substr(position, length) << '\n';
                position += length;
            } else {
                std::cout << schemas[type].name << '\n';
                stack.push_back({type, 0});
            }
        }
    }
}
