import java.math.BigInteger;
import java.util.Scanner;

public class Main {
    // all comparisons are exact: the center is (ux / d, uy / d) and the radius
    // times d is the square root of rho2; the products need more than 64 bits
    static BigInteger d, rho2;

    static BigInteger num(long v) { return BigInteger.valueOf(v); }

    // the sign of alpha - gamma * sqrt(rho2)
    static int signMinus(BigInteger alpha, BigInteger gamma) {
        if (gamma.signum() == 0) {
            return alpha.signum();
        }
        int squared = alpha.multiply(alpha).compareTo(gamma.multiply(gamma).multiply(rho2));
        if (gamma.signum() > 0) {
            return alpha.signum() <= 0 ? -1 : Integer.signum(squared);
        }
        return alpha.signum() >= 0 ? 1 : -Integer.signum(squared);
    }

    static boolean atLeastRho(BigInteger t) {
        return t.signum() >= 0 && t.multiply(t).compareTo(rho2) >= 0;
    }

    // the smallest integer k with k >= (u + sqrt(rho2)) / d
    static long ceilPlus(BigInteger u) {
        double estimate = (u.doubleValue() + Math.sqrt(rho2.doubleValue())) / d.doubleValue();
        long k = (long)Math.floor(estimate) - 2;
        while (!atLeastRho(num(k).multiply(d).subtract(u))) {
            k++;
        }
        return k;
    }

    // the largest integer k with k <= (u - sqrt(rho2)) / d
    static long floorMinus(BigInteger u) {
        double estimate = (u.doubleValue() - Math.sqrt(rho2.doubleValue())) / d.doubleValue();
        long k = (long)Math.ceil(estimate) + 2;
        while (!atLeastRho(u.subtract(num(k).multiply(d)))) {
            k--;
        }
        return k;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        long ax = in.nextLong(), ay = in.nextLong();
        long bx = in.nextLong(), by = in.nextLong();
        long cx = in.nextLong(), cy = in.nextLong();
        long a2 = ax * ax + ay * ay, b2 = bx * bx + by * by, c2 = cx * cx + cy * cy;
        long dv = 2 * (ax * (by - cy) + bx * (cy - ay) + cx * (ay - by));
        BigInteger ux = num(a2 * (by - cy) + b2 * (cy - ay) + c2 * (ay - by));
        BigInteger uy = num(a2 * (cx - bx) + b2 * (ax - cx) + c2 * (bx - ax));
        if (dv < 0) {
            dv = -dv;
            ux = ux.negate();
            uy = uy.negate();
        }
        d = num(dv);
        BigInteger dx = num(ax).multiply(d).subtract(ux);
        BigInteger dy = num(ay).multiply(d).subtract(uy);
        rho2 = dx.multiply(dx).add(dy.multiply(dy));
        // an extreme point of the circle is on the arc when it lies on the same side
        // of the chord AB as C; side(P) * d = alpha - gamma * sqrt(rho2)
        long ex = bx - ax, ey = by - ay;
        int sideC = Long.signum(ex * (cy - ay) - ey * (cx - ax));
        BigInteger alpha = num(ex)
                               .multiply(uy.subtract(num(ay).multiply(d)))
                               .subtract(num(ey).multiply(ux.subtract(num(ax).multiply(d))));
        long loX = Math.min(ax, bx), hiX = Math.max(ax, bx);
        long loY = Math.min(ay, by), hiY = Math.max(ay, by);
        if (signMinus(alpha, num(ey)) == sideC) {
            hiX = Math.max(hiX, ceilPlus(ux));
        }
        if (signMinus(alpha, num(-ey)) == sideC) {
            loX = Math.min(loX, floorMinus(ux));
        }
        if (signMinus(alpha, num(-ex)) == sideC) {
            hiY = Math.max(hiY, ceilPlus(uy));
        }
        if (signMinus(alpha, num(ex)) == sideC) {
            loY = Math.min(loY, floorMinus(uy));
        }
        System.out.println((hiX - loX) * (hiY - loY));
    }
}
