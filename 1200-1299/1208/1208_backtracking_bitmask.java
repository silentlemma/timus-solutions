import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static final int TEAM_SIZE = 3;
    static int[] clash;
    static int answer;

    static void search(int mask, int selected) {
        if (selected + Integer.bitCount(mask) <= answer)
            return;
        int chosen = 0, degree = 0;
        for (int remaining = mask; remaining != 0; remaining &= remaining - 1) {
            int i = Integer.numberOfTrailingZeros(remaining);
            int count = Integer.bitCount(mask & clash[i]);
            if (count > degree) {
                chosen = i;
                degree = count;
            }
        }
        // Take an edgeless remainder whole; otherwise try the team with
        // most conflicts first to tighten the bound for its skip branch.
        if (degree <= 1) {
            answer = Math.max(answer, selected + Integer.bitCount(mask));
            return;
        }
        search(mask & ~clash[chosen], selected + 1);
        search(mask & ~(1 << chosen), selected);
    }

    public static void main(String[] args) throws Exception {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        int k = Integer.parseInt(input.readLine().trim());
        String[][] teams = new String[k][TEAM_SIZE];
        for (int i = 0; i < k; i++) {
            StringTokenizer tokens = new StringTokenizer(input.readLine());
            for (int j = 0; j < TEAM_SIZE; j++)
                teams[i][j] = tokens.nextToken();
        }
        clash = new int[k];
        for (int i = 0; i < k; i++)
            for (int j = 0; j < k; j++)
                for (String first : teams[i])
                    for (String second : teams[j])
                        if (first.equals(second))
                            clash[i] |= 1 << j;
        search((1 << k) - 1, 0);
        System.out.println(answer);
    }
}
