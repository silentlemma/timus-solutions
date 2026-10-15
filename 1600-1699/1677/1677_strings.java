import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigInteger;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder text = new StringBuilder();
        for (String line = in.readLine(); line != null; line = in.readLine()) {
            text.append(line).append(' ');
        }
        StringTokenizer words = new StringTokenizer(text.toString());
        long n = Long.parseLong(words.nextToken());
        String word = words.nextToken();
        int size = word.length();
        // prefix function: pi[i] is the longest border of word[0..i]
        int[] pi = new int[size];
        for (int i = 1; i < size; i++) {
            int j = pi[i - 1];
            while (j > 0 && word.charAt(i) != word.charAt(j)) {
                j = pi[j - 1];
            }
            if (word.charAt(i) == word.charAt(j)) {
                j++;
            }
            pi[i] = j;
        }
        // the expected time is the sum of n^k over the lengths k of the word's
        // borders, the whole word included: the base-n powers are added up,
        // each one from the previous one
        boolean[] border = new boolean[size + 1];
        for (int k = size; k > 0; k = pi[k - 1]) {
            border[k] = true;
        }
        BigInteger base = BigInteger.valueOf(n);
        BigInteger power = BigInteger.ONE;
        BigInteger total = BigInteger.ZERO;
        for (int k = 1; k <= size; k++) {
            power = power.multiply(base);
            if (border[k]) {
                total = total.add(power);
            }
        }
        System.out.println(total);
    }
}
