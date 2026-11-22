import java.util.HashMap;
import java.util.Map;

public class Main {
    static final int ASCII_LIMIT = 128;

    private static final class FastInput {
        private static final int BUFFER_SIZE = 256, BYTE_MASK = 255;
        private final java.io.InputStream input;
        private final byte[] buffer = new byte[BUFFER_SIZE];
        private int position, available;
        FastInput(java.io.InputStream input) { this.input = input; }
        private int read() throws java.io.IOException {
            if (position == available) {
                do {
                    available = input.read(buffer);
                } while (available == 0);
                position = 0;
                if (available < 0)
                    return -1;
            }
            return buffer[position++] & BYTE_MASK;
        }
        private byte[] token = new byte[32];
        private char[] characters = new char[32];
        String next() throws java.io.IOException {
            int c = read();
            while (c >= 0 && c <= ' ')
                c = read();
            if (c < 0)
                throw new java.util.NoSuchElementException();
            int length = 0;
            boolean ascii = true;
            while (c > ' ') {
                if (length == token.length) {
                    byte[] larger = new byte[2 * token.length];
                    System.arraycopy(token, 0, larger, 0, length);
                    token = larger;
                }
                token[length++] = (byte)c;
                ascii &= c < ASCII_LIMIT;
                c = read();
            }
            if (!ascii)
                return new String(token, 0, length, java.nio.charset.StandardCharsets.UTF_8);
            if (characters.length < length)
                characters = new char[length];
            for (int i = 0; i < length; i++)
                characters[i] = (char)token[i];
            return new String(characters, 0, length);
        }
        int nextInt() throws java.io.IOException { return (int)nextLong(); }
        long nextLong() throws java.io.IOException {
            int c = read();
            while (c >= 0 && c <= ' ')
                c = read();
            boolean negative = c == '-';
            if (negative || c == '+')
                c = read();
            long value = 0;
            while (c >= '0' && c <= '9') {
                value = value * 10 - (c - '0');
                c = read();
            }
            return negative ? value : -value;
        }
    }

    static final String LYOSHA = "Efremov";
    static final String VADIK = "Kantorov";

    static final int TRIPLE = 1, PAIR = 2, THREE = 3;

    public static void main(String[] args) throws java.io.IOException {
        FastInput in = new FastInput(System.in);
        int n = in.nextInt();
        Map<String, Integer> played = new HashMap<>();
        for (int i = 0; i < n; i++) {
            int size = in.nextInt();
            String extra = null;
            for (int j = 0; j < size; j++) {
                String name = in.next();
                // Every past team has Kantorov; a triple also has Efremov.
                if (!name.equals(VADIK) && (size == PAIR || !name.equals(LYOSHA)))
                    extra = name;
            }
            if (extra != null) {
                int flag = size == THREE ? TRIPLE : PAIR;
                played.put(extra, played.getOrDefault(extra, 0) | flag);
            }
        }
        int lyosha = in.nextInt(), vadik = in.nextInt(), m = in.nextInt();
        int best = -1;
        String chosen = null;
        for (int i = 0; i < m; i++) {
            String name = in.next();
            int rating = in.nextInt(), flags = played.getOrDefault(name, 0), strength;
            if ((flags & TRIPLE) == 0)
                strength = lyosha + vadik + rating;
            else if ((flags & PAIR) == 0)
                strength = vadik + rating;
            else
                continue;
            if (strength > best) {
                best = strength;
                chosen = name;
            }
        }
        if (chosen == null) {
            System.out.write(new byte[] {'F', 'a', 'i', 'l', '\n'});
        } else {
            byte[] name;
            boolean ascii = true;
            for (int i = 0; i < chosen.length(); i++)
                ascii &= chosen.charAt(i) < ASCII_LIMIT;
            if (ascii) {
                name = new byte[chosen.length()];
                for (int i = 0; i < name.length; i++)
                    name[i] = (byte)chosen.charAt(i);
            } else {
                name = chosen.getBytes(java.nio.charset.StandardCharsets.UTF_8);
            }
            byte[] prefix = {'W', 'i', 'n', '\n'};
            byte[] answer = new byte[prefix.length + name.length + 1];
            System.arraycopy(prefix, 0, answer, 0, prefix.length);
            System.arraycopy(name, 0, answer, prefix.length, name.length);
            answer[answer.length - 1] = '\n';
            System.out.write(answer);
        }
    }
}
