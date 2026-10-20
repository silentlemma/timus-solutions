import java.io.BufferedInputStream;
import java.io.IOException;
import java.util.Arrays;
import java.util.Comparator;

public class Main {
    private static final int BUFFER_SIZE = 1 << 16;

    private static class FastInput {
        private final BufferedInputStream input = new BufferedInputStream(System.in, BUFFER_SIZE);

        long integer() throws IOException {
            int c;
            do {
                c = input.read();
            } while (c <= ' ');
            long sign = 1;
            if (c == '-') {
                sign = -1;
                c = input.read();
            }
            long value = 0;
            while (c >= '0' && c <= '9') {
                value = value * 10 + c - '0';
                c = input.read();
            }
            return value * sign;
        }
    }

    private static class Point {
        long x, y;
        int id;

        Point(long x, long y, int id) {
            this.x = x;
            this.y = y;
            this.id = id;
        }
    }

    private static int[] chainSizes(Point[] p, int[] left, int[] right, int[] order,
                                    int[] size, int turn) {
        int n = p.length;
        int[] head = new int[n + 1], tail = new int[n + 1], count = new int[n + 1];
        int[] previous = new int[n], following = new int[n];
        Arrays.fill(head, n);
        Arrays.fill(tail, n);
        Arrays.fill(previous, n);
        Arrays.fill(following, n);
        for (int k = n - 1; k >= 0; --k) {
            int v = order[k], a = left[v], b = right[v];
            boolean forward = size[a] >= size[b];
            int base = forward ? a : b, small = forward ? b : a;
            int[] back = forward ? previous : following;
            int[] ahead = forward ? following : previous;
            int start = forward ? head[base] : tail[base];
            int end = forward ? tail[base] : head[base];
            int other = forward ? head[small] : tail[small];
            int sign = forward ? turn : -turn, length = count[base];
            // Reuse the larger subtree's chain and insert from its nearer end.
            for (int c = v; c != n;) {
                int next = c == v ? other : ahead[c];
                while (length >= 2) {
                    a = back[end];
                    long cross = (p[end].x - p[a].x) * (p[c].y - p[a].y)
                        - (p[end].y - p[a].y) * (p[c].x - p[a].x);
                    if (cross * sign > 0) {
                        break;
                    }
                    end = a;
                    --length;
                }
                if (length != 0) {
                    ahead[end] = c;
                } else {
                    start = c;
                }
                back[c] = end;
                ahead[c] = n;
                end = c;
                ++length;
                c = next;
            }
            head[v] = forward ? start : end;
            tail[v] = forward ? end : start;
            count[v] = length;
        }
        return count;
    }

    public static void main(String[] args) throws IOException {
        FastInput input = new FastInput();
        int n = (int) input.integer();
        Point[] p = new Point[n];
        for (int i = 0; i < n; ++i) {
            p[i] = new Point(input.integer(), input.integer(), i);
        }
        Arrays.sort(p, Comparator.comparingLong(a -> a.x));
        int[] left = new int[n], right = new int[n], stack = new int[n];
        Arrays.fill(left, n);
        Arrays.fill(right, n);
        int top = 0;
        for (int v = 0; v < n; ++v) {
            int last = n;
            while (top != 0 && p[stack[top - 1]].y < p[v].y) {
                last = stack[--top];
            }
            left[v] = last;
            if (top != 0) {
                right[stack[top - 1]] = v;
            }
            stack[top++] = v;
        }
        int root = stack[0];
        top = 0;
        stack[top++] = root;
        int[] order = new int[n], size = new int[n + 1];
        int used = 0;
        while (top != 0) {
            int v = stack[--top];
            order[used++] = v;
            if (left[v] != n) {
                stack[top++] = left[v];
            }
            if (right[v] != n) {
                stack[top++] = right[v];
            }
        }
        for (int k = n - 1; k >= 0; --k) {
            int v = order[k];
            size[v] = size[left[v]] + size[right[v]] + 1;
        }
        int[] lower = chainSizes(p, left, right, order, size, 1);
        int[] upper = chainSizes(p, left, right, order, size, -1);
        int[] answer = new int[n];
        for (int v = 0; v < n; ++v) {
            answer[p[v].id] = Math.max(1, lower[v] + upper[v] - 2);
        }
        StringBuilder output = new StringBuilder();
        for (int value : answer) {
            output.append(value).append('\n');
        }
        System.out.print(output);
    }
}
