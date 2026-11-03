import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    static final int SIDE = 4, CELLS = SIDE * SIDE, LETTERS = 26, COLORS = 2,
                     STATE_BITS = CELLS - 1;
    static final int MEMO_BYTES = CELLS * (1 << STATE_BITS) / Byte.SIZE;
    static final int[] positions = new int[LETTERS], colors = new int[COLORS],
                       near = new int[CELLS], allowed = new int[CELLS];
    static final int[][] capacity = new int[COLORS][LETTERS];
    static final byte[] failed = new byte[MEMO_BYTES];
    static char[] word;

    static boolean walk(int cell, int used, int index) {
        if (index + 1 == word.length)
            return true;
        int compressed = (used & ((1 << cell) - 1)) | ((used >>> (cell + 1)) << cell);
        int key = (cell << STATE_BITS) | compressed, slot = key / Byte.SIZE,
            flag = 1 << (key % Byte.SIZE);
        if ((failed[slot] & flag) != 0)
            return false;
        int options = near[cell] & allowed[index + 1] & ~used;
        while (options != 0) {
            int bit = options & -options;
            if (walk(Integer.numberOfTrailingZeros(bit), used | bit, index + 1))
                return true;
            options -= bit;
        }
        failed[slot] = (byte)(failed[slot] | flag);
        return false;
    }

    static boolean found(String original) {
        word = original.toCharArray();
        int length = word.length;
        if (Integer.bitCount(positions[word[0] - 'a']) >
            Integer.bitCount(positions[word[length - 1] - 'a']))
            for (int left = 0, right = length - 1; left < right; left++, right--) {
                char swap = word[left];
                word[left] = word[right];
                word[right] = swap;
            }
        int[][] needed = new int[COLORS][LETTERS];
        for (int i = 0; i < length; i++)
            needed[i % COLORS][word[i] - 'a']++;
        int starts = 0;
        for (int color = 0; color < COLORS; color++) {
            boolean possible = true;
            for (int letter = 0; letter < LETTERS; letter++)
                if (needed[0][letter] > capacity[color][letter] ||
                    needed[1][letter] > capacity[color ^ 1][letter])
                    possible = false;
            if (possible)
                starts |= colors[color];
        }
        if (starts == 0)
            return false;
        allowed[length - 1] = positions[word[length - 1] - 'a'];
        for (int i = length - 2; i >= 0; i--) {
            allowed[i] = 0;
            int cells = positions[word[i] - 'a'];
            while (cells != 0) {
                int bit = cells & -cells, cell = Integer.numberOfTrailingZeros(bit);
                if ((near[cell] & allowed[i + 1]) != 0)
                    allowed[i] |= bit;
                cells -= bit;
            }
        }
        starts &= allowed[0];
        if (starts == 0)
            return false;
        Arrays.fill(failed, (byte)0);
        while (starts != 0) {
            int bit = starts & -starts;
            if (walk(Integer.numberOfTrailingZeros(bit), bit, 0))
                return true;
            starts -= bit;
        }
        return false;
    }

    public static void main(String[] args) throws Exception {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder grid = new StringBuilder();
        for (int row = 0; row < SIDE; row++)
            grid.append(in.readLine().trim());
        for (int cell = 0; cell < CELLS; cell++) {
            int bit = 1 << cell;
            positions[grid.charAt(cell) - 'a'] |= bit;
            int row = cell / SIDE, column = cell % SIDE;
            colors[(row + column) % COLORS] |= bit;
            if (row > 0)
                near[cell] |= 1 << (cell - SIDE);
            if (row + 1 < SIDE)
                near[cell] |= 1 << (cell + SIDE);
            if (column > 0)
                near[cell] |= 1 << (cell - 1);
            if (column + 1 < SIDE)
                near[cell] |= 1 << (cell + 1);
        }
        for (int color = 0; color < COLORS; color++)
            for (int letter = 0; letter < LETTERS; letter++)
                capacity[color][letter] = Integer.bitCount(positions[letter] & colors[color]);
        int n = Integer.parseInt(in.readLine().trim());
        String[] queries = new String[n];
        boolean[] answers = new boolean[n];
        StringBuilder out = new StringBuilder();
        for (int i = 0; i < n; i++) {
            queries[i] = in.readLine().trim();
            int previous = 0;
            while (previous < i && !queries[previous].equals(queries[i]))
                previous++;
            answers[i] = previous < i ? answers[previous] : found(queries[i]);
            out.append(queries[i]).append(answers[i] ? ": YES\n" : ": NO\n");
        }
        System.out.print(out);
    }
}
