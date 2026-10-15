import java.util.Scanner;

public class Main {
    static final long SCALE = 1000;
    static final long HALF_TURN = 180 * SCALE;
    static final long FULL_TURN = 2 * HALF_TURN;
    static final int DIGITS = 3;

    // the angle in thousandths of a degree, read exactly from the text
    static long thousandths(String text) {
        int dot = text.indexOf('.');
        String whole = dot < 0 ? text : text.substring(0, dot);
        String part = dot < 0 ? "" : text.substring(dot + 1);
        part = (part + "000").substring(0, DIGITS);
        return (whole.isEmpty() ? 0 : Long.parseLong(whole)) * SCALE + Long.parseLong(part);
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        double r = Double.parseDouble(in.next());
        long a = thousandths(in.next());
        // each shore point shows an arc of 2a, so the walk along the shore
        // covers 360 - 2a degrees; chords grow slower than their angles, so
        // it is shortest as full 2a chords and one short chord for the rest
        long steps = HALF_TURN / a;
        long rest = FULL_TURN - steps * 2 * a;
        double full = 2 * r * Math.sin(2 * a * Math.PI / FULL_TURN);
        double last = 2 * r * Math.sin(rest * Math.PI / FULL_TURN);
        System.out.printf("%.7f%n", r + (steps - 1) * full + last);
    }
}
