import java.util.Arrays;
import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

public class Main {
    static final String LYOSHA = "Efremov";
    static final String VADIK = "Kantorov";

    static String team(String... names) {
        String[] sorted = names.clone();
        Arrays.sort(sorted);
        return String.join(" ", sorted);
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        Set<String> played = new HashSet<>();
        for (int i = 0; i < n; i++) {
            String[] names = new String[in.nextInt()];
            for (int j = 0; j < names.length; j++) {
                names[j] = in.next();
            }
            played.add(team(names));
        }
        int lyosha = in.nextInt(), vadik = in.nextInt(), m = in.nextInt();
        int best = -1;
        String chosen = null;
        for (int i = 0; i < m; i++) {
            String name = in.next();
            int rating = in.nextInt(), strength;
            // Lyosha stays away from a team that has played before, and the
            // pair left over must then be new, or the team is out
            if (!played.contains(team(LYOSHA, VADIK, name))) {
                strength = lyosha + vadik + rating;
            } else if (!played.contains(team(VADIK, name))) {
                strength = vadik + rating;
            } else {
                continue;
            }
            if (strength > best) {
                best = strength;
                chosen = name;
            }
        }
        System.out.println(chosen == null ? "Fail" : "Win\n" + chosen);
    }
}
