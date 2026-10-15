import java.io.DataInputStream;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.Arrays;
import java.util.PriorityQueue;

public class Main {
    static final long FAR = Long.MAX_VALUE;
    static final int FACE_BITS = 17; // fewer faces than 2^17: a distance and a face share a long
    static final int BUFFER = 1 << 16;

    static DataInputStream in = new DataInputStream(System.in);
    static byte[] buffer = new byte[BUFFER];
    static int length;
    static int index;

    static int readByte() throws IOException {
        if (index == length) {
            length = in.read(buffer, 0, BUFFER);
            index = 0;
            if (length <= 0) {
                return -1;
            }
        }
        return buffer[index++];
    }

    static long readLong() throws IOException {
        int c = readByte();
        while (c != '-' && (c < '0' || c > '9')) {
            c = readByte();
        }
        boolean negative = c == '-';
        if (negative) {
            c = readByte();
        }
        long value = 0;
        while (c >= '0' && c <= '9') {
            value = value * 10 + (c - '0');
            c = readByte();
        }
        return negative ? -value : value;
    }

    public static void main(String[] args) throws IOException {
        int n = (int) readLong();
        long[] xs = new long[n];
        long[] ys = new long[n];
        for (int i = 0; i < n; i++) {
            xs[i] = readLong();
            ys[i] = readLong();
        }
        int m = (int) readLong();
        // half-edge 2i runs from ends[i] to tips[i], 2i + 1 back; pipe m is an
        // extra edge from the source, leaving to the left, round the outside to
        // the sink, arriving from the right
        int[] ends = new int[m + 1];
        int[] tips = new int[m + 1];
        long[] caps = new long[m];
        for (int i = 0; i < m; i++) {
            ends[i] = (int) readLong() - 1;
            tips[i] = (int) readLong() - 1;
            caps[i] = readLong();
        }
        ends[m] = 0;
        tips[m] = n - 1;
        int halves = 2 * m + 2;
        int[] origin = new int[halves];
        long[] dx = new long[halves];
        long[] dy = new long[halves];
        for (int i = 0; i <= m; i++) {
            int a = ends[i];
            int b = tips[i];
            origin[2 * i] = a;
            origin[2 * i + 1] = b;
            dx[2 * i] = xs[b] - xs[a];
            dy[2 * i] = ys[b] - ys[a];
            dx[2 * i + 1] = -dx[2 * i];
            dy[2 * i + 1] = -dy[2 * i];
        }
        dx[2 * m] = -1;
        dy[2 * m] = 0;
        dx[2 * m + 1] = 1;
        dy[2 * m + 1] = 0;
        // half-edges by origin, then counterclockwise from the +x axis, exactly
        Integer[] order = new Integer[halves];
        for (int h = 0; h < halves; h++) {
            order[h] = h;
        }
        Arrays.sort(order, (g, h) -> {
            if (origin[g] != origin[h]) {
                return Integer.compare(origin[g], origin[h]);
            }
            boolean lowG = dy[g] < 0 || (dy[g] == 0 && dx[g] < 0);
            boolean lowH = dy[h] < 0 || (dy[h] == 0 && dx[h] < 0);
            if (lowG != lowH) {
                return lowG ? 1 : -1;
            }
            return -Long.signum(dx[g] * dy[h] - dy[g] * dx[h]);
        });
        int[] first = new int[n + 1];
        int[] pos = new int[halves];
        int[] sorted = new int[halves];
        for (int k = 0; k < halves; k++) {
            sorted[k] = order[k];
            pos[order[k]] = k;
            first[origin[order[k]] + 1] = k + 1;
        }
        for (int v = 1; v <= n; v++) {
            first[v] = Math.max(first[v], first[v - 1]);
        }
        // faces: after arriving at a vertex, leave by the next edge clockwise
        int[] face = new int[halves];
        Arrays.fill(face, -1);
        int faces = 0;
        for (int h = 0; h < halves; h++) {
            if (face[h] >= 0) {
                continue;
            }
            for (int g = h; face[g] < 0;) {
                face[g] = faces;
                int back = g ^ 1;
                int v = origin[back];
                int k = pos[back] == first[v] ? first[v + 1] - 1 : pos[back] - 1;
                g = sorted[k];
            }
            faces++;
        }
        // the minimum cut is the shortest path between the two faces next to
        // the extra edge, with pipe capacities as lengths
        int[] degree = new int[faces + 1];
        for (int i = 0; i < m; i++) {
            degree[face[2 * i] + 1]++;
            degree[face[2 * i + 1] + 1]++;
        }
        for (int f = 0; f < faces; f++) {
            degree[f + 1] += degree[f];
        }
        int[] fill = Arrays.copyOf(degree, faces);
        int[] linkTo = new int[2 * m];
        long[] linkCap = new long[2 * m];
        for (int i = 0; i < m; i++) {
            int a = face[2 * i];
            int b = face[2 * i + 1];
            linkTo[fill[a]] = b;
            linkCap[fill[a]++] = caps[i];
            linkTo[fill[b]] = a;
            linkCap[fill[b]++] = caps[i];
        }
        long[] dist = new long[faces];
        Arrays.fill(dist, FAR);
        int start = face[2 * m];
        dist[start] = 0;
        PriorityQueue<Long> heap = new PriorityQueue<>();
        heap.add((long) start);
        long mask = (1L << FACE_BITS) - 1;
        while (!heap.isEmpty()) {
            long top = heap.poll();
            int f = (int) (top & mask);
            long d = top >>> FACE_BITS;
            if (d > dist[f]) {
                continue;
            }
            for (int k = degree[f]; k < degree[f + 1]; k++) {
                int g = linkTo[k];
                if (d + linkCap[k] < dist[g]) {
                    dist[g] = d + linkCap[k];
                    heap.add(dist[g] << FACE_BITS | g);
                }
            }
        }
        // the flow from ends[i] to tips[i] is the difference of the distances
        // of the faces on its two sides
        long[] flow = new long[m];
        long total = 0;
        for (int i = 0; i < m; i++) {
            long left = dist[face[2 * i]];
            long right = dist[face[2 * i + 1]];
            if (left != FAR && right != FAR) {
                flow[i] = right - left;
            }
            if (ends[i] == 0) {
                total += flow[i];
            } else if (tips[i] == 0) {
                total -= flow[i];
            }
        }
        long sign = total >= 0 ? 1 : -1;
        StringBuilder out = new StringBuilder();
        out.append(total * sign).append('\n');
        for (int i = 0; i < m; i++) {
            long f = flow[i] * sign;
            int from = f >= 0 ? ends[i] : tips[i];
            int to = f >= 0 ? tips[i] : ends[i];
            out.append(from + 1).append(' ').append(to + 1).append(' ');
            out.append(Math.abs(f)).append('\n');
        }
        PrintWriter writer = new PrintWriter(System.out);
        writer.print(out);
        writer.flush();
    }
}
