import java.io.BufferedInputStream;
import java.io.IOException;
import java.util.Arrays;

public class Main {
    static final int SHAVES = 2;
    static final int MAX_TIME = 2000;
    static final int INPUT_SIZE = 4096;
    static final int OUTPUT_RESERVE = 1200;
    static final int DECIMAL_BASE = 10;

    static class Flow {
        final char[] to, next, cap, head, at, level, queue;
        int size = SHAVES;
        Flow(int nodes, int edgeCount) {
            to = new char[edgeCount];
            next = new char[edgeCount];
            cap = new char[edgeCount];
            head = new char[nodes];
            at = new char[nodes];
            level = new char[nodes];
            queue = new char[nodes];
        }
        void add(int a, int b, int capacity) {
            to[size] = (char)b;
            next[size] = head[a];
            cap[size] = (char)capacity;
            head[a] = (char)size++;
            to[size] = (char)a;
            next[size] = head[b];
            head[b] = (char)size++;
        }
        int push(int v, int sink, int limit) {
            if (v == sink)
                return limit;
            while (at[v] != 0) {
                int e = at[v], w = to[e];
                if (cap[e] != 0 && level[w] == level[v] + 1) {
                    int got = push(w, sink, Math.min(limit, cap[e]));
                    if (got != 0) {
                        cap[e] -= got;
                        cap[e ^ 1] += got;
                        return got;
                    }
                }
                at[v] = next[e];
            }
            return 0;
        }
        int solve(int sink, int need) {
            int total = 0;
            while (total < need) {
                Arrays.fill(level, (char)0);
                System.arraycopy(head, 0, at, 0, head.length);
                queue[0] = 0;
                level[0] = 1;
                int length = 1;
                for (int i = 0; i < length; i++) {
                    int v = queue[i];
                    for (int e = head[v]; e != 0; e = next[e]) {
                        int w = to[e];
                        if (cap[e] != 0 && level[w] == 0) {
                            level[w] = (char)(level[v] + 1);
                            queue[length++] = (char)w;
                        }
                    }
                }
                if (level[sink] == 0)
                    break;
                while (total < need) {
                    int got = push(0, sink, need - total);
                    if (got == 0)
                        break;
                    total += got;
                }
            }
            return total;
        }
    }

    static int number(BufferedInputStream input) throws IOException {
        int c = input.read();
        while (c >= 0 && c <= ' ')
            c = input.read();
        int value = 0;
        while (c >= '0' && c <= '9') {
            value = value * DECIMAL_BASE + c - '0';
            c = input.read();
        }
        return value;
    }

    public static void main(String[] args) throws IOException {
        BufferedInputStream input = new BufferedInputStream(System.in, INPUT_SIZE);
        int n = number(input), k = number(input);
        int[] start = new int[n], end = new int[n], cuts = new int[SHAVES * n];
        char[] index = new char[MAX_TIME + 1];
        for (int i = 0; i < n; i++) {
            start[i] = number(input);
            end[i] = start[i] + number(input);
            index[start[i]] = index[end[i]] = 1;
        }
        int count = 0;
        for (int t = 0; t <= MAX_TIME; t++)
            if (index[t] != 0) {
                index[t] = (char)count;
                cuts[count++] = t;
            }
        int blocks = count - 1, sink = n + blocks + 1, edgeCount = n + blocks;
        for (int i = 0; i < n; i++) {
            start[i] = index[start[i]];
            end[i] = index[end[i]];
            edgeCount += end[i] - start[i];
        }
        Flow flow = new Flow(sink + 1, SHAVES * (edgeCount + 1));
        for (int i = 0; i < n; i++) {
            flow.add(0, i + 1, SHAVES);
            for (int j = start[i]; j < end[i]; j++)
                flow.add(i + 1, n + j + 1, Math.min(SHAVES, cuts[j + 1] - cuts[j]));
        }
        for (int j = 0; j < blocks; j++)
            flow.add(n + j + 1, sink, Math.min(SHAVES * n, k * (cuts[j + 1] - cuts[j])));
        if (flow.solve(sink, SHAVES * n) < SHAVES * n) {
            System.out.println("No");
            return;
        }
        StringBuilder output = new StringBuilder(OUTPUT_RESERVE);
        output.append("Yes\n");
        int[] dealt = new int[blocks];
        for (int i = 1; i <= n; i++) {
            int[] times = new int[SHAVES];
            int used = 0;
            for (int e = flow.head[i]; e != 0; e = flow.next[e]) {
                int w = flow.to[e];
                if (w <= n || w >= sink)
                    continue;
                int block = w - n - 1;
                for (int j = flow.cap[e ^ 1]; j > 0; j--)
                    times[used++] = cuts[block] + dealt[block]++ % (cuts[block + 1] - cuts[block]);
            }
            if (times[0] > times[1]) {
                int temp = times[0];
                times[0] = times[1];
                times[1] = temp;
            }
            output.append(times[0]).append(' ').append(times[1]).append('\n');
        }
        System.out.print(output);
    }
}
