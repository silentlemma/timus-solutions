import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        if (!in.hasNextInt())
            return;
        int a = in.nextInt(), b = in.nextInt(), c = in.nextInt(), d = in.nextInt();
        int petya = a, driver = c;
        // the driver never asks less than Petya offers, and the other way round
        if (petya >= driver) {
            System.out.println(petya);
            return;
        }
        while (true) {
            petya += b;
            if (petya >= driver) {
                System.out.println(driver);
                return;
            }
            driver -= d;
            if (driver <= petya) {
                System.out.println(petya);
                return;
            }
        }
    }
}
