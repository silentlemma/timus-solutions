import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(in.readLine().trim());
        String prev = null;
        // runs ending at each cell of the previous and current row, going
        // down, down-right and down-left
        int[] down = new int[n], right = new int[n], left = new int[n];
        int[] down2 = new int[n], right2 = new int[n], left2 = new int[n];
        int[] best = new int[2]; // longest runs of s and of S
        for (int i = 0; i < n; i++) {
            String row = in.readLine().trim();
            int across = 0;
            for (int j = 0; j < n; j++) {
                char c = row.charAt(j);
                across = j > 0 && row.charAt(j - 1) == c ? across + 1 : 1;
                down2[j] = i > 0 && prev.charAt(j) == c ? down[j] + 1 : 1;
                right2[j] = i > 0 && j > 0 && prev.charAt(j - 1) == c ? right[j - 1] + 1 : 1;
                left2[j] = i > 0 && j + 1 < n && prev.charAt(j + 1) == c ? left[j + 1] + 1 : 1;
                int k = c == 'S' ? 1 : 0;
                best[k] = Math.max(Math.max(best[k], across),
                                   Math.max(down2[j], Math.max(right2[j], left2[j])));
            }
            int[] t = down;
            down = down2;
            down2 = t;
            t = right;
            right = right2;
            right2 = t;
            t = left;
            left = left2;
            left2 = t;
            prev = row;
        }
        System.out.println(best[0] > best[1] ? "s" : best[1] > best[0] ? "S" : "?");
        System.out.println(Math.max(best[0], best[1]));
    }
}
