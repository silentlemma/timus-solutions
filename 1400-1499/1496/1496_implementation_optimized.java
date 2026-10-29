import java.util.HashMap;
import java.util.Map;

public class Main {
    private static final int MAX_NAME_LENGTH = 30;
    private static final int BUFFER_SIZE = 256;
    private static final byte[] buffer = new byte[BUFFER_SIZE];
    private static int position, length;

    // the input is read in 256-byte blocks and each team name, at most 30
    // characters, is cut out by hand instead of Scanner
    private static int readByte() throws java.io.IOException {
        if (position == length) {
            length = System.in.read(buffer);
            position = 0;
            if (length < 0) {
                return -1;
            }
        }
        return buffer[position++];
    }

    private static int nextInt() throws java.io.IOException {
        int ch;
        do {
            ch = readByte();
        } while (ch >= 0 && ch <= ' ');
        int value = 0;
        while (ch >= '0' && ch <= '9') {
            value = value * 10 + ch - '0';
            ch = readByte();
        }
        return value;
    }

    private static String nextName() throws java.io.IOException {
        int ch;
        do {
            ch = readByte();
        } while (ch >= 0 && ch <= ' ');
        char[] name = new char[MAX_NAME_LENGTH];
        int length = 0;
        while (ch > ' ') {
            name[length++] = (char)ch;
            ch = readByte();
        }
        return new String(name, 0, length);
    }

    public static void main(String[] args) throws java.io.IOException {
        int count = nextInt();
        // a team that submitted more than once is the spammer; the teams are
        // printed in the order of their second submission
        Map<String, Integer> submissions = new HashMap<>();
        StringBuilder output = new StringBuilder();
        for (int i = 0; i < count; ++i) {
            String team = nextName();
            Integer previous = submissions.get(team);
            int total = previous == null ? 1 : previous + 1;
            submissions.put(team, total);
            if (total == 2) {
                output.append(team).append('\n');
            }
        }
        System.out.print(output);
    }
}
