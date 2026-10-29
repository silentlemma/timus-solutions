public class Main {
    private static final int MOST = 100;
    private static final int DECIMAL_DIGITS = 10;

    private static final int BUFFER_SIZE = 8192;
    private static final byte[] input = new byte[BUFFER_SIZE];
    private static int position;
    private static int length;

    // numbers are read and written by hand through 8 KB buffers: with 150 000
    // lines this is much faster than StreamTokenizer and PrintWriter
    private static int readByte() throws java.io.IOException {
        if (position == length) {
            length = System.in.read(input);
            position = 0;
            if (length < 0)
                return -1;
        }
        return input[position++];
    }

    private static int readInt() throws java.io.IOException {
        int c;
        do {
            c = readByte();
        } while (c >= 0 && c <= ' ');
        int value = 0;
        while (c >= '0' && c <= '9') {
            value = value * 10 + c - '0';
            c = readByte();
        }
        return value;
    }

    private static final byte[] output = new byte[BUFFER_SIZE];
    private static final byte[] digits = new byte[DECIMAL_DIGITS];
    private static int used;

    private static void put(int c) throws java.io.IOException {
        if (used == output.length) {
            System.out.write(output, 0, used);
            used = 0;
        }
        output[used++] = (byte)c;
    }

    private static void writeInt(int value) throws java.io.IOException {
        int count = 0;
        do {
            digits[count++] = (byte)('0' + value % 10);
            value /= 10;
        } while (value != 0);
        while (count > 0)
            put(digits[--count]);
    }

    public static void main(String[] args) throws java.io.IOException {
        int n = readInt();
        int[] team = new int[n];
        // scores are at most 100, so a byte holds them
        byte[] solved = new byte[n];
        int[] count = new int[MOST + 2];
        for (int i = 0; i < n; i++) {
            team[i] = readInt();
            solved[i] = (byte)readInt();
            count[MOST - solved[i] + 1]++;
        }
        // bubble sort never swaps equal scores, so teams with the same score keep
        // their input order: a stable counting sort by score does the same
        for (int score = 1; score <= MOST + 1; score++)
            count[score] += count[score - 1];
        int[] order = new int[n];
        for (int i = 0; i < n; i++)
            order[count[MOST - solved[i]]++] = i;
        for (int i : order) {
            writeInt(team[i]);
            put(' ');
            writeInt(solved[i]);
            put('\n');
        }
        System.out.write(output, 0, used);
        System.out.flush();
    }
}
