import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        int n = new Scanner(System.in).nextInt();
        // every two flags need a common color, and a color on at most two flags
        // serves one pair only, so k(k - 1) / 2 <= n; one color per pair is enough
        int k = 1;
        while ((k + 1) * k / 2 <= n) {
            k++;
        }
        List<List<Integer>> flags = new ArrayList<>();
        for (int a = 0; a < k; a++) {
            flags.add(new ArrayList<>());
        }
        int color = 0;
        for (int a = 0; a < k; a++) {
            for (int b = a + 1; b < k; b++) {
                color++;
                flags.get(a).add(color);
                flags.get(b).add(color);
            }
        }
        StringBuilder out = new StringBuilder().append(k).append('\n');
        for (List<Integer> flag : flags) {
            out.append(flag.size());
            for (int c : flag) {
                out.append(' ').append(c);
            }
            out.append('\n');
        }
        System.out.print(out);
    }
}
