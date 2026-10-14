import java.util.*;

public class Main {
    static final int CELLS = 4;   // the program needs at most four cells
    static final int VALUES = 27; // a cell holds 0 or a letter, kept as 0 or 1 to 26
    static final int OTHERS = VALUES * VALUES * VALUES; // states of the cells away from the pointer
    static final int STATES = CELLS * OTHERS;
    static final int LETTER_BASE = 'a' - 1;
    static final int UNREACHABLE = 1 << 30;

    static String repeat(char c, int times) {
        char[] a = new char[times];
        Arrays.fill(a, c);
        return new String(a);
    }

    public static void main(String[] args) {
        String s = new Scanner(System.in).next();
        // a state, after a letter is printed, is the pointer's cell (holding that
        // letter) and the values of the other three cells, left to right; the
        // used cells form a block of four that holds the start cell somewhere
        int[] cost = new int[STATES];
        Arrays.fill(cost, UNREACHABLE);
        for (int start = 0; start < CELLS; start++)
            cost[start * OTHERS] = 0;
        List<int[]> cameFrom = new ArrayList<>();
        int previous = 0; // the value under the pointer: 0 before the first letter
        int[] w = new int[CELLS];
        for (char c : s.toCharArray()) {
            int letter = c - LETTER_BASE;
            int[] next = new int[STATES], back = new int[STATES];
            Arrays.fill(next, UNREACHABLE);
            for (int state = 0; state < STATES; state++) {
                int here = cost[state];
                if (here == UNREACHABLE)
                    continue;
                int p = state / OTHERS, rest = state % OTHERS;
                int[] digits = {rest / (VALUES * VALUES), rest / VALUES % VALUES, rest % VALUES};
                for (int cell = 0, k = 0; cell < CELLS; cell++)
                    w[cell] = cell == p ? previous : digits[k++];
                for (int q = 0; q < CELLS; q++) {
                    int change = w[q] != 0 ? letter - w[q] : letter + LETTER_BASE;
                    int total = here + Math.abs(p - q) + Math.abs(change) + 1;
                    int code = 0;
                    for (int cell = 0; cell < CELLS; cell++)
                        if (cell != q)
                            code = code * VALUES + w[cell];
                    code += q * OTHERS;
                    if (total < next[code]) {
                        next[code] = total;
                        back[code] = state;
                    }
                }
            }
            cameFrom.add(back);
            cost = next;
            previous = letter;
        }
        // walk back to recover the cells used, then write the program
        int state = 0;
        for (int st = 0; st < STATES; st++)
            if (cost[st] < cost[state])
                state = st;
        int n = s.length();
        int[] used = new int[n + 1];
        for (int i = n; i > 0; i--) {
            used[i] = state / OTHERS;
            state = cameFrom.get(i - 1)[state];
        }
        used[0] = state / OTHERS;
        int[] held = new int[CELLS];
        StringBuilder out = new StringBuilder();
        for (int i = 0; i < n; i++) {
            int p = used[i], q = used[i + 1], letter = s.charAt(i) - LETTER_BASE;
            out.append(repeat(q > p ? '>' : '<', Math.abs(q - p)));
            int change = held[q] != 0 ? letter - held[q] : letter + LETTER_BASE;
            out.append(repeat(change > 0 ? '+' : '-', Math.abs(change))).append('.');
            held[q] = letter;
        }
        System.out.println(out);
    }
}
