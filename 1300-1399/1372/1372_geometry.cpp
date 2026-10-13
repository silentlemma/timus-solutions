#include <algorithm>
#include <cmath>
#include <cstdio>

const double TINY = 1e-9; // a torque this small is no torque at all
const double TURN = 360.0;
const double HALF_UNIT = 5e-9; // half of the last printed digit
const double DEGREE = std::acos(-1.0) / 180;
const int FIELDS = 5, ENGINE = 4;

struct Vec {
    double x, y, z;
};

Vec unit(double lon, double lat) {
    lon *= DEGREE;
    lat *= DEGREE;
    return {std::cos(lat) * std::cos(lon), std::cos(lat) * std::sin(lon), std::sin(lat)};
}

Vec cross(Vec a, Vec b) {
    return {a.y * b.z - a.z * b.y, a.z * b.x - a.x * b.z, a.x * b.y - a.y * b.x};
}

double dot(Vec a, Vec b) { return a.x * b.x + a.y * b.y + a.z * b.z; }

void angles(Vec v, double &lon, double &lat) {
    double length = std::sqrt(dot(v, v));
    lat = std::asin(std::max(-1.0, std::min(1.0, v.z / length))) / DEGREE;
    lon = std::fmod(std::atan2(v.y, v.x) / DEGREE + TURN, TURN);
    if (lon >= TURN - HALF_UNIT)
        lon = 0; // it would print as 360
    lon += 0.0;
    lat += 0.0; // no negative zeros
}

int main() {
    double radius = 0, mass = 0, mast = 0, thrust = 0, count = 0;
    if (scanf("%lf %lf %lf %lf %lf", &radius, &mass, &mast, &thrust, &count) != FIELDS)
        return 0;
    double arm = radius + mast; // the engines sit on masts above the surface
    Vec torque = {0, 0, 0};
    for (int i = 0; i < (int)count; i++) {
        double lon = 0, lat = 0, dlon = 0, dlat = 0;
        if (scanf("%lf %lf %lf %lf", &lon, &lat, &dlon, &dlat) != ENGINE)
            return 0;
        Vec t = cross(unit(lon, lat), unit(dlon, dlat));
        torque = {torque.x + arm * thrust * t.x, torque.y + arm * thrust * t.y,
                  torque.z + arm * thrust * t.z};
    }
    double size = std::sqrt(dot(torque, torque));
    if (size < TINY) {
        printf("%.8f %.8f %.8f %.8f %.8f\n", 0.0, 0.0, 0.0, 0.0, 0.0);
        return 0;
    }
    // a force f at p turns the station by p x f, at most |p| |f|; so the
    // least thrust |T| / |p| needs p across the torque T and f = p x T / |p|^2
    Vec axis = {torque.x / size, torque.y / size, torque.z / size};
    Vec axes[] = {{1, 0, 0}, {0, 1, 0}, {0, 0, 1}};
    Vec pick = axes[0];
    for (Vec e : axes)
        if (std::fabs(dot(e, axis)) < std::fabs(dot(pick, axis)))
            pick = e;
    double d = dot(pick, axis);
    Vec place = {pick.x - d * axis.x, pick.y - d * axis.y, pick.z - d * axis.z};
    Vec push = cross(place, torque);
    double lon = 0, lat = 0, dlon = 0, dlat = 0;
    angles(place, lon, lat);
    angles(push, dlon, dlat);
    printf("%.8f %.8f %.8f %.8f %.8f\n", lon, lat, dlon, dlat, size / arm);
    return 0;
}
