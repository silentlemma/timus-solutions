import java.util.Scanner;

public class Main {
    private static final int HOSTS = 2; // Marshall and Lily
    private static final int UNLUCKY = 13;
    private static final int PRICE = 100;
    private static final String PLUS = "+one";

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int people = HOSTS;
        for (int i = 0; i < n; i++)
            people += in.next().endsWith(PLUS) ? 2 : 1;
        if (people == UNLUCKY)
            people++; // a dummy takes the extra seat
        System.out.println(people * PRICE);
    }
}
