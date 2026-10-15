import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
    static final int BLOCK = 4; // rows or columns added at a time
    static final int SMALLEST = 4; // boards with a shorter side have no tour, apart from 2 x 2
    static final int BOTTOM = SMALLEST - 1; // the last row of a strip

    static final int[] NO_TOUR = {5, 5}; // the one board with both sides at least 4 and no tour
    static final int[] ODD_BASE = {5, 9}; // the base when both sides are of the form 4k + 1

    // closed tours of small boards: rows, columns, then the (row, column) cells
    // in order, ending at the start; printed by 1674_constructive_table.py
    static final int[][] BASES = {
        {5, 6, 0, 0, 0, 1, 1, 2, 2, 2, 2, 3, 1, 3, 0, 2, 0, 3, 1, 4, 0, 4, 0, 5, 1, 5, 2, 4, 2, 5,
            3, 5, 3, 4, 4, 5, 4, 4, 3, 3, 4, 3, 4, 2, 3, 2, 4, 1, 4, 0, 3, 0, 3, 1, 2, 0, 2, 1, 1,
            0, 1, 1, 0, 0},
        {5, 7, 0, 0, 0, 1, 1, 2, 2, 2, 2, 3, 1, 3, 0, 2, 0, 3, 1, 4, 0, 4, 0, 5, 1, 5, 0, 6, 1, 6,
            2, 5, 2, 6, 3, 6, 3, 5, 4, 6, 4, 5, 3, 4, 2, 4, 3, 3, 4, 4, 4, 3, 3, 2, 4, 2, 3, 1, 4,
            1, 4, 0, 3, 0, 2, 1, 2, 0, 1, 0, 1, 1, 0, 0},
        {6, 6, 0, 0, 0, 1, 1, 2, 1, 3, 0, 2, 0, 3, 1, 4, 0, 4, 0, 5, 1, 5, 2, 4, 2, 5, 3, 5, 3, 4,
            2, 3, 2, 2, 3, 2, 3, 3, 4, 4, 4, 5, 5, 5, 5, 4, 4, 3, 5, 3, 5, 2, 4, 2, 5, 1, 5, 0, 4,
            0, 4, 1, 3, 0, 3, 1, 2, 0, 2, 1, 1, 0, 1, 1, 0, 0},
        {6, 7, 0, 0, 0, 1, 1, 2, 1, 3, 0, 2, 0, 3, 1, 4, 0, 4, 0, 5, 1, 5, 0, 6, 1, 6, 2, 5, 2, 4,
            3, 5, 2, 6, 3, 6, 4, 5, 4, 6, 5, 6, 5, 5, 4, 4, 5, 4, 4, 3, 3, 4, 2, 3, 2, 2, 3, 3, 3,
            2, 4, 2, 5, 3, 5, 2, 4, 1, 5, 1, 5, 0, 4, 0, 3, 1, 3, 0, 2, 0, 2, 1, 1, 0, 1, 1, 0, 0},
        {7, 7, 0, 0, 0, 1, 1, 2, 1, 3, 0, 2, 0, 3, 1, 4, 0, 4, 0, 5, 1, 5, 0, 6, 1, 6, 2, 5, 2, 4,
            3, 5, 2, 6, 3, 6, 4, 5, 4, 6, 5, 6, 5, 5, 6, 6, 6, 5, 5, 4, 6, 4, 5, 3, 4, 4, 3, 4, 2,
            3, 2, 2, 3, 3, 3, 2, 4, 3, 4, 2, 5, 2, 6, 3, 6, 2, 5, 1, 6, 1, 6, 0, 5, 0, 4, 1, 4, 0,
            3, 0, 3, 1, 2, 0, 2, 1, 1, 0, 1, 1, 0, 0},
        {5, 9, 0, 0, 0, 1, 1, 2, 2, 2, 2, 3, 1, 3, 0, 2, 0, 3, 1, 4, 2, 4, 2, 5, 1, 5, 0, 4, 0, 5,
            1, 6, 0, 6, 0, 7, 1, 7, 0, 8, 1, 8, 2, 7, 2, 8, 3, 8, 3, 7, 4, 8, 4, 7, 3, 6, 2, 6, 3,
            5, 4, 6, 4, 5, 3, 4, 4, 4, 3, 3, 4, 3, 4, 2, 3, 2, 4, 1, 4, 0, 3, 0, 3, 1, 2, 0, 2, 1,
            1, 0, 1, 1, 0, 0},
    };

    static char[][] grid;

    static void add(List<int[]> path, int r, int c) {
        path.add(new int[] {r, c});
    }

    // a closed tour of the 4 x m board: along the top two rows in a zigzag,
    // down the right end, back along the bottom two rows, up the left end
    static List<int[]> strip(int m) {
        List<int[]> path = new ArrayList<>();
        add(path, 0, 0);
        add(path, 0, 1);
        add(path, 1, 1);
        for (int c = 2; c < m - 1; c++) {
            add(path, 0, c);
            if (c < m - 2) {
                add(path, 1, c);
            }
        }
        add(path, 0, m - 1);
        add(path, 1, m - 1);
        add(path, 1, m - 2);
        add(path, 2, m - 1);
        add(path, BOTTOM, m - 1);
        for (int c = m - 2; c > 1; c--) {
            add(path, BOTTOM, c);
            add(path, 2, c);
        }
        add(path, BOTTOM, 1);
        add(path, BOTTOM, 0);
        add(path, 2, 0);
        add(path, 2, 1);
        add(path, 1, 0);
        add(path, 0, 0);
        return path;
    }

    static List<int[]> flip(List<int[]> path) {
        List<int[]> out = new ArrayList<>();
        for (int[] p : path) {
            out.add(new int[] {p[1], p[0]});
        }
        return out;
    }

    static List<int[]> base(int n, int m) {
        if (n == SMALLEST) {
            return strip(m);
        }
        if (m == SMALLEST) {
            return flip(strip(n));
        }
        int[] flat = null;
        boolean swapped = false;
        for (int[] entry : BASES) {
            if (entry[0] == n && entry[1] == m) {
                flat = entry;
            } else if (entry[0] == m && entry[1] == n) {
                flat = entry;
                swapped = true;
            }
        }
        List<int[]> path = new ArrayList<>();
        for (int i = 2; i < flat.length; i += 2) {
            add(path, flat[i], flat[i + 1]);
        }
        return swapped ? flip(path) : path;
    }

    // draw the move between cells (r1, c1) and (r2, c2), or with ch = ' ' erase it
    static void mark(int r1, int c1, int r2, int c2, char ch) {
        if (ch == 0) {
            if (r1 == r2) {
                ch = '-';
            } else if (c1 == c2) {
                ch = '|';
            } else {
                ch = r2 - r1 == c2 - c1 ? '\\' : '/';
            }
        }
        grid[r1 + r2][c1 + c2] = ch;
    }

    static void draw(List<int[]> path, int dr, int dc, boolean swap) {
        for (int i = 0; i + 1 < path.size(); i++) {
            int[] a = path.get(i);
            int[] b = path.get(i + 1);
            int s = swap ? 1 : 0;
            mark(a[s] + dr, a[1 - s] + dc, b[s] + dr, b[1 - s] + dc, (char) 0);
        }
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int m = in.nextInt();
        grid = new char[2 * n - 1][2 * m - 1];
        for (int y = 0; y < 2 * n - 1; y++) {
            for (int x = 0; x < 2 * m - 1; x++) {
                grid[y][x] = y % 2 == 0 && x % 2 == 0 ? 'o' : ' ';
            }
        }
        if (n == 2 && m == 2) {
            List<int[]> square = new ArrayList<>();
            add(square, 0, 0);
            add(square, 0, 1);
            add(square, 1, 1);
            add(square, 1, 0);
            add(square, 0, 0);
            draw(square, 0, 0, false);
        } else if (n < SMALLEST || m < SMALLEST || (n == NO_TOUR[0] && m == NO_TOUR[1])) {
            System.out.println("No");
            return;
        } else {
            // a base board whose sides leave multiples of 4; two sides of the
            // form 4k + 1 start from 5 x 9 instead, as 5 x 5 has no tour
            int bn = SMALLEST + (n - SMALLEST) % BLOCK;
            int bm = SMALLEST + (m - SMALLEST) % BLOCK;
            if (n % BLOCK == 1 && m % BLOCK == 1) {
                boolean wide = m >= ODD_BASE[1];
                bn = wide ? ODD_BASE[0] : ODD_BASE[1];
                bm = wide ? ODD_BASE[1] : ODD_BASE[0];
            }
            draw(base(bn, bm), 0, 0, false);
            // each new 4-wide block has its own strip tour; three edges at the
            // seam are swapped for three others, which joins the two cycles
            for (int cur = bm; cur < m; cur += BLOCK) {
                draw(strip(bn), 0, cur, true);
                mark(0, cur - 1, 1, cur - 1, ' ');
                mark(0, cur, 1, cur, ' ');
                mark(2, cur, 1, cur + 1, ' ');
                mark(0, cur - 1, 1, cur, (char) 0);
                mark(1, cur - 1, 2, cur, (char) 0);
                mark(0, cur, 1, cur + 1, (char) 0);
            }
            for (int cur = bn; cur < n; cur += BLOCK) {
                draw(strip(m), cur, 0, false);
                mark(cur - 1, 0, cur - 1, 1, ' ');
                mark(cur, 0, cur, 1, ' ');
                mark(cur, 2, cur + 1, 1, ' ');
                mark(cur - 1, 0, cur, 1, (char) 0);
                mark(cur - 1, 1, cur, 2, (char) 0);
                mark(cur, 0, cur + 1, 1, (char) 0);
            }
        }
        StringBuilder out = new StringBuilder("Yes\n");
        for (char[] row : grid) {
            out.append(row).append('\n');
        }
        System.out.print(out);
    }
}
