#include <algorithm>
#include <cstdint>
#include <cstdio>
#include <cstring>

constexpr int MAX_LENGTH = 100000;
constexpr int BUFFER_SIZE = 65536;
constexpr int DECIMAL = 10;
static char word[MAX_LENGTH], reversed[MAX_LENGTH];
static unsigned char buffer[BUFFER_SIZE];
static int position, available;

int next_byte() {
    if (position == available) {
        available = static_cast<int>(std::fread(buffer, 1, sizeof buffer, stdin));
        position = 0;
        if (available == 0)
            return EOF;
    }
    return buffer[position++];
}

int start_token() {
    int ch = next_byte();
    while (ch != EOF && ch <= ' ')
        ch = next_byte();
    return ch;
}

int next_int() {
    int value = 0;
    for (int ch = start_token(); ch >= '0' && ch <= '9'; ch = next_byte())
        value = value * DECIMAL + ch - '0';
    return value;
}

constexpr int IO_SIZE = 16384, DECIMAL_DIGITS = 16;
class Output {
    char data[IO_SIZE];
    int size = 0;

  public:
    void flush() {
        std::fwrite(data, 1, size, stdout);
        size = 0;
    }
    void byte(char c) {
        if (size == IO_SIZE)
            flush();
        data[size++] = c;
    }
    void number(unsigned value) {
        char digits[DECIMAL_DIGITS];
        int count = 0;
        do {
            digits[count++] = '0' + value % 10;
            value /= 10;
        } while (value);
        while (count)
            byte(digits[--count]);
    }
};

constexpr int HASH_BLOCK = 64;
constexpr int HASH_LEAVES = 2048;
constexpr std::uint64_t HASH_BASE = 131;
struct HashNode {
    std::uint64_t forward = 0, backward = 0;
    int length = 0;
};
static HashNode hash_tree[2 * HASH_LEAVES];
static std::uint64_t short_powers[HASH_BLOCK + 1];
static std::uint64_t block_powers[(MAX_LENGTH + HASH_BLOCK - 1) / HASH_BLOCK + 1];

std::uint64_t hash_power(int length) {
    return block_powers[length / HASH_BLOCK] * short_powers[length % HASH_BLOCK];
}
HashNode concatenate(HashNode a, HashNode b) {
    return {a.forward * hash_power(b.length) + b.forward,
            b.backward * hash_power(a.length) + a.backward, a.length + b.length};
}
HashNode hash_chars(int left, int end) {
    HashNode answer;
    answer.length = end - left;
    for (int i = 0; i < answer.length; ++i) {
        answer.forward = answer.forward * HASH_BASE + static_cast<unsigned char>(word[left + i]);
        answer.backward =
            answer.backward * HASH_BASE + static_cast<unsigned char>(word[end - 1 - i]);
    }
    return answer;
}
void initialize_hash(int size) {
    short_powers[0] = block_powers[0] = 1;
    for (int i = 1; i <= HASH_BLOCK; ++i)
        short_powers[i] = short_powers[i - 1] * HASH_BASE;
    for (int i = 1; i <= (MAX_LENGTH + HASH_BLOCK - 1) / HASH_BLOCK; ++i)
        block_powers[i] = block_powers[i - 1] * short_powers[HASH_BLOCK];
    for (int block = 0; block * HASH_BLOCK < size; ++block)
        hash_tree[HASH_LEAVES + block] =
            hash_chars(block * HASH_BLOCK, std::min(size, (block + 1) * HASH_BLOCK));
    for (int node = HASH_LEAVES - 1; node > 0; --node)
        hash_tree[node] = concatenate(hash_tree[2 * node], hash_tree[2 * node + 1]);
}
void update_hash(int position, int size) {
    const int block = position / HASH_BLOCK;
    int node = HASH_LEAVES + block;
    hash_tree[node] = hash_chars(block * HASH_BLOCK, std::min(size, (block + 1) * HASH_BLOCK));
    for (node /= 2; node > 0; node /= 2)
        hash_tree[node] = concatenate(hash_tree[2 * node], hash_tree[2 * node + 1]);
}
HashNode hash_blocks(int first, int end) {
    HashNode before, after;
    for (first += HASH_LEAVES, end += HASH_LEAVES; first < end; first /= 2, end /= 2) {
        if (first % 2)
            before = concatenate(before, hash_tree[first++]);
        if (end % 2)
            after = concatenate(hash_tree[--end], after);
    }
    return concatenate(before, after);
}
HashNode range_hash(int left, int end) {
    HashNode answer;
    if (left % HASH_BLOCK) {
        const int stop = std::min(end, (left / HASH_BLOCK + 1) * HASH_BLOCK);
        answer = hash_chars(left, stop);
        left = stop;
    }
    if (left == end)
        return answer;
    answer = concatenate(answer, hash_blocks(left / HASH_BLOCK, end / HASH_BLOCK));
    const int tail = end / HASH_BLOCK * HASH_BLOCK;
    if (tail < end)
        answer = concatenate(answer, hash_chars(tail, end));
    return answer;
}

constexpr unsigned CACHE_SIZE = 2048, CACHE_SHIFT = 21, HASH_MULTIPLIER = 2654435761U;
constexpr int CACHE_MIN_LENGTH = 64;
struct Proof {
    int center = 0, left = 0, right = 0;
    unsigned version = 0;
    bool palindrome = false;
};
static Proof proofs[CACHE_SIZE];
static unsigned version;

constexpr int WORD_BITS = 64;
constexpr int BOUNDARY_WORDS = (MAX_LENGTH + WORD_BITS - 1) / WORD_BITS;
constexpr int SUMMARY_WORDS = (BOUNDARY_WORDS + WORD_BITS - 1) / WORD_BITS;
static std::uint64_t boundaries[BOUNDARY_WORDS], summary[SUMMARY_WORDS], nonempty;

void set_boundary(int index, bool different) {
    const int word_index = index / WORD_BITS;
    const std::uint64_t bit = std::uint64_t{1} << (index % WORD_BITS);
    if (different)
        boundaries[word_index] |= bit;
    else
        boundaries[word_index] &= ~bit;
    const int group = word_index / WORD_BITS;
    const std::uint64_t group_bit = std::uint64_t{1} << (word_index % WORD_BITS);
    if (boundaries[word_index])
        summary[group] |= group_bit;
    else
        summary[group] &= ~group_bit;
    if (summary[group])
        nonempty |= std::uint64_t{1} << group;
    else
        nonempty &= ~(std::uint64_t{1} << group);
}

int next_boundary(int index) {
    if (index >= MAX_LENGTH)
        return MAX_LENGTH;
    int word_index = index / WORD_BITS;
    std::uint64_t bits = boundaries[word_index] & (~std::uint64_t{0} << (index % WORD_BITS));
    if (bits)
        return word_index * WORD_BITS + __builtin_ctzll(bits);
    ++word_index;
    int group = word_index / WORD_BITS;
    bits = summary[group] & (~std::uint64_t{0} << (word_index % WORD_BITS));
    if (!bits) {
        const int after = group + 1;
        bits = after < WORD_BITS ? nonempty & (~std::uint64_t{0} << after) : 0;
        if (!bits)
            return MAX_LENGTH;
        group = __builtin_ctzll(bits);
        bits = summary[group];
    }
    word_index = group * WORD_BITS + __builtin_ctzll(bits);
    return word_index * WORD_BITS + __builtin_ctzll(boundaries[word_index]);
}

constexpr unsigned SCAN_FACTOR = 16;
static std::uint16_t odd_radius[MAX_LENGTH], even_radius[MAX_LENGTH];
static std::uint64_t scanned;
static unsigned radius_version;
static bool radii_ready;

void build_radii(int size) {
    int left = 0, right = -1;
    for (int center = 0; center < size; ++center) {
        int reach = center > right
                        ? 1
                        : std::min<int>(odd_radius[left + right - center], right - center + 1);
        while (center - reach >= 0 && center + reach < size &&
               word[center - reach] == word[center + reach])
            ++reach;
        odd_radius[center] = static_cast<std::uint16_t>(reach);
        if (center + reach - 1 > right) {
            left = center - reach + 1;
            right = center + reach - 1;
        }
    }
    left = 0;
    right = -1;
    for (int center = 0; center < size; ++center) {
        int reach = center > right
                        ? 0
                        : std::min<int>(even_radius[left + right - center + 1], right - center + 1);
        while (center - reach - 1 >= 0 && center + reach < size &&
               word[center - reach - 1] == word[center + reach])
            ++reach;
        even_radius[center] = static_cast<std::uint16_t>(reach);
        if (center + reach - 1 > right) {
            left = center - reach;
            right = center + reach - 1;
        }
    }
    radius_version = version;
    radii_ready = true;
}

void account_scan(int compared, int size) {
    scanned += static_cast<unsigned>(compared);
    // A static epoch earns its linear preprocessing after enough exact scans.
    // With n <= 100000 both kinds of radius are at most 50000, so uint16 fits.
    if (scanned >= std::uint64_t{SCAN_FACTOR} * size)
        build_radii(size);
}

int mismatch_offset(const char *first, const char *second, int length) {
    constexpr int SMALL_SCAN = 8;
    int offset = 0;
    // The current range is unequal; every equal left half can be skipped.
    while (length > SMALL_SCAN) {
        const int half = length / 2;
        if (std::memcmp(first + offset, second + offset, half) == 0) {
            offset += half;
            length -= half;
        } else
            length = half;
    }
    const auto witness = std::mismatch(first + offset, first + offset + length, second + offset);
    return static_cast<int>(witness.first - first);
}
struct HotInterval {
    int center = 0, left = 0, right = 0, mismatches = 0;
};
static HotInterval hot;

bool palindrome(int left, int end, int size, int half) {
    if (word[left] != word[end - 1])
        return false;
    if (radii_ready && radius_version == version) {
        const int length = end - left;
        return length % 2 ? odd_radius[(left + end - 1) / 2] >= length / 2 + 1
                          : even_radius[(left + end) / 2] >= length / 2;
    }
    if (end - left < CACHE_MIN_LENGTH)
        return std::memcmp(word + left, reversed + size - end, half) == 0;
    const int center = left + end;
    if (hot.center == center && hot.mismatches == 0 && hot.left <= left && hot.right >= end - 1)
        return true;
    // No unequal adjacent letters inside the interval means a uniform palindrome.
    if (next_boundary(left + 1) >= end)
        return true;
    Proof &entry = proofs[(static_cast<unsigned>(center) * HASH_MULTIPLIER) >> CACHE_SHIFT];
    if (entry.center == center) {
        if (entry.palindrome) {
            // A matching version certifies no actual assignment anywhere since this proof.
            if (entry.version == version && entry.left <= left && entry.right >= end - 1) {
                hot = {center, entry.left, entry.right, 0};
                return true;
            }
        } else if (entry.left >= left && entry.right < end &&
                   word[entry.left] != word[entry.right]) {
            // The same mirrored unequal pair refutes every containing interval at this center.
            return false;
        }
    }
    // Unequal polynomial hashes prove inequality; equality NEVER proves a palindrome.
    // Collisions only fall through to the unchanged exact comparison/certificates.
    const HashNode hash = range_hash(left, end);
    if (hash.forward != hash.backward)
        return false;
    if (std::memcmp(word + left, reversed + size - end, half) == 0) {
        entry = {center, left, end - 1, version, true};
        hot = {center, left, end - 1, 0};
        account_scan(half, size);
        return true;
    }
    const int offset = mismatch_offset(word + left, reversed + size - end, half);
    account_scan(offset + 1, size);
    entry = {center, left + offset, end - 1 - offset, version, false};
    return false;
}

void track_change(int position, char value) {
    if (hot.center && hot.left <= position && position <= hot.right) {
        const int mirror = hot.left + hot.right - position;
        // Each pair is counted once; updating its other endpoint adjusts the same count.
        if (mirror != position)
            hot.mismatches += (value != word[mirror]) - (word[position] != word[mirror]);
    }
    ++version;
    scanned = 0;
}

int main() {
    Output output;
    int size = 0;
    for (int ch = start_token(); ch > ' '; ch = next_byte())
        word[size++] = static_cast<char>(ch);
    initialize_hash(size);
    int changes = 0;
    for (int i = 0; i < size; ++i) {
        reversed[size - 1 - i] = word[i];
        if (i > 0 && word[i - 1] != word[i]) {
            ++changes;
            set_boundary(i, true);
        }
    }
    for (int count = next_int(); count > 0; --count) {
        const bool update = start_token() == 'c';
        for (int ch = next_byte(); ch > ' '; ch = next_byte()) {
        }
        const int left = next_int() - 1;
        if (update) {
            const char value = static_cast<char>(start_token());
            if (word[left] != value) {
                track_change(left, value);
                if (left > 0) {
                    changes += (word[left - 1] != value) - (word[left - 1] != word[left]);
                    set_boundary(left, word[left - 1] != value);
                }
                if (left + 1 < size) {
                    changes += (word[left + 1] != value) - (word[left + 1] != word[left]);
                    set_boundary(left + 1, word[left + 1] != value);
                }
                word[left] = reversed[size - 1 - left] = value;
                update_hash(left, size);
            }
        } else {
            const int end = next_int();
            const int half = (end - left) / 2;
            const bool answer_yes = half == 0 || changes == 0 || palindrome(left, end, size, half);
            const char *answer = answer_yes ? "Yes\n" : "No\n";
            while (*answer)
                output.byte(*answer++);
        }
    }
    output.flush();
}
