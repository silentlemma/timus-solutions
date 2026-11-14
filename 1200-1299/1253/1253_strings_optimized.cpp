#include <algorithm>
#include <array>
#include <cstdio>
#include <string>

constexpr int LIMIT = 1000000;
constexpr int TEMPLATE_SLOTS = 10;

struct Template {
    std::string text;
    int length = 0;
    bool active = false;
    bool measured = false;
};

using Templates = std::array<Template, TEMPLATE_SLOTS>;

int measure(Templates &templates, int index) {
    auto &item = templates[index];
    if (item.active)
        return LIMIT + 1;
    if (item.measured)
        return item.length;

    item.active = true;
    for (std::size_t i = 0; i < item.text.size() && item.length <= LIMIT; ++i) {
        if (item.text[i] == '*')
            item.length += measure(templates, item.text[++i] - '0');
        else
            ++item.length;
    }
    item.active = false;
    item.measured = true;
    return item.length = std::min(item.length, LIMIT + 1);
}

void expand(const Templates &templates, int index) {
    const auto &item = templates[index];
    if (item.length == 0)
        return;

    std::size_t start = 0;
    for (std::size_t i = 0; i < item.text.size(); ++i) {
        if (item.text[i] == '*') {
            if (i > start)
                std::fwrite(item.text.data() + start, 1, i - start, stdout);
            expand(templates, item.text[++i] - '0');
            start = i + 1;
        }
    }
    if (start < item.text.size())
        std::fwrite(item.text.data() + start, 1, item.text.size() - start, stdout);
}

int main() {
    int count;
    if (std::scanf("%d", &count) != 1)
        return 0;

    Templates templates;
    int c = std::getchar();
    while (c != '\n' && c != EOF)
        c = std::getchar();
    for (int i = 1; i <= count; ++i) {
        for (c = std::getchar(); c != '#' && c != EOF; c = std::getchar()) {
            if (c != '\r')
                templates[i].text.push_back(static_cast<char>(c));
        }
        c = std::getchar();
        if (c == '\r')
            c = std::getchar();
        if (c != '\n' && c != EOF)
            std::ungetc(c, stdin);
    }
    if (measure(templates, 1) > LIMIT) {
        std::puts("#");
        return 0;
    }
    expand(templates, 1);
    std::putchar('\n');
}
