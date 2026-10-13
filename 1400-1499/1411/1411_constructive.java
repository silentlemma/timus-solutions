import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
    // bridgeless cubic maps with the whole border built, found by a search
    static final String[][] BLOCKS = {
        {"O-O-O-O", "|\\|/ /|", "O O O-O", "|\\   \\|", "O-O O O", "|/ /|\\|", "O-O-O-O"},
        {"O-O-O-O", "|\\ \\|/|", "O-O O O", "| |  /|", "O-O-O-O", "|     |", "O-O O-O", "|/| |\\|",
         "O-O-O-O"},
        {"O-O-O-O", "|\\|/ /|", "O O O-O", "|\\   \\|", "O-O-O O", "|   |\\|", "O-O O O",
         "|/|/ \\|", "O O O O", "|/ /|\\|", "O-O-O-O"},
        {"O-O-O-O", "|\\ \\|/|", "O O O O", "|\\|\\ /|", "O O O-O", "|\\|   |", "O-O O-O",
         "|   |\\|", "O-O-O O", "| |  \\|", "O-O O O", "|/ /|\\|", "O-O-O-O"},
        {"O-O-O-O-O-O", "|\\ \\|  \\|/|", "O-O O-O O O", "| |  /|  /|", "O-O O O O-O",
         "|/ /| |\\ \\|", "O-O-O-O-O-O"},
        {"O-O-O-O-O-O", "|\\ \\ \\ \\|/|", "O-O-O O O O", "|    \\|\\ /|", "O-O-O-O O O",
         "| | |  / /|", "O-O O O O-O", "|/ /| |\\ \\|", "O-O-O-O-O-O"},
        {"O-O-O-O-O-O", "|\\|  \\| |/|", "O-O O O-O O", "|  /|\\   /|", "O-O-O O O-O",
         "|  / /|/  |", "O O-O O O-O", "|\\ \\ \\|/ \\|", "O-O O O O O", "|/ /|  /|\\|",
         "O-O-O-O-O-O"},
        {"O-O-O-O-O-O", "|\\| |  \\|/|", "O-O O O O O", "|  /|/|\\ /|", "O-O-O O-O O",
         "|     |  /|", "O-O-O O O-O", "| | |\\|\\| |", "O-O O O O-O", "|  \\|\\ \\  |",
         "O-O O O O-O", "|/| | |\\ \\|", "O-O-O-O-O-O"},
        {"O-O-O-O-O-O-O-O", "|\\ \\ \\| | |/ /|", "O-O O O O O O-O", "|/ /| | |\\ \\ \\|",
         "O-O-O-O-O-O-O-O"},
        {"O-O-O-O-O-O-O-O-O-O", "|\\ \\ \\|  \\| |/ / /|", "O-O O O O-O O O O-O",
         "|/ /| | |\\  | |\\ \\|", "O-O-O-O-O-O-O-O-O-O"},
        {"O-O-O-O-O-O-O-O-O-O-O-O", "|\\ \\ \\ \\|/ /  | | |/ /|", "O-O O O O O-O O-O O O-O",
         "|/ /| |\\  | |\\ \\ \\ \\ \\|", "O-O-O-O-O-O-O-O-O-O-O-O"},
        {"O-O-O-O-O-O-O-O-O-O-O-O-O-O", "|\\ \\| |/   \\ \\|/ /  |/ / /|",
         "O-O O O O-O-O O O O-O O O-O", "|/ / / /| | |  /| |\\  |\\ \\|",
         "O-O-O-O-O-O-O-O-O-O-O-O-O-O"},
    };
    static final int MIN_SIDE = 3;
    static final int FLAT = 3; // a strip this high needs at least FLAT_STEP columns
    static final int FLAT_STEP = 8;
    static final int FLAT_TOP = 14;
    static final int STEP = 4;
    static final int WIDE_TOP = 6;
    static final int TALL_TOP = 7;
    static final String NO_WORLD = "Imaginary world";

    static List<Integer> split(int n, int step, int top) {
        List<Integer> parts = new ArrayList<>();
        while (n > top) {
            parts.add(step);
            n -= step;
        }
        parts.add(n);
        return parts;
    }

    static String[] shape(int w, int h) {
        for (String[] b : BLOCKS)
            if (b[0].length() / 2 + 1 == w && b.length / 2 + 1 == h)
                return b;
        return BLOCKS[0];
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int w = in.nextInt(), h = in.nextInt();
        if (w * h % 2 == 1 || Math.min(w, h) < MIN_SIDE) {
            System.out.println(NO_WORLD);
            return;
        }
        boolean turned = w % 2 == 1; // then h is even: build the turned map
        if (turned) {
            int t = w;
            w = h;
            h = t;
        }
        List<Integer> widths, heights;
        if (h == FLAT) {
            if (w < FLAT_STEP) {
                System.out.println(NO_WORLD);
                return;
            }
            widths = split(w, FLAT_STEP, FLAT_TOP);
            heights = new ArrayList<>();
            heights.add(FLAT);
        } else {
            widths = split(w, STEP, WIDE_TOP);
            heights = split(h, STEP, TALL_TOP);
        }
        char[][] grid = new char[2 * h - 1][2 * w - 1];
        for (char[] row : grid)
            java.util.Arrays.fill(row, ' ');
        int top = 0;
        for (int j = 0; j < heights.size(); j++) {
            int bh = heights.get(j), left = 0;
            for (int i = 0; i < widths.size(); i++) {
                int bw = widths.get(i), y = 2 * top, x = 2 * left;
                String[] block = shape(bw, bh);
                for (int r = 0; r < block.length; r++)
                    block[r].getChars(0, block[r].length(), grid[y + r], x);
                if (i > 0) {
                    // two vertical bridges at the seam, in the lowest two rows,
                    // give way to two horizontal ones
                    int z = 2 * (top + bh - 2);
                    grid[z + 1][x - 2] = grid[z + 1][x] = ' ';
                    grid[z][x - 1] = grid[z + 2][x - 1] = '-';
                }
                left += bw;
            }
            if (j > 0) {
                // the same exchange across a horizontal seam, in the last two columns
                int y = 2 * top, x = 2 * (w - 2);
                grid[y - 2][x + 1] = grid[y][x + 1] = ' ';
                grid[y - 1][x] = grid[y - 1][x + 2] = '|';
            }
            top += bh;
        }
        if (turned) {
            char[][] flipped = new char[grid[0].length][grid.length];
            for (int r = 0; r < grid.length; r++)
                for (int c = 0; c < grid[r].length; c++) {
                    char ch = grid[r][c];
                    flipped[c][r] = ch == '-' ? '|' : ch == '|' ? '-' : ch;
                }
            grid = flipped;
        }
        StringBuilder out = new StringBuilder();
        for (char[] row : grid)
            out.append(row).append('\n');
        System.out.print(out);
    }
}
