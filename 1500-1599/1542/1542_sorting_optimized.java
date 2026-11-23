import java.io.BufferedWriter;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.util.*;

public class Main {
    static final int SHOWN = 10; // suggestions per query

    public static void main(String[] args) throws IOException {
        GoalInput in = new GoalInput();
        in.nextToken();
        int n = (int)in.nval;
        String[] word = new String[n];
        int[] count = new int[n];
        for (int i = 0; i < n; i++) {
            in.nextToken();
            word[i] = in.sval;
            in.nextToken();
            count[i] = (int)in.nval;
        }
        in.nextToken();
        int m = (int)in.nval;
        String[] queries = new String[m];
        Map<String, List<Integer>> found = new HashMap<>(); // query -> indices of its words
        for (int j = 0; j < m; j++) {
            in.nextToken();
            queries[j] = in.sval;
            found.put(queries[j], new ArrayList<>());
        }
        // the best words come first, so every queried prefix simply keeps the
        // first ten words that start with it
        Integer[] order = new Integer[n];
        for (int i = 0; i < n; i++)
            order[i] = i;
        Arrays.sort(order,
                    (a, b)
                        -> count[a] != count[b] ? Integer.compare(count[b], count[a])
                                                : word[a].compareTo(word[b]));
        for (int i : order)
            for (int end = 1; end <= word[i].length(); end++) {
                List<Integer> box = found.get(word[i].substring(0, end));
                if (box != null && box.size() < SHOWN)
                    box.add(i);
            }
        BufferedWriter out = new BufferedWriter(new OutputStreamWriter(System.out));
        for (int j = 0; j < m; j++) {
            if (j > 0)
                out.write('\n');
            for (int i : found.get(queries[j])) {
                out.write(word[i]);
                out.write('\n');
            }
        }
        out.flush();
    }

    // Token conversion uses one reusable byte buffer rather than regex or reader wrappers.
    static final class GoalInput {
        private final byte[] data = new byte[4096];
        private int position, length;
        private String pending;
        double nval;
        String sval;

        int read() throws IOException {
            if (position >= length) {
                length = System.in.read(data);
                position = 0;
                if (length < 0)
                    return -1;
            }
            return data[position++] & 255;
        }

        private int first() throws IOException {
            int c;
            do {
                c = read();
            } while (c >= 0 && c <= ' ');
            return c;
        }

        long nextLong() throws IOException {
            int c = first();
            boolean negative = c == '-';
            if (negative || c == '+')
                c = read();
            long value = 0;
            while (c >= '0' && c <= '9') {
                value = value * 10 + c - '0';
                c = read();
            }
            return negative ? -value : value;
        }

        int nextInt() throws IOException { return (int)nextLong(); }

        String next() throws IOException {
            if (pending != null) {
                String word = pending;
                pending = null;
                return word;
            }
            int c = first();
            if (c < 0)
                return null;
            StringBuilder word = new StringBuilder();
            while (c > ' ') {
                word.append((char)c);
                c = read();
            }
            return word.toString();
        }

        boolean hasNext() throws IOException {
            if (pending == null)
                pending = next();
            return pending != null;
        }

        void nextToken() throws IOException {
            int c = first();
            if ((c >= '0' && c <= '9') || c == '-' || c == '+') {
                boolean negative = c == '-';
                if (negative || c == '+')
                    c = read();
                long value = 0;
                while (c >= '0' && c <= '9') {
                    value = value * 10 + c - '0';
                    c = read();
                }
                nval = negative ? -value : value;
                sval = null;
            } else {
                StringBuilder word = new StringBuilder();
                while (c > ' ') {
                    word.append((char)c);
                    c = read();
                }
                sval = word.toString();
            }
        }

        long scaled(int scale) throws IOException {
            int c = first();
            boolean negative = c == '-';
            if (negative || c == '+')
                c = read();
            long value = 0;
            boolean fraction = false;
            while (c > ' ') {
                if (c == '.')
                    fraction = true;
                else {
                    value = value * 10 + c - '0';
                    if (fraction)
                        scale /= 10;
                }
                c = read();
            }
            value *= scale;
            return negative ? -value : value;
        }
    }
}
