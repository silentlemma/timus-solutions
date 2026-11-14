import java.io.BufferedInputStream;
import java.io.IOException;
import java.util.Arrays;

public class Main {
    private static final int CAPACITY = 4096;
    private static final int HASH_MULTIPLIER = 0x9E3779B1;
    private static final int HASH_FOLD = 16;
    private static final int SLOT_SHIFT = 20;
    private static final int MAX_VALUE = 1_000_000_000;
    private static final int DECIMAL = 10;

    private static class Positions {
        private final int[] keys = new int[CAPACITY];
        private final char[] indices = new char[CAPACITY];

        int slot(int value) {
            int hash = value ^ (value >>> HASH_FOLD);
            int index = (hash * HASH_MULTIPLIER) >>> SLOT_SHIFT;
            while (indices[index] != 0 && keys[index] != value) {
                index = (index + 1) & (CAPACITY - 1);
            }
            return index;
        }

        boolean insert(int value, int index) {
            int position = slot(value);
            if (indices[position] != 0) {
                return false;
            }
            keys[position] = value;
            indices[position] = (char)index;
            return true;
        }

        int find(long value) {
            return value >= 0 && value <= MAX_VALUE ? indices[slot((int)value)] : 0;
        }
    }

    private static int number(BufferedInputStream input) throws IOException {
        int ch = input.read();
        while (ch >= 0 && ch <= ' ') {
            ch = input.read();
        }
        int value = 0;
        while (ch >= '0' && ch <= '9') {
            value = DECIMAL * value + ch - '0';
            ch = input.read();
        }
        return value;
    }

    public static void main(String[] args) throws IOException {
        BufferedInputStream input = new BufferedInputStream(System.in);
        int count = number(input);
        int[] values = new int[count];
        Positions positions = new Positions();
        int size = 0;
        for (int index = 1; index <= count; index++) {
            int value = number(input);
            if (positions.insert(value, index)) {
                values[size++] = value;
            }
        }
        Arrays.sort(values, 0, size);
        int best = 1;
        int first = values[0];
        long step = 0;
        int maximum = values[size - 1];
        for (int i = 0; i + best < size; i++) {
            int start = values[i];
            for (int j = i + 1; j < size; j++) {
                long delta = values[j] - start;
                long required = start + best * delta;
                // Improving the record requires the (best + 1)-st term.
                if (required > maximum) {
                    break;
                }
                if ((best > 1 && positions.find(required) == 0) ||
                    positions.find(start - delta) != 0) {
                    continue;
                }
                int length = 2;
                for (long next = values[j] + delta; positions.find(next) != 0; next += delta) {
                    length++;
                }
                if (length > best) {
                    best = length;
                    first = start;
                    step = delta;
                }
            }
        }
        StringBuilder output = new StringBuilder().append(best).append('\n');
        for (int i = 0; i < best; i++) {
            if (i != 0) {
                output.append(' ');
            }
            output.append(positions.find(first + i * step));
        }
        System.out.println(output);
    }
}
