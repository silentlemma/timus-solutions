import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.math.BigInteger;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Main {
    static final int BYTES = 256;
    // Java bytes are signed; this mask reads them as 0 to 255
    static final int UNSIGNED = BYTES - 1;
    static final int CHUNK = 1 << 16;

    // a line without the spaces and line breaks around it; letters are above 32
    static byte[] trim(byte[] data, int from, int to) {
        while (from < to && (data[from] & UNSIGNED) <= ' ') {
            from++;
        }
        while (to > from && (data[to - 1] & UNSIGNED) <= ' ') {
            to--;
        }
        return Arrays.copyOfRange(data, from, to);
    }

    public static void main(String[] args) throws IOException {
        // letters may be any bytes above 32, so the input is read as bytes
        ByteArrayOutputStream buffer = new ByteArrayOutputStream();
        byte[] chunk = new byte[CHUNK];
        for (int got = System.in.read(chunk); got > 0; got = System.in.read(chunk)) {
            buffer.write(chunk, 0, got);
        }
        byte[] data = buffer.toByteArray();
        List<byte[]> lines = new ArrayList<>();
        for (int start = 0, k = 0; k <= data.length; k++) {
            if (k == data.length || data[k] == '\n') {
                lines.add(trim(data, start, k));
                start = k + 1;
            }
        }
        String[] head = new String(lines.get(0), "ISO-8859-1").trim().split("\\s+");
        int n = Integer.parseInt(head[0]), m = Integer.parseInt(head[1]);
        int p = Integer.parseInt(head[2]);
        byte[] letters = lines.get(1);
        int[] index = new int[BYTES];
        for (int k = 0; k < n; k++) {
            index[letters[k] & UNSIGNED] = k;
        }
        List<byte[]> words = new ArrayList<>();
        for (int i = 2; i < lines.size() && words.size() < p; i++) {
            if (lines.get(i).length > 0) {
                words.add(lines.get(i));
            }
        }
        // Aho-Corasick automaton over the forbidden words; a state is bad
        // when some word ends there
        List<int[]> go = new ArrayList<>();
        List<Boolean> bad = new ArrayList<>();
        go.add(filled(n));
        bad.add(false);
        for (byte[] w : words) {
            int s = 0;
            for (byte b : w) {
                int c = index[b & UNSIGNED];
                if (go.get(s)[c] < 0) {
                    go.get(s)[c] = go.size();
                    go.add(filled(n));
                    bad.add(false);
                }
                s = go.get(s)[c];
            }
            bad.set(s, true);
        }
        int[] fail = new int[go.size()];
        ArrayDeque<Integer> queue = new ArrayDeque<>();
        for (int c = 0; c < n; c++) {
            if (go.get(0)[c] < 0) {
                go.get(0)[c] = 0;
            } else {
                queue.add(go.get(0)[c]);
            }
        }
        while (!queue.isEmpty()) {
            int s = queue.poll();
            bad.set(s, bad.get(s) || bad.get(fail[s]));
            for (int c = 0; c < n; c++) {
                int t = go.get(s)[c];
                if (t < 0) {
                    go.get(s)[c] = go.get(fail[s])[c];
                } else {
                    fail[t] = go.get(fail[s])[c];
                    queue.add(t);
                }
            }
        }
        // count the sentences letter by letter, never stepping into a bad state
        BigInteger[] ways = new BigInteger[go.size()];
        Arrays.fill(ways, BigInteger.ZERO);
        ways[0] = BigInteger.ONE;
        for (int step = 0; step < m; step++) {
            BigInteger[] next = new BigInteger[go.size()];
            Arrays.fill(next, BigInteger.ZERO);
            for (int s = 0; s < go.size(); s++) {
                if (ways[s].signum() > 0) {
                    for (int t : go.get(s)) {
                        if (!bad.get(t)) {
                            next[t] = next[t].add(ways[s]);
                        }
                    }
                }
            }
            ways = next;
        }
        BigInteger total = BigInteger.ZERO;
        for (BigInteger w : ways) {
            total = total.add(w);
        }
        System.out.println(total);
    }

    static int[] filled(int n) {
        int[] row = new int[n];
        Arrays.fill(row, -1);
        return row;
    }
}
