#include <iostream>
#include <utility>
#include <vector>

constexpr int SPLIT_DIVISOR = 4;

struct Answer {
    bool possible = true;
    std::vector<int> from, to;
};

struct State {
    std::vector<int> volume, previous, following, groups, value_previous, value_following;
    int odd_head = 0, even_head = 0, even_count = 0;
    Answer answer;

    State(int size, int target)
        : volume(size + 1), previous(size + 1), following(size + 1), groups(size + 1),
          value_previous(size + 1), value_following(size + 1) {
        volume[1] = target;
        attach(1);
        if (size != target) {
            volume[2] = size - target;
            attach(2);
        }
    }

    void attach(int index) {
        int value = volume[index], head;
        if (value % 2) {
            head = groups[value];
            if (head == 0) {
                value_previous[value] = 0;
                value_following[value] = odd_head;
                if (odd_head)
                    value_previous[odd_head] = value;
                odd_head = value;
            }
            groups[value] = index;
        } else {
            head = even_head;
            even_head = index;
            ++even_count;
        }
        previous[index] = 0;
        following[index] = head;
        if (head)
            previous[head] = index;
    }

    void detach(int index) {
        int value = volume[index];
        if (value == 0)
            return;
        int before = previous[index], after = following[index];
        if (before)
            following[before] = after;
        else if (value % 2)
            groups[value] = after;
        else
            even_head = after;
        if (after)
            previous[after] = before;
        if (value % 2) {
            if (groups[value] == 0) {
                before = value_previous[value];
                after = value_following[value];
                if (before)
                    value_following[before] = after;
                else
                    odd_head = after;
                if (after)
                    value_previous[after] = before;
            }
        } else
            --even_count;
    }

    void undo(int donor, int receiver) {
        detach(donor);
        detach(receiver);
        int half = volume[receiver] / 2;
        volume[receiver] = half;
        volume[donor] += half;
        attach(donor);
        attach(receiver);
        answer.from.push_back(donor);
        answer.to.push_back(receiver);
    }
};

Answer solve(int n, int k) {
    bool power = (k & (k - 1)) == 0;
    int size = power ? k : k + 1 + (k & 1);
    if (size > n)
        return {false, {}, {}};
    State state(size, k);
    std::vector<int> empty;
    for (int i = 1; i <= size; ++i)
        if (!state.volume[i])
            empty.push_back(i);
    while (state.even_count) {
        int receiver = state.even_head;
        if (state.even_count > 1 || state.volume[receiver] % SPLIT_DIVISOR == 0) {
            int donor = empty.back();
            empty.pop_back();
            state.undo(donor, receiver);
            continue;
        }
        int value = state.odd_head;
        if (value == state.volume[receiver] / 2)
            value = state.value_following[value];
        if (value == 0) {
            int donor = empty.back();
            empty.pop_back();
            state.undo(donor, receiver);
            continue;
        }
        int donor = state.groups[value];
        while (state.volume[receiver] % SPLIT_DIVISOR) {
            state.undo(donor, receiver);
            std::swap(donor, receiver);
        }
    }
    return std::move(state.answer);
}

void write_answer(const Answer &answer) {
    if (!answer.possible) {
        std::cout << "-1\n";
        return;
    }
    std::cout << answer.from.size() << '\n';
    for (std::size_t i = answer.from.size(); i > 0; --i)
        std::cout << answer.from[i - 1] << ' ' << answer.to[i - 1] << '\n';
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int n, k;
    std::cin >> n >> k;
    write_answer(solve(n, k));
}
