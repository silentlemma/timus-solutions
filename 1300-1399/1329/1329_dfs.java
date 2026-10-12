import java.io.IOException;
import java.util.Arrays;

public class Main {
    static final int IDS = 40001;
    static final int BUFFER = 1 << 16;
    static byte[] buffer = new byte[BUFFER];
    static int length = 0, position = 0;

    static int read() throws IOException {
        if (position == length) {
            length = System.in.read(buffer, 0, BUFFER);
            position = 0;
            if (length <= 0)
                return -1;
        }
        return buffer[position++];
    }

    static int next() throws IOException {
        int c = read();
        while (c != '-' && (c < '0' || c > '9')) {
            if (c < 0)
                return 0;
            c = read();
        }
        boolean negative = c == '-';
        if (negative)
            c = read();
        int value = 0;
        while (c >= '0' && c <= '9') {
            value = value * 10 + (c - '0');
            c = read();
        }
        return negative ? -value : value;
    }

    public static void main(String[] args) throws IOException {
        int n = next();
        int[] parentOf = new int[n], nodes = new int[n], childCount = new int[IDS + 1];
        int root = -1;
        for (int i = 0; i < n; i++) {
            nodes[i] = next();
            parentOf[i] = next();
            if (parentOf[i] < 0)
                root = nodes[i];
            else
                childCount[parentOf[i] + 1]++;
        }
        // children of each node in one array, cut by their counts
        for (int v = 0; v < IDS; v++)
            childCount[v + 1] += childCount[v];
        int[] first = childCount.clone(), children = new int[n];
        for (int i = 0; i < n; i++) {
            if (parentOf[i] >= 0)
                children[first[parentOf[i]]++] = nodes[i];
        }
        // enter[v] and leave[v] bound the times of the whole subtree of v
        int[] enter = new int[IDS], leave = new int[IDS], stack = new int[2 * n + 1];
        Arrays.fill(enter, -1);
        Arrays.fill(leave, -1);
        int clock = 0, top = 0;
        stack[top++] = root;
        while (top > 0) {
            int node = stack[--top];
            if (node >= 0) {
                enter[node] = clock++;
                stack[top++] = ~node;
                for (int k = childCount[node]; k < childCount[node + 1]; k++)
                    stack[top++] = children[k];
            } else {
                leave[~node] = clock;
            }
        }
        int queries = next();
        StringBuilder out = new StringBuilder();
        for (int i = 0; i < queries; i++) {
            int a = next(), b = next();
            if (enter[a] >= 0 && enter[a] <= enter[b] && enter[b] < leave[a])
                out.append("1\n");
            else if (enter[b] >= 0 && enter[b] <= enter[a] && enter[a] < leave[b])
                out.append("2\n");
            else
                out.append("0\n");
        }
        System.out.print(out);
    }
}
