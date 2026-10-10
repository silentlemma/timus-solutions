import java.util.Scanner;

public class Main {
    static final int LETTERS = 26;

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt(), m = in.nextInt(), p = in.nextInt();
        // the words take their letters out of the grid one cell each, so what
        // is left does not depend on where they lie
        int[] left = new int[LETTERS];
        for (int i = 0; i < n; i++) {
            for (char c : in.next().toCharArray()) {
                left[c - 'A']++;
            }
        }
        for (int i = 0; i < p; i++) {
            for (char c : in.next().toCharArray()) {
                left[c - 'A']--;
            }
        }
        StringBuilder answer = new StringBuilder();
        for (int c = 0; c < LETTERS; c++) {
            for (int k = 0; k < left[c]; k++) {
                answer.append((char)('A' + c));
            }
        }
        System.out.println(answer);
    }
}
