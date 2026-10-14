import java.io.*;
import java.util.*;

public class Main {
    static final int SIZE = 8;
    // the pairs of a jumped square and its landing square, square by square
    static List<List<int[]>> jumps = new ArrayList<>();
    static int total, best;

    // black, white: the pieces still on the board, the mover excluded; removed:
    // the white pieces taken away so far, taken: the blacks captured so far
    static void dfs(int square, long black, long white, int removed, int taken) {
        best = Math.min(best, removed + total - taken); // every black not captured is taken away
        for (int[] j : jumps.get(square)) {
            int mid = j[0], to = j[1];
            if ((black >> mid & 1) == 0)
                continue;
            long nb = black & ~(1L << mid), nw = white;
            int cost = removed;
            nb &= ~(1L << to); // a black in the way is taken away, uncaptured
            if ((nw >> to & 1) != 0) {
                nw &= ~(1L << to); // a white in the way costs one more
                cost++;
            }
            dfs(to, nb, nw, cost, taken + 1);
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        // square (x, y), both from 0, is bit x * SIZE + y; the first input line is y = 7
        long whites = 0, blacks = 0;
        for (int r = 0; r < SIZE;) {
            String line = br.readLine().trim();
            if (line.isEmpty())
                continue;
            for (int x = 0; x < SIZE; x++) {
                long bit = 1L << (x * SIZE + SIZE - 1 - r);
                if (line.charAt(x) == 'W')
                    whites |= bit;
                else if (line.charAt(x) == 'B')
                    blacks |= bit;
            }
            r++;
        }
        // only squares off the edge can be jumped, so the landing stays on the board
        for (int x = 0; x < SIZE; x++)
            for (int y = 0; y < SIZE; y++) {
                List<int[]> here = new ArrayList<>();
                for (int dx = -1; dx <= 1; dx += 2)
                    for (int dy = -1; dy <= 1; dy += 2) {
                        int tx = x + 2 * dx, ty = y + 2 * dy;
                        if (tx >= 0 && tx < SIZE && ty >= 0 && ty < SIZE)
                            here.add(new int[] {(x + dx) * SIZE + y + dy, tx * SIZE + ty});
                    }
                jumps.add(here);
            }
        total = best = Long.bitCount(blacks); // removing every black always wins
        for (int s = 0; s < SIZE * SIZE; s++)
            if ((whites >> s & 1) != 0)
                dfs(s, blacks, whites & ~(1L << s), 0, 0);
        System.out.println(best);
    }
}
