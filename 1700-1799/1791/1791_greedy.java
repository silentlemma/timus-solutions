import java.io.DataInputStream;
import java.io.IOException;

public class Main {
    static DataInputStream in = new DataInputStream(System.in);

    static long readLong() throws IOException {
        int c = in.read();
        while (c < '0') c = in.read();
        long v = 0;
        while (c >= '0') {
            v = v * 10 + (c - '0');
            c = in.read();
        }
        return v;
    }

    public static void main(String[] args) throws IOException {
        // ready and last: the first and the last minute a bus may enter
        long[][] ready = new long[2][], last = new long[2][];
        for (int s = 0; s < 2; s++) {
            int count = (int) readLong();
            ready[s] = new long[count];
            last[s] = new long[count];
            for (int i = 0; i < count; i++) {
                long t = readLong(), p = readLong();
                ready[s][i] = t;
                last[s][i] = t + p - 1;
            }
            // a bus must enter before the next one on its side
            for (int i = count - 2; i >= 0; i--) {
                last[s][i] = Math.min(last[s][i], last[s][i + 1] - 1);
            }
        }
        int[] head = {0, 0};
        long now = 0;
        while (head[0] < ready[0].length || head[1] < ready[1].length) {
            // among the waiting front buses, the one with the earlier last minute
            int pick = -1;
            long soonest = -1;
            for (int s = 0; s < 2; s++) {
                int h = head[s];
                if (h == ready[s].length) continue;
                if (soonest < 0 || ready[s][h] < soonest) soonest = ready[s][h];
                if (ready[s][h] <= now && (pick < 0 || last[s][h] < last[pick][head[pick]])) {
                    pick = s;
                }
            }
            if (pick < 0) {
                now = soonest;
                continue;
            }
            if (now > last[pick][head[pick]]) {
                System.out.println("NO");
                return;
            }
            head[pick]++;
            now++;
        }
        System.out.println("YES");
    }
}
