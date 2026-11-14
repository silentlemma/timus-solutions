import java.io.BufferedInputStream;
import java.io.IOException;

public class Main {
    private static final int ALPHABET = 26;
    private static final int MAX_LENGTH = 100000;

    private static boolean fill(byte[] pattern, int length, int limit) {
        boolean[] fixed = new boolean[ALPHABET];
        int[] holes = new int[2];
        for (int i = 0; i < length; i++) {
            if (pattern[i] == '?') {
                holes[i % 2]++;
            } else {
                fixed[pattern[i] - 'a'] = true;
            }
        }
        int[] missing = new int[ALPHABET];
        int absent = 0;
        for (int i = 0; i < ALPHABET; i++) {
            if (!fixed[i]) {
                missing[absent++] = i;
            }
        }
        int needed = Math.max(0, limit - (ALPHABET - absent));
        if (needed > holes[0] + holes[1]) {
            return false;
        }
        int[] low = new int[ALPHABET + 1], high = new int[ALPHABET + 1];
        for (int i = 0; i < absent; i++) {
            low[i + 1] = low[i] + missing[i];
            high[i + 1] = high[i] + ALPHABET - 1 - missing[absent - 1 - i];
        }
        int lower = Math.max(0, needed - holes[1]);
        int upper = Math.min(needed, holes[0]);
        int positive = 0, best = ALPHABET * ALPHABET;
        for (int take = lower; take <= upper; take++) {
            int cost = high[take] + low[needed - take];
            if (cost < best) {
                best = cost;
                positive = take;
            }
        }
        int[] remaining = {positive, needed - positive};
        int left = 0, right = absent;
        for (int i = 0; i < length; i++) {
            if (pattern[i] != '?') {
                continue;
            }
            int parity = i % 2;
            if (remaining[parity] == 0) {
                pattern[i] = (byte)(parity == 0 ? 'z' : 'a');
            } else {
                remaining[parity]--;
                pattern[i] = (byte)('a' + (parity == 0 ? missing[--right] : missing[left++]));
            }
        }
        return true;
    }

    public static void main(String[] args) throws IOException {
        BufferedInputStream input = new BufferedInputStream(System.in);
        byte[] pattern = new byte[MAX_LENGTH];
        int c = input.read();
        while (c >= 0 && c <= ' ') {
            c = input.read();
        }
        int length = 0;
        while (c > ' ') {
            pattern[length++] = (byte)c;
            c = input.read();
        }
        while (c >= 0 && c <= ' ') {
            c = input.read();
        }
        int limit = 0;
        while (c >= '0' && c <= '9') {
            limit = limit * 10 + c - '0';
            c = input.read();
        }
        if (fill(pattern, length, limit)) {
            System.out.write(pattern, 0, length);
            System.out.write('\n');
            System.out.flush();
        } else {
            System.out.println("-1");
        }
    }
}
