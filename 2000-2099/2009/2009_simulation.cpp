#include <algorithm>
#include <array>
#include <iostream>
#include <utility>
#include <vector>

struct Group {
    int time;
    std::vector<int> students;
};

void readCase(std::vector<std::vector<int>> &friends, std::vector<Group> &groups) {
    int count, group_count;
    std::cin >> count >> group_count;
    friends.resize(count);
    for (auto &row : friends) {
        int friend_id;
        while (std::cin >> friend_id && friend_id)
            row.push_back(friend_id - 1);
    }
    groups.resize(group_count);
    for (auto &group : groups) {
        int size;
        std::cin >> group.time >> size;
        group.students.resize(size);
        for (int &student : group.students) {
            std::cin >> student;
            --student;
        }
    }
}

std::vector<std::pair<int, int>> solve(const std::vector<std::vector<int>> &friends,
                                       const std::vector<Group> &groups) {
    int count = static_cast<int>(friends.size());
    std::array<std::vector<int>, 2> queues;
    std::array<int, 2> next_completion{};
    std::vector<int> which(count, -1), position(count, -1);
    std::vector<std::pair<int, int>> answer(count);
    for (const auto &group : groups) {
        int now = group.time;
        for (int side = 0; side < 2; ++side) {
            auto &queue = queues[side];
            if (queue.empty() || next_completion[side] > now)
                continue;
            int served = std::min(static_cast<int>(queue.size()), now - next_completion[side] + 1);
            for (int at = 0; at < served; ++at) {
                answer[queue[at]] = {next_completion[side] + at, side};
                which[queue[at]] = -1;
            }
            queue.erase(queue.begin(), queue.begin() + served);
            for (int at = 0; at < static_cast<int>(queue.size()); ++at)
                position[queue[at]] = at;
            next_completion[side] = queue.empty() ? 0 : next_completion[side] + served;
        }
        for (int student : group.students) {
            std::array<int, 2> best{static_cast<int>(queues[0].size()),
                                    static_cast<int>(queues[1].size())};
            for (int friend_id : friends[student]) {
                int side = which[friend_id];
                if (side >= 0)
                    best[side] = std::min(best[side], position[friend_id] + 1);
            }
            int side = best[0] < best[1] ? 0 : 1;
            auto &queue = queues[side];
            int at = best[side];
            queue.insert(queue.begin() + at, student);
            which[student] = side;
            for (int index = at; index < static_cast<int>(queue.size()); ++index)
                position[queue[index]] = index;
            if (queue.size() == 1)
                next_completion[side] = now + 1;
        }
    }
    for (int side = 0; side < 2; ++side)
        for (int at = 0; at < static_cast<int>(queues[side].size()); ++at)
            answer[queues[side][at]] = {next_completion[side] + at, side};
    return answer;
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::vector<std::vector<int>> friends;
    std::vector<Group> groups;
    readCase(friends, groups);
    for (auto [time, side] : solve(friends, groups))
        std::cout << time << ' ' << (side ? "right" : "left") << '\n';
}
