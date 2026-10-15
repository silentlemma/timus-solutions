#include <algorithm>
#include <array>
#include <cmath>
#include <cstdio>
#include <tuple>
#include <vector>

const int DIM = 3;
typedef std::array<double, DIM> Vec;
typedef std::array<Vec, DIM> Frame;
typedef std::array<long long, DIM> Int3;
const int STEPS = 60;  // halvings in each bisection
const int SPHERE = 1500;  // directions tried for the narrowest width

const int GRID = 80;  // grid side of the fallback search
const int STARTS = 4;  // best grid cells it zooms in around
const int ZOOMS = 14;  // rounds of zooming, each one ZOOM times finer
const int ZOOM = 5;

const double TINY = 1e-13;  // where the local search stops
const double CLOSE = 1e-10;  // equal widths, relative to the diameter
const int ROUNDS = 400;  // passes of a local search, which may creep on forever

const double HELPER = 0.9;  // a helper axis closer than this to n gives a poor cross product
const double GOLDEN = 2.399963229728653;  // the golden angle, spreading directions over the sphere
const double FIRST_TURN = 0.7853981633974483;  // pi / 4, the first turn of the polish
const double PI = acos(-1.0);

double dot(Vec a, Vec b) { return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]; }

Vec cross(Vec a, Vec b) {
    return {a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0]};
}

// s * a + t * b
Vec comb(Vec a, double s, Vec b, double t) {
    return {s * a[0] + t * b[0], s * a[1] + t * b[1], s * a[2] + t * b[2]};
}

Vec unit(Vec a) {
    double norm = sqrt(dot(a, a));
    return {a[0] / norm, a[1] / norm, a[2] / norm};
}

// v turned by angle around the unit vector axis (Rodrigues)
Vec turn(Vec v, Vec axis, double angle) {
    double c = cos(angle), s = sin(angle), k = dot(axis, v) * (1 - c);
    Vec w = cross(axis, v);
    return {v[0] * c + w[0] * s + axis[0] * k, v[1] * c + w[1] * s + axis[1] * k,
            v[2] * c + w[2] * s + axis[2] * k};
}

// two unit vectors completing n to a right-handed frame
std::pair<Vec, Vec> across(Vec n) {
    Vec helper = fabs(n[0]) > HELPER ? Vec{0, 1, 0} : Vec{1, 0, 0};
    Vec a = unit(cross(n, helper));
    return {a, cross(n, a)};
}

std::vector<Vec> pts;

double width(Vec u) {
    double lo = HUGE_VAL, hi = -HUGE_VAL;
    for (const Vec& p : pts) {
        double s = dot(p, u);
        lo = std::min(lo, s);
        hi = std::max(hi, s);
    }
    return hi - lo;
}

double spread(const Frame& f) {
    Vec w = {width(f[0]), width(f[1]), width(f[2])};
    return std::max({w[0], w[1], w[2]}) - std::min({w[0], w[1], w[2]});
}

double cost(const Frame& f) {
    double w0 = width(f[0]), w1 = width(f[1]), w2 = width(f[2]);
    return (w0 - w1) * (w0 - w1) + (w1 - w2) * (w1 - w2) + (w2 - w0) * (w2 - w0);
}

void show(const Frame& f) {
    for (const Vec& u : f) {
        printf("%.15f %.15f %.15f\n", u[0], u[1], u[2]);
    }
}

int main() {
    int count;
    scanf("%d", &count);
    std::vector<Int3> ints(count);
    for (auto& p : ints) {
        scanf("%lld %lld %lld", &p[0], &p[1], &p[2]);
        pts.push_back({(double)p[0], (double)p[1], (double)p[2]});
    }
    // the shape of the swarm, decided exactly on the integers
    auto diff = [&](int i) {
        return Int3{ints[i][0] - ints[0][0], ints[i][1] - ints[0][1], ints[i][2] - ints[0][2]};
    };
    auto icross = [](Int3 a, Int3 b) {
        return Int3{a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2],
                    a[0] * b[1] - a[1] * b[0]};
    };
    auto zero = [](Int3 a) { return !a[0] && !a[1] && !a[2]; };
    Int3 first{}, normal{};
    for (int i = 1; i < count && zero(first); i++) {
        first = diff(i);
    }
    for (int i = 1; i < count && zero(normal); i++) {
        normal = icross(first, diff(i));
    }
    if (zero(normal)) {
        // all on a line of direction d: an axis at angle acos(1/sqrt 3) to the
        // line each, so the three widths are the length over sqrt 3
        Vec d = unit({(double)first[0], (double)first[1], (double)first[2]});
        auto [u, v] = across(d);
        double r3 = 1 / sqrt((double)DIM), r2 = 1 / sqrt(2.0), r6 = 1 / sqrt(2.0 * DIM);
        show({comb(comb(d, r3, u, r2), 1, v, r6), comb(comb(d, r3, u, -r2), 1, v, r6),
              comb(d, r3, v, -2 * r6)});
        return 0;
    }
    bool flat = true;
    for (int i = 1; i < count; i++) {
        auto d = diff(i);
        flat = flat && normal[0] * d[0] + normal[1] * d[1] + normal[2] * d[2] == 0;
    }
    // widest direction: the diameter, where no other width can be larger
    long long bestLength = -1;
    Vec nMax{};
    for (auto& p : ints) {
        for (auto& q : ints) {
            long long dx = p[0] - q[0], dy = p[1] - q[1], dz = p[2] - q[2];
            if (dx * dx + dy * dy + dz * dz > bestLength) {
                bestLength = dx * dx + dy * dy + dz * dz;
                nMax = {(double)dx, (double)dy, (double)dz};
            }
        }
    }
    nMax = unit(nMax);
    // narrowest direction: the normal of a flat swarm, else a search
    Vec nMin;
    if (flat) {
        nMin = unit({(double)normal[0], (double)normal[1], (double)normal[2]});
    } else {
        double wMin = HUGE_VAL;
        for (int i = 0; i < SPHERE; i++) {
            double z = 1 - (2.0 * i + 1) / (2 * SPHERE), r = sqrt(1 - z * z);
            Vec u = {r * cos(GOLDEN * i), r * sin(GOLDEN * i), z};
            double w = width(u);
            if (w < wMin) {
                wMin = w;
                nMin = u;
            }
        }
        double step = 2 * PI / sqrt((double)SPHERE);
        for (int round = 0; round < ROUNDS && step > TINY; round++) {
            auto [a, b] = across(nMin);
            bool moved = false;
            for (Vec axis : {a, b, unit(comb(a, 1, b, 1)), unit(comb(a, 1, b, -1))}) {
                for (int sign : {1, -1}) {
                    Vec cand = unit(turn(nMin, axis, sign * step));
                    double w = width(cand);
                    if (w < wMin) {
                        wMin = w;
                        nMin = cand;
                        moved = true;
                    }
                }
            }
            if (!moved) {
                step /= 2;
            }
        }
    }
    // frames along the great circle from nMin to nMax: the third axis is the
    // turned n, the first two the turned a0, b0 rotated by phi
    Vec hinge = cross(nMin, nMax);
    if (dot(hinge, hinge) < TINY) {
        hinge = across(nMin).first;
    }
    hinge = unit(hinge);
    double angle = acos(std::max(-1.0, std::min(1.0, dot(nMin, nMax))));
    auto [a0, b0] = across(nMin);
    auto frame = [&](double t, double phi) {
        Vec n = turn(nMin, hinge, angle * t);
        Vec a = turn(a0, hinge, angle * t), b = turn(b0, hinge, angle * t);
        double c = cos(phi), s = sin(phi);
        return Frame{comb(a, c, b, s), comb(a, -s, b, c), n};
    };
    // phi in [0, pi/2] with equal first two widths: the difference changes
    // sign over a quarter turn, as the axes swap places
    auto balance = [&](double t) {
        auto gapAt = [&](double phi) {
            Frame f = frame(t, phi);
            return width(f[0]) - width(f[1]);
        };
        double lo = 0, hi = PI / 2;
        if (gapAt(lo) > 0) {
            std::swap(lo, hi);
        }
        for (int i = 0; i < STEPS; i++) {
            double mid = (lo + hi) / 2;
            (gapAt(mid) > 0 ? hi : lo) = mid;
        }
        return (lo + hi) / 2;
    };
    // at nMin the third width is the smallest, at nMax the largest
    double lo = 0, hi = 1;
    for (int i = 0; i < STEPS; i++) {
        double mid = (lo + hi) / 2;
        Frame f = frame(mid, balance(mid));
        (width(f[2]) - width(f[0]) < 0 ? lo : hi) = mid;
    }
    double t = (lo + hi) / 2;
    Frame result = frame(t, balance(t));
    double scale = std::max(1.0, width(nMax));
    if (spread(result) > CLOSE * scale) {
        // the chosen balance jumped. A solution still lies in the (t, phi)
        // square, as the third width is the smallest along t = 0 and the
        // largest along t = 1: scan it, then zoom in around the best cells
        double quarter = PI / 2;
        std::vector<std::tuple<double, double, double>> cells;
        for (int i = 0; i < GRID; i++) {
            for (int j = 0; j < GRID; j++) {
                double ti = (double)i / (GRID - 1), pj = quarter * j / (GRID - 1);
                cells.emplace_back(cost(frame(ti, pj)), ti, pj);
            }
        }
        std::sort(cells.begin(), cells.end());
        for (int k = 0; k < STARTS; k++) {
            auto [c0, t0, p0] = cells[k];
            double dt = 1.0 / (GRID - 1), dp = quarter / (GRID - 1);
            double hc = c0, ht = t0, hp = p0;
            for (int z = 0; z < ZOOMS; z++) {
                double tc = ht, pc = hp;
                for (int a = -ZOOM; a <= ZOOM; a++) {
                    double ta = std::min(1.0, std::max(0.0, tc + a * dt / ZOOM));
                    for (int b = -ZOOM; b <= ZOOM; b++) {
                        double pb = pc + b * dp / ZOOM, c = cost(frame(ta, pb));
                        if (c < hc) {
                            hc = c, ht = ta, hp = pb;
                        }
                    }
                }
                dt /= ZOOM, dp /= ZOOM;
            }
            result = frame(ht, hp);
            if (spread(result) <= CLOSE * scale) {
                break;
            }
        }
    }
    // polish by small turns of the frame about its own axes
    double best = cost(result);
    double step = spread(result) > CLOSE * scale ? FIRST_TURN : TINY * 2;
    for (int round = 0; round < ROUNDS && step > TINY; round++) {
        bool moved = false;
        for (int k = 0; k < DIM; k++) {
            for (int sign : {1, -1}) {
                Frame cand = result;
                for (int i = 0; i < DIM; i++) {
                    if (i != k) {
                        cand[i] = turn(result[i], result[k], sign * step);
                    }
                }
                double c = cost(cand);
                if (c < best) {
                    best = c;
                    result = cand;
                    moved = true;
                }
            }
        }
        if (!moved) {
            step /= 2;
        }
    }
    show(result);
}
