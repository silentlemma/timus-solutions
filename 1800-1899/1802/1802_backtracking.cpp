#include <bitset>
#include <iostream>
#include <string>
#include <vector>

const int FACES = 6, TURNS = 4, AXES = 3, MAX_CELLS = 8000;
typedef std::bitset<MAX_CELLS> Mask;

int n;
std::vector<std::vector<std::vector<int>>> parts;
std::vector<Mask> options[FACES][FACES];  // [part][face], all different
int faceOf[FACES];                         // -1 while a part is unused
Mask chosen[FACES];

// the cell at depth k under row r, column c of a face; every face is the
// bottom one turned by a rotation of the cube, so no part is mirrored
int cellIndex(int face, int r, int c, int k) {
    int last = n - 1;
    const int cells[FACES][AXES] = {{k, r, c},        {last - k, last - r, c},
                                    {r, last - k, c}, {r, k, last - c},
                                    {r, c, k},        {r, last - c, last - k}};
    const int *at = cells[face];
    return (at[0] * n + at[1]) * n + at[2];
}

Mask placement(int p, int face, int turns) {
    Mask mask;
    for (int r = 0; r < n; r++) {
        for (int c = 0; c < n; c++) {
            int rr = r, cc = c;
            for (int t = 0; t < turns; t++) {
                int keep = rr;
                rr = cc;
                cc = n - 1 - keep;
            }
            for (int k = 0; k < parts[p][r][c]; k++) mask.set(cellIndex(face, rr, cc, k));
        }
    }
    return mask;
}

bool solve(const Mask &used, int freeFaces) {
    if (freeFaces == 0) return true;
    // fill next the face with the fewest ways left
    int bestFace = -1;
    std::vector<std::pair<int, int>> best;
    for (int f = 0; f < FACES; f++) {
        if (!(freeFaces >> f & 1)) continue;
        std::vector<std::pair<int, int>> ways;
        for (int p = 0; p < FACES; p++) {
            if (faceOf[p] != -1) continue;
            for (int i = 0; i < (int)options[p][f].size(); i++) {
                if ((options[p][f][i] & used).none()) ways.push_back({p, i});
            }
        }
        if (ways.empty()) return false;
        if (bestFace == -1 || ways.size() < best.size()) {
            bestFace = f;
            best = ways;
        }
    }
    for (auto [p, i] : best) {
        faceOf[p] = bestFace;
        chosen[p] = options[p][bestFace][i];
        if (solve(used | chosen[p], freeFaces & ~(1 << bestFace))) return true;
        faceOf[p] = -1;
    }
    return false;
}

int main() {
    if (!(std::cin >> n)) return 0;
    parts.assign(FACES, std::vector<std::vector<int>>(n, std::vector<int>(n)));
    std::vector<int> volume(FACES, 0);
    for (int p = 0; p < FACES; p++) {
        for (auto &row : parts[p]) {
            for (int &h : row) {
                std::cin >> h;
                volume[p] += h;
            }
        }
    }
    for (int p = 0; p < FACES; p++) {
        for (int f = 0; f < FACES; f++) {
            for (int t = 0; t < TURNS; t++) {
                Mask m = placement(p, f, t);
                bool seen = false;
                for (const Mask &o : options[p][f]) seen = seen || o == m;
                if (!seen) options[p][f].push_back(m);
            }
        }
    }
    // a turn of the whole cube brings the largest part onto face 0 unturned
    int anchor = 0;
    for (int p = 1; p < FACES; p++) {
        if (volume[p] > volume[anchor]) anchor = p;
    }
    for (int p = 0; p < FACES; p++) faceOf[p] = -1;
    faceOf[anchor] = 0;
    chosen[anchor] = placement(anchor, 0, 0);
    if (!solve(chosen[anchor], ((1 << FACES) - 1) & ~1)) {
        std::cout << "No\n";
        return 0;
    }
    std::vector<int> label(n * n * n, 0);
    for (int p = 0; p < FACES; p++) {
        for (int i = 0; i < n * n * n; i++) {
            if (chosen[p][i]) label[i] = p + 1;
        }
    }
    std::string out = "Yes\n";
    for (int row = 0; row < n * n; row++) {
        for (int x = 0; x < n; x++) {
            if (x > 0) out += ' ';
            out += std::to_string(label[row * n + x]);
        }
        out += '\n';
    }
    std::cout << out;
    return 0;
}
