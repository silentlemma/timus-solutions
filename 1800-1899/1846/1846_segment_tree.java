import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;
import java.util.ArrayDeque;
import java.util.HashMap;
import java.util.Map;

public class Main {
    static StreamTokenizer input =
        new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));

    static int number() throws IOException {
        input.nextToken();
        return (int)input.nval;
    }

    static int sign() throws IOException { return input.nextToken(); }

    static int gcd(int a, int b) {
        while (b != 0) {
            int t = a % b;
            a = b;
            b = t;
        }
        return a;
    }

    public static void main(String[] args) throws IOException {
        input.ordinaryChar('-');
        int q = number();
        int size = 1;
        while (size < q) {
            size *= 2;
        }
        // every addition gets its own leaf; an empty leaf holds 0, which
        // does not change a gcd
        int[] tree = new int[2 * size];
        Map<Integer, ArrayDeque<Integer>> leaves = new HashMap<>();
        StringBuilder out = new StringBuilder();
        for (int k = 0; k < q; k++) {
            int operation = sign();
            int x = number();
            int v;
            int value = 0;
            if (operation == '+') {
                ArrayDeque<Integer> held = leaves.get(x);
                if (held == null) {
                    held = new ArrayDeque<>();
                    leaves.put(x, held);
                }
                held.push(k);
                v = k + size;
                value = x;
            } else {
                v = leaves.get(x).pop() + size;
            }
            tree[v] = value;
            // once a node keeps its value, so do all above it
            for (v /= 2; v > 0; v /= 2) {
                int g = gcd(tree[2 * v], tree[2 * v + 1]);
                if (tree[v] == g) {
                    break;
                }
                tree[v] = g;
            }
            out.append(tree[1] == 0 ? 1 : tree[1]).append('\n');
        }
        System.out.print(out);
    }
}
