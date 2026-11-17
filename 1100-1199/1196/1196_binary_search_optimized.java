public class Main {
    private static final int BUFFER_SIZE = 4096;
    private static final byte[] buffer = new byte[BUFFER_SIZE];
    private static int position, length;

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

    private static boolean contains(int[] known, int year) {
        int left = 0, right = known.length;
        while (left < right) {
            int middle = left + (right - left) / 2;
            if (known[middle] == year) {
                return true;
            }
            if (known[middle] < year) {
                left = middle + 1;
            } else {
                right = middle;
            }
        }
        return false;
    }

    public static void main(String[] args) throws java.io.IOException {
        int[] known = new int[nextInt()];
        for (int i = 0; i < known.length; ++i) {
            known[i] = nextInt();
        }
        int queries = nextInt(), count = 0;
        for (int i = 0; i < queries; ++i) {
            if (contains(known, nextInt())) {
                ++count;
            }
        }
        System.out.println(count);
    }
}
