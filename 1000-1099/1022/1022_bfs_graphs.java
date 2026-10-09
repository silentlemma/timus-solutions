import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        List<List<Integer>> children = new ArrayList<>();
        int[] parents = new int[n + 1];
        children.add(new ArrayList<>());
        for (int v = 1; v <= n; v++) {
            List<Integer> kids = new ArrayList<>();
            for (int c = in.nextInt(); c != 0; c = in.nextInt()) {
                kids.add(c);
                parents[c]++;
            }
            children.add(kids);
        }
        // Kahn's algorithm: a member may speak once all its parents have spoken
        List<Integer> order = new ArrayList<>();
        for (int v = 1; v <= n; v++) {
            if (parents[v] == 0) {
                order.add(v);
            }
        }
        for (int i = 0; i < order.size(); i++) {
            for (int c : children.get(order.get(i))) {
                if (--parents[c] == 0) {
                    order.add(c);
                }
            }
        }
        StringBuilder out = new StringBuilder();
        for (int v : order) {
            out.append(out.length() > 0 ? " " : "").append(v);
        }
        System.out.println(out);
    }
}
