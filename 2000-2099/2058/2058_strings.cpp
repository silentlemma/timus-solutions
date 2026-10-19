#include <iostream>
#include <string>
#include <vector>

std::string solve(const std::string &word) {
    int n = static_cast<int>(word.size()), infinity = n + 1;
    std::string data(1, '\0');
    data += word;
    std::vector<int> length(n + 2), link(n + 2), difference(n + 2), series(n + 2);
    std::vector<int> cache_odd(n + 2, infinity), cache_even(n + 2, infinity);
    std::vector<int> odd(n + 1, infinity), even(n + 1, infinity);
    std::vector<int> first(n + 2), next(n + 2), label(n + 2);
    auto lookup = [&](int node, int code) {
        int child = first[node];
        while (child != 0 && label[child] != code)
            child = next[child];
        return child;
    };
    length[0] = -1;
    even[0] = 0;
    int nodes = 2, last = 1;
    std::string output;
    for (int end = 1; end <= n; ++end) {
        int letter = data[end], code = letter - 'a', node = last;
        while (data[end - length[node] - 1] != letter)
            node = link[node];
        int found = lookup(node, code);
        if (found == 0) {
            found = nodes++;
            length[found] = length[node] + 2;
            int suffix = 1;
            if (length[found] != 1) {
                int candidate = link[node];
                while (data[end - length[candidate] - 1] != letter)
                    candidate = link[candidate];
                suffix = lookup(candidate, code);
            }
            link[found] = suffix;
            difference[found] = length[found] - length[suffix];
            series[found] = difference[found] == difference[suffix] ? series[suffix] : suffix;
            next[found] = first[node];
            first[node] = found;
            label[found] = code;
        }
        last = found;
        for (node = last; length[node] > 0; node = series[node]) {
            int suffix = link[node], before = end - length[series[node]] - difference[node];
            cache_odd[node] = odd[before];
            cache_even[node] = even[before];
            if (difference[node] == difference[suffix]) {
                cache_odd[node] = std::min(cache_odd[node], cache_odd[suffix]);
                cache_even[node] = std::min(cache_even[node], cache_even[suffix]);
            }
            odd[end] = std::min(odd[end], cache_even[node] + 1);
            even[end] = std::min(even[end], cache_odd[node] + 1);
        }
        output += std::to_string(odd[end] < infinity ? odd[end] : -1) + " " +
                  std::to_string(even[end] < infinity ? even[end] : -2) + "\n";
    }
    return output;
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::string word;
    std::cin >> word;
    std::cout << solve(word);
}
