import java.io.BufferedInputStream;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.HashMap;
import java.util.HashSet;
import java.util.PriorityQueue;

public class Main {
  static final int DIMENSION = 3;
  static final int QUATERNION_SIZE = 4;
  static final int FIT_ITERATIONS = 12;
  static final int WEIGHTED_ITERATIONS = 6;
  static final int JACOBI_ITERATIONS = 24;
  static final int BALANCE_ITERATIONS = 128;
  static final int EIGEN_ROUNDOFF_FACTOR = 256;
  static final int CELL_BITS = 21;
  static final long CELL_OFFSET = 1L << (CELL_BITS - 1);
  static final double EPS = 1e-6;
  static final double CELL = 10 * EPS;
  static final double GATE = 5 * EPS;
  static final double ROUNDOFF_GUARD = 2e-15;
  static final double NUMERIC_EPS = EPS + ROUNDOFF_GUARD;
  static final double EPS2 = NUMERIC_EPS * NUMERIC_EPS;
  static final double ANGLE_ROUNDOFF = 1e-12;
  static final double SEARCH_ROUNDOFF = 1e-16;
  static final double CERTIFICATE_ROUNDOFF = ROUNDOFF_GUARD * EPS / 2;
  static final double SINGULAR_LIMIT = 1e-30;
  static final double STEP_LIMIT = 1e-15;
  static final double MIN_WEIGHT = 1e-10;
  static final int[] WEIGHT_POWERS = {0, 1, 2, 4, 8, 16};

  static double dot(double[] a, double[] b) {
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2];
  }

  static double[] cross(double[] a, double[] b) {
    return new double[] {
        a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0]};
  }

  static double norm(double[] a) {
    return Math.sqrt(dot(a, a));
  }

  static double[] unit(double[] a) {
    double length = norm(a);
    return new double[] {a[0] / length, a[1] / length, a[2] / length};
  }

  static double[] subtract(double[] a, double[] b) {
    return new double[] {a[0] - b[0], a[1] - b[1], a[2] - b[2]};
  }

  static double distance2(double[] a, double[] b) {
    double x = a[0] - b[0], y = a[1] - b[1], z = a[2] - b[2];
    return x * x + y * y + z * z;
  }

  static double[][] frame(double[] a, double[] b) {
    double[] z = unit(a), y = unit(cross(z, unit(b)));
    return new double[][] {cross(y, z), y, z};
  }

  static double[] project(double[] a, double[][] basis) {
    return new double[] {dot(a, basis[0]), dot(a, basis[1]), dot(a, basis[2])};
  }

  static double[] unproject(double[] a, double[][] basis) {
    double[] result = new double[DIMENSION];
    for (int i = 0; i < DIMENSION; i++)
      for (int j = 0; j < DIMENSION; j++) result[i] += a[j] * basis[j][i];
    return result;
  }

  static long key(int x, int y, int z) {
    return (((x + CELL_OFFSET) << CELL_BITS) | (y + CELL_OFFSET)) << CELL_BITS | (z + CELL_OFFSET);
  }

  static long cell(double[] p) {
    return key((int) Math.floor(p[0] / CELL), (int) Math.floor(p[1] / CELL),
        (int) Math.floor(p[2] / CELL));
  }

  static double[] solve3(double[][] matrix, double[] rhs) {
    double[][] a = new double[DIMENSION][];
    for (int i = 0; i < DIMENSION; i++) a[i] = matrix[i].clone();
    rhs = rhs.clone();
    for (int column = 0; column < DIMENSION; column++) {
      int pivot = column;
      for (int i = column + 1; i < DIMENSION; i++)
        if (Math.abs(a[i][column]) > Math.abs(a[pivot][column]))
          pivot = i;
      if (Math.abs(a[pivot][column]) < SINGULAR_LIMIT)
        return null;
      double[] row = a[pivot];
      a[pivot] = a[column];
      a[column] = row;
      double value = rhs[pivot];
      rhs[pivot] = rhs[column];
      rhs[column] = value;
      double divisor = a[column][column];
      for (int j = 0; j < DIMENSION; j++) a[column][j] /= divisor;
      rhs[column] /= divisor;
      for (int i = 0; i < DIMENSION; i++) {
        if (i == column)
          continue;
        double factor = a[i][column];
        for (int j = 0; j < DIMENSION; j++) a[i][j] -= factor * a[column][j];
        rhs[i] -= factor * rhs[column];
      }
    }
    return rhs;
  }

  static double[][] normalMatrix(double[][] points, double[] weights, double scale) {
    double xx = 0, yy = 0, zz = 0, xy = 0, xz = 0, yz = 0;
    for (int i = 0; i < points.length; i++) {
      double[] p = points[i];
      double w = weights[i];
      xx += w * p[0] * p[0];
      yy += w * p[1] * p[1];
      zz += w * p[2] * p[2];
      xy += w * p[0] * p[1];
      xz += w * p[0] * p[2];
      yz += w * p[1] * p[2];
    }
    return new double[][] {{yy + zz, -xy, -xz / scale}, {-xy, xx + zz, -yz / scale},
        {-xz / scale, -yz / scale, (xx + yy) / (scale * scale)}};
  }

  static double[] gradient(double[][] points, double[][] targets, double[] weights) {
    double[] result = new double[DIMENSION];
    for (int i = 0; i < points.length; i++) {
      double[] g = cross(points[i], subtract(targets[i], points[i]));
      for (int j = 0; j < DIMENSION; j++) result[j] += weights[i] * g[j];
    }
    return result;
  }

  static class Sum {
    double total, correction;
    void add(double x) {
      double next = total + x;
      correction += Math.abs(total) >= Math.abs(x) ? (total - next) + x : (x - next) + total;
      total = next;
    }
    double value() {
      return total + correction;
    }
  }

  static double[] quaternionStep(double[] omega, double[] pose) {
    double angle = norm(omega);
    if (angle == 0)
      return pose;
    double factor = Math.sin(angle / 2) / angle, a = Math.cos(angle / 2);
    double b = omega[0] * factor, c = omega[1] * factor, d = omega[2] * factor;
    double w = pose[0], x = pose[1], y = pose[2], z = pose[DIMENSION];
    double[] result = {a * w - b * x - c * y - d * z, a * x + b * w + c * z - d * y,
        a * y - b * z + c * w + d * x, a * z + b * y - c * x + d * w};
    Sum squared = new Sum();
    for (double value : result) squared.add(value * value);
    double length = Math.sqrt(squared.value());
    for (int i = 0; i < QUATERNION_SIZE; i++) result[i] /= length;
    return result;
  }

  static double[][] quaternionApply(double[][] points, double[] pose) {
    double w = pose[0], x = pose[1], y = pose[2], z = pose[DIMENSION];
    double[][] rows = {{1 - 2 * (y * y + z * z), 2 * (x * y - w * z), 2 * (x * z + w * y)},
        {2 * (x * y + w * z), 1 - 2 * (x * x + z * z), 2 * (y * z - w * x)},
        {2 * (x * z - w * y), 2 * (y * z + w * x), 1 - 2 * (x * x + y * y)}};
    double[][] result = new double[points.length][];
    for (int i = 0; i < points.length; i++) result[i] = project(points[i], rows);
    return result;
  }

  static double[] residuals(double[][] points, double[][] targets) {
    double[] result = new double[points.length];
    for (int i = 0; i < points.length; i++) result[i] = distance2(points[i], targets[i]);
    return result;
  }

  static double maximum(double[] values) {
    double result = 0;
    for (double value : values) result = Math.max(result, value);
    return result;
  }

  static double eigenLower(double[][] matrix) {
    double[][] a = new double[DIMENSION][];
    for (int i = 0; i < DIMENSION; i++) a[i] = matrix[i].clone();
    for (int iteration = 0; iteration < JACOBI_ITERATIONS; iteration++) {
      int p = 0, q = 1;
      for (int i = 0; i < DIMENSION; i++)
        for (int j = i + 1; j < DIMENSION; j++)
          if (Math.abs(a[i][j]) > Math.abs(a[p][q])) {
            p = i;
            q = j;
          }
      double value = a[p][q];
      if (Math.abs(value) < SINGULAR_LIMIT)
        break;
      double tau = (a[q][q] - a[p][p]) / (2 * value);
      double t = Math.copySign(1, tau) / (Math.abs(tau) + Math.hypot(1, tau));
      double c = 1 / Math.sqrt(1 + t * t), s = t * c;
      a[p][p] -= t * value;
      a[q][q] += t * value;
      a[p][q] = a[q][p] = 0;
      for (int k = 0; k < DIMENSION; k++) {
        if (k == p || k == q)
          continue;
        double oldp = a[k][p], oldq = a[k][q];
        a[k][p] = a[p][k] = c * oldp - s * oldq;
        a[k][q] = a[q][k] = s * oldp + c * oldq;
      }
    }
    double lower = Double.POSITIVE_INFINITY;
    for (int i = 0; i < DIMENSION; i++) {
      double bound = a[i][i];
      for (int j = 0; j < DIMENSION; j++)
        if (i != j)
          bound -= Math.abs(a[i][j]);
      lower = Math.min(lower, bound);
    }
    return lower;
  }

  static double lowerCertificate(double[][] points, double[][] targets, double[] weights) {
    Sum error = new Sum();
    Sum[] gradients = new Sum[DIMENSION];
    Sum[][] entries = new Sum[DIMENSION][DIMENSION];
    for (int i = 0; i < DIMENSION; i++) {
      gradients[i] = new Sum();
      for (int j = 0; j < DIMENSION; j++) entries[i][j] = new Sum();
    }
    for (int k = 0; k < points.length; k++) {
      double[] p = points[k], q = targets[k], e = subtract(q, p), g = cross(p, e);
      double w = weights[k];
      error.add(w * dot(e, e));
      for (int i = 0; i < DIMENSION; i++) {
        gradients[i].add(w * g[i]);
        double diagonal = 0;
        for (int j = 0; j < DIMENSION; j++)
          if (i != j)
            diagonal += p[j] * q[j];
        entries[i][i].add(w * diagonal);
        for (int j = 0; j < i; j++) entries[i][j].add(-w / 2 * (p[i] * q[j] + p[j] * q[i]));
      }
    }
    double[][] h = new double[DIMENSION][DIMENSION];
    double[] g = new double[DIMENSION];
    for (int i = 0; i < DIMENSION; i++) {
      g[i] = gradients[i].value();
      for (int j = 0; j <= i; j++) h[i][j] = h[j][i] = entries[i][j].value();
    }
    double rowNorm = 0;
    for (double[] row : h)
      rowNorm = Math.max(rowNorm, Math.abs(row[0]) + Math.abs(row[1]) + Math.abs(row[2]));
    double eigen = eigenLower(h) - EIGEN_ROUNDOFF_FACTOR * Math.ulp(1.0) * rowNorm;
    if (eigen <= 0)
      return Double.NEGATIVE_INFINITY;
    return error.value() - dot(g, g) / eigen;
  }

  static double[] parameterRotation(double[] p, double[] center) {
    double u = center[0], v = center[1], theta = center[2];
    double sine = Math.sin(theta), cosine = Math.cos(theta);
    double x = cosine * p[0] - sine * p[1], y = sine * p[0] + cosine * p[1], z = p[2];
    double c = 1 / Math.sqrt(1 + u * u + v * v), value = u * x + v * y;
    double h = c * z - c * c * value / (1 + c);
    return new double[] {x + u * h, y + v * h, c * (z - value)};
  }

  static class Box {
    final double lower;
    final long serial;
    final double[] center, radii;
    Box(double lower, long serial, double[] center, double[] radii) {
      this.lower = lower;
      this.serial = serial;
      this.center = center;
      this.radii = radii;
    }
  }

  static class Fit {
    double[][] points;
    double[] pose;
    Fit(double[][] points, double[] pose) {
      this.points = points;
      this.pose = pose;
    }
  }

  static class Solver {
    double[][] points, normalized, source, targets, angles, normal;
    int[] mapping;
    double scale, angular, chord;
    Solver(double[][] points) {
      this.points = points;
      angles = new double[points.length][];
    }

    double[] angleRow(int index) {
      if (angles[index] == null) {
        double[] row = new double[points.length], p = normalized[index];
        for (int i = 0; i < points.length; i++)
          row[i] = Math.atan2(norm(cross(p, normalized[i])), dot(p, normalized[i]));
        angles[index] = row;
      }
      return angles[index];
    }

    boolean angleExcluded(int index) {
      double[] a = angleRow(index), b = angleRow(mapping[index]);
      for (int i = 0; i < mapping.length; i++)
        if (Math.abs(a[i] - b[mapping[i]]) > 2 * angular + ANGLE_ROUNDOFF)
          return true;
      return false;
    }

    Fit fit(double[] weights, int iterations, double[] pose) {
      double[][] current = quaternionApply(source, pose);
      for (int iteration = 0; iteration < iterations; iteration++) {
        double[] g = gradient(current, targets, weights);
        g[2] /= scale;
        double[] omega = solve3(normalMatrix(current, weights, scale), g);
        if (omega == null)
          break;
        omega[2] /= scale;
        pose = quaternionStep(omega, pose);
        current = quaternionApply(source, pose);
        if (maximum(residuals(current, targets)) <= EPS2 || norm(omega) < STEP_LIMIT)
          break;
      }
      return new Fit(current, pose);
    }

    class Search {
      double[] norms = new double[source.length], rho = new double[source.length];
      PriorityQueue<Box> heap = new PriorityQueue<>(
          Comparator.comparingDouble((Box b) -> b.lower).thenComparingLong(b -> b.serial));
      long serial;
      Search() {
        for (int i = 0; i < source.length; i++) {
          norms[i] = norm(source[i]);
          rho[i] = Math.hypot(source[i][0], source[i][1]);
        }
      }
      boolean add(double[] center, double[] radii) {
        double planar = 2 * Math.hypot(radii[0], radii[1]), lower = 0, worst = 0;
        for (int i = 0; i < source.length; i++) {
          double d = Math.sqrt(distance2(parameterRotation(source[i], center), targets[i]));
          double bound = norms[i] * planar + rho[i] * radii[2];
          if (d > EPS + bound + SEARCH_ROUNDOFF)
            return false;
          worst = Math.max(worst, d);
          lower = Math.max(lower, d - bound);
        }
        if (worst <= NUMERIC_EPS)
          return true;
        heap.add(new Box(lower, ++serial, center, radii));
        return false;
      }
      boolean run(double twist) {
        if (add(new double[DIMENSION], new double[] {Math.tan(angular), Math.tan(angular), twist}))
          return true;
        while (!heap.isEmpty()) {
          Box b = heap.remove();
          int axis = 0;
          double largest = b.radii[0];
          for (int i = 1; i < DIMENSION; i++) {
            double value = b.radii[i] * (i == 2 ? scale : 1);
            if (value > largest) {
              largest = value;
              axis = i;
            }
          }
          double[] radii = b.radii.clone();
          radii[axis] /= 2;
          for (int sign : new int[] {-1, 1}) {
            double[] child = b.center.clone();
            child[axis] += sign * radii[axis];
            if (add(child, radii))
              return true;
          }
        }
        return false;
      }
    }

    boolean feasible(double twist) {
      double[] weights = new double[source.length];
      Arrays.fill(weights, 1);
      double[] g = gradient(source, targets, weights);
      g[2] /= scale;
      double[] omega = solve3(normal, g);
      double[][] quick = source;
      if (omega != null) {
        omega[2] /= scale;
        quick = quaternionApply(source, quaternionStep(omega, new double[] {1, 0, 0, 0}));
        if (maximum(residuals(quick, targets)) <= EPS2)
          return true;
      }
      double[] distances = residuals(quick, targets);
      int critical = 0;
      for (int i = 1; i < distances.length; i++)
        if (distances[i] > distances[critical])
          critical = i;
      if (angleExcluded(critical))
        return false;
      Fit current = fit(weights, FIT_ITERATIONS, new double[] {1, 0, 0, 0});
      for (int power : WEIGHT_POWERS) {
        distances = residuals(current.points, targets);
        double largest = maximum(distances);
        if (largest <= EPS2)
          return true;
        Sum total = new Sum();
        for (int i = 0; i < weights.length; i++) {
          weights[i] =
              power == 0 ? 1 : Math.max(MIN_WEIGHT, Math.pow(distances[i] / largest, power));
          total.add(weights[i]);
        }
        if (lowerCertificate(current.points, targets, weights)
            > (EPS * EPS + CERTIFICATE_ROUNDOFF) * total.value())
          return false;
        current = fit(weights, WEIGHTED_ITERATIONS, current.pose);
      }
      Arrays.fill(weights, 1);
      for (int iteration = 0; iteration < BALANCE_ITERATIONS; iteration++) {
        distances = residuals(current.points, targets);
        double largest = maximum(distances);
        if (largest <= EPS2)
          return true;
        Sum total = new Sum();
        for (int i = 0; i < weights.length; i++) {
          double grown = weights[i] * Math.exp((distances[i] / largest - 1) / 2);
          weights[i] = Math.max(MIN_WEIGHT, grown);
          total.add(weights[i]);
        }
        for (int i = 0; i < weights.length; i++) weights[i] /= total.value();
        if (lowerCertificate(current.points, targets, weights) > EPS * EPS + CERTIFICATE_ROUNDOFF)
          return false;
        current = fit(weights, WEIGHTED_ITERATIONS, current.pose);
      }
      return new Search().run(twist);
    }

    int count() {
      int n = points.length, anchor = 1;
      normalized = new double[n][];
      source = new double[n][];
      double minimumNorm = Double.POSITIVE_INFINITY;
      for (int i = 0; i < n; i++) {
        normalized[i] = unit(points[i]);
        minimumNorm = Math.min(minimumNorm, norm(points[i]));
      }
      for (int i = 1; i < n; i++) {
        double candidate = norm(cross(normalized[0], normalized[i]));
        if (candidate > scale) {
          scale = candidate;
          anchor = i;
        }
      }
      double cosine = dot(normalized[0], normalized[anchor]), alpha = Math.atan2(scale, cosine);
      double[][] basis = frame(points[0], points[anchor]);
      for (int i = 0; i < n; i++) source[i] = project(points[i], basis);
      double[] weights = new double[n];
      Arrays.fill(weights, 1);
      normal = normalMatrix(source, weights, scale);
      chord = EPS / minimumNorm;
      angular = 2 * Math.asin(chord / 2);
      HashMap<Long, ArrayList<Integer>> lookup = new HashMap<>();
      for (int i = 0; i < n; i++) {
        int x = (int) Math.floor(points[i][0] / CELL), y = (int) Math.floor(points[i][1] / CELL);
        int z = (int) Math.floor(points[i][2] / CELL);
        for (int dx = -1; dx <= 1; dx++)
          for (int dy = -1; dy <= 1; dy++)
            for (int dz = -1; dz <= 1; dz++) {
              long k = key(x + dx, y + dy, z + dz);
              ArrayList<Integer> list = lookup.get(k);
              if (list == null) {
                list = new ArrayList<>();
                lookup.put(k, list);
              }
              list.add(i);
            }
      }
      HashSet<String> accepted = new HashSet<>();
      for (int p = 0; p < n; p++) {
        for (int q = 0; q < n; q++) {
          if (p == q)
            continue;
          double sine = norm(cross(normalized[p], normalized[q]));
          double targetCosine = dot(normalized[p], normalized[q]);
          double tolerance = 2 * angular + ANGLE_ROUNDOFF;
          if (Math.abs(sine - scale) > tolerance || Math.abs(targetCosine - cosine) > tolerance)
            continue;
          double beta = Math.atan2(sine, targetCosine);
          if (sine == 0 || Math.abs(alpha - beta) > tolerance)
            continue;
          double[][] targetBasis = frame(points[p], points[q]);
          mapping = new int[n];
          boolean[] used = new boolean[n];
          int matched = 0;
          double worst = 0;
          for (double[] coordinate : source) {
            double[] rotated = unproject(coordinate, targetBasis);
            ArrayList<Integer> bucket = lookup.get(cell(rotated));
            double best = GATE * GATE;
            int closest = -1;
            if (bucket != null)
              for (int j : bucket) {
                double error = distance2(rotated, points[j]);
                if (error < best) {
                  best = error;
                  closest = j;
                }
              }
            if (closest < 0 || used[closest])
              break;
            used[closest] = true;
            mapping[matched++] = closest;
            worst = Math.max(worst, best);
          }
          if (matched != n)
            continue;
          char[] encoded = new char[n];
          for (int i = 0; i < n; i++) encoded[i] = (char) mapping[i];
          if (worst <= EPS2) {
            accepted.add(new String(encoded));
            continue;
          }
          targets = new double[n][];
          for (int i = 0; i < n; i++) targets[i] = project(points[mapping[i]], targetBasis);
          double twist = 2 * Math.asin(Math.min(1, chord / Math.sqrt(scale * sine)));
          if (feasible(twist))
            accepted.add(new String(encoded));
        }
      }
      return accepted.size();
    }
  }

  static class Input {
    BufferedInputStream in = new BufferedInputStream(System.in);
    String next() throws Exception {
      StringBuilder text = new StringBuilder();
      int c;
      do {
        c = in.read();
      } while (c >= 0 && Character.isWhitespace(c));
      while (c >= 0 && !Character.isWhitespace(c)) {
        text.append((char) c);
        c = in.read();
      }
      return text.toString();
    }
  }

  public static void main(String[] args) throws Exception {
    Input in = new Input();
    String first = in.next();
    if (first.isEmpty())
      return;
    int n = Integer.parseInt(first);
    double[][] points = new double[n][DIMENSION];
    for (int i = 0; i < n; i++)
      for (int j = 0; j < DIMENSION; j++) points[i][j] = Double.parseDouble(in.next());
    System.out.println(new Solver(points).count());
  }
}
