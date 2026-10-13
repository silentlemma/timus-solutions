import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int a = in.nextInt(), b = in.nextInt(), c = in.nextInt();
        // 2^(C-1) + 2^(C-1) = 2^C, and A and B both divide C - 1
        System.out.println(1L << ((c - 1) / a));
        System.out.println(1L << ((c - 1) / b));
        System.out.println(2);
    }
}
