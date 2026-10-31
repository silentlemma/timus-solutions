public class Main {

    static final int BUFFER_SIZE = 4096;
    static final int BYTE_MASK = 255;
    static final byte[] BUFFER = new byte[BUFFER_SIZE];
    static int position, available;
    // a refillable buffer keeps input memory constant for any number of records.
    static int read() throws java.io.IOException {
        if (position == available) {
            available = System.in.read(BUFFER);
            position = 0;
            if (available < 0)
                return -1;
        }
        return BUFFER[position++] & BYTE_MASK;
    }
    static int nextInt() throws java.io.IOException {
        int c;
        do {
            c = read();
        } while (c <= ' ' && c >= 0);
        int value = 0, sign = 1;
        if (c == '-') {
            sign = -1;
            c = read();
        }
        while (c >= '0' && c <= '9') {
            value = value * 10 + c - '0';
            c = read();
        }
        return sign * value;
    }

    static final int CHAR_COUNT = 128, DEGREE = 3;
    // the cube: A B C D around the bottom face, E F G H above them
    static final String[] EDGES = {"AB", "BC", "CD", "DA", "EF", "FG",
                                   "GH", "HE", "AE", "BF", "CG", "DH"};
    // the cube is bipartite; every operation changes one chamber of each side
    static final String EVEN = "ACFH", CELLS = "ABCDEFGH";

    static boolean even(char c) { return EVEN.indexOf(c) >= 0; }

    public static void main(String[] args) throws java.io.IOException {
        // eight ascii labels and three neighbors per vertex need no boxed maps.
        int[] count = new int[CHAR_COUNT];
        int balance = 0;
        for (char c : CELLS.toCharArray()) {
            int v = nextInt();
            count[c] = v;
            balance += even(c) ? v : -v;
        }
        if (balance != 0) {
            System.out.println("IMPOSSIBLE");
            return;
        }
        char[][] near = new char[CHAR_COUNT][DEGREE];
        int[] degree = new int[CHAR_COUNT];
        for (String e : EDGES) {
            near[e.charAt(0)][degree[e.charAt(0)]++] = e.charAt(1);
            near[e.charAt(1)][degree[e.charAt(1)]++] = e.charAt(0);
        }
        StringBuilder out = new StringBuilder();
        // annihilate along every edge as long as both ends hold duons, so that
        // afterwards every edge has an empty end
        for (String e : EDGES) {
            char a = e.charAt(0), b = e.charAt(1);
            int k = Math.min(count[a], count[b]);
            for (int j = 0; j < k; j++) {
                out.append(a).append(b).append("-\n");
            }
            count[a] = count[a] - k;
            count[b] = count[b] - k;
        }
        // what is left can only sit at two opposite corners u and w, in equal
        // numbers; a pair made on the middle edge of a path u x y w removes both
        for (char u : EVEN.toCharArray()) {
            int left = count[u];
            if (left == 0) {
                continue;
            }
            char w = 0, y = 0;
            for (char c : CELLS.toCharArray()) {
                if (w == 0 && count[c] > 0 && !even(c)) {
                    w = c;
                }
            }
            char x = near[u][0];
            for (char c : near[x]) {
                for (char d : near[w])
                    if (y == 0 && c == d)
                        y = c;
            }
            for (int k = 0; k < left; k++) {
                out.append(x).append(y).append("+\n");
                out.append(u).append(x).append("-\n");
                out.append(y).append(w).append("-\n");
            }
            count[w] = count[w] - left;
            count[u] = 0;
        }
        System.out.print(out);
    }
}
