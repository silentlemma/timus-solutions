import java.util.Scanner;

public class Main {
    private static final int PREMIUM_LAST = 2;
    private static final int BUSINESS_LAST = 20;

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        String seat = input.next();
        int row = Integer.parseInt(seat.substring(0, seat.length() - 1));
        char letter = seat.charAt(seat.length() - 1);
        char rightWindow;
        String aisles;
        if (row <= PREMIUM_LAST) {
            rightWindow = 'D';
            aisles = "BC";
        } else if (row <= BUSINESS_LAST) {
            rightWindow = 'F';
            aisles = "BCDE";
        } else {
            rightWindow = 'K';
            aisles = "CDGH";
        }
        if (letter == 'A' || letter == rightWindow)
            System.out.println("window");
        else if (aisles.indexOf(letter) >= 0)
            System.out.println("aisle");
        else
            System.out.println("neither");
    }
}
