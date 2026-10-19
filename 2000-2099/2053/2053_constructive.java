public class Main {
  static final int GRID = 4;
  static final int VERTICES = GRID * GRID;
  static final int OUTER_SCALE = 900;
  static final int DIMENSION = 2;
  static final double ROUNDING_OFFSET = 0.5;

  static class Answer {
    final int[][] points, graph;
    Answer(int[][] p, int[][] g) {
      points = p;
      graph = g;
    }
  }

  static void connect(int[][] graph, int a, int b) {
    graph[a][b] = graph[b][a] = 1;
  }

  static Answer solve() {
    int[][] graph = new int[VERTICES][VERTICES];
    for (int row = 0; row < GRID; row++)
      for (int column = 0; column < GRID; column++) {
        int vertex = row * GRID + column;
        if (column + 1 < GRID)
          connect(graph, vertex, vertex + 1);
        if (row + 1 < GRID)
          connect(graph, vertex, vertex + GRID);
        if (row + 1 < GRID && column + 1 < GRID)
          connect(graph, vertex, vertex + GRID + 1);
      }
    int[] corners = {0, GRID - 1, VERTICES - 1, VERTICES - GRID};
    for (int side = 0; side < GRID; side++) {
      int a = corners[side], d = corners[(side + 1) % GRID];
      int step = (d - a) / (GRID - 1);
      connect(graph, a, d);
      connect(graph, a, d - step);
    }
    connect(graph, corners[1], corners[GRID - 1]);
    int[][] points = new int[VERTICES][DIMENSION];
    boolean[] fixed = new boolean[VERTICES];
    points[corners[0]] = new int[] {-OUTER_SCALE, -OUTER_SCALE};
    points[corners[1]] = new int[] {OUTER_SCALE, -OUTER_SCALE};
    points[corners[GRID - 1]] = new int[] {0, OUTER_SCALE};
    fixed[corners[0]] = fixed[corners[1]] = fixed[corners[GRID - 1]] = true;
    int[] index = new int[VERTICES], inside = new int[VERTICES];
    int size = 0;
    for (int vertex = 0; vertex < VERTICES; vertex++)
      if (!fixed[vertex]) {
        index[vertex] = size;
        inside[size++] = vertex;
      }
    double[][] matrix = new double[size][size + DIMENSION];
    for (int i = 0; i < size; i++) {
      int vertex = inside[i];
      double[] row = matrix[i];
      for (int neighbour = 0; neighbour < VERTICES; neighbour++)
        if (graph[vertex][neighbour] != 0) {
          row[i]++;
          if (!fixed[neighbour])
            row[index[neighbour]]--;
          else
            for (int axis = 0; axis < DIMENSION; axis++)
              row[size + axis] += points[neighbour][axis];
        }
    }
    for (int column = 0; column < size; column++) {
      int pivot = column;
      for (int row = column + 1; row < size; row++)
        if (Math.abs(matrix[row][column]) > Math.abs(matrix[pivot][column]))
          pivot = row;
      double[] swap = matrix[column];
      matrix[column] = matrix[pivot];
      matrix[pivot] = swap;
      double divisor = matrix[column][column];
      for (int entry = 0; entry < size + DIMENSION; entry++) matrix[column][entry] /= divisor;
      for (int row = 0; row < size; row++)
        if (row != column) {
          double factor = matrix[row][column];
          for (int entry = 0; entry < size + DIMENSION; entry++)
            matrix[row][entry] -= factor * matrix[column][entry];
        }
    }
    for (int i = 0; i < size; i++)
      for (int axis = 0; axis < DIMENSION; axis++)
        points[inside[i]][axis] = (int) Math.floor(matrix[i][size + axis] + ROUNDING_OFFSET);
    return new Answer(points, graph);
  }

  public static void main(String[] args) {
    Answer answer = solve();
    StringBuilder out = new StringBuilder();
    for (int[] point : answer.points)
      out.append(point[0]).append(' ').append(point[1]).append('\n');
    for (int[] row : answer.graph) {
      for (int bit : row) out.append(bit);
      out.append('\n');
    }
    System.out.print(out);
  }
}
