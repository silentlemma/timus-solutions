import java.io.BufferedOutputStream;
import java.io.IOException;
import java.util.Scanner;

public class Main {
    static final int FULL = 100; // brightness is given in percent

    public static void main(String[] args) throws IOException {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt(), b = in.nextInt();
        // lamp i is on when floor((i + 1) b / 100) grows: every stretch then holds
        // less than one lamp more or less than L b / 100, and the pattern repeats
        byte[] row = new byte[n + 1];
        for (int i = 0; i < n; i++)
            row[i] = (byte)((i % FULL + 1) * b / FULL > i % FULL * b / FULL ? '1' : '0');
        row[n] = '\n';
        BufferedOutputStream out = new BufferedOutputStream(System.out);
        out.write(row);
        out.flush();
    }
}
