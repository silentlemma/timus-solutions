import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        int n = new Scanner(System.in).nextInt();
        // a row ends in white or red; it comes from a row one shorter ending in
        // the other of the two, or from one two shorter followed by blue
        long prev = 2, cur = 2;
        for (int i = 2; i < n; i++) {
            long next = prev + cur;
            prev = cur;
            cur = next;
        }
        System.out.println(cur);
    }
}
