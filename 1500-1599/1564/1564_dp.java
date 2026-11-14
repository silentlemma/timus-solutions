import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    private static final int DECIMAL = 10;
    private static final int PLACES = 18;

    private static String floorFor(long target) {
        long floor = 0;
        long prefixOnes = 0;
        long width = 1;
        for (int i = 1; i < PLACES; i++) {
            width *= DECIMAL;
        }
        for (int remaining = PLACES - 1; remaining >= 0; remaining--, width /= DECIMAL) {
            // Every free position has a one in exactly one tenth of the completions.
            long fixedCost = prefixOnes * width + remaining * (width / DECIMAL);
            for (int digit = 0; digit < DECIMAL; digit++) {
                long block = fixedCost + (digit == 1 ? width : 0);
                if (target <= block) {
                    floor = DECIMAL * floor + digit;
                    if (digit == 1) {
                        prefixOnes++;
                    }
                    break;
                }
                target -= block;
            }
        }
        return target == prefixOnes ? Long.toString(floor) : "Petr lies";
    }

    public static void main(String[] args) throws IOException {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        System.out.println(floorFor(Long.parseLong(input.readLine().trim())));
    }
}
