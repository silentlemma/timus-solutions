import java.util.*;

public class Main {
    static final int CORNERS = 4; // cells in a group of mirror positions
    static final int INF = 1 << 29;
    static final int LETTERS = 26;

    // the least total cost of giving each row its own column of a square matrix,
    // by the potentials method in O(n^3)
    static int hungarian(int[][] cost) {
        int n = cost.length;
        int[] u = new int[n + 1], v = new int[n + 1], owner = new int[n + 1], prev = new int[n + 1];
        for (int row = 1; row <= n; row++) {
            owner[0] = row;
            int col0 = 0;
            int[] least = new int[n + 1];
            Arrays.fill(least, INF);
            boolean[] used = new boolean[n + 1];
            while (owner[col0] != 0) {
                used[col0] = true;
                int r = owner[col0], delta = INF, col1 = 0;
                for (int c = 1; c <= n; c++)
                    if (!used[c]) {
                        int reduced = cost[r - 1][c - 1] - u[r] - v[c];
                        if (reduced < least[c]) {
                            least[c] = reduced;
                            prev[c] = col0;
                        }
                        if (least[c] < delta) {
                            delta = least[c];
                            col1 = c;
                        }
                    }
                for (int c = 0; c <= n; c++)
                    if (used[c]) {
                        u[owner[c]] += delta;
                        v[c] -= delta;
                    } else
                        least[c] -= delta;
                col0 = col1;
            }
            while (col0 != 0) {
                int col1 = prev[col0];
                owner[col0] = owner[col1];
                col0 = col1;
            }
        }
        return -v[0];
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt(), m = in.nextInt();
        String[] grid = new String[n];
        for (int i = 0; i < n; i++)
            grid[i] = in.next();
        // every row and column symmetric means the four mirror images of a cell
        // hold one kind of statue; each group then gets one kind
        List<char[]> groups = new ArrayList<>();
        for (int i = 0; i < n / 2; i++)
            for (int j = 0; j < m / 2; j++)
                groups.add(new char[] {grid[i].charAt(j), grid[i].charAt(m - 1 - j),
                                       grid[n - 1 - i].charAt(j),
                                       grid[n - 1 - i].charAt(m - 1 - j)});
        // a kind with c statues fills c / 4 groups; one column per such place
        int[] count = new int[LETTERS];
        for (String row : grid)
            for (char c : row.toCharArray())
                count[c - 'a']++;
        List<Character> slots = new ArrayList<>();
        for (int k = 0; k < LETTERS; k++)
            for (int t = 0; t < count[k] / CORNERS; t++)
                slots.add((char)('a' + k));
        // a statue not already in place is carried once, and a cycle of k statues
        // takes k carries, so the answer is the number of statues that change
        int[][] cost = new int[groups.size()][slots.size()];
        for (int g = 0; g < groups.size(); g++)
            for (int s = 0; s < slots.size(); s++) {
                int same = 0;
                for (char c : groups.get(g))
                    if (c == slots.get(s))
                        same++;
                cost[g][s] = CORNERS - same;
            }
        System.out.println(hungarian(cost));
    }
}
