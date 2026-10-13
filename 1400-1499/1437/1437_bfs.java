import java.util.ArrayDeque;
import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

public class Main {
    static final int CANS = 3;

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int[] cap = new int[CANS], sz = new int[CANS];
        for (int i = 0; i < CANS; i++) {
            cap[i] = in.nextInt();
            sz[i] = cap[i] + 1;
        }
        // a state (x, y, z) as one number; every move leaves some can empty or full
        boolean[] seen = new boolean[sz[0] * sz[1] * sz[2]];
        seen[0] = true;
        ArrayDeque<int[]> queue = new ArrayDeque<>();
        queue.add(new int[CANS]);
        Set<Integer> volumes = new HashSet<>();
        while (!queue.isEmpty()) {
            int[] v = queue.poll();
            for (int mask = 1; mask < 1 << CANS; mask++) {
                int sum = 0;
                for (int i = 0; i < CANS; i++)
                    if ((mask >> i & 1) == 1)
                        sum += v[i];
                volumes.add(sum);
            }
            for (int i = 0; i < CANS; i++)
                for (int j = -1; j < CANS; j++) {
                    int[] w = v.clone();
                    if (j < 0) { // fill can i from the pump up to the brim
                        w[i] = cap[i];
                    } else if (i != j) { // pour i into j
                        int move = Math.min(v[i], cap[j] - v[j]);
                        w[i] -= move;
                        w[j] += move;
                    }
                    int k = (w[0] * sz[1] + w[1]) * sz[2] + w[2];
                    if (!seen[k]) {
                        seen[k] = true;
                        queue.add(w);
                    }
                }
        }
        volumes.remove(0);
        System.out.println(volumes.size());
    }
}
