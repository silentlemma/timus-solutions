#include <algorithm>
#include <cstdio>
#include <utility>
#include <vector>

using namespace std;

typedef pair<long long, long long> Point;

long long cross(const Point &o, const Point &a, const Point &b) {
    return (a.first - o.first) * (b.second - o.second) -
           (a.second - o.second) * (b.first - o.first);
}

// marks the points of one monotone chain, keeping points that lie on its edges
void chain(const vector<Point> &p, const vector<int> &order, vector<bool> &border) {
    vector<int> stack;
    for (int i : order) {
        while (stack.size() > 1 && cross(p[stack[stack.size() - 2]], p[stack.back()], p[i]) < 0)
            stack.pop_back();
        stack.push_back(i);
    }
    for (int i : stack)
        border[i] = true;
}

bool flat(const vector<Point> &p) {
    for (const Point &q : p)
        if (cross(p.front(), p.back(), q) != 0)
            return false;
    return true;
}

int main() {
    int n;
    scanf("%d", &n);
    vector<Point> points(n);
    for (Point &p : points)
        scanf("%lld %lld", &p.first, &p.second);
    sort(points.begin(), points.end());
    int layers = 0;
    // peel hulls with their whole border while the rest still has area
    while (points.size() > 2 && !flat(points)) {
        layers++;
        int size = points.size();
        vector<int> order(size);
        for (int i = 0; i < size; i++)
            order[i] = i;
        vector<bool> border(size, false);
        chain(points, order, border);
        reverse(order.begin(), order.end());
        chain(points, order, border);
        vector<Point> rest;
        for (int i = 0; i < size; i++)
            if (!border[i])
                rest.push_back(points[i]);
        points.swap(rest);
    }
    printf("%d\n", layers);
}
