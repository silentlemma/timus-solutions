import java.math.BigInteger;
import java.util.Scanner;

public class Main {
    private static final class Vector {
        final BigInteger x;
        final BigInteger y;
        final BigInteger z;

        Vector(BigInteger x, BigInteger y, BigInteger z) {
            this.x = x;
            this.y = y;
            this.z = z;
        }
    }

    private static BigInteger dot(Vector a, Vector b) {
        return a.x.multiply(b.x).add(a.y.multiply(b.y)).add(a.z.multiply(b.z));
    }

    private static Vector subtract(Vector a, Vector b) {
        return new Vector(a.x.subtract(b.x), a.y.subtract(b.y), a.z.subtract(b.z));
    }

    private static Vector scale(Vector a, BigInteger factor) {
        return new Vector(a.x.multiply(factor), a.y.multiply(factor), a.z.multiply(factor));
    }

    private static Vector cross(Vector a, Vector b) {
        return new Vector(a.y.multiply(b.z).subtract(a.z.multiply(b.y)),
                a.z.multiply(b.x).subtract(a.x.multiply(b.z)),
                a.x.multiply(b.y).subtract(a.y.multiply(b.x)));
    }

    private static int projectionSign(Vector point, Vector edge, Vector velocity,
            BigInteger a, BigInteger b, BigInteger planeDiscriminant, BigInteger radiusSquared) {
        BigInteger x = dot(edge, point);
        BigInteger y = dot(edge, velocity);
        if (y.signum() == 0) {
            return x.signum();
        }
        BigInteger numerator = y.signum() > 0 ? x.negate() : x;
        BigInteger denominator = y.abs();
        BigInteger vertexOffset = a.multiply(numerator).add(b.multiply(denominator));
        int comparison;
        if (vertexOffset.signum() >= 0) {
            comparison = vertexOffset.signum() == 0 && planeDiscriminant.signum() == 0 ? 0 : -1;
        } else {
            Vector scaled = subtract(scale(point, y), scale(velocity, x));
            comparison = dot(scaled, scaled)
                    .subtract(radiusSquared.multiply(y).multiply(y)).signum();
        }
        return comparison * y.signum();
    }

    private static boolean rayHits(Vector point, Vector velocity, BigInteger radiusSquared) {
        BigInteger projection = dot(point, velocity);
        return projection.signum() < 0 && projection.multiply(projection).compareTo(
                dot(velocity, velocity).multiply(dot(point, point).subtract(radiusSquared))) >= 0;
    }

    private static String classify(Vector center, BigInteger radius, Vector first,
            Vector second, Vector velocity) {
        Vector left = subtract(first, center);
        Vector right = subtract(second, center);
        Vector edge = subtract(right, left);
        Vector normal = cross(edge, velocity);
        Vector offset = cross(edge, left);
        BigInteger radiusSquared = radius.multiply(radius);
        BigInteger a = dot(normal, normal);
        BigInteger b = dot(offset, normal);
        BigInteger c = dot(offset, offset).subtract(radiusSquared.multiply(dot(edge, edge)));
        if (a.signum() != 0 && c.signum() > 0 && b.signum() < 0) {
            BigInteger height = dot(left, normal);
            BigInteger planeDiscriminant = radiusSquared.multiply(a)
                    .subtract(height.multiply(height));
            if (planeDiscriminant.signum() >= 0) {
                int leftSign = projectionSign(left, edge, velocity, a, b,
                        planeDiscriminant, radiusSquared);
                int rightSign = projectionSign(right, edge, velocity, a, b,
                        planeDiscriminant, radiusSquared);
                if (leftSign < 0 && rightSign > 0) {
                    return "Warning";
                }
            }
        }
        if (rayHits(left, velocity, radiusSquared) || rayHits(right, velocity, radiusSquared)) {
            return "Crash";
        }
        return "False alarm";
    }

    private static Vector readVector(Scanner in) {
        return new Vector(in.nextBigInteger(), in.nextBigInteger(), in.nextBigInteger());
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        Vector center = readVector(in);
        BigInteger radius = in.nextBigInteger();
        Vector first = readVector(in);
        Vector second = readVector(in);
        Vector velocity = readVector(in);
        System.out.println(classify(center, radius, first, second, velocity));
    }
}
