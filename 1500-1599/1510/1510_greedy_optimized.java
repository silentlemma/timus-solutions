import java.io.IOException;

public class Main {
    private static final int INPUT_BUFFER_SIZE = 16384;
    private static final byte[] BUFFER = new byte[INPUT_BUFFER_SIZE];
    private static int position;
    private static int length;

    // up to 500 000 numbers are parsed by hand from 16 KB blocks, faster than
    // StreamTokenizer; the values are at most 10^9 and fit in an int
    private static int nextByte() throws IOException {
        if (position == length) {
            length = System.in.read(BUFFER);
            position = 0;
            if (length <= 0)
                return -1;
        }
        return BUFFER[position++];
    }

    private static int nextInt() throws IOException {
        int ch;
        do {
            ch = nextByte();
        } while (ch != -1 && ch <= ' ');
        int value = 0;
        while (ch >= '0' && ch <= '9') {
            value = value * 10 + ch - '0';
            ch = nextByte();
        }
        return value;
    }

    public static void main(String[] args) throws IOException {
        int count = nextInt();
        // the Boyer-Moore vote: a value met more often than all the others together
        // survives pairing every note with a different one
        int leader = 0, lead = 0;
        for (int i = 0; i < count; i++) {
            int value = nextInt();
            if (lead == 0) {
                leader = value;
                lead = 1;
            } else if (value == leader) {
                lead++;
            } else {
                lead--;
            }
        }
        System.out.println(leader);
    }
}
