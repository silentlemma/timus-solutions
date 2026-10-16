import java.util.ArrayList;
import java.util.Arrays;
import java.util.BitSet;
import java.util.List;
import java.util.Scanner;

public class Main {
    static int[] t, index, low, group;
    static double[] p;
    static boolean[] onStack;
    static int[][] deps;
    static List<List<Integer>> groups = new ArrayList<>();
    static int[] stack;
    static int top = 0, counter = 0;

    // hypotheses on one cycle of dependencies are all true or all false,
    // and Tarjan's method finds those groups, dependencies first
    static void visit(int v) {
        index[v] = low[v] = counter++;
        stack[top++] = v;
        onStack[v] = true;
        for (int w : deps[v]) {
            if (index[w] < 0) {
                visit(w);
                low[v] = Math.min(low[v], low[w]);
            } else if (onStack[w]) {
                low[v] = Math.min(low[v], index[w]);
            }
        }
        if (low[v] == index[v]) {
            List<Integer> members = new ArrayList<>();
            while (true) {
                int w = stack[--top];
                onStack[w] = false;
                group[w] = groups.size();
                members.add(w);
                if (w == v) {
                    break;
                }
            }
            groups.add(members);
        }
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        t = new int[n];
        p = new double[n];
        deps = new int[n][];
        for (int i = 0; i < n; i++) {
            t[i] = in.nextInt();
            p[i] = Double.parseDouble(in.next());
            deps[i] = new int[in.nextInt()];
            for (int j = 0; j < deps[i].length; j++) {
                deps[i][j] = in.nextInt() - 1;
            }
        }
        index = new int[n];
        low = new int[n];
        group = new int[n];
        onStack = new boolean[n];
        stack = new int[n];
        Arrays.fill(index, -1);
        for (int v = 0; v < n; v++) {
            if (index[v] < 0) {
                visit(v);
            }
        }
        // a group is worth checking only when every group it rests on is
        // fully admissible; inside it, checks stop at the first failure, so
        // the order by t / (1 - p) is the cheapest
        int count = groups.size();
        double[] cost = new double[count], sound = new double[count];
        BitSet[] reach = new BitSet[count];
        for (int g = 0; g < count; g++) {
            List<Integer> members = groups.get(g);
            members.sort((a, b) -> Double.compare(t[a] * (1 - p[b]), t[b] * (1 - p[a])));
            double still = 1, expected = 0;
            for (int v : members) {
                expected += still * t[v];
                still *= p[v];
            }
            cost[g] = expected;
            sound[g] = still;
            reach[g] = new BitSet(count);
            for (int v : members) {
                for (int w : deps[v]) {
                    if (group[w] != g) {
                        reach[g].or(reach[group[w]]);
                        reach[g].set(group[w]);
                    }
                }
            }
        }
        double answer = 0;
        for (int g = 0; g < count; g++) {
            double chance = 1;
            for (int h = reach[g].nextSetBit(0); h >= 0; h = reach[g].nextSetBit(h + 1)) {
                chance *= sound[h];
            }
            answer += chance * cost[g];
        }
        System.out.printf("%.3f%n", answer);
    }
}
