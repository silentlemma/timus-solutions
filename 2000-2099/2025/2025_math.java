import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int tests = in.nextInt();
        StringBuilder out = new StringBuilder();
        for (int t = 0; t < tests; t++) {
            long count = in.nextLong(), groups = in.nextLong();
            // groups of sizes small and small + 1, as equal as possible
            long small = count / groups, larger = count % groups;
            long squares = (groups - larger) * small * small + larger * (small + 1) * (small + 1);
            out.append((count * count - squares) / 2).append('\n');
        }
        System.out.print(out);
    }
}
