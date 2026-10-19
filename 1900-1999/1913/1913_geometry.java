import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigInteger;
import java.util.Locale;
import java.util.StringTokenizer;

public class Main {
    private static final int TERMINALS = 3;
    private static final long DISCRIMINANT_SCALE = 4;

    private static long squaredDistance(long[] first, long[] second) {
        long dx = first[0] - second[0];
        long dy = first[1] - second[1];
        return dx * dx + dy * dy;
    }

    private static boolean radicalAtMost(long target, long coefficient, long radicand) {
        if (coefficient == 0 || radicand == 0) {
            return target >= 0;
        }
        BigInteger left = BigInteger.valueOf(target).pow(2);
        BigInteger right = BigInteger.valueOf(coefficient).pow(2)
            .multiply(BigInteger.valueOf(radicand));
        int comparison = left.compareTo(right);
        if (coefficient > 0) {
            return target >= 0 && comparison >= 0;
        }
        return target >= 0 || comparison <= 0;
    }

    private static double[] commonPoint(long[][] points, long[] radii) {
        for (long[] point : points) {
            boolean inside = true;
            for (int index = 0; index < TERMINALS; index++) {
                inside &= squaredDistance(point, points[index]) <= radii[index] * radii[index];
            }
            if (inside) {
                return new double[] {point[0], point[1]};
            }
        }
        for (int first = 0; first < TERMINALS; first++) {
            for (int second = first + 1; second < TERMINALS; second++) {
                int third = TERMINALS - first - second;
                long[] origin = points[first];
                long dx = points[second][0] - origin[0];
                long dy = points[second][1] - origin[1];
                long distance = dx * dx + dy * dy;
                long radiusSquared = radii[first] * radii[first];
                long along = distance + radiusSquared - radii[second] * radii[second];
                long discriminant = DISCRIMINANT_SCALE * radiusSquared * distance - along * along;
                if (discriminant < 0) {
                    continue;
                }
                long wx = origin[0] - points[third][0];
                long wy = origin[1] - points[third][1];
                long target = distance * (radii[third] * radii[third] - radiusSquared
                    - wx * wx - wy * wy) - along * (wx * dx + wy * dy);
                long cross = wy * dx - wx * dy;
                for (int sign : new int[] {-1, 1}) {
                    if (radicalAtMost(target, sign * cross, discriminant)) {
                        double height = sign * Math.sqrt((double) discriminant);
                        return new double[] {
                            origin[0] + ((double) along * dx - height * dy) / (2 * distance),
                            origin[1] + ((double) along * dy + height * dx) / (2 * distance)
                        };
                    }
                }
            }
        }
        return null;
    }

    static double[][] solve(long radius, long[][] points) {
        long reachSquared = (2 * radius) * (2 * radius);
        if (squaredDistance(points[0], points[1]) <= reachSquared
            && squaredDistance(points[0], points[2]) <= reachSquared) {
            double[][] answer = new double[2][2];
            for (int index = 0; index < 2; index++) {
                for (int axis = 0; axis < 2; axis++) {
                    answer[index][axis] = (points[0][axis] + points[index + 1][axis]) / 2.0;
                }
            }
            return answer;
        }
        for (int doubled = 0; doubled < TERMINALS; doubled++) {
            long[] radii = {radius, radius, radius};
            radii[doubled] *= 2;
            double[] hub = commonPoint(points, radii);
            if (hub != null) {
                return new double[][] {hub, {
                    (hub[0] + points[doubled][0]) / 2,
                    (hub[1] + points[doubled][1]) / 2
                }};
            }
        }
        return null;
    }

    private static final class Input {
        final BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer tokens = new StringTokenizer("");

        long next() throws IOException {
            while (!tokens.hasMoreTokens()) {
                tokens = new StringTokenizer(reader.readLine());
            }
            return Long.parseLong(tokens.nextToken());
        }
    }

    public static void main(String[] args) throws IOException {
        Input input = new Input();
        long radius = input.next();
        long[][] points = new long[TERMINALS][2];
        for (long[] point : points) {
            point[0] = input.next();
            point[1] = input.next();
        }
        double[][] answer = solve(radius, points);
        if (answer == null) {
            System.out.println("Death");
        } else {
            System.out.println("Now we have enough power");
            for (double[] point : answer) {
                System.out.printf(Locale.US, "%.12f %.12f%n", point[0], point[1]);
            }
        }
    }
}
