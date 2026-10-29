import java.util.Scanner;

public class Main {
    static final int LETTERS = 26;

    // every occurrence of a spell starts with an occurrence of its first
    // letter, so a most frequent single letter is a strongest spell
    public static void main(String[] args) {
        String s = new Scanner(System.in).next();
        int[] count = new int[LETTERS];
        int best = 0;
        for (char c : s.toCharArray()) {
            count[c - 'a']++;
            if (count[c - 'a'] > count[best]) {
                best = c - 'a';
            }
        }
        System.out.println((char)('a' + best));
    }
}
