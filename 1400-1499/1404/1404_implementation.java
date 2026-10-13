import java.util.Scanner;

public class Main {
    static final int SHIFT = 5; // added to the first letter
    static final int LETTERS = 26;

    public static void main(String[] args) {
        String word = new Scanner(System.in).next();
        // each code is the previous code plus the letter, modulo 26: take differences
        StringBuilder plain = new StringBuilder();
        int prev = SHIFT;
        for (char ch : word.toCharArray()) {
            int code = ch - 'a';
            plain.append((char)('a' + Math.floorMod(code - prev, LETTERS)));
            prev = code;
        }
        System.out.println(plain);
    }
}
