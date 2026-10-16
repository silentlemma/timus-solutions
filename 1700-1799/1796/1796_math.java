import java.util.Scanner;

public class Main {
    static final int[] NOTES = {10, 50, 100, 500, 1000, 5000};

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        long total = 0, smallest = 0;
        for (int note : NOTES) {
            long count = in.nextLong();
            total += count * note;
            if (count > 0 && smallest == 0) smallest = note;
        }
        long price = in.nextLong();
        // k tickets fit when k * price <= total, and taking away the smallest
        // note must leave too little: total - smallest < k * price
        long low = (total - smallest) / price + 1, high = total / price;
        StringBuilder out = new StringBuilder();
        out.append(high - low + 1).append('\n');
        for (long k = low; k <= high; k++) {
            if (k > low) out.append(' ');
            out.append(k);
        }
        System.out.println(out);
    }
}
