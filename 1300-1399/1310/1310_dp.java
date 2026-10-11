import java.math.BigInteger;
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int length = in.nextInt(), top = in.nextInt(), k = in.nextInt();
        BigInteger n = new BigInteger(in.next());
        // ways[i][r]: how many ways i registers can hold values 1..M with a sum
        // that leaves remainder r modulo K
        BigInteger[][] ways = new BigInteger[length + 1][k];
        for (BigInteger[] row : ways)
            Arrays.fill(row, BigInteger.ZERO);
        ways[0][0] = BigInteger.ONE;
        for (int i = 1; i <= length; i++) {
            for (int v = 1; v <= top; v++) {
                for (int r = 0; r < k; r++) {
                    int to = (r + v) % k;
                    ways[i][to] = ways[i][to].add(ways[i - 1][r]);
                }
            }
        }
        StringBuilder out = new StringBuilder();
        int total = 0;
        for (int pos = 0; pos < length; pos++) {
            int left = length - pos - 1;
            // try the values in increasing order and skip whole blocks of states
            for (int v = 1; v <= top; v++) {
                BigInteger block = ways[left][Math.floorMod(-(total + v), k)];
                if (n.compareTo(block) < 0) {
                    out.append(pos > 0 ? " " : "").append(v);
                    total += v;
                    break;
                }
                n = n.subtract(block);
            }
        }
        System.out.println(out);
    }
}
