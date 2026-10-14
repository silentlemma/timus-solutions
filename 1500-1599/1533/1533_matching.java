import java.io.*;
import java.util.*;

public class Main {
    static int n;
    static boolean[][] heavier; // heavier[i][j]: hobbit i is known to outweigh j
    static int[] matchOf;       // the heavier hobbit matched to a lighter one
    static boolean[] seen;

    static boolean augment(int i) {
        for (int j = 0; j < n; j++)
            if (heavier[i][j] && !seen[j]) {
                seen[j] = true;
                if (matchOf[j] < 0 || augment(matchOf[j])) {
                    matchOf[j] = i;
                    return true;
                }
            }
        return false;
    }

    public static void main(String[] args) throws IOException {
        StreamTokenizer st =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        st.nextToken();
        n = (int)st.nval;
        heavier = new boolean[n][n];
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++) {
                st.nextToken();
                heavier[i][j] = st.nval == 1;
            }
        // the weighings are consistent, so the closure is a strict order
        for (int k = 0; k < n; k++)
            for (int i = 0; i < n; i++)
                if (heavier[i][k])
                    for (int j = 0; j < n; j++)
                        heavier[i][j] |= heavier[k][j];
        // by Dilworth, the largest set of incomparable hobbits is n minus a
        // maximum matching between "heavier" copies and "lighter" copies
        matchOf = new int[n];
        Arrays.fill(matchOf, -1);
        boolean[] matched = new boolean[n];
        for (int i = 0; i < n; i++) {
            seen = new boolean[n];
            matched[i] = augment(i);
        }
        // Konig: walk alternating paths from the unmatched heavier copies; the
        // hobbits reached on the heavier side but not on the lighter side form
        // the answer, as everything else is a vertex cover
        boolean[] left = new boolean[n], right = new boolean[n];
        ArrayDeque<Integer> stack = new ArrayDeque<>();
        for (int i = 0; i < n; i++)
            if (!matched[i]) {
                left[i] = true;
                stack.push(i);
            }
        while (!stack.isEmpty()) {
            int i = stack.pop();
            for (int j = 0; j < n; j++)
                if (heavier[i][j] && !right[j]) {
                    right[j] = true;
                    int owner = matchOf[j];
                    if (owner >= 0 && !left[owner]) {
                        left[owner] = true;
                        stack.push(owner);
                    }
                }
        }
        StringBuilder list = new StringBuilder();
        int count = 0;
        for (int i = 0; i < n; i++)
            if (left[i] && !right[i]) {
                list.append(count++ > 0 ? " " : "").append(i + 1);
            }
        System.out.println(count);
        System.out.println(list);
    }
}
