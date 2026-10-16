import java.io.DataInputStream;
import java.io.IOException;

public class Main {
    static DataInputStream in = new DataInputStream(System.in);

    static int readInt() throws IOException {
        int c = in.read();
        while (c < '0') c = in.read();
        int v = 0;
        while (c >= '0') {
            v = v * 10 + (c - '0');
            c = in.read();
        }
        return v;
    }

    public static void main(String[] args) throws IOException {
        int n = readInt();
        // votes[k]: how many students get their wish if student k starts
        int[] votes = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            int want = readInt();
            // student i speaks want-th when student i - want + 1 starts
            votes[((i - want) % n + n) % n + 1]++;
        }
        int best = 1;
        for (int k = 2; k <= n; k++) {
            if (votes[k] > votes[best]) best = k;
        }
        System.out.println(best);
    }
}
