#include <iostream>
#include <sstream>
#include <string>
#include <unordered_map>
#include <vector>

using namespace std;

constexpr size_t CALL_PREFIX = 3;

vector<string> words(string line) {
    for (char& letter : line) {
        bool alphabetic = (letter >= 'a' && letter <= 'z') || (letter >= 'A' && letter <= 'Z');
        if (!alphabetic) letter = ' ';
    }
    istringstream input(line);
    vector<string> result;
    string token;
    while (input >> token) result.push_back(token);
    return result;
}

string signature(const string& name, const vector<string>& arguments) {
    string result = name + ':';
    for (const string& argument : arguments) result += argument + ',';
    return result;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string line;
    getline(cin, line);
    int function_count = stoi(line);
    unordered_map<string, string> functions;
    for (int i = 0; i < function_count; ++i) {
        getline(cin, line);
        auto tokens = words(line);
        vector<string> arguments(tokens.begin() + 1, tokens.end() - 1);
        functions[signature(tokens.front(), arguments)] = tokens.back();
    }
    getline(cin, line);
    int line_count = stoi(line);
    unordered_map<string, string> variables;
    string inferred;
    for (int number = 1; number <= line_count; ++number) {
        getline(cin, line);
        auto tokens = words(line);
        const string& declared = tokens[0];
        const string& name = tokens[1];
        string error;
        vector<string> argument_types;
        if (variables.count(name)) {
            error = "Double declaration";
        } else {
            for (size_t i = CALL_PREFIX; i < tokens.size(); ++i) {
                auto argument = variables.find(tokens[i]);
                if (argument == variables.end()) {
                    error = "Unknown variable";
                    break;
                }
                argument_types.push_back(argument->second);
            }
        }
        if (error.empty()) {
            auto function = functions.find(signature(tokens[2], argument_types));
            if (function == functions.end()) {
                error = "No such function";
            } else if (declared != "auto" && declared != function->second) {
                error = "Invalid initialization";
            } else {
                variables[name] = function->second;
                if (declared == "auto") inferred += name + " : " + function->second + '\n';
            }
        }
        if (!error.empty()) {
            cout << "Error on line " << number << ": " << error << '\n';
            return 0;
        }
    }
    cout << inferred;
}
