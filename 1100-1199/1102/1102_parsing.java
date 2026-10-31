import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class Main {
    static final int ALPHABET = 26;
    static final String[] WORDS = {"out", "output", "puton", "in", "input", "one"};

    static final int BUFFER_SIZE = 4096;
    static final int BYTE_MASK = 255;
    static final byte[] BUFFER = new byte[BUFFER_SIZE];
    static int position, available;
    // a refillable buffer keeps input memory constant for any number of records.
    static int read() throws java.io.IOException {
        if (position == available) {
            available = System.in.read(BUFFER);
            position = 0;
            if (available < 0)
                return -1;
        }
        return BUFFER[position++] & BYTE_MASK;
    }
    static int nextInt() throws java.io.IOException {
        int c;
        do {
            c = read();
        } while (c <= ' ' && c >= 0);
        int value = 0, sign = 1;
        if (c == '-') {
            sign = -1;
            c = read();
        }
        while (c >= '0' && c <= '9') {
            value = value * 10 + c - '0';
            c = read();
        }
        return sign * value;
    }

    static int[] empty() {
        int[] row = new int[ALPHABET];
        Arrays.fill(row, -1);
        return row;
    }
    public static void main(String[] args) throws java.io.IOException {
        ArrayList<int[]> trie = new ArrayList<>();
        ArrayList<Boolean> terminal = new ArrayList<>();
        trie.add(empty());
        terminal.add(false);
        for (String word : WORDS) {
            int node = 0;
            for (int i = 0; i < word.length(); ++i) {
                int c = word.charAt(i) - 'a';
                if (trie.get(node)[c] < 0) {
                    trie.get(node)[c] = trie.size();
                    trie.add(empty());
                    terminal.add(false);
                }
                node = trie.get(node)[c];
            }
            terminal.set(node, true);
        }
        // the six words have 24 letters in total, so all trie nodes fit in 32 bits.
        // bit zero permits a new word; other bits are unfinished matching prefixes.
        ArrayList<Integer> masks = new ArrayList<>();
        Map<Integer, Integer> ids = new HashMap<>();
        ArrayList<int[]> table = new ArrayList<>();
        masks.add(1);
        ids.put(1, 0);
        for (int s = 0; s < masks.size(); ++s) {
            int[] row = new int[ALPHABET];
            for (int c = 0; c < ALPHABET; ++c) {
                int mask = 0;
                for (int node = 0; node < trie.size(); ++node) {
                    int to = trie.get(node)[c];
                    if ((masks.get(s) & (1 << node)) != 0 && to >= 0) {
                        mask |= 1 << to;
                        if (terminal.get(to))
                            mask |= 1;
                    }
                }
                if (!ids.containsKey(mask)) {
                    ids.put(mask, masks.size());
                    masks.add(mask);
                }
                row[c] = ids.get(mask);
            }
            table.add(row);
        }
        int[][] transitions = table.toArray(new int[0][]);
        boolean[] accepting = new boolean[masks.size()];
        for (int i = 0; i < masks.size(); ++i)
            accepting[i] = (masks.get(i) & 1) != 0;
        int n = nextInt(), state = 0, lines = 0;
        boolean started = false;
        StringBuilder out = new StringBuilder();
        // each byte makes one transition; even a rejected line is consumed fully.
        for (int c; (c = read()) >= 0;) {
            if (c >= 'a' && c <= 'z') {
                state = transitions[state][c - 'a'];
                started = true;
            } else if (started) {
                out.append(accepting[state] ? "YES\n" : "NO\n");
                state = 0;
                started = false;
                ++lines;
            }
        }
        if (started && lines < n)
            out.append(accepting[state] ? "YES\n" : "NO\n");
        System.out.print(out);
    }
}
