import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        long ar = in.nextLong(), ai = in.nextLong(), br = in.nextLong(), bi = in.nextLong();
        long norm = br * br + bi * bi;
        if (norm == 0) {
            System.out.println(0); // no remainder is shorter than zero
            return;
        }
        // a / b = (x + y i) / norm; every quotient q lies within 1 of it
        long x = ar * br + ai * bi, y = ai * br - ar * bi;
        long fx = Math.floorDiv(x, norm), fy = Math.floorDiv(y, norm);
        int count = 0;
        for (long qr = fx - 1; qr <= fx + 1; qr++)
            for (long qi = fy - 1; qi <= fy + 1; qi++) {
                long rr = ar - (br * qr - bi * qi), ri = ai - (br * qi + bi * qr);
                if (rr * rr + ri * ri < norm)
                    count++;
            }
        System.out.println(count);
    }
}
