import java.util.HashMap;

public class Main {
    static final int SIZE = 4, PATTERN = 3, CELLS = SIZE * SIZE, ALL = (1 << CELLS) - 1;

    static final int HALF = CELLS / 2;

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

    static String next() throws java.io.IOException {
        int c = read();
        while (c <= ' ')
            c = read();
        StringBuilder value = new StringBuilder();
        while (c > ' ') {
            value.append((char)c);
            c = read();
        }
        return value.toString();
    }

    public static void main(String[] args) throws java.io.IOException {
        String[] rows = new String[SIZE], pattern = new String[PATTERN];
        for (int i = 0; i < SIZE; i++) {
            rows[i] = next();
        }
        for (int i = 0; i < PATTERN; i++) {
            pattern[i] = next();
        }
        int board = 0;
        for (int r = 0; r < SIZE; r++) {
            for (int c = 0; c < SIZE; c++) {
                if (rows[r].charAt(c) == 'B') {
                    board |= 1 << (r * SIZE + c);
                }
            }
        }
        // the flips of a move in each cell, the pattern clipped at the edges
        int[] moves = new int[CELLS];
        for (int r = 0; r < SIZE; r++) {
            for (int c = 0; c < SIZE; c++) {
                for (int dr = 0; dr < PATTERN; dr++) {
                    for (int dc = 0; dc < PATTERN; dc++) {
                        int rr = r + dr - 1, cc = c + dc - 1;
                        boolean inside = rr >= 0 && rr < SIZE && cc >= 0 && cc < SIZE;
                        if (pattern[dr].charAt(dc) == '1' && inside) {
                            moves[r * SIZE + c] |= 1 << (rr * SIZE + cc);
                        }
                    }
                }
            }
        }
        // Split the commuting moves in half and match their XOR effects.
        // Duplicate left effects retain only the cheapest number of moves.
        HashMap<Integer, Integer> left = new HashMap<>();
        int effect = 0;
        for (int step = 0; step < (1 << HALF); step++) {
            if (step > 0)
                effect ^= moves[Integer.numberOfTrailingZeros(step)];
            int count = Integer.bitCount(step ^ (step >> 1));
            Integer old = left.get(effect);
            if (old == null || count < old)
                left.put(effect, count);
        }
        int best = CELLS + 1;
        effect = 0;
        for (int step = 0; step < (1 << HALF); step++) {
            if (step > 0)
                effect ^= moves[HALF + Integer.numberOfTrailingZeros(step)];
            int count = Integer.bitCount(step ^ (step >> 1));
            for (int target : new int[] {board ^ effect, board ^ ALL ^ effect}) {
                Integer other = left.get(target);
                if (other != null)
                    best = Math.min(best, count + other);
            }
        }
        System.out.println(best > CELLS ? "Impossible" : String.valueOf(best));
    }
}
