import java.util.*;

public class Main {
    static final int SIDE = 3, CUBES = SIDE * SIDE * SIDE, WAYS = 6;
    // the six directions; cells are numbered x * 9 + y * 3 + z
    static final int[] DX = {1, -1, 0, 0, 0, 0}, DY = {0, 0, 1, -1, 0, 0};
    static final int[] DZ = {0, 0, 0, 0, 1, -1}, AXIS = {0, 0, 1, 1, 2, 2};
    static final String NAMES = "RLFBUD";
    static final int RIGHT = 0, UP = 4; // indices of R and U
    static String snake;
    static StringBuilder answer = new StringBuilder();
    static int[][] near = new int[CUBES][WAYS];
    static boolean[] used = new boolean[CUBES];

    static int cellOf(int x, int y, int z) {
        if (x < 0 || x >= SIDE || y < 0 || y >= SIDE || z < 0 || z >= SIDE)
            return -1;
        return (x * SIDE + y) * SIDE + z;
    }

    // the free cells must stay one piece for the rest of the snake
    static boolean connected(int left) {
        int start = 0;
        while (start < CUBES && used[start])
            start++;
        if (start == CUBES)
            return true;
        boolean[] seen = new boolean[CUBES];
        int[] stack = new int[CUBES];
        int top = 0, count = 0;
        stack[top++] = start;
        seen[start] = true;
        while (top > 0) {
            int at = stack[--top];
            count++;
            for (int next : near[at])
                if (next >= 0 && !used[next] && !seen[next]) {
                    seen[next] = true;
                    stack[top++] = next;
                }
        }
        return count == left;
    }

    // place cube k + 1 after cube k, which sits at cell at
    static boolean fold(int k, int at, int way) {
        if (k == CUBES - 1)
            return true;
        for (int d = 0; d < WAYS; d++) {
            // a straight cube keeps the direction, a turning one changes axis
            if (snake.charAt(k) == 'F' ? d != way : AXIS[d] == AXIS[way])
                continue;
            int next = near[at][d];
            if (next < 0 || used[next])
                continue;
            used[next] = true;
            answer.append(NAMES.charAt(d));
            if (connected(CUBES - 2 - k) && fold(k + 1, next, d))
                return true;
            answer.setLength(answer.length() - 1);
            used[next] = false;
        }
        return false;
    }

    public static void main(String[] args) {
        snake = new Scanner(System.in).next();
        for (int x = 0; x < SIDE; x++)
            for (int y = 0; y < SIDE; y++)
                for (int z = 0; z < SIDE; z++)
                    for (int d = 0; d < WAYS; d++)
                        near[cellOf(x, y, z)][d] = cellOf(x + DX[d], y + DY[d], z + DZ[d]);
        // the cube colours 14 cells one way and 13 the other, and the snake
        // alternates, so it starts on the larger colour: a corner or the
        // centre of a face; up to symmetry that leaves three first moves
        int[][] roots = {{cellOf(0, 0, 0), RIGHT}, {cellOf(1, 1, 0), UP}, {cellOf(1, 1, 0), RIGHT}};
        for (int[] root : roots) {
            int start = root[0], d = root[1], next = near[start][d];
            Arrays.fill(used, false);
            used[start] = used[next] = true;
            answer.setLength(0);
            answer.append(NAMES.charAt(d));
            if (connected(CUBES - 2) && fold(1, next, d)) {
                System.out.println(answer);
                return;
            }
        }
        System.out.println("IMPOSSIBLE");
    }
}
