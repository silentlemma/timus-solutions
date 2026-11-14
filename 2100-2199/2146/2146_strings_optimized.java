import java.io.BufferedInputStream;
import java.io.BufferedOutputStream;
import java.io.IOException;
import java.util.Arrays;

public class Main {
    private static final int LETTERS = 26;

    private static int number(BufferedInputStream input) throws IOException {
        int c = input.read();
        while (c >= 0 && c <= ' ') {
            c = input.read();
        }
        int value = 0;
        while (c >= '0' && c <= '9') {
            value = value * 10 + c - '0';
            c = input.read();
        }
        return value;
    }

    private static boolean repair(byte[] drum, byte[] pattern, int period, int budget) {
        int perClass = drum.length / period;
        int changes = 0;
        int[] counts = new int[LETTERS];
        for (int residue = 0; residue < period; residue++) {
            Arrays.fill(counts, 0);
            int best = 0;
            for (int i = residue; i < drum.length; i += period) {
                int letter = drum[i] - 'a';
                if (++counts[letter] > counts[best]) {
                    best = letter;
                }
            }
            changes += perClass - counts[best];
            if (changes > budget) {
                return false;
            }
            pattern[residue] = (byte)('a' + best);
        }
        return true;
    }

    public static void main(String[] args) throws IOException {
        BufferedInputStream input = new BufferedInputStream(System.in);
        int size = number(input);
        int budget = number(input);
        byte[] drum = new byte[size];
        int c = input.read();
        while (c >= 0 && c <= ' ') {
            c = input.read();
        }
        drum[0] = (byte)c;
        for (int i = 1; i < size;) {
            int read = input.read(drum, i, size - i);
            if (read < 0) {
                return;
            }
            i += read;
        }

        byte[] pattern = new byte[size / 2];
        byte[] result = drum;
        int length = size;
        for (int period = 1; period <= pattern.length; period++) {
            if (size % period == 0 && repair(drum, pattern, period, budget)) {
                result = pattern;
                length = period;
                break;
            }
        }
        System.out.println(length);
        BufferedOutputStream output = new BufferedOutputStream(System.out);
        for (int remaining = size; remaining > 0; remaining -= length) {
            output.write(result, 0, length);
        }
        output.write('\n');
        output.flush();
    }
}
