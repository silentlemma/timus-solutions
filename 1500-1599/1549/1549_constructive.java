import java.util.*;

public class Main {
    static final int CORNERS = 4;        // a loop turns at least four times, by 90 degrees each
    static final int FIRST_STAIR = 12;   // all-turn loops have 4 or at least 12 turns
    static final int NOTCHED_HEIGHT = 3; // rows of the box when a corner is cut in

    // F, L or R for every cell {x, y} of a closed loop of cells
    static String letters(List<int[]> cells) {
        int n = cells.size();
        StringBuilder out = new StringBuilder();
        for (int i = 0; i < n; i++) {
            int[] a = cells.get((i + n - 1) % n), b = cells.get(i), c = cells.get((i + 1) % n);
            int dx1 = b[0] - a[0], dy1 = b[1] - a[1], dx2 = c[0] - b[0], dy2 = c[1] - b[1];
            out.append(dx1 == dx2 && dy1 == dy2 ? 'F' : dx1 * dy2 - dy1 * dx2 > 0 ? 'L' : 'R');
        }
        return out.toString();
    }

    // the border of a width x height box, counterclockwise from the lower left
    // corner, with bumps (2 cells wide, 1 high) on the top and bottom rows, and
    // with the lower left corner cut in if notch is set
    static List<int[]> ring(int width, int height, int bumps, boolean notch) {
        List<Integer> freeTop = new ArrayList<>(), freeBottom = new ArrayList<>();
        for (int x = width - 2; x > 1; x -= 2)
            freeTop.add(x);
        for (int x = 2 + (notch ? 1 : 0); x < width - 1; x += 2)
            freeBottom.add(x);
        int up = Math.min(bumps, freeTop.size());
        Set<Integer> upAt = new HashSet<>(freeTop.subList(0, up));
        Set<Integer> downAt = new HashSet<>(freeBottom.subList(0, bumps - up));
        List<int[]> cells = new ArrayList<>();
        if (notch) {
            cells.add(new int[] {1, 1});
            cells.add(new int[] {1, 0});
        } else {
            cells.add(new int[] {0, 0});
        }
        for (int x = cells.get(cells.size() - 1)[0] + 1; x < width;
             x++) { // the bottom row, going east
            if (downAt.contains(x)) {
                cells.add(new int[] {x - 1, -1});
                cells.add(new int[] {x, -1});
            }
            cells.add(new int[] {x, 0});
        }
        for (int y = 1; y < height; y++)
            cells.add(new int[] {width - 1, y});
        for (int x = width - 2; x >= 0; x--) { // the top row, going west
            cells.add(new int[] {x, height - 1});
            if (upAt.contains(x)) {
                cells.add(new int[] {x, height});
                cells.add(new int[] {x - 1, height});
                cells.add(new int[] {x - 1, height - 1});
                x--;
            }
        }
        // the left column, going south; with a notch its last cell (0, 1) leads
        // into (1, 1) instead of the corner
        for (int y = height - 2; y > 0; y--)
            cells.add(new int[] {0, y});
        return cells;
    }

    static String build(int straights, int turns) {
        if (straights == 0 && turns >= FIRST_STAIR) {
            // a staircase loop: four corners and steps LR on the sides
            StringBuilder sideA = new StringBuilder();
            for (int i = 1; i < (turns - CORNERS) / CORNERS; i++)
                sideA.append("LR");
            String half = "L" + sideA + "L"
                          + "LR";
            return half + half;
        }
        boolean notch = turns % CORNERS == 2;
        int bumps = (turns - CORNERS) / CORNERS; // a notch takes the other 2 turns
        return letters(ring(2 + straights / 2 + bumps, notch ? NOTCHED_HEIGHT : 2, bumps, notch));
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int s = in.nextInt(), t = in.nextInt();
        // both counts even, at least 4 turns, and without straights the turns
        // must be 4 or a multiple of 4 from 12
        int straights = s - s % 2, turns = t - t % 2;
        if (turns < CORNERS) {
            System.out.println("Atawazu");
            return;
        }
        if (straights == 0) {
            turns -= turns % CORNERS;
            if (turns < FIRST_STAIR)
                turns = CORNERS;
        }
        String path = build(straights, turns);
        System.out.println(path.length() + "\n" + path);
    }
}
