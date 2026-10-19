#include <cstdint>
#include <cstdio>
#include <vector>

constexpr std::size_t IO_BUFFER_SIZE = 65536;
constexpr std::size_t MAX_QUERIES = 100000;
constexpr std::size_t MAX_CHANGES = 100000;
constexpr int SPACE = ' ';
constexpr int ZERO = '0';

class FastInput {
    char buffer[IO_BUFFER_SIZE];
    std::size_t position = 0;
    std::size_t length = 0;

    int nextByte() {
        if (position == length) {
            length = std::fread(buffer, 1, IO_BUFFER_SIZE, stdin);
            position = 0;
            if (length == 0) {
                return 0;
            }
        }
        return buffer[position++];
    }

  public:
    std::int32_t nextInt() {
        int digit = nextByte();
        while (digit <= SPACE) {
            digit = nextByte();
        }
        std::int32_t value = 0;
        while (digit > SPACE) {
            value = value * 10 + digit - ZERO;
            digit = nextByte();
        }
        return value;
    }
};

class FastOutput {
    char buffer[IO_BUFFER_SIZE];
    std::size_t position = 0;

  public:
    ~FastOutput() { flush(); }

    void flush() {
        std::fwrite(buffer, 1, position, stdout);
        position = 0;
    }

    void put(char character) {
        if (position == IO_BUFFER_SIZE) {
            flush();
        }
        buffer[position++] = character;
    }

    void writeInt(std::int32_t value) {
        char digits[10];
        std::size_t length = 0;
        do {
            digits[length++] = static_cast<char>(ZERO + value % 10);
            value /= 10;
        } while (value != 0);
        while (length != 0) {
            put(digits[--length]);
        }
    }
};

struct Change {
    std::int32_t day;
    std::int32_t count;
    std::int32_t step;
    std::int32_t value;
};

struct Query {
    std::int32_t day;
    std::int32_t next;
};

int main() {
    FastInput input;
    const std::int32_t days = input.nextInt();
    const std::int32_t friends = input.nextInt();
    std::vector<std::int32_t> plan(days);
    for (auto &activity : plan) {
        activity = input.nextInt();
    }

    std::vector<std::int32_t> firstChild(friends + 1, -1);
    std::vector<std::int32_t> nextSibling(friends + 1, -1);
    std::vector<std::int32_t> firstQuery(friends + 1, -1);
    std::vector<std::int32_t> changeBegin(friends + 2, 0);
    std::vector<std::int32_t> answerBegin(friends + 2, 0);
    std::vector<Change> changes;
    std::vector<Query> queries;
    changes.reserve(MAX_CHANGES);
    queries.reserve(MAX_QUERIES);
    std::size_t totalAssignments = 0;

    for (std::int32_t person = 1; person <= friends; ++person) {
        answerBegin[person] = static_cast<std::int32_t>(queries.size());
        const std::int32_t questionCount = input.nextInt();
        for (std::int32_t question = 0; question < questionCount; ++question) {
            const std::int32_t version = input.nextInt();
            const std::int32_t day = input.nextInt() - 1;
            queries.push_back({day, firstQuery[version]});
            firstQuery[version] = static_cast<std::int32_t>(queries.size()) - 1;
        }

        const std::int32_t parent = input.nextInt();
        nextSibling[person] = firstChild[parent];
        firstChild[parent] = person;
        const std::int32_t changeCount = input.nextInt();
        changeBegin[person] = static_cast<std::int32_t>(changes.size());
        for (std::int32_t change = 0; change < changeCount; ++change) {
            const std::int32_t day = input.nextInt() - 1;
            const std::int32_t count = input.nextInt();
            const std::int32_t step = input.nextInt();
            const std::int32_t value = input.nextInt();
            changes.push_back({day, count, step, value});
            totalAssignments += count;
        }
    }
    changeBegin[friends + 1] = static_cast<std::int32_t>(changes.size());
    answerBegin[friends + 1] = static_cast<std::int32_t>(queries.size());

    std::vector<std::int32_t> answers(queries.size());
    std::vector<std::int32_t> history(totalAssignments);
    std::size_t historySize = 0;
    std::vector<std::int32_t> events;
    events.reserve(friends + 1);
    events.push_back(1);

    // Each exit restores all writes in reverse order, including overlapping writes.
    while (!events.empty()) {
        const std::int32_t event = events.back();
        events.pop_back();
        if (event > 0) {
            const std::int32_t version = event - 1;
            for (std::int32_t index = changeBegin[version]; index < changeBegin[version + 1];
                 ++index) {
                const auto &change = changes[index];
                std::int32_t day = change.day;
                for (std::int32_t left = change.count; left != 0; --left) {
                    history[historySize++] = plan[day];
                    plan[day] = change.value;
                    day += change.step;
                }
            }
            for (std::int32_t query = firstQuery[version]; query != -1;
                 query = queries[query].next) {
                answers[query] = plan[queries[query].day];
            }
            events.push_back(-event);
            for (std::int32_t child = firstChild[version]; child != -1;
                 child = nextSibling[child]) {
                events.push_back(child + 1);
            }
        } else {
            const std::int32_t version = -event - 1;
            for (std::int32_t index = changeBegin[version + 1]; index > changeBegin[version];) {
                const auto &change = changes[--index];
                std::int32_t day = change.day + (change.count - 1) * change.step;
                for (std::int32_t left = change.count; left != 0; --left) {
                    plan[day] = history[--historySize];
                    day -= change.step;
                }
            }
        }
    }

    FastOutput output;
    for (std::int32_t person = 1; person <= friends; ++person) {
        for (std::int32_t query = answerBegin[person]; query < answerBegin[person + 1]; ++query) {
            if (query != answerBegin[person]) {
                output.put(' ');
            }
            output.writeInt(answers[query]);
        }
        output.put('\n');
    }
}
