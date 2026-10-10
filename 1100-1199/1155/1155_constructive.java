import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Scanner;

public class Main {
    // the cube: A B C D around the bottom face, E F G H above them
    static final String[] EDGES = {"AB", "BC", "CD", "DA", "EF", "FG",
                                   "GH", "HE", "AE", "BF", "CG", "DH"};
    // the cube is bipartite; every operation changes one chamber of each side
    static final String EVEN = "ACFH", CELLS = "ABCDEFGH";

    static boolean even(char c) { return EVEN.indexOf(c) >= 0; }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        Map<Character, Integer> count = new HashMap<>();
        int balance = 0;
        for (char c : CELLS.toCharArray()) {
            int v = in.nextInt();
            count.put(c, v);
            balance += even(c) ? v : -v;
        }
        if (balance != 0) {
            System.out.println("IMPOSSIBLE");
            return;
        }
        Map<Character, List<Character>> near = new HashMap<>();
        for (String e : EDGES) {
            near.computeIfAbsent(e.charAt(0), c -> new ArrayList<>()).add(e.charAt(1));
            near.computeIfAbsent(e.charAt(1), c -> new ArrayList<>()).add(e.charAt(0));
        }
        StringBuilder out = new StringBuilder();
        // annihilate along every edge as long as both ends hold duons, so that
        // afterwards every edge has an empty end
        for (String e : EDGES) {
            char a = e.charAt(0), b = e.charAt(1);
            int k = Math.min(count.get(a), count.get(b));
            for (int j = 0; j < k; j++) {
                out.append(a).append(b).append("-\n");
            }
            count.put(a, count.get(a) - k);
            count.put(b, count.get(b) - k);
        }
        // what is left can only sit at two opposite corners u and w, in equal
        // numbers; a pair made on the middle edge of a path u x y w removes both
        for (char u : EVEN.toCharArray()) {
            int left = count.get(u);
            if (left == 0) {
                continue;
            }
            char w = 0, y = 0;
            for (char c : CELLS.toCharArray()) {
                if (w == 0 && count.get(c) > 0 && !even(c)) {
                    w = c;
                }
            }
            char x = near.get(u).get(0);
            for (char c : near.get(x)) {
                if (y == 0 && near.get(w).contains(c)) {
                    y = c;
                }
            }
            for (int k = 0; k < left; k++) {
                out.append(x).append(y).append("+\n");
                out.append(u).append(x).append("-\n");
                out.append(y).append(w).append("-\n");
            }
            count.put(w, count.get(w) - left);
            count.put(u, 0);
        }
        System.out.print(out);
    }
}
