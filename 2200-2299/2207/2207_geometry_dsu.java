import java.io.BufferedInputStream;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;

public class Main {
    static final long INF = 10_000_000_000L;

    static class Input {
        final BufferedInputStream stream = new BufferedInputStream(System.in);

        int nextInt() throws IOException {
            int c;
            do {
                c = stream.read();
            } while (c <= ' ' && c != -1);
            int value = 0;
            while (c > ' ') {
                value = value * 10 + c - '0';
                c = stream.read();
            }
            return value;
        }
    }

    static class Dsu {
        final int[] parent;

        Dsu(int n) {
            parent = new int[n];
            Arrays.fill(parent, -1);
        }

        int find(int v) {
            if (parent[v] < 0) {
                return v;
            }
            parent[v] = find(parent[v]);
            return parent[v];
        }

        boolean join(int a, int b) {
            a = find(a);
            b = find(b);
            if (a == b) {
                return false;
            }
            if (parent[a] > parent[b]) {
                int swap = a;
                a = b;
                b = swap;
            }
            parent[a] += parent[b];
            parent[b] = a;
            return true;
        }
    }

    static class Sweep {
        final Integer[] order;
        final int[] rank;
        final long[] value;

        Sweep(long[] x, long[] y, long[] ys, int span, int sx, int sy) {
            int count = x.length;
            order = new Integer[count];
            rank = new int[count];
            value = new long[count + 1];
            value[count] = -INF;
            for (int i = 0; i < count; ++i) {
                order[i] = i;
                int r = Arrays.binarySearch(ys, 0, span, y[i]);
                rank[i] = sy == 1 ? r + 1 : span - r;
                value[i] = sx * x[i] + sy * y[i];
            }
            Arrays.sort(order, (a, b) -> {
                int cmp = Long.compare(sx * x[a], sx * x[b]);
                return cmp != 0 ? cmp : Long.compare(sy * y[a], sy * y[b]);
            });
        }
    }

    static class Edge {
        final long distance;
        final int u;
        final int v;

        Edge(long distance, int u, int v) {
            this.distance = distance;
            this.u = u;
            this.v = v;
        }
    }

    public static void main(String[] args) throws IOException {
        Input in = new Input();
        in.nextInt();
        in.nextInt();
        int n = in.nextInt();
        int m = in.nextInt();
        int count = n + m;
        long[] x = new long[count];
        long[] y = new long[count];
        long[] people = new long[count];
        long[] jobs = new long[count];
        long totalPeople = 0;
        long totalJobs = 0;
        for (int i = 0; i < count; ++i) {
            x[i] = in.nextInt();
            y[i] = in.nextInt();
            long amount = in.nextInt();
            if (i < n) {
                people[i] = amount;
                totalPeople += amount;
            } else {
                jobs[i] = amount;
                totalJobs += amount;
            }
        }
        long target = Math.min(totalPeople, totalJobs);
        long[] ys = y.clone();
        Arrays.sort(ys);
        int span = 0;
        for (long value : ys) {
            if (span == 0 || ys[span - 1] != value) {
                ys[span++] = value;
            }
        }
        List<Sweep> sweeps = new ArrayList<>();
        for (int sx : new int[] {1, -1}) {
            for (int sy : new int[] {1, -1}) {
                sweeps.add(new Sweep(x, y, ys, span, sx, sy));
            }
        }
        Dsu dsu = new Dsu(count);
        int components = count;
        List<Edge> edges = new ArrayList<>();
        while (components > 1) {
            int[] roots = new int[count + 1];
            int[] from = new int[count];
            int[] to = new int[count];
            long[] best = new long[count];
            Arrays.fill(from, -1);
            Arrays.fill(best, INF);
            roots[count] = -1;
            for (int i = 0; i < count; ++i) {
                roots[i] = dsu.find(i);
            }
            for (Sweep s : sweeps) {
                int[][] first = new int[2][span + 1];
                int[][] second = new int[2][span + 1];
                for (int color = 0; color < 2; ++color) {
                    Arrays.fill(first[color], count);
                    Arrays.fill(second[color], count);
                }
                for (int i : s.order) {
                    int color = i < n ? 0 : 1;
                    int root = roots[i];
                    int candidate = count;
                    for (int k = s.rank[i]; k > 0; k -= k & -k) {
                        int v = first[1 - color][k];
                        if (roots[v] == root) {
                            v = second[1 - color][k];
                        }
                        if (s.value[v] > s.value[candidate]) {
                            candidate = v;
                        }
                    }
                    if (candidate != count && s.value[i] - s.value[candidate] < best[root]) {
                        best[root] = s.value[i] - s.value[candidate];
                        from[root] = i;
                        to[root] = candidate;
                    }
                    // Keep maxima from two distinct frozen components.
                    for (int k = s.rank[i]; k <= span; k += k & -k) {
                        int v = first[color][k];
                        if (s.value[i] > s.value[v]) {
                            if (roots[v] != root) {
                                second[color][k] = v;
                            }
                            first[color][k] = i;
                        } else if (roots[v] != root && s.value[i] > s.value[second[color][k]]) {
                            second[color][k] = i;
                        }
                    }
                }
            }
            for (int r = 0; r < count; ++r) {
                if (from[r] != -1 && dsu.join(from[r], to[r])) {
                    edges.add(new Edge(best[r], from[r], to[r]));
                    --components;
                }
            }
        }
        edges.sort(Comparator.comparingLong(edge -> edge.distance));
        dsu = new Dsu(count);
        long score = 0;
        for (Edge edge : edges) {
            int a = dsu.find(edge.u);
            int b = dsu.find(edge.v);
            score -= Math.min(people[a], jobs[a]) + Math.min(people[b], jobs[b]);
            long population = people[a] + people[b];
            long capacity = jobs[a] + jobs[b];
            dsu.join(a, b);
            int root = dsu.find(a);
            people[root] = population;
            jobs[root] = capacity;
            score += Math.min(population, capacity);
            if (score == target) {
                System.out.println(target + " " + edge.distance);
                return;
            }
        }
    }
}
