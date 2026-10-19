import java.util.Scanner;

public class Main {
    // page i open is bit i - 1 of a Gray code word: F1 flips bit 0, the other
    // move flips the bit above the lowest set one; these are the reflected Gray
    // code steps, so the states form one path ordered by the decoded word
    static long rank(String pages) {
        long gray = 0, place = 0;
        for (int i = pages.length() - 1; i >= 0; i--) {
            gray = gray * 2 + (pages.charAt(i) - '0');
        }
        for (; gray != 0; gray >>= 1) {
            place ^= gray;
        }
        return place;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        in.nextInt();
        String start = in.next(), goal = in.next();
        System.out.println(Math.abs(rank(start) - rank(goal)));
    }
}
