import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Scanner;

public class Main {
    static final int TRIANGLE = 3;

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        String color = in.next();
        List<Integer> poly = new ArrayList<>();
        for (int v = 0; v < n; v++) {
            poly.add(v);
        }
        StringBuilder cuts = new StringBuilder();
        int made = 0;
        while (poly.size() > TRIANGLE) {
            int m = poly.size();
            Map<Character, Integer> counts = new HashMap<>();
            for (int v : poly) {
                counts.merge(color.charAt(v), 1, Integer::sum);
            }
            int lonely = -1;
            for (int k = 0; k < m && lonely < 0; k++) {
                if (counts.get(color.charAt(poly.get(k))) == 1) {
                    lonely = k;
                }
            }
            if (lonely >= 0) {
                // a color met once: every triangle of the fan from that
                // vertex has it plus two neighbouring vertices, which differ
                for (int j = 2; j < m - 1; j++) {
                    cuts.append(poly.get(lonely) + 1).append(' ');
                    cuts.append(poly.get((lonely + j) % m) + 1).append('\n');
                    made++;
                }
                break;
            }
            // every color is met twice or more; a vertex whose neighbours
            // differ exists, as otherwise two colors would alternate around
            // the polygon, and cutting it off leaves all three colors
            int k = 0;
            while (color.charAt(poly.get((k + m - 1) % m)) == color.charAt(poly.get((k + 1) % m))) {
                k++;
            }
            cuts.append(poly.get((k + m - 1) % m) + 1).append(' ');
            cuts.append(poly.get((k + 1) % m) + 1).append('\n');
            made++;
            poly.remove(k);
        }
        System.out.print(made + "\n" + cuts);
    }
}
