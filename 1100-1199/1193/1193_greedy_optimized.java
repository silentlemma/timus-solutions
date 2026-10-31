public class Main {

    // refillable storage keeps input memory constant, regardless of input length.
    static final int BUFFER_SIZE = 4096;
    static final byte[] buffer = new byte[BUFFER_SIZE];
    static int at, size;
    static int read() throws java.io.IOException {
        if (at == size) {
            size = System.in.read(buffer);
            at = 0;
            if (size < 0)
                return -1;
        }
        return buffer[at++];
    }
    static long nextLong() throws java.io.IOException {
        int c;
        do {
            c = read();
        } while (c >= 0 && c <= ' ');
        boolean negative = c == '-';
        if (negative)
            c = read();
        long value = 0;
        while (c >= '0' && c <= '9') {
            value = value * 10 + c - '0';
            c = read();
        }
        return negative ? -value : value;
    }

    public static void main(String[] args) throws java.io.IOException {
        int n = (int)nextLong();
        int[] ready = new int[n], talk = new int[n], deadline = new int[n];
        for (int i = 0; i < n; i++) {
            int r = (int)nextLong(), t = (int)nextLong(), d = (int)nextLong();
            // insertion sort needs at most forty records and no boxed comparator or lambda.
            int j = i;
            while (j > 0 && ready[j - 1] > r) {
                ready[j] = ready[j - 1];
                talk[j] = talk[j - 1];
                deadline[j] = deadline[j - 1];
                j--;
            }
            ready[j] = r;
            talk[j] = t;
            deadline[j] = d;
        }
        // moving the start earlier changes nobody's order or wait, it only adds
        // the same amount to every deadline: the answer is the worst lateness
        int busy = 0, worst = 0;
        for (int i = 0; i < n; i++) {
            busy = Math.max(busy, ready[i]) + talk[i];
            worst = Math.max(worst, busy - deadline[i]);
        }
        System.out.println(worst);
    }
}
