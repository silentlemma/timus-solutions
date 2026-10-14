import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        // every record is two words, the kind and "Penguin"
        Map<String, Integer> seen = new HashMap<>();
        String best = null;
        for (int i = 0; i < n; i++) {
            String kind = in.next();
            in.next();
            seen.merge(kind, 1, Integer::sum);
            if (best == null || seen.get(kind) > seen.get(best))
                best = kind;
        }
        System.out.println(best + " Penguin");
    }
}
