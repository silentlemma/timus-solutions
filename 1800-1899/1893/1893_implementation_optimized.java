import java.io.IOException;

public class Main {
    private static final int PREMIUM_LAST = 2;
    private static final int BUSINESS_LAST = 20;

    public static void main(String[] args) throws IOException {
        // the seat is read byte by byte: the digits make the row, the next byte is
        // the letter
        int ch;
        do {
            ch = System.in.read();
        } while (ch <= ' ' && ch != -1);
        int row = 0;
        while (ch >= '0' && ch <= '9') {
            row = row * 10 + ch - '0';
            ch = System.in.read();
        }
        char letter = (char)ch;
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
