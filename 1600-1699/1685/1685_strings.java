import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        String line = in.readLine();
        String text = line == null ? "" : line;
        int n = text.length();
        char[] out = new char[n];
        // the encoded text lists the middle of a range, then its left part,
        // then its right part: replay that order and put each letter back
        Deque<int[]> stack = new ArrayDeque<>();
        stack.push(new int[] {0, n - 1});
        int at = 0;
        while (!stack.isEmpty()) {
            int[] range = stack.pop();
            if (range[0] > range[1]) {
                continue;
            }
            int mid = (range[0] + range[1]) / 2;
            out[mid] = text.charAt(at++);
            stack.push(new int[] {mid + 1, range[1]});
            stack.push(new int[] {range[0], mid - 1});
        }
        System.out.println(new String(out));
    }
}
