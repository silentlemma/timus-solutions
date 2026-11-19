import java.util.*;

public class Main {

    private static final class FastInput {
        private static final int BUFFER_SIZE = 1024;
        private final java.io.InputStream input;
        private final byte[] buffer = new byte[BUFFER_SIZE];
        private int position, length;
        private String cached;

        FastInput(java.io.InputStream input) { this.input = input; }

        private int read() {
            if (position == length) {
                try {
                    do {
                        length = input.read(buffer);
                    } while (length == 0);
                } catch (java.io.IOException failure) {
                    throw new IllegalStateException(failure);
                }
                position = 0;
                if (length < 0) {
                    length = 0;
                    return -1;
                }
            }
            return buffer[position++] & 255;
        }

        private String token() {
            int character = read();
            while (character >= 0 && character <= ' ') {
                character = read();
            }
            if (character < 0) {
                return null;
            }
            byte[] bytes = new byte[32];
            int size = 0;
            while (character > ' ') {
                if (size == bytes.length) {
                    bytes = java.util.Arrays.copyOf(bytes, 2 * bytes.length);
                }
                bytes[size++] = (byte)character;
                character = read();
            }
            return new String(bytes, 0, size, java.nio.charset.StandardCharsets.UTF_8);
        }

        boolean hasNext() {
            if (cached == null) {
                cached = token();
            }
            return cached != null;
        }

        boolean hasNextLong() {
            if (!hasNext()) {
                return false;
            }
            try {
                Long.parseLong(cached);
                return true;
            } catch (NumberFormatException invalid) {
                return false;
            }
        }

        String next() {
            String value;
            if (cached == null) {
                value = token();
            } else {
                value = cached;
                cached = null;
            }
            if (value == null) {
                throw new java.util.NoSuchElementException();
            }
            return value;
        }

        long nextLong() {
            if (cached != null) {
                return Long.parseLong(next());
            }
            int character = read();
            while (character >= 0 && character <= ' ') {
                character = read();
            }
            if (character < 0) {
                throw new java.util.NoSuchElementException();
            }
            boolean negative = character == '-';
            if (negative || character == '+') {
                character = read();
            }
            long value = 0;
            while (character >= '0' && character <= '9') {
                // Negative accumulation also represents Long.MIN_VALUE exactly.
                value = value * 10 - (character - '0');
                character = read();
            }
            return negative ? value : -value;
        }

        int nextInt() { return (int)nextLong(); }
        double nextDouble() { return Double.parseDouble(next()); }
        FastInput useLocale(java.util.Locale ignored) { return this; }
    }

    static final int SMALL = 2;

    // english, or else the first name of one or two letters that no team
    // speaks: at most 100 teams cannot take all 702 of them
    static String freeLanguage(Set<String> spoken) {
        if (!spoken.contains("english"))
            return "english";
        List<String> names = new ArrayList<>();
        for (char a = 'a'; a <= 'z'; a++)
            names.add(String.valueOf(a));
        for (char a = 'a'; a <= 'z'; a++)
            for (char b = 'a'; b <= 'z'; b++)
                names.add("" + a + b);
        for (String name : names)
            if (!spoken.contains(name))
                return name;
        return "";
    }

    public static void main(String[] args) {
        FastInput in = new FastInput(System.in);
        int n = in.nextInt();
        String[] langs = new String[n];
        for (int i = 0; i < n; i++)
            langs[i] = in.next();
        Set<String> distinct = new HashSet<>(Arrays.asList(langs));
        StringBuilder out = new StringBuilder();
        if (distinct.size() < n) {
            // a third team would overhear two teams of one language
            out.append(n == SMALL ? "0" : "Impossible").append('\n');
        } else if (n == 1) {
            out.append("0\n");
        } else if (n == SMALL) {
            out.append("1\n").append(langs[0]).append('-').append(langs[1]).append('\n');
        } else {
            // a talk through another team's language is overheard, so every talk
            // goes through a language no team speaks
            String hub = freeLanguage(distinct);
            out.append(n).append('\n');
            for (String lang : langs)
                out.append(lang).append('-').append(hub).append('\n');
        }
        System.out.print(out);
    }
}
