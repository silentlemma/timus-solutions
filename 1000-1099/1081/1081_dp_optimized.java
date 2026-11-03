public class Main {
    static int nextInt() throws Exception {
        int c = System.in.read();
        while (c <= ' ')
            c = System.in.read();
        int value = 0;
        while (c >= '0' && c <= '9') {
            value = value * 10 + c - '0';
            c = System.in.read();
        }
        return value;
    }
    public static void main(String[] args) throws Exception {
        int n = nextInt(), rank = nextInt(), total = 1, zero = 1;
        for (int i = 0; i < n; i++) {
            int next = total + zero;
            zero = total;
            total = next;
        }
        if (rank > total) {
            System.out.println(-1);
            return;
        }
        rank--;
        char[] result = new char[n];
        for (int i = 0; i < n; i++) {
            result[i] = '0';
            if (rank >= zero) {
                rank -= zero;
                result[i] = '1';
            }
            // After choosing1, rank is below the next weight: the next bit is0.
            int previous = total - zero;
            total = zero;
            zero = previous;
        }
        System.out.println(new String(result));
    }
}
