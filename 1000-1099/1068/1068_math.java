import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        int n = new Scanner(System.in).nextInt();
        // the numbers between 1 and N form one interval whichever side N is on,
        // and its sum is the count times the average of the ends
        long count = Math.abs(n - 1) + 1;
        System.out.println((1 + n) * count / 2);
    }
}
