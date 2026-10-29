import java.io.IOException;

public class Main {
    // the numbers are parsed byte by byte from System.in, which needs much
    // less memory than Scanner
    private static int readInt() throws IOException {
        int c;
        do {
            c = System.in.read();
        } while (c <= ' ' && c != -1);
        int value = 0;
        while (c >= '0' && c <= '9') {
            value = value * 10 + c - '0';
            c = System.in.read();
        }
        return value;
    }

    private static final int[][] ORDERS = {{0, 1, 2}, {0, 2, 1}, {1, 0, 2},
                                           {1, 2, 0}, {2, 0, 1}, {2, 1, 0}};
    private static final char[] OPS = {'+', '-', '*'};

    private static int apply(int x, char op, int y) {
        if (op == '*')
            return x * y;
        return op == '+' ? x + y : x - y;
    }

    // x op1 y op2 z, multiplication first
    private static int evaluate(int x, char op1, int y, char op2, int z) {
        if (op2 == '*' && op1 != '*')
            return apply(x, op1, y * z);
        return apply(apply(x, op1, y), op2, z);
    }

    public static void main(String[] args) throws IOException {
        int[] v = {readInt(), readInt(), readInt()};
        int best = v[0] + v[1] + v[2];
        for (int[] o : ORDERS)
            for (char a : OPS)
                for (char b : OPS)
                    best = Math.min(best, evaluate(v[o[0]], a, v[o[1]], b, v[o[2]]));
        System.out.println(best);
    }
}
