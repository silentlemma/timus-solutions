import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StreamTokenizer in = new StreamTokenizer(reader);
        in.nextToken();
        int n = (int)in.nval;
        int[] place = new int[n + 1]; // place[s]: finishing position of skier s
        for (int p = 1; p <= n; p++) {
            in.nextToken();
            place[(int)in.nval] = p;
        }
        int[] tree = new int[n + 1]; // finishing positions of the skiers who started before
        StringBuilder sb = new StringBuilder();
        for (int skier = 1; skier <= n; skier++) {
            int p = place[skier], earlier = 0; // started and finished before: undecided
            for (int i = p - 1; i > 0; i &= i - 1)
                earlier += tree[i];
            // started later yet finished before: surely faster
            int faster = p - 1 - earlier;
            // started before yet finished later: surely slower, the rest undecided
            sb.append(faster + 1).append(' ').append((n - skier) + earlier + 1).append('\n');
            for (int i = p; i <= n; i += i & -i)
                tree[i]++;
        }
        System.out.print(sb);
    }
}
