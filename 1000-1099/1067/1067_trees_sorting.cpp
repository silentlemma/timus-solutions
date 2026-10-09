#include <iostream>
#include <map>
#include <sstream>
#include <string>

struct Folder {
    std::map<std::string, Folder> sub;
};

void print(const Folder &f, int depth, std::string &out) {
    for (const auto &[name, child] : f.sub) {
        out.append(depth, ' ');
        out += name;
        out += '\n';
        print(child, depth + 1, out);
    }
}

int main() {
    std::ios::sync_with_stdio(false);
    int n;
    std::cin >> n;
    Folder root;
    for (int i = 0; i < n; i++) {
        std::string path, name;
        std::cin >> path;
        std::istringstream parts(path);
        Folder *cur = &root;
        while (std::getline(parts, name, '\\'))
            cur = &cur->sub[name];
    }
    // the map keeps every folder's subfolders sorted by name
    std::string out;
    print(root, 0, out);
    std::cout << out;
}
