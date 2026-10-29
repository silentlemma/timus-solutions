import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.Locale;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        List<Long> nums = new ArrayList<>();
        for (String line; (line = in.readLine()) != null;) {
            StringTokenizer tokens = new StringTokenizer(line);
            while (tokens.hasMoreTokens()) {
                nums.add(Long.parseLong(tokens.nextToken()));
            }
        }
        // Locale.US: in other locales the decimal separator may be a comma
        StringBuilder out = new StringBuilder();
        for (int i = nums.size() - 1; i >= 0; i--) {
            out.append(String.format(Locale.US, "%.4f\n", Math.sqrt(nums.get(i))));
        }
        System.out.print(out);
    }
}
