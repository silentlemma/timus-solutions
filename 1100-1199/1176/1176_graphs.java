import java.io.BufferedInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.util.Arrays;

public class Main {
    static final int BUFFER = 1 << 16;
    static InputStream in = new BufferedInputStream(System.in, BUFFER);

    static int read() throws IOException {
        int c = in.read();
        while (c < '0') {
            c = in.read();
        }
        int v = 0;
        while (c >= '0') {
            v = v * 10 + c - '0';
            c = in.read();
        }
        return v;
    }

    public static void main(String[] args) throws IOException {
        int n = read(), a = read();
        // the channels still to lay are the missing ones; every planet has as
        // many of them going out as coming in, so they form one Euler circuit
        int[][] todo = new int[n + 1][];
        todo[0] = new int[0];
        int[] row = new int[n];
        for (int i = 1; i <= n; i++) {
            int count = 0;
            for (int j = 1; j <= n; j++) {
                if (read() == 0 && i != j) {
                    row[count++] = j;
                }
            }
            todo[i] = Arrays.copyOf(row, count);
        }
        // Hierholzer: walk until stuck, then back up and splice in side loops
        int[] next = new int[n + 1];
        int total = 0;
        for (int[] t : todo) {
            total += t.length;
        }
        int[] stack = new int[total + 1], circuit = new int[total + 1];
        int top = 0, size = 0;
        stack[top++] = a;
        while (top > 0) {
            int v = stack[top - 1];
            if (next[v] < todo[v].length) {
                stack[top++] = todo[v][next[v]++];
            } else {
                circuit[size++] = stack[--top];
            }
        }
        StringBuilder out = new StringBuilder();
        for (int k = size - 1; k > 0; k--) {
            out.append(circuit[k]).append(' ').append(circuit[k - 1]).append('\n');
        }
        System.out.print(out);
    }
}
