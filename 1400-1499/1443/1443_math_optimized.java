import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    private static final int TICKS_PER_METER = 10000;

    public static void main(String[] args) throws IOException {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        int lines = Integer.parseInt(input.readLine().trim());
        // The input is specified to four decimal places. Rounding recovers the exact ticks.
        long length = Math.round(Double.parseDouble(input.readLine().trim()) * TICKS_PER_METER);
        long rail = Math.round(Double.parseDouble(input.readLine().trim()) * TICKS_PER_METER);
        long whole = lines * (length / rail);
        long rest = length % rail;
        long perRail = rest == 0 ? 1 : rail / rest;
        System.out.println(whole + (rest == 0 ? 0 : 1 + (lines - 1) / perRail));
    }
}
