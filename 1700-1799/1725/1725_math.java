import java.util.Scanner;

public class Main {
    // everyone on the far side of Vasya can be made to trip except the two
    // seats at the far end, who always come in from their own end
    static final int SAFE = 2;

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt(), k = in.nextInt();
        int far = Math.max(k - 1, n - k);
        System.out.println(Math.max(0, far - SAFE));
    }
}
