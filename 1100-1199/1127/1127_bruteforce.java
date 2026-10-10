import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Scanner;
import java.util.Set;

public class Main {
    // face positions in the input: front, right, left, back, top, bottom; a
    // quarter turn about the vertical axis (front goes right) and one about the
    // left-right axis (top goes front), as new position from old position
    static final int FACES = 6, FRONT = 0, RIGHT = 1, LEFT = 2, BACK = 3;
    static final int[] SPIN = {2, 0, 3, 1, 4, 5}, TIP = {4, 1, 2, 5, 3, 0};

    static List<Integer> key(int[] a) {
        List<Integer> out = new ArrayList<>();
        for (int v : a) {
            out.add(v);
        }
        return out;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        // all 24 rotations as position -> original face
        int[] start = new int[FACES];
        for (int p = 0; p < FACES; p++) {
            start[p] = p;
        }
        Set<List<Integer>> seen = new HashSet<>();
        seen.add(key(start));
        List<int[]> rotations = new ArrayList<>();
        ArrayDeque<int[]> stack = new ArrayDeque<>();
        stack.push(start);
        while (!stack.isEmpty()) {
            int[] cur = stack.pop();
            rotations.add(cur);
            for (int[] turn : new int[][] {SPIN, TIP}) {
                int[] next = new int[FACES];
                for (int p = 0; p < FACES; p++) {
                    next[p] = cur[turn[p]];
                }
                if (seen.add(key(next))) {
                    stack.push(next);
                }
            }
        }
        // each cube can show a given ring of side colours at most once, since its
        // faces all differ; the tallest tower is the most common ring
        Map<String, Integer> rings = new HashMap<>();
        int best = 0;
        for (int i = 0; i < n; i++) {
            String cube = in.next();
            for (int[] rot : rotations) {
                String ring = "" + cube.charAt(rot[FRONT]) + cube.charAt(rot[RIGHT]) +
                              cube.charAt(rot[BACK]) + cube.charAt(rot[LEFT]);
                best = Math.max(best, rings.merge(ring, 1, Integer::sum));
            }
        }
        System.out.println(best);
    }
}
