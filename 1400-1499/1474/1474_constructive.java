import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
    static final int EMPTY = 0, WHITE = 1, BLACK = 2;

    public static void main(String[] args) {
        int n = new Scanner(System.in).nextInt();
        int[] hummocks = new int[2 * n + 1];
        for (int i = 0; i <= 2 * n; i++)
            hummocks[i] = i < n ? WHITE : BLACK;
        hummocks[n] = EMPTY;
        int hole = n;
        // runs of 1, 2, ..., n, n, n, ..., 1 moves, the colours taking turns,
        // and in a run a frog jumps into the hole when it can and slides otherwise
        List<Integer> runs = new ArrayList<>();
        for (int i = 1; i <= n; i++)
            runs.add(i);
        runs.add(n);
        for (int i = n; i >= 1; i--)
            runs.add(i);
        StringBuilder out = new StringBuilder();
        int count = 0, colour = BLACK;
        for (int run : runs) {
            int step = colour == BLACK ? 1 : -1; // where the frogs come from
            int other = colour == BLACK ? WHITE : BLACK;
            for (int k = 0; k < run; k++) {
                int far = hole + 2 * step, near = hole + step;
                boolean jump =
                    far >= 0 && far <= 2 * n && hummocks[far] == colour && hummocks[near] == other;
                int frog = jump ? far : near;
                hummocks[hole] = colour;
                hummocks[frog] = EMPTY;
                hole = frog;
                out.append(count++ == 0 ? "" : " ").append(frog);
            }
            colour = other;
        }
        System.out.println(count);
        System.out.println(out);
    }
}
