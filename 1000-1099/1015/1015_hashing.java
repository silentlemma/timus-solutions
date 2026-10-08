import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Main {
    static final int FACES = 6, BASE = 7;
    // quarter turns around the vertical and the left-right axes: the new face
    // at position i is the old face at position TURNS[t][i]
    static final int[][] TURNS = {{3, 5, 2, 1, 4, 0}, {0, 1, 5, 2, 3, 4}};

    static List<int[]> rotations() {
        List<int[]> all = new ArrayList<>();
        int[] identity = new int[FACES];
        for (int i = 0; i < FACES; i++) {
            identity[i] = i;
        }
        all.add(identity);
        for (int k = 0; k < all.size(); k++) {
            for (int[] turn : TURNS) {
                int[] r = new int[FACES];
                for (int i = 0; i < FACES; i++) {
                    r[i] = all.get(k)[turn[i]];
                }
                boolean known = false;
                for (int[] q : all) {
                    known |= Arrays.equals(q, r);
                }
                if (!known) {
                    all.add(r);
                }
            }
        }
        return all;
    }

    public static void main(String[] args) throws IOException {
        List<int[]> rots = rotations();
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StreamTokenizer in = new StreamTokenizer(reader);
        in.nextToken();
        int n = (int)in.nval;
        // the key of a die is the smallest code among its 24 rotations
        Map<Integer, Integer> group = new HashMap<>();
        List<StringBuilder> members = new ArrayList<>();
        int[] face = new int[FACES];
        for (int d = 1; d <= n; d++) {
            for (int i = 0; i < FACES; i++) {
                in.nextToken();
                face[i] = (int)in.nval;
            }
            int key = -1;
            for (int[] r : rots) {
                int code = 0;
                for (int i = 0; i < FACES; i++) {
                    code = code * BASE + face[r[i]];
                }
                if (key < 0 || code < key) {
                    key = code;
                }
            }
            Integer g = group.get(key);
            if (g == null) {
                group.put(key, members.size());
                members.add(new StringBuilder().append(d));
            } else {
                members.get(g).append(' ').append(d);
            }
        }
        StringBuilder out = new StringBuilder().append(members.size()).append('\n');
        for (StringBuilder m : members) {
            out.append(m).append('\n');
        }
        System.out.print(out);
    }
}
