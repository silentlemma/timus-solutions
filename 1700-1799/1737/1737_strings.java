import java.util.Scanner;
import java.util.TreeSet;

public class Main {
    static final int LIMIT = 100000;

    public static void main(String[] args) {
        int n = new Scanner(System.in).nextInt();
        // a palindrome of two or more letters has one of two or three
        // letters in its middle, so any three letters in a row must differ,
        // and a name is one order of a, b, c repeated
        String[] orders = {"abc", "acb", "bac", "bca", "cab", "cba"};
        TreeSet<String> names = new TreeSet<>();
        for (String order : orders) {
            StringBuilder name = new StringBuilder();
            for (int i = 0; i < n; i++) {
                name.append(order.charAt(i % order.length()));
            }
            names.add(name.toString());
        }
        if ((long) names.size() * n > LIMIT) {
            System.out.println("TOO LONG");
            return;
        }
        StringBuilder out = new StringBuilder();
        for (String name : names) {
            out.append(name).append('\n');
        }
        System.out.print(out);
    }
}
