#include <algorithm>
#include <array>
#include <cmath>
#include <iostream>
#include <limits>
#include <map>
#include <queue>
#include <set>
#include <tuple>
#include <vector>

using namespace std;

constexpr int DIMENSION = 3;
constexpr int QUATERNION_SIZE = 4;
constexpr int FIT_ITERATIONS = 12;
constexpr int WEIGHTED_ITERATIONS = 6;
constexpr int JACOBI_ITERATIONS = 24;
constexpr int EIGEN_ROUNDOFF_FACTOR = 256;
constexpr double EPS = 1e-6;
constexpr double CELL = 10 * EPS;
constexpr double GATE = 5 * EPS;
constexpr double ROUNDOFF_GUARD = 2e-15;
constexpr double NUMERIC_EPS = EPS + ROUNDOFF_GUARD;
constexpr double EPS2 = NUMERIC_EPS * NUMERIC_EPS;
constexpr double ANGLE_ROUNDOFF = 1e-12;
constexpr double SEARCH_ROUNDOFF = 1e-16;
constexpr double CERTIFICATE_ROUNDOFF = 1e-20;
constexpr double SINGULAR_LIMIT = 1e-30;
constexpr double STEP_LIMIT = 1e-15;
constexpr double MIN_WEIGHT = 1e-10;
constexpr array<int, WEIGHTED_ITERATIONS> WEIGHT_POWERS = {0, 1, 2, 4, 8, 16};

using Vec = array<double, DIMENSION>;
using Matrix = array<Vec, DIMENSION>;
using Pose = array<double, QUATERNION_SIZE>;
using Key = array<int, DIMENSION>;

double dot(const Vec &a, const Vec &b) { return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]; }
Vec cross(const Vec &a, const Vec &b) {
    return {a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0]};
}
double norm(const Vec &a) { return sqrt(dot(a, a)); }
Vec unit(Vec a) {
    double length = norm(a);
    for (double &x : a)
        x /= length;
    return a;
}
Vec subtract(const Vec &a, const Vec &b) { return {a[0] - b[0], a[1] - b[1], a[2] - b[2]}; }
double distance2(const Vec &a, const Vec &b) {
    Vec d = subtract(a, b);
    return dot(d, d);
}
Matrix frame(const Vec &a, const Vec &b) {
    Vec z = unit(a), y = unit(cross(z, unit(b)));
    return {cross(y, z), y, z};
}
Vec project(const Vec &a, const Matrix &basis) {
    return {dot(a, basis[0]), dot(a, basis[1]), dot(a, basis[2])};
}
Vec unproject(const Vec &a, const Matrix &basis) {
    Vec result{};
    for (int i = 0; i < DIMENSION; ++i)
        for (int j = 0; j < DIMENSION; ++j)
            result[i] += a[j] * basis[j][i];
    return result;
}
Key cell(const Vec &p) {
    return {int(floor(p[0] / CELL)), int(floor(p[1] / CELL)), int(floor(p[2] / CELL))};
}
bool solve3(Matrix a, Vec rhs, Vec &answer) {
    for (int column = 0; column < DIMENSION; ++column) {
        int pivot = column;
        for (int i = column + 1; i < DIMENSION; ++i)
            if (abs(a[i][column]) > abs(a[pivot][column]))
                pivot = i;
        if (abs(a[pivot][column]) < SINGULAR_LIMIT)
            return false;
        swap(a[pivot], a[column]);
        swap(rhs[pivot], rhs[column]);
        double divisor = a[column][column];
        for (double &value : a[column])
            value /= divisor;
        rhs[column] /= divisor;
        for (int i = 0; i < DIMENSION; ++i) {
            if (i == column)
                continue;
            double factor = a[i][column];
            for (int j = 0; j < DIMENSION; ++j)
                a[i][j] -= factor * a[column][j];
            rhs[i] -= factor * rhs[column];
        }
    }
    answer = rhs;
    return true;
}
Matrix normalMatrix(const vector<Vec> &points, const vector<double> &weights, double scale) {
    double xx = 0, yy = 0, zz = 0, xy = 0, xz = 0, yz = 0;
    for (size_t i = 0; i < points.size(); ++i) {
        const Vec &p = points[i];
        double w = weights[i];
        xx += w * p[0] * p[0];
        yy += w * p[1] * p[1];
        zz += w * p[2] * p[2];
        xy += w * p[0] * p[1];
        xz += w * p[0] * p[2];
        yz += w * p[1] * p[2];
    }
    return {{{yy + zz, -xy, -xz / scale},
             {-xy, xx + zz, -yz / scale},
             {-xz / scale, -yz / scale, (xx + yy) / (scale * scale)}}};
}
Vec gradient(const vector<Vec> &points, const vector<Vec> &targets, const vector<double> &weights) {
    Vec result{};
    for (size_t i = 0; i < points.size(); ++i) {
        Vec g = cross(points[i], subtract(targets[i], points[i]));
        for (int j = 0; j < DIMENSION; ++j)
            result[j] += weights[i] * g[j];
    }
    return result;
}
Pose quaternionStep(Vec omega, const Pose &pose) {
    double angle = norm(omega);
    if (angle == 0)
        return pose;
    double factor = sin(angle / 2) / angle, a = cos(angle / 2);
    double b = omega[0] * factor, c = omega[1] * factor, d = omega[2] * factor;
    double w = pose[0], x = pose[1], y = pose[2], z = pose[DIMENSION];
    Pose result = {a * w - b * x - c * y - d * z, a * x + b * w + c * z - d * y,
                   a * y - b * z + c * w + d * x, a * z + b * y - c * x + d * w};
    long double squared = 0;
    for (double value : result)
        squared += (long double)value * value;
    double length = sqrt(squared);
    for (double &value : result)
        value /= length;
    return result;
}
vector<Vec> quaternionApply(const vector<Vec> &points, const Pose &pose) {
    double w = pose[0], x = pose[1], y = pose[2], z = pose[DIMENSION];
    Matrix rows = {{{1 - 2 * (y * y + z * z), 2 * (x * y - w * z), 2 * (x * z + w * y)},
                    {2 * (x * y + w * z), 1 - 2 * (x * x + z * z), 2 * (y * z - w * x)},
                    {2 * (x * z - w * y), 2 * (y * z + w * x), 1 - 2 * (x * x + y * y)}}};
    vector<Vec> result;
    for (const Vec &p : points)
        result.push_back(project(p, rows));
    return result;
}
vector<double> residuals(const vector<Vec> &points, const vector<Vec> &targets) {
    vector<double> result;
    for (size_t i = 0; i < points.size(); ++i)
        result.push_back(distance2(points[i], targets[i]));
    return result;
}
double worstResidual(const vector<Vec> &points, const vector<Vec> &targets) {
    double result = 0;
    for (size_t i = 0; i < points.size(); ++i)
        result = max(result, distance2(points[i], targets[i]));
    return result;
}
double eigenLower(Matrix a) {
    for (int iteration = 0; iteration < JACOBI_ITERATIONS; ++iteration) {
        int p = 0, q = 1;
        for (int i = 0; i < DIMENSION; ++i)
            for (int j = i + 1; j < DIMENSION; ++j)
                if (abs(a[i][j]) > abs(a[p][q]))
                    p = i, q = j;
        double value = a[p][q];
        if (abs(value) < SINGULAR_LIMIT)
            break;
        double tau = (a[q][q] - a[p][p]) / (2 * value);
        double t = copysign(1.0, tau) / (abs(tau) + hypot(1, tau));
        double c = 1 / sqrt(1 + t * t), s = t * c;
        a[p][p] -= t * value;
        a[q][q] += t * value;
        a[p][q] = a[q][p] = 0;
        for (int k = 0; k < DIMENSION; ++k) {
            if (k == p || k == q)
                continue;
            double oldp = a[k][p], oldq = a[k][q];
            a[k][p] = a[p][k] = c * oldp - s * oldq;
            a[k][q] = a[q][k] = s * oldp + c * oldq;
        }
    }
    double lower = numeric_limits<double>::infinity();
    for (int i = 0; i < DIMENSION; ++i) {
        double bound = a[i][i];
        for (int j = 0; j < DIMENSION; ++j)
            if (i != j)
                bound -= abs(a[i][j]);
        lower = min(lower, bound);
    }
    return lower;
}
double lowerCertificate(const vector<Vec> &points, const vector<Vec> &targets,
                        const vector<double> &weights) {
    long double error = 0;
    array<long double, DIMENSION> gradientSum{};
    array<array<long double, DIMENSION>, DIMENSION> sum{};
    for (size_t k = 0; k < points.size(); ++k) {
        const Vec &p = points[k];
        const Vec &q = targets[k];
        Vec e = subtract(q, p), g = cross(p, e);
        double w = weights[k];
        error += (long double)w * dot(e, e);
        for (int i = 0; i < DIMENSION; ++i) {
            gradientSum[i] += (long double)w * g[i];
            double diagonal = 0;
            for (int j = 0; j < DIMENSION; ++j)
                if (i != j)
                    diagonal += p[j] * q[j];
            sum[i][i] += (long double)w * diagonal;
            for (int j = 0; j < i; ++j)
                sum[i][j] -= (long double)(w / 2) * (p[i] * q[j] + p[j] * q[i]);
        }
    }
    Matrix h{};
    Vec g{};
    for (int i = 0; i < DIMENSION; ++i) {
        g[i] = gradientSum[i];
        for (int j = 0; j <= i; ++j)
            h[i][j] = h[j][i] = sum[i][j];
    }
    double rowNorm = 0;
    for (const Vec &row : h)
        rowNorm = max(rowNorm, abs(row[0]) + abs(row[1]) + abs(row[2]));
    double eigen =
        eigenLower(h) - EIGEN_ROUNDOFF_FACTOR * numeric_limits<double>::epsilon() * rowNorm;
    if (eigen <= 0)
        return -numeric_limits<double>::infinity();
    return (double)error - dot(g, g) / eigen;
}
Vec parameterRotation(const Vec &p, const Vec &center) {
    double u = center[0], v = center[1], theta = center[2];
    double sine = sin(theta), cosine = cos(theta);
    double x = cosine * p[0] - sine * p[1], y = sine * p[0] + cosine * p[1], z = p[2];
    double c = 1 / sqrt(1 + u * u + v * v), value = u * x + v * y;
    double h = c * z - c * c * value / (1 + c);
    return {x + u * h, y + v * h, c * (z - value)};
}

struct Cell {
    double lower;
    size_t serial;
    Vec center, radii;
    bool operator<(const Cell &other) const {
        if (lower != other.lower)
            return lower > other.lower;
        return serial > other.serial;
    }
};

class Solver {
    vector<Vec> points, normalized, source, targets;
    vector<vector<double>> angles;
    vector<int> mapping;
    Matrix normal{};
    double scale = 0, angular = 0, chord = 0;

    const vector<double> &angleRow(int index) {
        if (angles[index].empty()) {
            for (const Vec &q : normalized)
                angles[index].push_back(
                    atan2(norm(cross(normalized[index], q)), dot(normalized[index], q)));
        }
        return angles[index];
    }
    bool angleExcluded(int index) {
        const auto &a = angleRow(index);
        const auto &b = angleRow(mapping[index]);
        for (size_t i = 0; i < mapping.size(); ++i)
            if (abs(a[i] - b[mapping[i]]) > 2 * angular + ANGLE_ROUNDOFF)
                return true;
        return false;
    }
    vector<Vec> fit(const vector<double> &weights, int iterations, Pose &pose) {
        vector<Vec> current = quaternionApply(source, pose);
        for (int iteration = 0; iteration < iterations; ++iteration) {
            Vec g = gradient(current, targets, weights), omega{};
            g[2] /= scale;
            if (!solve3(normalMatrix(current, weights, scale), g, omega))
                break;
            omega[2] /= scale;
            pose = quaternionStep(omega, pose);
            current = quaternionApply(source, pose);
            if (worstResidual(current, targets) <= EPS2 || norm(omega) < STEP_LIMIT)
                break;
        }
        return current;
    }
    bool bounded(double twist) {
        vector<double> norms, rho;
        for (const Vec &p : source) {
            norms.push_back(norm(p));
            rho.push_back(hypot(p[0], p[1]));
        }
        priority_queue<Cell> heap;
        size_t serial = 0;
        auto add = [&](const Vec &center, const Vec &radii) {
            double planar = 2 * hypot(radii[0], radii[1]), lower = 0, worst = 0;
            for (size_t i = 0; i < source.size(); ++i) {
                double d = sqrt(distance2(parameterRotation(source[i], center), targets[i]));
                double bound = norms[i] * planar + rho[i] * radii[2];
                if (d > EPS + bound + SEARCH_ROUNDOFF)
                    return false;
                worst = max(worst, d);
                lower = max(lower, d - bound);
            }
            if (worst <= NUMERIC_EPS)
                return true;
            heap.push({lower, ++serial, center, radii});
            return false;
        };
        if (add({0, 0, 0}, {tan(angular), tan(angular), twist}))
            return true;
        while (!heap.empty()) {
            Cell box = heap.top();
            heap.pop();
            int axis = 0;
            for (int i = 1; i < DIMENSION; ++i)
                if (box.radii[i] * (i == 2 ? scale : 1) > box.radii[axis] * (axis == 2 ? scale : 1))
                    axis = i;
            box.radii[axis] /= 2;
            for (int sign : {-1, 1}) {
                Vec child = box.center;
                child[axis] += sign * box.radii[axis];
                if (add(child, box.radii))
                    return true;
            }
        }
        return false;
    }
    bool feasible(double twist) {
        vector<double> weights(source.size(), 1);
        Vec g = gradient(source, targets, weights), omega{};
        g[2] /= scale;
        vector<Vec> quick = source;
        if (solve3(normal, g, omega)) {
            omega[2] /= scale;
            quick = quaternionApply(source, quaternionStep(omega, {1, 0, 0, 0}));
            if (worstResidual(quick, targets) <= EPS2)
                return true;
        }
        auto distances = residuals(quick, targets);
        int critical = int(max_element(distances.begin(), distances.end()) - distances.begin());
        if (angleExcluded(critical))
            return false;
        Pose pose = {1, 0, 0, 0};
        auto current = fit(weights, FIT_ITERATIONS, pose);
        for (int power : WEIGHT_POWERS) {
            distances = residuals(current, targets);
            double maximum = *max_element(distances.begin(), distances.end());
            if (maximum <= EPS2)
                return true;
            long double total = 0;
            for (size_t i = 0; i < weights.size(); ++i) {
                weights[i] = power == 0 ? 1 : max(MIN_WEIGHT, pow(distances[i] / maximum, power));
                total += weights[i];
            }
            if (lowerCertificate(current, targets, weights) > (EPS2 + CERTIFICATE_ROUNDOFF) * total)
                return false;
            current = fit(weights, WEIGHTED_ITERATIONS, pose);
        }
        return bounded(twist);
    }

  public:
    explicit Solver(vector<Vec> input) : points(move(input)), angles(points.size()) {}
    int count() {
        int n = int(points.size()), anchor = 1;
        double minimumNorm = numeric_limits<double>::infinity();
        for (const Vec &p : points) {
            normalized.push_back(unit(p));
            minimumNorm = min(minimumNorm, norm(p));
        }
        for (int i = 1; i < n; ++i) {
            double candidate = norm(cross(normalized[0], normalized[i]));
            if (candidate > scale)
                scale = candidate, anchor = i;
        }
        double cosine = dot(normalized[0], normalized[anchor]);
        double alpha = atan2(scale, cosine);
        Matrix basis = frame(points[0], points[anchor]);
        for (const Vec &p : points)
            source.push_back(project(p, basis));
        normal = normalMatrix(source, vector<double>(n, 1), scale);
        chord = EPS / minimumNorm;
        angular = 2 * asin(chord / 2);
        map<Key, vector<int>> lookup;
        for (int i = 0; i < n; ++i) {
            Key key = cell(points[i]);
            for (int dx = -1; dx <= 1; ++dx)
                for (int dy = -1; dy <= 1; ++dy)
                    for (int dz = -1; dz <= 1; ++dz)
                        lookup[{key[0] + dx, key[1] + dy, key[2] + dz}].push_back(i);
        }
        set<vector<int>> accepted;
        for (int p = 0; p < n; ++p) {
            for (int q = 0; q < n; ++q) {
                if (p == q)
                    continue;
                double sine = norm(cross(normalized[p], normalized[q]));
                double targetCosine = dot(normalized[p], normalized[q]);
                double tolerance = 2 * angular + ANGLE_ROUNDOFF;
                if (abs(sine - scale) > tolerance || abs(targetCosine - cosine) > tolerance)
                    continue;
                double beta = atan2(sine, targetCosine);
                if (sine == 0 || abs(alpha - beta) > tolerance)
                    continue;
                Matrix targetBasis = frame(points[p], points[q]);
                mapping.clear();
                vector<bool> used(n, false);
                double worst = 0;
                for (const Vec &coordinate : source) {
                    Vec rotated = unproject(coordinate, targetBasis);
                    auto bucket = lookup.find(cell(rotated));
                    double best = GATE * GATE;
                    int closest = -1;
                    if (bucket != lookup.end()) {
                        for (int j : bucket->second) {
                            double error = distance2(rotated, points[j]);
                            if (error < best)
                                best = error, closest = j;
                        }
                    }
                    if (closest < 0 || used[closest])
                        break;
                    used[closest] = true;
                    mapping.push_back(closest);
                    worst = max(worst, best);
                }
                if (int(mapping.size()) != n)
                    continue;
                if (worst <= EPS2) {
                    accepted.insert(mapping);
                    continue;
                }
                targets.clear();
                for (int index : mapping)
                    targets.push_back(project(points[index], targetBasis));
                double twist = 2 * asin(min(1.0, chord / sqrt(scale * sine)));
                if (feasible(twist))
                    accepted.insert(mapping);
            }
        }
        return int(accepted.size());
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n))
        return 0;
    vector<Vec> points(n);
    for (Vec &p : points)
        cin >> p[0] >> p[1] >> p[2];
    cout << Solver(move(points)).count() << '\n';
}
