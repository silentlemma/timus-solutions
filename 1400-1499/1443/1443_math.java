import java.util.Scanner;

public class Main {
    static final int DIGITS = 4; // lengths are given to a tenth of a millimetre

    // a length in tenths of a millimetre, read exactly
    static long tenths(String text) {
        int dot = text.indexOf('.');
        String whole = dot < 0 ? text : text.substring(0, dot);
        String frac = dot < 0 ? "" : text.substring(dot + 1);
        StringBuilder padded = new StringBuilder(frac);
        while (padded.length() < DIGITS)
            padded.append('0');
        long scale = 1;
        for (int i = 0; i < DIGITS; i++)
            scale *= 10;
        return Long.parseLong("0" + whole) * scale + Long.parseLong(padded.substring(0, DIGITS));
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        long n = in.nextLong();
        long s = tenths(in.next()), rail = tenths(in.next());
        long full = s / rail, rest = s % rail;
        if (rest == 0) {
            System.out.println(n * full);
            return;
        }
        // each line takes its full rails and a short piece; a rail holds rail / rest such pieces
        long perRail = rail / rest;
        System.out.println(n * full + (n + perRail - 1) / perRail);
    }
}
