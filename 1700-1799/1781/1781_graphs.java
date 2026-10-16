import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int[][] grid = new int[n][n];
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++) grid[i][j] = in.nextInt();
        // renumbering contests and rooms together, room j must be free of every
        // later contest, so a contest that uses room b must come no later than
        // contest b: an order of the graph with an edge a -> b for each such use
        int[] waiting = new int[n];
        for (int a = 0; a < n; a++)
            for (int b = 0; b < n; b++)
                if (a != b && grid[a][b] == 1) waiting[b]++;
        ArrayDeque<Integer> ready = new ArrayDeque<>();
        for (int v = 0; v < n; v++)
            if (waiting[v] == 0) ready.add(v);
        List<Integer> order = new ArrayList<>();
        while (!ready.isEmpty()) {
            int a = ready.poll();
            order.add(a);
            for (int b = 0; b < n; b++)
                if (a != b && grid[a][b] == 1 && --waiting[b] == 0) ready.add(b);
        }
        if (order.size() < n) {
            System.out.println(-1);
            return;
        }
        // each swap puts the next contest of the order in its place, so at most
        // n - 1 swaps are needed
        int[] where = new int[n], here = new int[n];
        for (int v = 0; v < n; v++) where[v] = here[v] = v;
        StringBuilder out = new StringBuilder();
        int count = 0;
        for (int i = 0; i < n; i++) {
            int j = where[order.get(i)];
            if (j == i) continue;
            out.append(i + 1).append(' ').append(j + 1).append('\n');
            count++;
            int t = here[i];
            here[i] = here[j];
            here[j] = t;
            where[here[i]] = i;
            where[here[j]] = j;
        }
        System.out.print(count + "\n" + out);
    }
}
