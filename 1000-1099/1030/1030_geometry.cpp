#include <algorithm>
#include <cmath>
#include <cstdio>
#include <sstream>
#include <string>
#include <vector>

const double RADIANS_PER_DEGREE = std::acos(-1.0) / 180;
const double RADIUS = 6875.0 / 2, DANGER = 100.0, SECONDS = 3600, MINUTES = 60;
const double HUNDREDTHS = 100;
const int PARTS = 3;

int main() {
    std::string text;
    for (int c; (c = getchar()) != EOF;)
        text += c == '^' || c == '\'' || c == '"' ? ' ' : (char)c;
    // every coordinate is "degrees minutes seconds" followed by NL, SL, EL or WL
    std::istringstream in(text);
    std::vector<std::string> tokens;
    for (std::string t; in >> t;)
        tokens.push_back(t);
    std::vector<double> angle;
    for (size_t i = PARTS; i < tokens.size(); i++) {
        const std::string &t = tokens[i];
        if (t.size() < 2 || t[1] != 'L' || std::string("NSEW").find(t[0]) == std::string::npos)
            continue;
        double degrees = std::stod(tokens[i - PARTS]) + std::stod(tokens[i - 2]) / MINUTES +
                         std::stod(tokens[i - 1]) / SECONDS;
        angle.push_back((t[0] == 'S' || t[0] == 'W' ? -degrees : degrees) * RADIANS_PER_DEGREE);
    }
    // the haversine formula keeps its precision for small distances
    double lat1 = angle[0], lon1 = angle[1], lat2 = angle[2], lon2 = angle.back();
    double h = std::pow(std::sin((lat2 - lat1) / 2), 2) +
               std::cos(lat1) * std::cos(lat2) * std::pow(std::sin((lon2 - lon1) / 2), 2);
    double distance = 2 * RADIUS * std::asin(std::min(1.0, std::sqrt(h)));
    printf("The distance to the iceberg: %.2f miles.\n", distance);
    // the comparison uses the printed value: 99.996 is printed as 100.00
    if (std::round(distance * HUNDREDTHS) < DANGER * HUNDREDTHS)
        printf("DANGER!\n");
}
