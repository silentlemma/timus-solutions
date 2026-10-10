import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;
import java.util.HashSet;
import java.util.Set;

public class Main {
    static int[] parent;

    static int find(int x) {
        while (parent[x] != x) {
            parent[x] = parent[parent[x]];
            x = parent[x];
        }
        return x;
    }

    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        int m = (int)in.nval;
        in.nextToken();
        int n = (int)in.nval;
        parent = new int[m];
        for (int i = 0; i < m; i++) {
            parent[i] = i;
        }
        // a piece of colour c in box b is an edge b -> c; every box has n pieces
        // and should get n back, so each connected group of boxes is an Euler
        // circuit, walked one carried piece per move
        int moves = 0;
        boolean[] touched = new boolean[m];
        for (int box = 0; box < m; box++) {
            for (int k = 0; k < n; k++) {
                in.nextToken();
                int colour = (int)in.nval - 1;
                if (colour != box) {
                    moves++;
                    touched[box] = touched[colour] = true;
                    parent[find(box)] = find(colour);
                }
            }
        }
        Set<Integer> groups = new HashSet<>();
        for (int x = 0; x < m; x++) {
            if (touched[x]) {
                groups.add(find(x));
            }
        }
        // one empty move of the hand between groups
        System.out.println(moves == 0 ? 0 : moves + groups.size() - 1);
    }
}
