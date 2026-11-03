public class Main {
    static final int SIDE = 4, HALF = SIDE / 2;
    static final int BUFFER_SIZE = 4096;
    static final byte[] input = new byte[BUFFER_SIZE];
    static int position, available;

    static int read() throws java.io.IOException {
        if (position == available) {
            available = System.in.read(input);
            position = 0;
            if (available < 0)
                return -1;
        }
        return input[position++];
    }

    static int nextInt() throws java.io.IOException {
        int c = read();
        while (c <= ' ')
            c = read();
        int value = 0;
        while (c >= '0' && c <= '9') {
            value = value * 10 + c - '0';
            c = read();
        }
        return value;
    }

    public static void main(String[] args) throws Exception {
        int[] count = new int[SIDE];
        for (int r = 0; r < SIDE; r++)
            for (int c = 0; c < SIDE; c++)
                if (nextInt() == 1)
                    count[(r / HALF) * 2 + c / HALF]++;
        // Cost=4-count[target]+count[opposite]. Minimize over opposite pairs.
        System.out.println(
            SIDE - Math.max(Math.abs(count[0] - count[SIDE - 1]), Math.abs(count[1] - count[2])));
    }
}
