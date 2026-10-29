import java.util.Scanner;

public class Main {
    private static final int[][] ORDERS = {{0, 1, 2}, {0, 2, 1}, {1, 0, 2},
                                           {1, 2, 0}, {2, 0, 1}, {2, 1, 0}};
    private static final String OPS = "+-*";

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

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int[] v = {in.nextInt(), in.nextInt(), in.nextInt()};
        int best = v[0] + v[1] + v[2];
        for (int[] o : ORDERS)
            for (char a : OPS.toCharArray())
                for (char b : OPS.toCharArray())
                    best = Math.min(best, evaluate(v[o[0]], a, v[o[1]], b, v[o[2]]));
        System.out.println(best);
    }
}
