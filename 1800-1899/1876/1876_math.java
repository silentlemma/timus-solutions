import java.util.Scanner;

public class Main {
    static final int LEGS = 40;

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int a = in.nextInt();
        int b = in.nextInt();
        // either every right slipper turns up while the left legs are dressed,
        // or 39 rights do, and then every spare left slipper is thrown away
        // before the last right leg is dressed
        System.out.println(Math.max(2 * b + LEGS, 2 * a + LEGS - 1));
    }
}
