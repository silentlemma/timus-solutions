#include <algorithm>
#include <cctype>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <map>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

const long long LIMIT = 10000000;

enum Kind { SET, NOT, CALC, END, PRINT, GOTO, IF };

// the operations and comparisons in the order of their codes
enum Calc { ADD, SUB, MUL, DIV, MOD, OR, AND, XOR };
enum Test { EQ, NE, GE, GT, LE, LT };
const vector<string> CALCS = {"+", "-", "*", "/", "%", "or", "and", "xor"};
const vector<string> TESTS = {"==", "!=", ">=", ">", "<=", "<"};

// operands are slots in one value table: variables and constants
struct Op {
    Kind kind;
    int dst = 0, a = 0, b = 0, target = 0, code = 0;
};

int codeOf(const vector<string> &list, const string &op) {
    return find(list.begin(), list.end(), op) - list.begin();
}

string lower(string s) {
    for (char &c : s)
        c = tolower((unsigned char)c);
    return s;
}

long long calc(int code, long long a, long long b) {
    switch (code) {
    case ADD:
        return a + b;
    case SUB:
        return a - b;
    case MUL:
        return a * b;
    case DIV:
        return a / b; // rounds towards zero
    case MOD:
        return (a % b + llabs(b)) % llabs(b); // never negative
    case OR:
        return a | b;
    case AND:
        return a & b;
    }
    return a ^ b;
}

bool test(int code, long long a, long long b) {
    switch (code) {
    case EQ:
        return a == b;
    case NE:
        return a != b;
    case GE:
        return a >= b;
    case GT:
        return a > b;
    case LE:
        return a <= b;
    }
    return a < b;
}

int main() {
    // a line is "label:", "label: command" or "command"; lines with only a label are no commands
    map<string, int> labels;
    vector<vector<string>> commands;
    string line;
    while (getline(cin, line)) {
        istringstream in(line);
        vector<string> t;
        for (string w; in >> w;)
            t.push_back(w);
        if (!t.empty() && t[0].back() == ':') {
            labels[lower(t[0].substr(0, t[0].size() - 1))] = commands.size();
            t.erase(t.begin());
        }
        if (!t.empty())
            commands.push_back(t);
    }
    map<string, int> names;
    vector<long long> values;
    auto operand = [&](const string &tok) {
        bool number = tok.find_first_not_of("-0123456789") == string::npos;
        if (number) {
            values.push_back(stoll(tok));
            return (int)values.size() - 1;
        }
        auto it = names.find(tok);
        if (it != names.end())
            return it->second;
        values.push_back(0);
        return names[tok] = values.size() - 1;
    };
    vector<Op> ops;
    for (auto &t : commands) {
        Op o;
        string head = lower(t[0]);
        if (t.size() > 1 && t[1] == "=") {
            o.dst = operand(t[0]);
            // a value, "not" and a value, or a value, an operation and a value
            vector<string> rest(t.begin() + 2, t.end());
            if (rest.size() == 1) {
                o.kind = SET;
                o.a = operand(rest[0]);
            } else if (rest.size() == 2) {
                o.kind = NOT;
                o.a = operand(rest[1]);
            } else {
                o.kind = CALC;
                o.a = operand(rest[0]);
                o.b = operand(rest[2]);
                o.code = codeOf(CALCS, lower(rest[1]));
            }
        } else if (head == "end") {
            o.kind = END;
        } else if (head == "print") {
            o.kind = PRINT;
            o.a = operand(t[1]);
        } else if (head == "goto") {
            o.kind = GOTO;
            o.target = labels[lower(t[1])];
        } else { // a conditional jump: two values around a comparison, then a label
            vector<string> rest(t.begin() + 1, t.end());
            o.kind = IF;
            o.a = operand(rest[0]);
            o.b = operand(rest[2]);
            o.code = codeOf(TESTS, rest[1]);
            o.target = labels[lower(rest.back())];
        }
        ops.push_back(o);
    }
    vector<bool> assigned(values.size(), false);
    string out;
    int pc = 0, len = ops.size();
    long long executed = 0;
    bool ended = false;
    while (pc < len && executed < LIMIT) {
        const Op &o = ops[pc++];
        executed++;
        switch (o.kind) {
        case SET:
            values[o.dst] = values[o.a];
            assigned[o.dst] = true;
            break;
        case NOT:
            values[o.dst] = ~values[o.a];
            assigned[o.dst] = true;
            break;
        case CALC:
            values[o.dst] = calc(o.code, values[o.a], values[o.b]);
            assigned[o.dst] = true;
            break;
        case END:
            ended = true;
            pc = len;
            break;
        case PRINT:
            out += to_string(values[o.a]) + "\n";
            break;
        case GOTO:
            pc = o.target;
            break;
        case IF:
            if (test(o.code, values[o.a], values[o.b]))
                pc = o.target;
            break;
        }
    }
    if (!ended && executed == LIMIT) {
        // ten million commands done and the program still runs
        out += "Program terminated. Variables state:\n";
        for (auto &[name, k] : names)
            if (assigned[k])
                out += name + ": " + to_string(values[k]) + "\n";
    }
    fputs(out.c_str(), stdout);
}
