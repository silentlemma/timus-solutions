import java.util.Locale;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        double a = in.nextInt();
        double b = in.nextInt();
        // the right triangle on the birch and the ground holds at most a quarter
        // of the squared diagonal; with the triangle of the sticks added, the
        // total is largest when the sticks meet at 135 degrees
        double x = a / 2;
        double y = b / 2;
        double area = x * x + y * y + 2 * Math.sqrt(2) * x * y;
        System.out.println(String.format(Locale.US, "%.9f", area));
    }
}
