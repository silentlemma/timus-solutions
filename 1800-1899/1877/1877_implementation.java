import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int first = Integer.parseInt(in.next());
        int second = Integer.parseInt(in.next());
        // on night k the thief tries code k on lock 1 when k is even and on
        // lock 2 when k is odd
        System.out.println(first % 2 == 0 || second % 2 == 1 ? "yes" : "no");
    }
}
