import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;
import java.util.ArrayList;
import java.util.List;

public class Main {
    static final int CLASSES = 4; // houses by the parities of x and y
    static final int CANDIDATES_PER_PLACE = 5; // 5n names for n places

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StreamTokenizer in = new StreamTokenizer(reader);
        in.nextToken();
        int n = (int) in.nval;
        List<List<Integer>> groups = new ArrayList<>();
        for (int c = 0; c < CLASSES; c++) {
            groups.add(new ArrayList<>());
        }
        for (int i = 1; i <= CANDIDATES_PER_PLACE * n; i++) {
            in.nextToken();
            int x = (int) in.nval;
            in.nextToken();
            int y = (int) in.nval;
            groups.get(2 * (x & 1) + (y & 1)).add(i);
        }
        // two houses with the same parities differ by even dx and dy, so the
        // middle of their segment is a lattice point; 5n houses in 4 classes
        // leave one class with at least n of them, so the army always exists
        List<Integer> best = groups.get(0);
        for (List<Integer> g : groups) {
            if (g.size() > best.size()) {
                best = g;
            }
        }
        StringBuilder out = new StringBuilder("OK\n");
        for (int i = 0; i < n; i++) {
            out.append(i > 0 ? " " : "").append(best.get(i));
        }
        System.out.println(out);
    }
}
