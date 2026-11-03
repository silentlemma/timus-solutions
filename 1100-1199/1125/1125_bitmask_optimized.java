import java.util.ArrayList;

public class Main {
    static final int MAX_SIDE = 50, MAX_SQUARED = 2 * MAX_SIDE * MAX_SIDE;
    static final int COLOUR_XOR = 'W' ^ 'B';
    static final int BUFFER_SIZE = 4096;
    static final byte[] input = new byte[BUFFER_SIZE];
    static int position, available;

    static int read() throws java.io.IOException {
        if (position == available) {
            available = System.in.read(input);
            position = 0;
            if (available < 0)
                return -1;
        }
        return input[position++];
    }

    static int nextInt() throws java.io.IOException {
        int c = read();
        while (c <= ' ')
            c = read();
        int value = 0;
        while (c >= '0' && c <= '9') {
            value = value * 10 + c - '0';
            c = read();
        }
        return value;
    }

    public static void main(String[] args) throws Exception {
        int m = nextInt(), n = nextInt();
        StringBuilder out = new StringBuilder();
        if (m == 0 || n == 0) {
            for (int r = 0; r < m; r++)
                out.append('\n');
            System.out.print(out);
            return;
        }
        char[][] fin = new char[m][n];
        for (int r = 0; r < m; r++)
            for (int c = 0; c < n; c++) {
                int ch = read();
                while (ch <= ' ')
                    ch = read();
                fin[r][c] = (char)ch;
            }
        long[] odd = new long[m];
        long columns = 0;
        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++)
                odd[r] |= (long)(nextInt() & 1) << c;
            columns ^= odd[r];
        }
        boolean[] square = new boolean[MAX_SQUARED];
        for (int k = 0; k * k < MAX_SQUARED; k++)
            square[k * k] = true;
        ArrayList<int[]> offsets = new ArrayList<>();
        for (int dr = 1; dr < m; dr++)
            for (int dc = 1; dc < n; dc++)
                if (square[dr * dr + dc * dc])
                    offsets.add(new int[] {dr, dc});
        long full = (1L << n) - 1;
        for (int r = 0; r < m; r++) {
            // Restore the origin after the row/column overlap, then group signs.
            long flips = columns ^ odd[r];
            if ((Long.bitCount(odd[r]) & 1) != 0)
                flips ^= full;
            for (int[] delta : offsets) {
                long combined = 0;
                if (r >= delta[0])
                    combined ^= odd[r - delta[0]];
                if (r + delta[0] < m)
                    combined ^= odd[r + delta[0]];
                flips ^= (combined << delta[1]) ^ (combined >>> delta[1]);
            }
            for (int c = 0; c < n; c++)
                if (((flips >>> c) & 1) != 0)
                    fin[r][c] ^= COLOUR_XOR;
            out.append(fin[r]).append('\n');
        }
        System.out.print(out);
    }
}
