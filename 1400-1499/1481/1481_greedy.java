import java.util.Arrays;
import java.util.Scanner;

public class Main {
    static char flip(char side) { return side == 'L' ? 'R' : 'L'; }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int[] weights = new int[n];
        for (int i = 0; i < n; i++)
            weights[i] = in.nextInt();
        Arrays.sort(weights);
        String record = in.next();
        // the weights in use always form a block of the sorted list whose
        // neighbours stand on opposite pans, so the pan of the largest one wins,
        // and a change adds a new largest weight, any other step a new smallest
        int changes = 0;
        for (int i = 1; i < n; i++)
            if (record.charAt(i) != record.charAt(i - 1))
                changes++;
        int low = n - 1 - changes, high = low;
        char lowSide = record.charAt(0), highSide = lowSide;
        StringBuilder out = new StringBuilder();
        out.append(weights[low]).append(' ').append(lowSide).append('\n');
        for (int i = 1; i < n; i++) {
            if (record.charAt(i) != record.charAt(i - 1)) {
                highSide = flip(highSide);
                out.append(weights[++high]).append(' ').append(highSide).append('\n');
            } else {
                lowSide = flip(lowSide);
                out.append(weights[--low]).append(' ').append(lowSide).append('\n');
            }
        }
        System.out.print(out);
    }
}
