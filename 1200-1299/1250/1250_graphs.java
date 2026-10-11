import java.io.*;
import java.util.*;

public class Main {
    static final int HEADER = 4;
    static int[] reached, stack;

    // marks in free (clearing it) every cell reachable from start through
    // cells where free is set, moving along the given steps; they are the
    // first cells of reached, and their number is returned
    static int flood(int start, boolean[] free, int[] steps) {
        int count = 0, top = 0;
        free[start] = false;
        reached[count++] = start;
        stack[top++] = start;
        while (top > 0) {
            int c = stack[--top];
            for (int d : steps) {
                int n = c + d;
                if (n >= 0 && n < free.length && free[n]) {
                    free[n] = false;
                    reached[count++] = n;
                    stack[top++] = n;
                }
            }
        }
        return count;
    }

    public static void main(String[] args) throws IOException {
        DataInputStream in = new DataInputStream(new BufferedInputStream(System.in));
        StringBuilder head = new StringBuilder();
        int[] v = new int[HEADER];
        for (int k = 0; k < v.length;) {
            int c = in.read();
            if (c >= '0' && c <= '9') {
                head.append((char)c);
            } else if (head.length() > 0) {
                v[k++] = Integer.parseInt(head.toString());
                head.setLength(0);
            }
        }
        int w = v[0], h = v[1], x = v[2], y = v[HEADER - 1];
        // the map padded by a ring of outside cells
        int pw = w + 2, size = (w + 2) * (h + 2);
        boolean[] land = new boolean[size], sea = new boolean[size];
        reached = new int[size];
        stack = new int[size];
        for (int i = 1; i <= h; i++)
            for (int j = 1; j <= w;) {
                int c = in.read();
                if (c < 0)
                    break;
                if (c == '#' || c == '.') {
                    land[i * pw + j] = c == '#';
                    sea[i * pw + j] = c == '.';
                    j++;
                }
            }
        int[] step4 = {1, -1, pw, -pw};
        int[] step8 = {1, -1, pw, -pw, pw + 1, pw - 1, -pw + 1, -pw - 1};
        // the sacred sea: sea cells joined to the drowning point by 8 directions
        boolean[] free = new boolean[size];
        Arrays.fill(free, true);
        int start = y * pw + x;
        if (sea[start])
            for (int k = flood(start, sea, step8) - 1; k >= 0; k--)
                free[reached[k]] = false;
        // an eight-connected sea stops every four-connected path, so what the
        // outside cannot reach without crossing the sacred sea lies inside it
        for (int k = flood(0, free, step4) - 1; k >= 0; k--)
            land[reached[k]] = false;
        int count = 0;
        for (int c = 0; c < size; c++)
            if (land[c]) {
                count++;
                flood(c, land, step4);
            }
        System.out.println(count);
    }
}
