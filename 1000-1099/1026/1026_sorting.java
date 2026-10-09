import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(in.readLine().trim());
        int[] base = new int[n];
        for (int i = 0; i < n; i++) {
            base[i] = Integer.parseInt(in.readLine().trim());
        }
        in.readLine();
        int k = Integer.parseInt(in.readLine().trim());
        // the i-th smallest element is the i-th element of the sorted database
        Arrays.sort(base);
        StringBuilder out = new StringBuilder();
        for (int q = 0; q < k; q++) {
            out.append(base[Integer.parseInt(in.readLine().trim()) - 1]).append('\n');
        }
        System.out.print(out);
    }
}
