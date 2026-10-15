import java.util.Scanner;

public class Main {
    static final String HEAD = "aabab";
    static final String BLOCK = "bbaaba"; // each block forces two more palindromes

    // short lengths where the pattern is not yet the best, found by search
    static final int[] SPECIAL_LENGTHS = {2, 8, 11};
    static final String[] SPECIAL_WORDS = {"ab", "aababbaa", "aababbaabab"};

    public static void main(String[] args) {
        int n = new Scanner(System.in).nextInt();
        // the end after the blocks for each remainder of n mod 6
        String[] tails = {"b", "bb", "bbaaababb", "bbaa", "bbaab", ""};
        String special = null;
        for (int i = 0; i < SPECIAL_LENGTHS.length; i++) {
            if (SPECIAL_LENGTHS[i] == n) {
                special = SPECIAL_WORDS[i];
            }
        }
        StringBuilder word = new StringBuilder();
        if (special != null) {
            word.append(special);
        } else if (n <= HEAD.length()) {
            word.append(HEAD, 0, n);
        } else {
            String tail = tails[n % BLOCK.length()];
            word.append(HEAD);
            for (int k = (n - HEAD.length() - tail.length()) / BLOCK.length(); k > 0; k--) {
                word.append(BLOCK);
            }
            word.append(tail);
        }
        System.out.println(word);
    }
}
