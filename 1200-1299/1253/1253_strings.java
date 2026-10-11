import java.io.*;

public class Main {
    static final int LIMIT = 1000000;
    static final int CHUNK = 1 << 16;
    static String[] text;
    static int[] size, state;
    static StringBuilder out = new StringBuilder();

    // the fully expanded length, capped above the limit; state 1 marks
    // templates being expanded, so meeting one again is a cycle
    static boolean measure(int i) {
        state[i] = 1;
        for (int k = 0; k < text[i].length(); k++) {
            if (text[i].charAt(k) != '*') {
                size[i] = Math.min(size[i] + 1, LIMIT + 1);
                continue;
            }
            int j = text[i].charAt(++k) - '0';
            if (state[j] == 1 || (state[j] == 0 && !measure(j)))
                return false;
            size[i] = Math.min(size[i] + size[j], LIMIT + 1);
        }
        state[i] = 2;
        return true;
    }

    static void write(int i) {
        for (int k = 0; k < text[i].length(); k++) {
            char c = text[i].charAt(k);
            if (c == '*')
                write(text[i].charAt(++k) - '0');
            else
                out.append(c);
        }
    }

    public static void main(String[] args) throws IOException {
        ByteArrayOutputStream bytes = new ByteArrayOutputStream();
        byte[] buf = new byte[CHUNK];
        for (int r; (r = System.in.read(buf)) > 0;)
            bytes.write(buf, 0, r);
        String data = bytes.toString("ISO-8859-1").replace("\r", "");
        int line = data.indexOf('\n');
        int n = Integer.parseInt(data.substring(0, line).trim());
        // a template runs from the start of a line to its '#'
        text = new String[n + 1];
        int pos = line + 1;
        for (int i = 1; i <= n; i++) {
            int end = data.indexOf('#', pos);
            text[i] = data.substring(pos, end);
            pos = end + 1;
            if (pos < data.length() && data.charAt(pos) == '\n')
                pos++;
        }
        size = new int[n + 1];
        state = new int[n + 1];
        PrintStream stdout = new PrintStream(System.out, false, "ISO-8859-1");
        if (!measure(1) || size[1] > LIMIT) {
            stdout.print("#\n");
        } else {
            write(1);
            stdout.print(out.append('\n'));
        }
        stdout.flush();
    }
}
