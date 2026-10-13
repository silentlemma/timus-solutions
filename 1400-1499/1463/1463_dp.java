import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Main {
    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        int n = (int)in.nval;
        in.nextToken();
        int k = (int)in.nval;
        long[] joy = new long[n + 1];
        for (int i = 1; i <= n; i++) {
            in.nextToken();
            joy[i] = (long)in.nval;
        }
        int[] head = new int[n + 1], next = new int[2 * k], to = new int[2 * k];
        long[] gain = new long[2 * k];
        java.util.Arrays.fill(head, -1);
        for (int i = 0; i < 2 * k; i += 2) {
            in.nextToken();
            int a = (int)in.nval;
            in.nextToken();
            int b = (int)in.nval;
            in.nextToken();
            long c = (long)in.nval;
            to[i] = b;
            gain[i] = c;
            next[i] = head[a];
            head[a] = i;
            to[i + 1] = a;
            gain[i + 1] = c;
            next[i + 1] = head[b];
            head[b] = i + 1;
        }
        // down[v]: the best route that starts at v and goes away from its parent,
        // nxt[v] the next city on it; the routes are in a forest, so each tree once
        long[] down = joy.clone();
        int[] nxt = new int[n + 1], parent = new int[n + 1];
        java.util.Arrays.fill(parent, -1);
        long best = -1;
        int center = 0, endA = 0, endB = 0;
        int[] order = new int[n], stack = new int[n];
        for (int root = 1; root <= n; root++) {
            if (parent[root] != -1)
                continue;
            parent[root] = 0;
            int size = 0, top = 0;
            stack[top++] = root;
            while (top > 0) {
                int v = stack[--top];
                order[size++] = v;
                for (int e = head[v]; e != -1; e = next[e])
                    if (parent[to[e]] == -1) {
                        parent[to[e]] = v;
                        stack[top++] = to[e];
                    }
            }
            for (int i = size - 1; i >= 0; i--) {
                int v = order[i];
                long firstValue = 0, secondValue = 0; // the best two routes through children
                int firstChild = 0, secondChild = 0;
                for (int e = head[v]; e != -1; e = next[e]) {
                    int w = to[e];
                    if (w == parent[v])
                        continue;
                    long value = gain[e] + down[w];
                    if (value > firstValue || (value == firstValue && w > firstChild)) {
                        secondValue = firstValue;
                        secondChild = firstChild;
                        firstValue = value;
                        firstChild = w;
                    } else if (value > secondValue || (value == secondValue && w > secondChild)) {
                        secondValue = value;
                        secondChild = w;
                    }
                }
                down[v] = joy[v] + firstValue;
                nxt[v] = firstChild;
                if (joy[v] + firstValue + secondValue > best) {
                    best = joy[v] + firstValue + secondValue;
                    center = v;
                    endA = firstChild;
                    endB = secondChild;
                }
            }
        }
        List<Integer> route = new ArrayList<>();
        for (int a = endA; a != 0; a = nxt[a])
            route.add(a);
        Collections.reverse(route);
        route.add(center);
        for (int b = endB; b != 0; b = nxt[b])
            route.add(b);
        StringBuilder out = new StringBuilder();
        out.append(best).append('\n').append(route.size()).append('\n');
        for (int i = 0; i < route.size(); i++)
            out.append(route.get(i)).append(i + 1 == route.size() ? '\n' : ' ');
        System.out.print(out);
    }
}
