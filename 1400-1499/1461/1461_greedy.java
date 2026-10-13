import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static final String BOOK = "dhu"; // letters in the order of the book

    static int step(char c) { return c == 'u' ? 1 : c == 'd' ? -1 : 0; }

    // can a garland at this height end at the ground in exactly `left` links?
    // on the ground a link must go up, above it horizontal links can pad
    static boolean finishes(int height, int left) {
        return height == 0 ? left == 0 || left >= 2 : left >= height;
    }

    // never below the ground, and no horizontal link on it
    static boolean allowed(char c, int height) {
        return height + step(c) >= 0 && !(c == 'h' && height == 0);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(in.readLine().trim());
        String s = in.readLine().trim();
        int[] heights = new int[n + 1];
        for (int i = 0; i < n; i++)
            heights[i + 1] = heights[i] + step(s.charAt(i));
        // the last link that can take a larger letter and still be finished
        for (int i = n - 1; i >= 0; i--)
            for (char c : BOOK.toCharArray())
                if (c > s.charAt(i) && allowed(c, heights[i]) &&
                    finishes(heights[i] + step(c), n - i - 1)) {
                    StringBuilder out = new StringBuilder(s.substring(0, i)).append(c);
                    int height = heights[i] + step(c);
                    // the rest is the smallest garland that still finishes
                    for (int left = n - i - 1; left > 0; left--)
                        for (char d : BOOK.toCharArray())
                            if (allowed(d, height) && finishes(height + step(d), left - 1)) {
                                out.append(d);
                                height += step(d);
                                break;
                            }
                    System.out.println(out);
                    return;
                }
        System.out.println("No solution");
    }
}
