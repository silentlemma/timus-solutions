import java.io.InputStreamReader;
import java.io.StreamTokenizer;

public class Main {
    static final int MIN_DIVISOR = 3, SMALLEST_EVEN_DIVISOR = 4, FIRST_ODD_CANDIDATE = 5;
    public static void main(String[] args) throws Exception {
        StreamTokenizer input = new StreamTokenizer(new InputStreamReader(System.in));
        input.nextToken();
        int buttons = (int)input.nval;
        if (buttons % MIN_DIVISOR == 0) {
            System.out.println(MIN_DIVISOR - 1);
            return;
        }
        if (buttons % SMALLEST_EVEN_DIVISOR == 0) {
            System.out.println(SMALLEST_EVEN_DIVISOR - 1);
            return;
        }
        // Any composite divisor not divisible by4 has an odd prime factor.
        for (int divisor = FIRST_ODD_CANDIDATE; divisor * divisor <= buttons; divisor += 2)
            if (buttons % divisor == 0) {
                System.out.println(divisor - 1);
                return;
            }
        int divisor = buttons % 2 == 0 ? buttons / 2 : buttons;
        System.out.println(divisor - 1);
    }
}
