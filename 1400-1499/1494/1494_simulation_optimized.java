public class Main {
    static final int BUFFER_SIZE = 4096;
    static final byte[] buffer = new byte[BUFFER_SIZE];
    static int position, length;

    // the input is read in 4 KB blocks and parsed by hand instead of
    // StreamTokenizer
    static int readByte() throws java.io.IOException {
        if (position == length) {
            length = System.in.read(buffer);
            position = 0;
            if (length < 0)
                return -1;
        }
        return buffer[position++];
    }

    static int nextInt() throws java.io.IOException {
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
        // each ball is checked as it is read, so their order is never stored
        int n = nextInt();
        // the pocket is a stack: roll the balls in order, and whenever the top
        // one is the next ball the inspector took out, take it out
        int[] pocket = new int[n];
        int top = 0, next = 1;
        for (int i = 0; i < n; i++) {
            int ball = nextInt();
            while (next <= ball)
                pocket[top++] = next++;
            if (top == 0 || pocket[top - 1] != ball) {
                System.out.println("Cheater");
                return;
            }
            top--;
        }
        System.out.println("Not a proof");
    }
}
