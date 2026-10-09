import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        int n = new Scanner(System.in).nextInt();
        // on sorted numbers every partition peels off just the first one
        StringBuilder out = new StringBuilder();
        for (int i = 1; i <= n; i++) {
            out.append(i).append(i < n ? " " : "");
        }
        System.out.println(out);
    }
}
