import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Scanner;
import java.util.Set;

public class Main {
    static Set<String> readSet(Scanner in) {
        int count = in.nextInt();
        Set<String> items = new HashSet<>();
        for (int i = 0; i < count; i++)
            items.add(in.next());
        return items;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        Set<String> menu = readSet(in);
        int k = in.nextInt();
        List<Set<String>> blocks = new ArrayList<>();
        for (int i = 0; i <= k; i++)
            blocks.add(readSet(in));
        int m = in.nextInt();
        // the first student was fine, so the meal is m products of the rest
        List<String> safe = new ArrayList<>();
        for (String p : menu) {
            if (!blocks.get(0).contains(p))
                safe.add(p);
        }
        StringBuilder out = new StringBuilder();
        for (int i = 1; i <= k; i++) {
            int risky = 0;
            for (String p : safe) {
                if (blocks.get(i).contains(p))
                    risky++;
            }
            if (m == 0 || risky == 0)
                out.append("YES\n");
            else if (safe.size() - risky < m)
                out.append("NO\n"); // every possible meal holds a dangerous product
            else
                out.append("MAYBE\n");
        }
        System.out.print(out);
    }
}
