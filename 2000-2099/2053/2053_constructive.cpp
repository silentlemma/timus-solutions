#include <algorithm>
#include <array>
#include <cmath>
#include <iostream>
#include <vector>

constexpr int GRID = 4;
constexpr int VERTICES = GRID * GRID;
constexpr int OUTER_SCALE = 900;
constexpr int DIMENSION = 2;
constexpr double ROUNDING_OFFSET = 0.5;
using Graph = std::array<std::array<int, VERTICES>, VERTICES>;
using Points = std::array<std::array<int, DIMENSION>, VERTICES>;
struct Answer {
    Points points;
    Graph graph;
};

void connect(Graph &graph, int a, int b) { graph[a][b] = graph[b][a] = 1; }

Answer solve() {
    Graph graph{};
    for (int row = 0; row < GRID; ++row)
        for (int column = 0; column < GRID; ++column) {
            int vertex = row * GRID + column;
            if (column + 1 < GRID)
                connect(graph, vertex, vertex + 1);
            if (row + 1 < GRID)
                connect(graph, vertex, vertex + GRID);
            if (row + 1 < GRID && column + 1 < GRID)
                connect(graph, vertex, vertex + GRID + 1);
        }
    std::array<int, GRID> corners{0, GRID - 1, VERTICES - 1, VERTICES - GRID};
    for (int side = 0; side < GRID; ++side) {
        int a = corners[side], d = corners[(side + 1) % GRID];
        int step = (d - a) / (GRID - 1);
        connect(graph, a, d);
        connect(graph, a, d - step);
    }
    connect(graph, corners[1], corners.back());
    Points points{};
    std::array<bool, VERTICES> fixed{};
    points[corners[0]] = {-OUTER_SCALE, -OUTER_SCALE};
    points[corners[1]] = {OUTER_SCALE, -OUTER_SCALE};
    points[corners.back()] = {0, OUTER_SCALE};
    fixed[corners[0]] = fixed[corners[1]] = fixed[corners.back()] = true;
    std::array<int, VERTICES> index{};
    std::vector<int> inside;
    for (int vertex = 0; vertex < VERTICES; ++vertex)
        if (!fixed[vertex]) {
            index[vertex] = static_cast<int>(inside.size());
            inside.push_back(vertex);
        }
    int size = static_cast<int>(inside.size());
    std::vector<std::vector<double>> matrix(size, std::vector<double>(size + DIMENSION));
    for (int vertex : inside) {
        auto &row = matrix[index[vertex]];
        for (int neighbour = 0; neighbour < VERTICES; ++neighbour)
            if (graph[vertex][neighbour]) {
                row[index[vertex]] += 1;
                if (!fixed[neighbour])
                    row[index[neighbour]] -= 1;
                else
                    for (int axis = 0; axis < DIMENSION; ++axis)
                        row[size + axis] += points[neighbour][axis];
            }
    }
    for (int column = 0; column < size; ++column) {
        int pivot = column;
        for (int row = column + 1; row < size; ++row)
            if (std::abs(matrix[row][column]) > std::abs(matrix[pivot][column]))
                pivot = row;
        std::swap(matrix[column], matrix[pivot]);
        double divisor = matrix[column][column];
        for (double &value : matrix[column])
            value /= divisor;
        for (int row = 0; row < size; ++row)
            if (row != column) {
                double factor = matrix[row][column];
                for (int entry = 0; entry < size + DIMENSION; ++entry)
                    matrix[row][entry] -= factor * matrix[column][entry];
            }
    }
    for (int vertex : inside)
        for (int axis = 0; axis < DIMENSION; ++axis)
            points[vertex][axis] =
                static_cast<int>(std::floor(matrix[index[vertex]][size + axis] + ROUNDING_OFFSET));
    return {points, graph};
}

int main() {
    Answer answer = solve();
    for (auto point : answer.points)
        std::cout << point[0] << ' ' << point[1] << '\n';
    for (auto row : answer.graph) {
        for (int bit : row)
            std::cout << bit;
        std::cout << '\n';
    }
}
