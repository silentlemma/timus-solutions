import java.io.BufferedInputStream;
import java.io.IOException;
import java.util.Arrays;

public class Main {
    private static final int SCALE = 1000;

    private static int start(BufferedInputStream input) throws IOException {
        int c = input.read();
        while (c >= 0 && c <= ' ') {
            c = input.read();
        }
        return c;
    }

    private static int size(BufferedInputStream input) throws IOException {
        int c = start(input);
        if (c == '+') {
            c = input.read();
        }
        int value = 0;
        while (c >= '0' && c <= '9') {
            value = value * 10 + c - '0';
            c = input.read();
        }
        return value;
    }

    private static int residue(BufferedInputStream input) throws IOException {
        int c = start(input);
        boolean negative = c == '-';
        while (c > ' ' && c != '.') {
            c = input.read();
        }
        if (c != '.') {
            return 0;
        }
        int fraction = 0, place = SCALE / 10;
        for (c = input.read(); c >= '0' && c <= '9'; c = input.read()) {
            fraction += (c - '0') * place;
            place /= 10;
        }
        return negative && fraction != 0 ? SCALE - fraction : fraction;
    }

    public static void main(String[] args) throws IOException {
        BufferedInputStream input = new BufferedInputStream(System.in);
        int[] keys = new int[size(input)];
        for (int i = 0; i < keys.length; i++) {
            keys[i] = residue(input) * SCALE + residue(input);
        }
        Arrays.sort(keys);
        int bestCount = 0, bestNorm = 0;
        for (int first = 0; first < keys.length;) {
            int key = keys[first];
            int end = first + 1;
            while (end < keys.length && keys[end] == key) {
                end++;
            }
            int count = end - first;
            if (count >= bestCount) {
                int x = key / SCALE, y = key % SCALE;
                int dx = Math.min(x, SCALE - x), dy = Math.min(y, SCALE - y);
                int norm = dx * dx + dy * dy;
                if (count > bestCount || norm < bestNorm) {
                    bestCount = count;
                    bestNorm = norm;
                }
            }
            first = end;
        }
        System.out.println(bestCount + " " + (Math.sqrt(bestNorm) / SCALE));
    }
}
