import java.util.*;

public class Main {
    // four times the square of the shortest longest chord of a cover of side or
    // radius 1: a circle's diameter, a square's side, a triangle's height
    static final int[] NARROWEST = {0, 16, 4, 3};
    // four times the square of the longest segment in a hole: a circle's
    // diameter, a square's diagonal, a triangle's side
    static final int[] WIDEST = {0, 16, 8, 4};

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int kind = in.nextInt(), size = in.nextInt();
        int hole = WIDEST[kind] * size * size;
        int n = in.nextInt(), count = 0;
        // a cover held upright crosses the plane of the hole along parallel chords,
        // so it passes when its longest chord in some direction fits in the hole
        for (int i = 0; i < n; i++) {
            kind = in.nextInt();
            size = in.nextInt();
            if (NARROWEST[kind] * size * size <= hole)
                count++;
        }
        System.out.println(count);
    }
}
