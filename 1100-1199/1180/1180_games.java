import java.util.Scanner;

public class Main {
    static final int SPLIT = 3;

    public static void main(String[] args) {
        String digits = new Scanner(System.in).next();
        // no power of two is divisible by 3, so from a multiple of 3 every
        // move leaves a non-multiple, and from a non-multiple taking 1 or 2
        // stones leaves a multiple; the remainder is also the smallest move
        int rest = 0;
        for (char c : digits.toCharArray()) {
            rest = (rest + c - '0') % SPLIT;
        }
        System.out.println(rest == 0 ? "2" : "1\n" + rest);
    }
}
