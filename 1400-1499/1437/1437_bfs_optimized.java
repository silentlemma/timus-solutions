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
    private static final int CANS = 3;
    private static final int WORD_BITS = Long.SIZE;
    private static long[] seen;
    private static int[] queue;
    private static int tail;

    static void offer(int state) {
        int word = state / WORD_BITS;
        long mask = 1L << (state % WORD_BITS);
        if ((seen[word] & mask) == 0) {
            seen[word] |= mask;
            queue[tail++] = state;
        }
    }

    public static void main(String[] args) throws java.io.IOException {
        int[] capacity = {number(), number(), number()};
        int[] stride = {(capacity[1] + 1) * (capacity[2] + 1), capacity[2] + 1, 1};
        int states = (capacity[0] + 1) * stride[0];
        int interior = 1;
        for (int value : capacity)
            interior *= Math.max(0, value - 1);
        // Filling or pouring always leaves at least one can empty or full.
        queue = new int[states - interior];
        seen = new long[(states + WORD_BITS - 1) / WORD_BITS];
        boolean[] volumes = new boolean[capacity[0] + capacity[1] + capacity[2] + 1];
        int[] current = new int[CANS];
        offer(0);
        for (int at = 0; at < tail; at++) {
            int state = queue[at];
            current[0] = state / stride[0];
            current[1] = state / stride[1] % (capacity[1] + 1);
            current[2] = state % stride[1];
            for (int subset = 1; subset < 1 << CANS; subset++) {
                int amount = 0;
                for (int i = 0; i < CANS; i++)
                    if ((subset & (1 << i)) != 0)
                        amount += current[i];
                volumes[amount] = true;
            }
            for (int from = 0; from < CANS; from++) {
                offer(state + (capacity[from] - current[from]) * stride[from]);
                for (int to = 0; to < CANS; to++)
                    if (to != from) {
                        int moved = Math.min(current[from], capacity[to] - current[to]);
                        offer(state + moved * (stride[to] - stride[from]));
                    }
            }
        }
        int answer = 0;
        for (int amount = 1; amount < volumes.length; amount++)
            if (volumes[amount])
                answer++;
        System.out.println(answer);
    }
}
