#include <algorithm>
#include <array>
#include <cstdio>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <vector>

// front, back, down, up, left, right: face 2a + side lies on axis a
const std::string FACES = "FBDULR";
const int SIDES = 6;
const int AXES = SIDES / 2;
// the axis other than a and b is AXIS_SUM - a - b
const int AXIS_SUM = AXES * (AXES - 1) / 2;
const char INSIDE = '.';
// quarter turns about the vertical and the front-back axis: the face at
// each letter's place comes from the place of the next letter, cyclically
const std::string QUARTER_TURNS[] = {"FLBR", "DLUR"};

using Turn = std::array<int, SIDES>;
using Extents = std::array<int, AXES>;

struct Piece {
    Extents dims;
    std::string colors;
};

// a turn p puts the old face p[k] at place k; the two quarter turns
// generate all 24
std::vector<Turn> rotations() {
    Turn start;
    for (int k = 0; k < SIDES; k++) start[k] = k;
    std::vector<Turn> turns;
    for (const std::string &cycle : QUARTER_TURNS) {
        Turn p = start;
        for (size_t i = 0; i < cycle.size(); i++) {
            p[FACES.find(cycle[i])] = FACES.find(cycle[(i + 1) % cycle.size()]);
        }
        turns.push_back(p);
    }
    std::set<Turn> seen = {start};
    std::vector<Turn> todo = {start};
    while (!todo.empty()) {
        Turn p = todo.back();
        todo.pop_back();
        for (const Turn &q : turns) {
            Turn r;
            for (int k = 0; k < SIDES; k++) r[k] = p[q[k]];
            if (seen.insert(r).second) todo.push_back(r);
        }
    }
    return std::vector<Turn>(seen.begin(), seen.end());
}

// the extents and colours of a turned piece, written as one string
std::string turned(const Turn &p, const Piece &x) {
    std::string s;
    for (int a = 0; a < AXES; a++) s += std::to_string(x.dims[p[2 * a] / 2]) + ",";
    for (int k = 0; k < SIDES; k++) s += x.colors[p[k]];
    return s;
}

int main() {
    std::ios::sync_with_stdio(false);
    Extents size;
    std::string box;
    int n;
    for (int &v : size) std::cin >> v;
    std::cin >> box >> n;
    std::vector<Piece> pieces(n);
    for (auto &x : pieces) {
        for (int &v : x.dims) std::cin >> v;
        std::cin >> x.colors;
    }
    std::vector<Turn> turns = rotations();
    auto canonical = [&](const Piece &x) {
        std::string best = turned(turns[0], x);
        for (const Turn &p : turns) best = std::min(best, turned(p, x));
        return best;
    };
    // the pieces on the edge along an axis carry the two box colours of the
    // faces before it on the other axes; their remaining extents are the
    // sections, the first one also coloured like the start face
    std::array<std::vector<int>, AXES> cuts;
    for (int axis = 0; axis < AXES; axis++) {
        int a = axis == 0 ? 1 : 0, b = AXIS_SUM - axis - a;
        std::vector<int> first, middle, last;
        for (const auto &x : pieces) {
            size_t fa = x.colors.find(box[2 * a]), fb = x.colors.find(box[2 * b]);
            if (fa == std::string::npos || fb == std::string::npos) continue;
            int extent = x.dims[AXIS_SUM - fa / 2 - fb / 2];
            if (x.colors.find(box[2 * axis]) != std::string::npos) {
                first.push_back(extent);
            } else if (x.colors.find(box[2 * axis + 1]) != std::string::npos) {
                last.push_back(extent);
            } else {
                middle.push_back(extent);
            }
        }
        cuts[axis] = first;
        cuts[axis].insert(cuts[axis].end(), middle.begin(), middle.end());
        cuts[axis].insert(cuts[axis].end(), last.begin(), last.end());
    }
    // middle sections may come in any order: the pieces are the same
    std::map<std::string, std::vector<int>> groups;
    for (int i = 0; i < n; i++) groups[canonical(pieces[i])].push_back(i);
    std::vector<std::string> answer(n);
    Extents place, corner = {};
    for (place[0] = 0; place[0] < (int)cuts[0].size(); place[0]++) {
        corner[1] = 0;
        for (place[1] = 0; place[1] < (int)cuts[1].size(); place[1]++) {
            corner[2] = 0;
            for (place[2] = 0; place[2] < (int)cuts[2].size(); place[2]++) {
                Piece want;
                for (int axis = 0; axis < AXES; axis++) {
                    int end = cuts[axis].size() - 1;
                    want.dims[axis] = cuts[axis][place[axis]];
                    want.colors += place[axis] == 0 ? box[2 * axis] : INSIDE;
                    want.colors += place[axis] == end ? box[2 * axis + 1] : INSIDE;
                }
                std::vector<int> &group = groups[canonical(want)];
                int piece = group.back();
                group.pop_back();
                std::string target = turned(turns[0], want);
                for (const Turn &p : turns) {
                    if (turned(p, pieces[piece]) == target) {
                        answer[piece] = std::string(1, FACES[p[0]]) + " " + FACES[p[2]] + " " +
                                        std::to_string(corner[0]) + " " +
                                        std::to_string(corner[1]) + " " +
                                        std::to_string(corner[2]);
                        break;
                    }
                }
                corner[2] += want.dims[2];
            }
            corner[1] += cuts[1][place[1]];
        }
        corner[0] += cuts[0][place[0]];
    }
    for (const auto &line : answer) printf("%s\n", line.c_str());
    return 0;
}
