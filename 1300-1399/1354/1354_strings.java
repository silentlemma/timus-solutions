import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        String word = new BufferedReader(new InputStreamReader(System.in)).readLine().trim();
        // the added part is never empty, so look for the longest palindromic
        // suffix of the word without its first letter
        String tail = word.substring(1);
        String text = new StringBuilder(tail).reverse() + "#" + tail;
        int[] border = new int[text.length()];
        for (int i = 1; i < text.length(); i++) {
            int k = border[i - 1];
            while (k > 0 && text.charAt(i) != text.charAt(k))
                k = border[k - 1];
            if (text.charAt(i) == text.charAt(k))
                k++;
            border[i] = k;
        }
        int longest = tail.isEmpty() ? 0 : border[text.length() - 1];
        String head = word.substring(0, word.length() - longest);
        System.out.println(word + new StringBuilder(head).reverse());
    }
}
