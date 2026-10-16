import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int k = in.nextInt(), n = in.nextInt();
        int jam = 0;
        for (int i = 0; i < n; i++) {
            // the light lets k cars through, but never more than are waiting
            jam = Math.max(0, jam + in.nextInt() - k);
        }
        System.out.println(jam);
    }
}
