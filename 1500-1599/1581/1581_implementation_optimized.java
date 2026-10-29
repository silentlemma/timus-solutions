public class Main {

    private static final int BUFFER_SIZE = 1024;
    private static final byte[] input = new byte[BUFFER_SIZE];
    private static int position;
    private static int length;

    // the numbers are parsed by hand from a small buffer, much lighter than Scanner
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

    public static void main(String[] args) throws java.io.IOException {
        int n = readInt();
        // the numbers are not stored: each is compared with the previous one
        int previous = readInt();
        int count = 1;
        StringBuilder output = new StringBuilder();
        // each run of equal numbers is said as its length and then the number
        for (int i = 1; i < n; i++) {
            int value = readInt();
            if (value == previous) {
                count++;
            } else {
                output.append(count).append(' ').append(previous).append(' ');
                previous = value;
                count = 1;
            }
        }
        output.append(count).append(' ').append(previous);
        System.out.println(output);
    }
}
