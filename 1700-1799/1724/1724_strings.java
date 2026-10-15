import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    // the stack after each prefix is a tree node: a push makes a new node, a
    // matching close returns to the parent, a wrong close starts a lone node,
    // and a piece is human exactly when it ends on the node it started on
    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        String dna = in.readLine().trim();
        int n = dna.length();
        int[] parent = new int[n + 1];
        char[] letter = new char[n + 1];
        int[] state = new int[n + 1];
        parent[0] = -1;
        int nodes = 1, cur = 0;
        for (int i = 0; i < n; i++) {
            char c = dna.charAt(i);
            if (Character.isUpperCase(c)) {
                parent[nodes] = cur;
                letter[nodes] = c;
                cur = nodes++;
            } else if (letter[cur] == Character.toUpperCase(c)) {
                cur = parent[cur];
            } else {
                parent[nodes] = -1;
                cur = nodes++;
            }
            state[i + 1] = cur;
        }
        int q = Integer.parseInt(in.readLine().trim());
        StringBuilder out = new StringBuilder();
        for (int k = 0; k < q; k++) {
            StringTokenizer st = new StringTokenizer(in.readLine());
            int left = Integer.parseInt(st.nextToken());
            int right = Integer.parseInt(st.nextToken());
            out.append(state[left - 1] == state[right] ? '1' : '0');
        }
        System.out.println(out);
    }
}
