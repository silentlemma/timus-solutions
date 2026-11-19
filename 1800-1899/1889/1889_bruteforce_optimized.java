public class Main {
    private static final int INPUT_CAPACITY = 256;
    private static final int ASCII_MASK = 255;
    private static final byte[] buffer = new byte[INPUT_CAPACITY];
    private static int position, length;

    static int read() throws java.io.IOException {
        if (position == length) {
            do {
                length = System.in.read(buffer);
            } while (length == 0);
            position = 0;
            if (length < 0) {
                length = 0;
                return -1;
            }
        }
        return buffer[position++] & ASCII_MASK;
    }

    static int number() throws java.io.IOException {
        int character = read();
        while (character >= 0 && character <= ' ')
            character = read();
        boolean negative = character == '-';
        if (negative || character == '+')
            character = read();
        int result = 0;
        while (character >= '0' && character <= '9') {
            result = result * 10 + character - '0';
            character = read();
        }
        return negative ? -result : result;
    }
    private static final int TOKEN_CAPACITY = 32;

    static String word() throws java.io.IOException {
        int character = read();
        while (character >= 0 && character <= ' ')
            character = read();
        byte[] text = new byte[TOKEN_CAPACITY];
        int size = 0;
        while (character > ' ') {
            if (size == text.length)
                text = java.util.Arrays.copyOf(text, 2 * text.length);
            text[size++] = (byte)character;
            character = read();
        }
        return new String(text, 0, size, java.nio.charset.StandardCharsets.UTF_8);
    }
    static boolean fits(int[] phrases, int blockSize, int[] seen, int generation) {
        for (int start = 0; start < phrases.length; start += blockSize) {
            int language = 0;
            for (int i = start; i < start + blockSize; i++) {
                if (phrases[i] == 0)
                    continue;
                if (language == 0)
                    language = phrases[i];
                else if (language != phrases[i])
                    return false;
            }
            if (language != 0) {
                if (seen[language] == generation)
                    return false;
                seen[language] = generation;
            }
        }
        return true;
    }

    public static void main(String[] args) throws java.io.IOException {
        int count = number();
        int[] phrases = new int[count];
        java.util.Map<String, Integer> ids = new java.util.HashMap<>();
        for (int i = 0; i < count; i++) {
            String name = word();
            if (!name.equals("unknown")) {
                Integer id = ids.get(name);
                if (id == null) {
                    id = ids.size() + 1;
                    ids.put(name, id);
                }
                phrases[i] = id;
            }
        }
        int[] seen = new int[ids.size() + 1];
        int generation = 0;
        StringBuilder answer = new StringBuilder();
        for (int languages = 1; languages <= count; languages++) {
            if (count % languages != 0)
                continue;
            if (fits(phrases, count / languages, seen, ++generation)) {
                if (answer.length() != 0)
                    answer.append(' ');
                answer.append(languages);
            }
        }
        System.out.println(answer.length() == 0 ? "Igor is wrong." : answer);
    }
}
