import java.io.DataInputStream;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class Main {
    static int n, h, d;
    static int[] lefts;

    // the place of a left end on the line from start, or -1 if it has none
    static int spot(int value, int start) {
        int diff = value - start;
        if (diff % d != 0) return -1;
        int step = diff / d;
        return step >= 0 && step < n ? step : -1;
    }

    // the places of strip k unturned and turned, -1 for none
    static int[] choices(int k, int start) {
        // with a flat line every strip keeps its own place in the order
        int a = d != 0 ? spot(lefts[k], start) : (lefts[k] == start ? k : -1);
        int b = d != 0 ? spot(h - d - lefts[k], start) : (h - lefts[k] == start ? k : -1);
        return new int[] {a, b == a ? -1 : b};
    }

    // the strips in order, signed when turned over, if their left ends can be
    // start, start + d, ..., start + (n - 1) d; null otherwise
    static int[] arrange(int start) {
        int[] place = new int[n];
        List<Integer> flexible = new ArrayList<>();
        for (int k = 0; k < n; k++) {
            int[] c = choices(k, start);
            if (c[0] < 0 && c[1] < 0) return null;
            if (c[0] >= 0 && c[1] >= 0) {
                flexible.add(k);
                continue;
            }
            int step = c[0] >= 0 ? c[0] : c[1];
            if (place[step] != 0) return null;
            place[step] = c[0] >= 0 ? k + 1 : -(k + 1);
        }
        // a strip that fits two places pairs place i with place K - i, so only
        // strips of the same pair compete once the strips with one choice are in
        for (int k : flexible) {
            int[] c = choices(k, start);
            if (place[c[0]] == 0) place[c[0]] = k + 1;
            else if (place[c[1]] == 0) place[c[1]] = -(k + 1);
            else return null;
        }
        return place;
    }

    public static void main(String[] args) throws IOException {
        Reader in = new Reader();
        h = in.nextInt();
        n = in.nextInt();
        lefts = new int[n];
        int[] rights = new int[n];
        for (int i = 0; i < n; i++) {
            lefts[i] = in.nextInt();
            rights[i] = in.nextInt();
        }
        // turning a strip over keeps its slope, so all slopes must be equal; the
        // left end x of a strip turns into h - d - x
        d = rights[0] - lefts[0];
        for (int i = 0; i < n; i++) {
            if (rights[i] - lefts[i] != d) {
                System.out.println(0);
                return;
            }
        }
        int[] starts = {lefts[0], h - lefts[0]};
        if (d != 0) {
            int low = h, high = 0;
            for (int x : lefts) {
                low = Math.min(low, Math.min(x, h - d - x));
                high = Math.max(high, Math.max(x, h - d - x));
            }
            // the strip with the extreme end either starts the line or, turned,
            // ends it
            int first = d > 0 ? low : high, last = d > 0 ? high : low;
            starts = new int[] {first, last - (n - 1) * d};
        }
        for (int start : starts) {
            int[] place = arrange(start);
            if (place == null) continue;
            StringBuilder out = new StringBuilder();
            for (int i = 0; i < n; i++) out.append(i > 0 ? " " : "").append(place[i]);
            System.out.println(out);
            return;
        }
        System.out.println(0);
    }

    static class Reader {
        private static final int SIZE = 1 << 16;
        private final DataInputStream stream = new DataInputStream(System.in);
        private final byte[] buffer = new byte[SIZE];
        private int length, pointer;

        private int read() throws IOException {
            if (pointer == length) {
                length = stream.read(buffer, 0, SIZE);
                pointer = 0;
                if (length <= 0) return -1;
            }
            return buffer[pointer++];
        }

        int nextInt() throws IOException {
            int c = read();
            while (c != -1 && (c < '0' || c > '9')) c = read();
            int x = 0;
            while (c >= '0' && c <= '9') {
                x = x * 10 + (c - '0');
                c = read();
            }
            return x;
        }
    }
}
