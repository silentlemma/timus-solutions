public class Main {
    private static final int BUFFER_SIZE = 1024;
    private static final byte[] buffer = new byte[BUFFER_SIZE];
    private static int position;
    private static int available;

    // the numbers are parsed by hand from a small buffer, much lighter than Scanner
    private static int read() throws java.io.IOException {
        if (position == available) {
            available = System.in.read(buffer);
            position = 0;
            if (available < 0) {
                return -1;
            }
        }
        return buffer[position++];
    }

    private static int nextInt() throws java.io.IOException {
        int ch;
        do {
            ch = read();
        } while (ch <= ' ' && ch >= 0);
        int value = 0;
        while (ch >= '0' && ch <= '9') {
            value = value * 10 + ch - '0';
            ch = read();
        }
        return value;
    }

    public static void main(String[] args) throws java.io.IOException {
        int pages = nextInt();
        int cover = nextInt();
        int start = nextInt();
        int stop = nextInt();
        // on a shelf a volume's first page faces its right neighbour and its
        // last page faces the left one
        int whole = pages + 2 * cover;
        int length = pages;
        if (start < stop) {
            length = 2 * cover + (stop - start - 1) * whole;
        } else if (start > stop) {
            length = 2 * pages + 2 * cover + (start - stop - 1) * whole;
        }
        System.out.println(length);
    }
}
