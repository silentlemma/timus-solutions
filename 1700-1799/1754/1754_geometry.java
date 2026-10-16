import java.math.BigInteger;
import java.util.Scanner;

public class Main {
    static final int CORNERS = 3, POINTS = 5;

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        long mana = in.nextLong(), h = in.nextLong(), top = in.nextLong();
        long[] x = new long[POINTS], y = new long[POINTS];
        for (int i = 0; i < POINTS; i++) {
            x[i] = in.nextLong();
            y[i] = in.nextLong();
        }
        // after flying up, mana - h is left for the radius, and the field must
        // reach the nearest of the floor and the three walls
        long spare = mana - h;
        boolean ok = spare >= h;
        for (int i = 1; i <= CORNERS && spare >= 0; i++) {
            int j = i % CORNERS + 1;
            long ux = x[j] - x[i], uy = y[j] - y[i];
            long wx = x[CORNERS + 1] - x[i], wy = y[CORNERS + 1] - y[i], wz = top;
            long nx = uy * wz, ny = -ux * wz, nz = ux * wy - uy * wx;
            BigInteger reach = BigInteger.valueOf(nx * (x[0] - x[i]) + ny * (y[0] - y[i]) + nz * h);
            // the distance to the wall is reach / |normal|, compared exactly
            BigInteger length = BigInteger.valueOf(nx * nx + ny * ny + nz * nz);
            BigInteger budget = BigInteger.valueOf(spare * spare).multiply(length);
            if (reach.multiply(reach).compareTo(budget) <= 0) ok = true;
        }
        System.out.println(ok && spare >= 0 ? "YES" : "NO");
    }
}
