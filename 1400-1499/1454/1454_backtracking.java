import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Scanner;
import java.util.Set;

public class Main {
    static final int PIECES = 5;
    static int[] pw = new int[PIECES], ph = new int[PIECES];
    static boolean[] used = new boolean[PIECES];
    static int height;

    // a stretch of the outline: its start, width and level
    static int[] seg(int x, int span, int level) { return new int[] {x, span, level}; }

    // skyline filling: the lowest, then leftmost, stretch of the outline must
    // hold the bottom-left corner of some piece in every tiling
    static boolean fill(List<int[]> sky, int left) {
        if (left == 0)
            return true;
        int k = 0;
        for (int i = 1; i < sky.size(); i++)
            if (sky.get(i)[2] < sky.get(k)[2])
                k = i;
        int[] s = sky.get(k);
        Set<String> tried = new HashSet<>();
        for (int i = 0; i < PIECES; i++) {
            if (used[i])
                continue;
            int[][] ways = {{pw[i], ph[i]}, {ph[i], pw[i]}};
            for (int[] o : ways) {
                int w = o[0], h = o[1];
                String key = w + "x" + h;
                if (tried.contains(key) || w > s[1] || s[2] + h > height)
                    continue;
                tried.add(key);
                List<int[]> all = new ArrayList<>(sky.subList(0, k));
                all.add(seg(s[0], w, s[2] + h));
                if (w < s[1])
                    all.add(seg(s[0] + w, s[1] - w, s[2]));
                all.addAll(sky.subList(k + 1, sky.size()));
                List<int[]> next = new ArrayList<>();
                for (int[] g : all) {
                    int[] last = next.isEmpty() ? null : next.get(next.size() - 1);
                    if (last != null && last[2] == g[2])
                        next.set(next.size() - 1, seg(last[0], last[1] + g[1], g[2]));
                    else
                        next.add(g);
                }
                used[i] = true;
                if (fill(next, left - 1))
                    return true;
                used[i] = false;
            }
        }
        return false;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        long area = 0;
        for (int i = 0; i < PIECES; i++) {
            pw[i] = in.nextInt();
            ph[i] = in.nextInt();
            area += (long)pw[i] * ph[i];
        }
        for (long width = 1; width * width <= area; width++)
            if (area % width == 0) {
                height = (int)(area / width);
                List<int[]> start = new ArrayList<>();
                start.add(seg(0, (int)width, 0));
                if (fill(start, PIECES)) {
                    System.out.println("YES");
                    return;
                }
            }
        System.out.println("NO");
    }
}
