import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.List;

public class Main {
    // identification numbers are positive and below this bound, so 0 means none
    static final int LIMIT = 65536;

    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        int n = (int)in.nval;
        int[] post = new int[n];
        for (int k = 0; k < n; k++) {
            in.nextToken();
            post[k] = (int)in.nval;
        }
        // read backwards, the odd-session order gives every chairman, then the
        // right wing, then the left wing; a stack of the open chairmen rebuilds the
        // tree from that
        int[] left = new int[LIMIT], right = new int[LIMIT];
        ArrayDeque<Integer> stack = new ArrayDeque<>();
        for (int k = n - 1; k >= 0; k--) {
            int v = post[k];
            if (!stack.isEmpty() && v > stack.peek()) {
                right[stack.peek()] = v;
            } else if (!stack.isEmpty()) {
                int parent = stack.pop();
                while (!stack.isEmpty() && stack.peek() > v) {
                    parent = stack.pop();
                }
                left[parent] = v;
            }
            stack.push(v);
        }
        // the even-session order is the plain order root, left, right reversed
        List<Integer> order = new ArrayList<>();
        stack.clear();
        stack.push(post[n - 1]);
        while (!stack.isEmpty()) {
            int v = stack.pop();
            order.add(v);
            if (right[v] != 0) {
                stack.push(right[v]);
            }
            if (left[v] != 0) {
                stack.push(left[v]);
            }
        }
        StringBuilder out = new StringBuilder();
        for (int k = n - 1; k >= 0; k--) {
            out.append(order.get(k)).append('\n');
        }
        System.out.print(out);
    }
}
