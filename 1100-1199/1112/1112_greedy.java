import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int[][] segs = new int[n][];
        for (int i = 0; i < n; i++) {
            segs[i] = new int[] {in.nextInt(), in.nextInt()};
        }
        // the segment that ends first leaves the most room for the rest; touching
        // ends share no inner point
        Arrays.sort(segs, (p, q) -> Integer.compare(p[1], q[1]));
        List<int[]> chosen = new ArrayList<>();
        for (int[] s : segs) {
            if (chosen.isEmpty() || s[0] >= chosen.get(chosen.size() - 1)[1]) {
                chosen.add(s);
            }
        }
        StringBuilder out = new StringBuilder().append(chosen.size()).append('\n');
        for (int[] s : chosen) {
            out.append(s[0]).append(' ').append(s[1]).append('\n');
        }
        System.out.print(out);
    }
}
