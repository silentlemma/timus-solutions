import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;
import java.util.ArrayList;
import java.util.List;

public class Main {
    static final int LEAF = 0;
    static final int DIRECT = 1;
    static final int SKEW = 2;
    static final int TEXT = 0;
    static final int EXPR = 1;
    static final int SEQ = 2;

    static int[] kinds;
    static int[] lefts;
    static int[] rights;
    static int[] values;
    static int count;

    static int newNode(int kind, int left, int right, int value) {
        kinds[count] = kind;
        lefts[count] = left;
        rights[count] = right;
        values[count] = value;
        return count++;
    }

    // the children of the maximal run of nodes of the same kind below and
    // including node, in order of position (both joins are associative)
    static List<Integer> parts(int node) {
        List<Integer> out = new ArrayList<>();
        List<Integer> todo = new ArrayList<>();
        todo.add(node);
        while (!todo.isEmpty()) {
            int cur = todo.remove(todo.size() - 1);
            if (kinds[cur] == kinds[node]) {
                todo.add(rights[cur]);
                todo.add(lefts[cur]);
            } else {
                out.add(cur);
            }
        }
        return out;
    }

    // a direct node is a sequence of its parts; a skew node is its parts
    // joined by stars from the smallest values up; built without recursion,
    // as the tree can be 10^4 levels deep; a work item holds what, node and char
    static String show(int root) {
        StringBuilder out = new StringBuilder();
        List<int[]> work = new ArrayList<>();
        work.add(new int[] {EXPR, root, 0});
        while (!work.isEmpty()) {
            int[] item = work.remove(work.size() - 1);
            int node = item[1];
            if (item[0] == TEXT) {
                out.append((char) item[2]);
            } else if (kinds[node] == LEAF) {
                if (item[0] == EXPR) {
                    out.append(values[node]);
                } else {
                    out.append('(').append(values[node]).append(')');
                }
            } else if (kinds[node] == SKEW) {
                List<Integer> children = parts(node);
                // pushed in reverse: the largest values come out first as text
                for (int i = 0; i < children.size(); i++) {
                    if (i > 0) {
                        work.add(new int[] {TEXT, 0, '*'});
                    }
                    work.add(new int[] {SEQ, children.get(i), 0});
                }
            } else {
                List<Integer> children = parts(node);
                work.add(new int[] {TEXT, 0, ')'});
                for (int i = children.size() - 1; i >= 0; i--) {
                    work.add(new int[] {EXPR, children.get(i), 0});
                    work.add(new int[] {TEXT, 0, i > 0 ? ',' : '('});
                }
            }
        }
        // a lone number at the top must still be a sequence
        return kinds[root] == LEAF ? "(" + out + ")" : out.toString();
    }

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StreamTokenizer in = new StreamTokenizer(reader);
        in.nextToken();
        int n = (int) in.nval;
        kinds = new int[2 * n];
        lefts = new int[2 * n];
        rights = new int[2 * n];
        values = new int[2 * n];
        // blocks of consecutive positions holding consecutive values, as
        // {lowest value, highest value, tree}; two neighbours whose value
        // ranges touch join into one block
        List<int[]> stack = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            in.nextToken();
            int v = (int) in.nval;
            int[] cur = {v, v, newNode(LEAF, -1, -1, v)};
            while (!stack.isEmpty()) {
                int[] prev = stack.get(stack.size() - 1);
                if (prev[1] + 1 == cur[0]) {
                    cur[2] = newNode(DIRECT, prev[2], cur[2], 0);
                } else if (cur[1] + 1 == prev[0]) {
                    cur[2] = newNode(SKEW, prev[2], cur[2], 0);
                } else {
                    break;
                }
                stack.remove(stack.size() - 1);
                cur[0] = Math.min(cur[0], prev[0]);
                cur[1] = Math.max(cur[1], prev[1]);
            }
            stack.add(cur);
        }
        System.out.println(stack.size() == 1 ? show(stack.get(0)[2]) : "IMPOSSIBLE");
    }
}
