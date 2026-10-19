#include <algorithm>
#include <iostream>
#include <vector>

using Integer = long long;
struct Point {
    Integer time, height;
};
using Curve = std::vector<Point>;

Curve contacts_of(const Curve &upper, const Curve &lower, Integer duration) {
    std::size_t i = 0, j = 0;
    Integer time = 0;
    Curve contacts;
    while (true) {
        while (i + 2 < upper.size() && upper[i + 1].time <= time)
            ++i;
        while (j + 2 < lower.size() && lower[j + 1].time <= time)
            ++j;
        Point a = upper[i], b = upper[i + 1], c = lower[j], d = lower[j + 1];
        Integer hn = a.height * (b.time - time) + b.height * (time - a.time);
        Integer gn = c.height * (d.time - time) + d.height * (time - c.time);
        Integer hd = b.time - a.time, gd = d.time - c.time;
        if (hn * gd == gn * hd && 0 < time && time < duration)
            contacts.push_back({time, hn / hd});
        if (time == duration)
            return contacts;
        time = std::min(b.time, d.time);
    }
}

Curve augment(const Curve &curve, const Curve &contacts) {
    Curve result;
    result.reserve(curve.size() + contacts.size());
    std::size_t i = 0, j = 0;
    while (i < curve.size() || j < contacts.size()) {
        if (j == contacts.size() || (i < curve.size() && curve[i].time < contacts[j].time))
            result.push_back(curve[i++]);
        else if (i == curve.size() || contacts[j].time < curve[i].time)
            result.push_back(contacts[j++]);
        else {
            result.push_back(curve[i++]);
            ++j;
        }
    }
    return result;
}

std::vector<Integer> areas(const Curve &curve, const std::vector<Integer> &boundaries) {
    std::vector<Integer> result;
    Integer total = 0;
    std::size_t region = 1;
    for (std::size_t i = 0; i + 1 < curve.size(); ++i) {
        Point a = curve[i], b = curve[i + 1];
        total += (a.height + b.height) * (b.time - a.time);
        if (b.time == boundaries[region]) {
            result.push_back(total);
            total = 0;
            ++region;
        }
    }
    return result;
}

unsigned choose(const std::vector<Integer> &weights) {
    int count = static_cast<int>(weights.size()), left_count = count / 2;
    Integer total = 0;
    for (Integer weight : weights)
        total += weight;
    Integer target = total / 2, scale = Integer(1) << left_count;
    std::vector<Integer> keys{0};
    keys.reserve(std::size_t(1) << left_count);
    for (int bit = 0; bit < left_count; ++bit) {
        Integer step = weights[bit] * scale + (Integer(1) << bit);
        std::size_t old_size = keys.size();
        for (std::size_t i = 0; i < old_size; ++i)
            keys.push_back(keys[i] + step);
    }
    std::sort(keys.begin(), keys.end());
    unsigned previous = 0;
    Integer right_sum = 0;
    for (unsigned index = 0; index < (1U << (count - left_count)); ++index) {
        unsigned gray = index ^ (index >> 1);
        if (index) {
            unsigned changed = gray ^ previous;
            int bit = __builtin_ctz(changed);
            Integer weight = weights[left_count + bit];
            right_sum += (gray & changed) ? weight : -weight;
        }
        previous = gray;
        Integer need = target - right_sum;
        auto found = std::lower_bound(keys.begin(), keys.end(), need * scale);
        if (found != keys.end() && *found / scale == need)
            return static_cast<unsigned>(*found & (scale - 1)) | (gray << left_count);
    }
    return 0;
}

void add(Curve &curve, Point point) {
    if (!curve.empty() && curve.back().time == point.time)
        return;
    while (curve.size() >= 2) {
        Point a = curve[curve.size() - 2], b = curve.back();
        if ((b.height - a.height) * (point.time - b.time) !=
            (point.height - b.height) * (b.time - a.time))
            break;
        curve.pop_back();
    }
    curve.push_back(point);
}

std::vector<Curve> solve(Integer duration, const Curve &original_upper,
                         const Curve &original_lower) {
    Curve contacts = contacts_of(original_upper, original_lower, duration);
    std::vector<Integer> boundaries{0};
    for (Point point : contacts)
        boundaries.push_back(point.time);
    boundaries.push_back(duration);
    Curve upper = augment(original_upper, contacts), lower = augment(original_lower, contacts);
    auto upper_areas = areas(upper, boundaries), lower_areas = areas(lower, boundaries);
    std::vector<Integer> weights;
    for (std::size_t i = 0; i < upper_areas.size(); ++i)
        weights.push_back(upper_areas[i] - lower_areas[i]);
    unsigned mask = choose(weights);
    std::vector<Curve> result(2);
    std::size_t hi = 0, lo = 0;
    for (std::size_t region = 0; region + 1 < boundaries.size(); ++region) {
        int destination = (mask & (1U << region)) ? 0 : 1;
        Integer end = boundaries[region + 1];
        while (hi < upper.size() && upper[hi].time <= end)
            add(result[destination], upper[hi++]);
        while (lo < lower.size() && lower[lo].time <= end)
            add(result[1 - destination], lower[lo++]);
        --hi;
        --lo;
    }
    return result;
}

Curve read_curve() {
    std::size_t count;
    std::cin >> count;
    Curve result(count);
    for (auto &point : result)
        std::cin >> point.time >> point.height;
    return result;
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    Integer duration;
    std::cin >> duration;
    Curve upper = read_curve(), lower = read_curve();
    for (const Curve &curve : solve(duration, upper, lower)) {
        std::cout << curve.size() << '\n';
        for (Point point : curve)
            std::cout << point.time << ' ' << point.height << '\n';
    }
}
