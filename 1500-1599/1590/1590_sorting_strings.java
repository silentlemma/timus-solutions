import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        String text = input.readLine().trim();
        String[] suffixes = new String[text.length()];
        for (int i = 0; i < text.length(); i++)
            suffixes[i] = text.substring(i);
        Arrays.sort(suffixes);
        long answer = (long)text.length() * (text.length() + 1) / 2;
        // The previous suffix has every prefix of the current suffix that
        // has already appeared earlier in lexicographic order.
        for (int i = 1; i < suffixes.length; i++) {
            String previous = suffixes[i - 1], current = suffixes[i];
            int common = 0;
            while (common < Math.min(previous.length(), current.length()) &&
                   previous.charAt(common) == current.charAt(common))
                common++;
            answer -= common;
        }
        System.out.println(answer);
    }
}
