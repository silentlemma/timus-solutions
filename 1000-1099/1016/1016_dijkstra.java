import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.PriorityQueue;
import java.util.Scanner;

public class Main {
    static final int SIZE = 8, FACES = 6, DIRECTIONS = 4, BOTTOM = 4;
    static final long INF = 1L << 60;
    // faces in the input order near, far, top, right, bottom, left; a roll in
    // direction d puts the face from position SOURCE[d][i] to position i
    static final int[] DX = {0, 0, 1, -1}, DY = {1, -1, 0, 0};
    static final int[][] SOURCE = {
        {4, 2, 0, 3, 1, 5}, {2, 4, 1, 3, 0, 5}, {0, 1, 5, 2, 3, 4}, {0, 1, 3, 4, 5, 2}};

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String from = in.next(), to = in.next();
        long[] value = new long[FACES];
        for (int i = 0; i < FACES; i++) {
            value[i] = in.nextLong();
        }

        // the 24 orientations: which original face is at each position
        int[] identity = new int[FACES];
        for (int i = 0; i < FACES; i++) {
            identity[i] = i;
        }
        List<int[]> orient = new ArrayList<>();
        Map<String, Integer> id = new HashMap<>();
        orient.add(identity);
        id.put(Arrays.toString(identity), 0);
        List<int[]> next = new ArrayList<>();
        for (int o = 0; o < orient.size(); o++) {
            int[] step = new int[DIRECTIONS];
            for (int d = 0; d < DIRECTIONS; d++) {
                int[] r = new int[FACES];
                for (int i = 0; i < FACES; i++) {
                    r[i] = orient.get(o)[SOURCE[d][i]];
                }
                String key = Arrays.toString(r);
                if (!id.containsKey(key)) {
                    id.put(key, orient.size());
                    orient.add(r);
                }
                step[d] = id.get(key);
            }
            next.add(step);
        }

        // Dijkstra over (cell, orientation); a state costs its bottom face
        int m = orient.size(), states = SIZE * SIZE * m;
        long[] dist = new long[states];
        int[] prev = new int[states];
        Arrays.fill(dist, INF);
        Arrays.fill(prev, -1);
        int sx = from.charAt(0) - 'a', sy = from.charAt(1) - '1';
        int tx = to.charAt(0) - 'a', ty = to.charAt(1) - '1';
        int first = (sx * SIZE + sy) * m;
        dist[first] = value[orient.get(0)[BOTTOM]];
        PriorityQueue<long[]> heap = new PriorityQueue<>((a, b) -> Long.compare(a[0], b[0]));
        heap.add(new long[] {dist[first], first});
        while (!heap.isEmpty()) {
            long[] top = heap.poll();
            int s = (int)top[1];
            if (top[0] > dist[s]) {
                continue;
            }
            int o = s % m, x = s / m / SIZE, y = s / m % SIZE;
            for (int k = 0; k < DIRECTIONS; k++) {
                int nx = x + DX[k], ny = y + DY[k];
                if (nx < 0 || ny < 0 || nx >= SIZE || ny >= SIZE) {
                    continue;
                }
                int no = next.get(o)[k], ns = (nx * SIZE + ny) * m + no;
                long nd = top[0] + value[orient.get(no)[BOTTOM]];
                if (nd < dist[ns]) {
                    dist[ns] = nd;
                    prev[ns] = s;
                    heap.add(new long[] {nd, ns});
                }
            }
        }

        int best = (tx * SIZE + ty) * m;
        for (int o = 0; o < m; o++) {
            if (dist[(tx * SIZE + ty) * m + o] < dist[best]) {
                best = (tx * SIZE + ty) * m + o;
            }
        }
        List<String> route = new ArrayList<>();
        for (int s = best; s >= 0; s = prev[s]) {
            int c = s / m;
            route.add(0, "" + (char)('a' + c / SIZE) + (char)('1' + c % SIZE));
        }
        System.out.println(dist[best] + " " + String.join(" ", route));
    }
}
