import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    private static final int SIDE = 3;
    private static final int RIGHT_START = 6;
    private static final int UNREACHABLE = -1000;
    private static final int[] MASKS = {0, 1, 2, 4, 5};

    private static int chooseSeats(byte[] rows) {
        int[] scores = new int[MASKS.length];
        int[] next = new int[MASKS.length];
        byte[] previous = new byte[rows.length * MASKS.length];
        Arrays.fill(scores, UNREACHABLE);
        scores[0] = 0;
        for (int row = 0; row < rows.length; ++row) {
            Arrays.fill(next, UNREACHABLE);
            for (int state = 0; state < MASKS.length; ++state) {
                int mask = MASKS[state];
                if ((rows[row] & mask) != mask) {
                    continue;
                }
                int blocked = mask | (mask << 1) | (mask >> 1);
                int best = UNREACHABLE;
                for (int prior = 0; prior < MASKS.length; ++prior) {
                    if ((blocked & MASKS[prior]) == 0 && scores[prior] > best) {
                        best = scores[prior];
                        previous[row * MASKS.length + state] = (byte)prior;
                    }
                }
                if (best != UNREACHABLE) {
                    next[state] = best + Integer.bitCount(mask);
                }
            }
            int[] swap = scores;
            scores = next;
            next = swap;
        }

        int state = 0;
        for (int i = 1; i < MASKS.length; ++i) {
            if (scores[i] > scores[state]) {
                state = i;
            }
        }
        int count = scores[state];
        for (int row = rows.length - 1; row >= 0; --row) {
            rows[row] = (byte)MASKS[state];
            state = previous[row * MASKS.length + state];
        }
        return count;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer header = new StringTokenizer(input.readLine());
        int rowCount = Integer.parseInt(header.nextToken());
        int remaining = Integer.parseInt(header.nextToken());
        byte[][] seats = new byte[2][rowCount];
        for (int row = 0; row < rowCount; ++row) {
            String line = input.readLine().trim();
            for (int column = 0; column < SIDE; ++column) {
                if (line.charAt(column) == '.') {
                    seats[0][row] |= 1 << column;
                }
                if (line.charAt(RIGHT_START + column) == '.') {
                    seats[1][row] |= 1 << column;
                }
            }
        }
        int capacity = chooseSeats(seats[0]) + chooseSeats(seats[1]);
        if (capacity < remaining) {
            System.out.println("PORAZHENIE");
            return;
        }
        StringBuilder output = new StringBuilder("POBEDA\n");
        for (int row = 0; row < rowCount && remaining > 0; ++row) {
            for (int half = 0; half < seats.length && remaining > 0; ++half) {
                for (int column = 0; column < SIDE && remaining > 0; ++column) {
                    if ((seats[half][row] & (1 << column)) != 0) {
                        output.append(row + 1)
                            .append((char)('A' + half * SIDE + column))
                            .append('\n');
                        --remaining;
                    }
                }
            }
        }
        System.out.print(output);
    }
}
