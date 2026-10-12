#include <cmath>
#include <cstdio>

const double RADIUS = 6400.0;
const double HALF_TURN = 180.0;
const double SHOWN = 0.0005; // values that print as 0.000
const int FIELDS = 3;

// three decimals, without a minus sign on zero
void show(double value) { printf("%.3f\n", std::fabs(value) < SHOWN ? 0.0 : value); }

int main() {
    double w = 0, lon = 0, side = 0;
    if (scanf("%lf %lf %lf", &w, &lon, &side) != FIELDS)
        return 0;
    double pi = std::acos(-1.0);
    double arc = side / RADIUS; // the angle of one side seen from the center
    double south = w * pi / HALF_TURN, north = south + arc;
    // north and south along meridians cancel; east runs along the northern
    // parallel and west along the southern one, at different speeds
    lon += (arc / std::cos(north) - arc / std::cos(south)) * HALF_TURN / pi;
    lon = std::fmod(lon, 2 * HALF_TURN);
    if (lon > HALF_TURN)
        lon -= 2 * HALF_TURN;
    else if (lon <= -HALF_TURN)
        lon += 2 * HALF_TURN;
    show(w);
    show(lon);
    return 0;
}
