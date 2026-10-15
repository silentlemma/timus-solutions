import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
    static String[] animals;
    static int[] owner;
    static List<String> rows = new ArrayList<>();

    static int gcd(int a, int b) {
        return b == 0 ? a : gcd(b, a % b);
    }

    static int build(int lo, int hi) {
        if (owner[lo] == owner[hi - 1]) {
            rows.add(animals[owner[lo]]);
        } else {
            int mid = (lo + hi) / 2;
            int left = build(lo, mid);
            int right = build(mid, hi);
            rows.add(left + " " + right);
        }
        return rows.size();
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        animals = in.next().split("-");
        int m = animals.length;
        int[] num = new int[m], den = new int[m];
        int leaves = 1;
        for (int i = 0; i < m; i++) {
            String[] part = in.next().split("/");
            int a = Integer.parseInt(part[0]), b = Integer.parseInt(part[1]);
            int g = gcd(a, b);
            num[i] = a / g;
            den[i] = b / g;
            // a crossing halves every share, so only shares with a power of
            // two below can come out
            if ((den[i] & (den[i] - 1)) != 0) {
                System.out.println("No solution");
                return;
            }
            leaves = Math.max(leaves, den[i]);
        }
        // give each animal its share of the equal leaves, in order, and
        // cross halves; a half that is one animal is just that animal
        owner = new int[leaves];
        int filled = 0;
        for (int i = 0; i < m; i++) {
            for (int k = 0; k < num[i] * (leaves / den[i]); k++) {
                owner[filled++] = i;
            }
        }
        build(0, leaves);
        StringBuilder out = new StringBuilder();
        out.append(rows.size()).append('\n');
        for (String row : rows) {
            out.append(row).append('\n');
        }
        System.out.print(out);
    }
}
