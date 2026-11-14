#include <cstdio>
#include <iostream>
#include <string>
#include <string_view>
#include <unordered_map>

constexpr unsigned TYPE_BITS = 2;

bool letter(char ch) { return ('a' <= ch && ch <= 'z') || ('A' <= ch && ch <= 'Z'); }

std::string_view word(std::string_view &line) {
    while (!line.empty() && !letter(line.front()))
        line.remove_prefix(1);
    size_t length = 0;
    while (length < line.size() && letter(line[length]))
        ++length;
    auto token = line.substr(0, length);
    line.remove_prefix(length);
    return token;
}

enum Type { Auto, Integer, Real, String };
constexpr const char *TYPES[] = {"auto", "int", "real", "string"};

Type type(std::string_view text) {
    if (text == "int")
        return Integer;
    if (text == "real")
        return Real;
    return text == "string" ? String : Auto;
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::string buffer;
    std::unordered_map<std::string, std::unordered_map<unsigned, Type>> functions;
    std::getline(std::cin, buffer);
    int headers = std::stoi(buffer);
    for (int i = 0; i < headers; ++i) {
        std::getline(std::cin, buffer);
        std::string_view line(buffer);
        std::string name(word(line));
        Type previous = type(word(line));
        unsigned signature = 0;
        for (auto token = word(line); !token.empty(); token = word(line)) {
            signature = (signature << TYPE_BITS) | previous;
            previous = type(token);
        }
        functions[name][signature] = previous;
    }
    std::getline(std::cin, buffer);
    int declarations = std::stoi(buffer);
    std::unordered_map<std::string, Type> variables;
    std::string inferred;
    for (int index = 1; index <= declarations; ++index) {
        std::getline(std::cin, buffer);
        std::string_view line(buffer);
        Type declared = type(word(line));
        std::string name(word(line)), function(word(line));
        const char *error = variables.count(name) ? "Double declaration" : nullptr;
        unsigned signature = 0;
        for (auto token = word(line); !error && !token.empty(); token = word(line)) {
            auto argument = variables.find(std::string(token));
            if (argument == variables.end())
                error = "Unknown variable";
            else
                signature = (signature << TYPE_BITS) | argument->second;
        }
        if (!error) {
            auto overloads = functions.find(function);
            Type result = Auto;
            if (overloads != functions.end()) {
                auto match = overloads->second.find(signature);
                if (match != overloads->second.end())
                    result = match->second;
            }
            if (result == Auto)
                error = "No such function";
            else if (declared != Auto && declared != result)
                error = "Invalid initialization";
            else {
                variables.emplace(name, result);
                if (declared == Auto)
                    inferred.append(name).append(" : ").append(TYPES[result]).push_back('\n');
            }
        }
        if (error) {
            printf("Error on line %d: %s\n", index, error);
            return 0;
        }
    }
    fputs(inferred.c_str(), stdout);
}
