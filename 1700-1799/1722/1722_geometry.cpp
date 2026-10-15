#include <cmath>
#include <cstdio>
#include <iostream>

const double PERCENT = 100;
const double PI = std::acos(-1.0);

double cross(double ax, double ay, double bx, double by) {
    return ax * by - ay * bx;
}

// signed area, positive for a counterclockwise triangle
double triangle(double ax, double ay, double bx, double by, double cx, double cy) {
    return cross(bx - ax, by - ay, cx - ax, cy - ay) / 2;
}

int main() {
    double big, small, near, x, y;
    std::cin >> big >> small >> near >> x >> y;
    double d = std::hypot(x, y);
    double ux = x / d, uy = y / d;
    // the outer common tangents touch both buildings at n * radius from
    // each center, n making cos = -k with the direction to the new one
    double k = (near - small) / d;
    double s = std::sqrt(1 - k * k);
    double tx[2], ty[2], ex[2], ey[2];
    for (int i = 0; i < 2; i++) {
        int side = i == 0 ? -1 : 1;
        double nx = -k * ux - side * s * uy;
        double ny = -k * uy + side * s * ux;
        tx[i] = x + near * nx;
        ty[i] = y + near * ny;
        // the line runs away from the old building through the tangent
        // point, and leaves the city where |T + t D| = R
        double dx = x + (near - small) * nx, dy = y + (near - small) * ny;
        double a = dx * dx + dy * dy;
        double b = tx[i] * dx + ty[i] * dy;
        double c = tx[i] * tx[i] + ty[i] * ty[i] - big * big;
        double t = (-b + std::sqrt(b * b - a * c)) / a;
        ex[i] = tx[i] + t * dx;
        ey[i] = ty[i] + t * dy;
    }
    // go around the hidden part counterclockwise: the arc of the new
    // building that faces the old one, the first tangent out to the city
    // border, along the border, the second tangent back
    double area = std::acos(k) * near * near;
    area += triangle(x, y, tx[0], ty[0], ex[0], ey[0]);
    area += triangle(x, y, ex[1], ey[1], tx[1], ty[1]);
    double turn = std::atan2(cross(ex[0], ey[0], ex[1], ey[1]), ex[0] * ex[1] + ey[0] * ey[1]);
    if (turn < 0) turn += 2 * PI;
    // the border arc seen from the new center: a triangle plus the piece
    // of the city cut off by the chord
    area += triangle(x, y, ex[0], ey[0], ex[1], ey[1]);
    area += turn * big * big / 2 - triangle(0, 0, ex[0], ey[0], ex[1], ey[1]);
    printf("%.10f\n", PERCENT * area / (PI * big * big));
}
