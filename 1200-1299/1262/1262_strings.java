import java.io.*;

public class Main {
    // Roman digits needed for each decimal digit: -, I, II, III, IV, V, VI,
    // VII, VIII, IX
    static final int[] LENGTHS = {0, 1, 2, 3, 2, 1, 2, 3, 4, 2};

    public static void main(String[] args) throws IOException {
        String s = new BufferedReader(new InputStreamReader(System.in)).readLine().trim();
        int total = 0;
        for (char c : s.toCharArray())
            total += LENGTHS[c - '0'];
        System.out.println(total);
    }
}
