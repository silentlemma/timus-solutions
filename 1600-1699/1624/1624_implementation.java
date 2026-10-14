import java.io.*;
import java.util.*;

public class Main {
    static final int KINDS = 2; // walls above a cell and left of it
    static int w, h, width;
    static int[] conflict; // reports ruling out the second start being the first shifted

    static class Scout {
        int r, c; // the position relative to the unknown start
        int loR, hiR, loC, hiC;
        HashMap<Long, Integer> seen = new HashMap<>(); // edge -> 1 for a door, 0 for a wall
        // the edges seen as (r, c), at kind * 2 + (1 for a door, 0 for a wall)
        List<List<int[]>> byKind = new ArrayList<>();

        Scout() {
            for (int i = 0; i < KINDS * 2; i++)
                byKind.add(new ArrayList<>());
        }
    }

    static Scout[] scouts = {new Scout(), new Scout()};

    // the start pairs left: 0, 1, or 2 for two or more
    static int starts() {
        Scout a = scouts[0], b = scouts[1];
        int lo1r = -a.loR, hi1r = h - 1 - a.hiR, lo1c = -a.loC, hi1c = w - 1 - a.hiC;
        int lo2r = -b.loR, hi2r = h - 1 - b.hiR, lo2c = -b.loC, hi2c = w - 1 - b.hiC;
        long total = 0;
        for (int dr = -(h - 1); dr < h; dr++) {
            int top = Math.max(lo1r, lo2r - dr), bottom = Math.min(hi1r, hi2r - dr);
            if (top > bottom)
                continue;
            for (int dc = -(w - 1); dc < w; dc++) {
                if (conflict[(dr + h - 1) * width + dc + w - 1] != 0)
                    continue;
                int left = Math.max(lo1c, lo2c - dc), right = Math.min(hi1c, hi2c - dc);
                if (left <= right) {
                    total += (long)(bottom - top + 1) * (right - left + 1);
                    if (total > 1)
                        return 2;
                }
            }
        }
        return (int)total;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(in.readLine());
        w = Integer.parseInt(st.nextToken());
        h = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        width = 2 * w - 1;
        conflict = new int[(2 * h - 1) * width];
        int safe = -1, count = starts();
        for (int step = 1; step <= k; step++) {
            String report = in.readLine().trim();
            char d = report.charAt(0);
            int door = report.charAt(1) == '+' ? 1 : 0;
            int who = (step - 1) % 2;
            Scout me = scouts[who], other = scouts[1 - who];
            // the wall or door crossed: kind 0 above row r, kind 1 left of column c
            int kind = d == 'N' || d == 'S' ? 0 : 1;
            int er = me.r + (d == 'S' ? 1 : 0), ec = me.c + (d == 'E' ? 1 : 0);
            long key = ((long)kind * (2 * MAX + 1) + er + MAX) * (2 * MAX + 1) + ec + MAX;
            boolean changed = false;
            Integer old = me.seen.get(key);
            if (old == null) {
                me.seen.put(key, door);
                me.byKind.get(kind * 2 + door).add(new int[] {er, ec});
                int sign = who == 0 ? 1 : -1;
                for (int[] f : other.byKind.get(kind * 2 + 1 - door)) {
                    int dr = sign * (er - f[0]), dc = sign * (ec - f[1]);
                    if (-h < dr && dr < h && -w < dc && dc < w) {
                        conflict[(dr + h - 1) * width + dc + w - 1]++;
                        changed = true;
                    }
                }
            } else if (old != door) {
                System.out.println("A mistake has been made at step number " + step);
                return;
            }
            if (door == 1) {
                me.r += d == 'S' ? 1 : d == 'N' ? -1 : 0;
                me.c += d == 'E' ? 1 : d == 'W' ? -1 : 0;
                if (me.r < me.loR || me.r > me.hiR || me.c < me.loC || me.c > me.hiC) {
                    me.loR = Math.min(me.loR, me.r);
                    me.hiR = Math.max(me.hiR, me.r);
                    me.loC = Math.min(me.loC, me.c);
                    me.hiC = Math.max(me.hiC, me.c);
                    changed = true;
                }
            }
            if (changed) // the count changes only with a new conflict or a wider path
                count = starts();
            if (count == 0) {
                System.out.println("A mistake has been made at step number " + step);
                return;
            }
            if (count == 1 && safe < 0)
                safe = step;
        }
        System.out.println(safe > 0 ? "The scouts are safe at step number " + safe
                                    : "There is not enough data");
    }

    static final int MAX = 1 << 17; // relative coordinates stay within the number of reports
}
