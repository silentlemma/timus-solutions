import java.io.BufferedInputStream;
import java.io.IOException;
import java.util.ArrayList;

public strictfp class Main {
    private static final double MAX_DISTANCE = 3.0e9;
    private static final double CLOSE_DISTANCE = 1.0e-5;
    private static final double SPLITTER = 134217729.0;
    private static final double PI_HIGH = 3.141592653589793;
    private static final double PI_LOW = 1.2246467991473532e-16;

    private static final class DoubleDouble {
        final double high;
        final double low;

        DoubleDouble(double high, double low) {
            this.high = high;
            this.low = low;
        }

        static DoubleDouble integer(long value) {
            double high = (double) value;
            return new DoubleDouble(high, (double) (value - (long) high));
        }

        DoubleDouble add(DoubleDouble other) {
            double sum = high + other.high;
            double part = sum - high;
            double error = (high - (sum - part)) + (other.high - part) + low + other.low;
            double result = sum + error;
            return new DoubleDouble(result, error - (result - sum));
        }

        DoubleDouble subtract(DoubleDouble other) {
            return add(new DoubleDouble(-other.high, -other.low));
        }

        DoubleDouble multiply(DoubleDouble other) {
            double product = high * other.high;
            double splitA = SPLITTER * high;
            double highA = splitA - (splitA - high);
            double lowA = high - highA;
            double splitB = SPLITTER * other.high;
            double highB = splitB - (splitB - other.high);
            double lowB = other.high - highB;
            double error = ((highA * highB - product) + highA * lowB) + lowA * highB;
            error += lowA * lowB + high * other.low + low * other.high;
            double result = product + error;
            return new DoubleDouble(result, error - (result - product));
        }

        boolean nonnegative() {
            return high > 0 || (high == 0 && low >= 0);
        }
    }

    private static final class Point {
        final long x;
        final long y;

        Point(long x, long y) {
            this.x = x;
            this.y = y;
        }
    }

    private static final class Distance {
        final double value;
        final long base;
        final long denominator;
        final boolean square;

        Distance(double value, long base, long denominator, boolean square) {
            this.value = value;
            this.base = base;
            this.denominator = denominator;
            this.square = square;
        }
    }

    private static long cross(long ax, long ay, long bx, long by) {
        return ax * by - ay * bx;
    }

    private static final class Polygon {
        final Point[] vertices;
        final long[] dx;
        final long[] dy;
        final long[] lengthSquared;
        final long[] rx;
        final long[] ry;
        final ArrayList<Double> radii = new ArrayList<>();
        final ArrayList<DoubleDouble> extras = new ArrayList<>();
        final int size;
        final double perimeter;

        Polygon(Point[] input) {
            ArrayList<Point> filtered = new ArrayList<>();
            int count = input.length;
            for (int i = 0; i < count; ++i) {
                Point previous = input[(i + count - 1) % count];
                Point current = input[i];
                Point next = input[(i + 1) % count];
                if (cross(current.x - previous.x, current.y - previous.y,
                        next.x - current.x, next.y - current.y) != 0) {
                    filtered.add(current);
                }
            }
            size = filtered.size();
            vertices = filtered.toArray(new Point[size]);
            dx = new long[size];
            dy = new long[size];
            lengthSquared = new long[size];
            rx = new long[size];
            ry = new long[size];
            double totalPerimeter = 0;
            double correction = 0;
            long twiceArea = 0;
            for (int i = 0; i < size; ++i) {
                Point next = vertices[(i + 1) % size];
                dx[i] = next.x - vertices[i].x;
                dy[i] = next.y - vertices[i].y;
                lengthSquared[i] = dx[i] * dx[i] + dy[i] * dy[i];
                rx[i] = vertices[i].x - vertices[0].x;
                ry[i] = vertices[i].y - vertices[0].y;
                double adjusted = Math.hypot((double) dx[i], (double) dy[i]) - correction;
                double total = totalPerimeter + adjusted;
                correction = (total - totalPerimeter) - adjusted;
                totalPerimeter = total;
                if (i > 1) {
                    twiceArea += cross(rx[i - 1], ry[i - 1], rx[i], ry[i]);
                }
            }
            perimeter = totalPerimeter;
            double area = (double) twiceArea / 2;
            double halfPerimeter = perimeter / 2;
            double multiplier = 1;
            double radius = 0;
            DoubleDouble exactArea = DoubleDouble.integer(twiceArea)
                    .multiply(new DoubleDouble(1.0 / 2, 0));
            DoubleDouble threshold = exactArea;
            radii.add(radius);
            extras.add(new DoubleDouble(0, 0));
            // A + P*r + pi*r*r = A*2^day; use the stable positive root.
            while (radius <= MAX_DISTANCE) {
                threshold = threshold.add(threshold);
                extras.add(threshold.subtract(exactArea));
                multiplier *= 2;
                double extra = area * (multiplier - 1);
                radius = extra / (halfPerimeter
                        + Math.sqrt(halfPerimeter * halfPerimeter + Math.PI * extra));
                radii.add(radius);
            }
        }

        boolean visible(int edge, Point query) {
            return cross(dx[edge], dy[edge], query.x - vertices[edge].x,
                    query.y - vertices[edge].y) < 0;
        }

        long endDot(int edge, Point query) {
            Point next = vertices[(edge + 1) % size];
            return (next.x - query.x) * dx[edge] + (next.y - query.y) * dy[edge];
        }

        Distance distance(Point query) {
            boolean first = visible(0, query);
            boolean last = visible(size - 1, query);
            int shown;
            int hidden;
            if (first != last) {
                shown = first ? 0 : size - 1;
                hidden = first ? size - 1 : 0;
            } else {
                long qx = query.x - vertices[0].x;
                long qy = query.y - vertices[0].y;
                int low = 1;
                int high = size - 1;
                while (high - low > 1) {
                    int middle = (low + high) / 2;
                    long turn = cross(rx[middle], ry[middle], qx, qy);
                    if (first ? turn <= 0 : turn >= 0) {
                        low = middle;
                    } else {
                        high = middle;
                    }
                }
                if (first) {
                    shown = 0;
                    hidden = low;
                } else {
                    shown = low;
                    hidden = 0;
                    if (!visible(shown, query)) {
                        return new Distance(0, 0, 1, false);
                    }
                }
            }

            long projection = (query.x - vertices[shown].x) * dx[shown]
                    + (query.y - vertices[shown].y) * dy[shown];
            int closest = shown;
            // Restrict the derivative test to the visible chain to keep each search monotone.
            if (projection > lengthSquared[shown]) {
                int low = 0;
                int high = (hidden - shown + size) % size;
                while (high - low > 1) {
                    int middle = (low + high) / 2;
                    int edge = (shown + middle) % size;
                    if (!visible(edge, query) || endDot(edge, query) >= 0) {
                        high = middle;
                    } else {
                        low = middle;
                    }
                }
                closest = (shown + high) % size;
            } else if (projection < 0) {
                int low = 0;
                int high = (shown - hidden + size) % size;
                while (high - low > 1) {
                    int middle = (low + high) / 2;
                    int edge = (hidden + middle) % size;
                    if (visible(edge, query) && endDot(edge, query) >= 0) {
                        high = middle;
                    } else {
                        low = middle;
                    }
                }
                closest = (hidden + high) % size;
            }

            long qx = query.x - vertices[closest].x;
            long qy = query.y - vertices[closest].y;
            projection = qx * dx[closest] + qy * dy[closest];
            if (projection <= 0) {
                return new Distance(Math.hypot((double) qx, (double) qy),
                        qx * qx + qy * qy, 1, false);
            }
            if (projection >= lengthSquared[closest]) {
                Point next = vertices[(closest + 1) % size];
                qx = query.x - next.x;
                qy = query.y - next.y;
                return new Distance(Math.hypot((double) qx, (double) qy),
                        qx * qx + qy * qy, 1, false);
            }
            long base = cross(dx[closest], dy[closest], qx, qy);
            double value = Math.abs((double) base) / Math.sqrt((double) lengthSquared[closest]);
            return new Distance(value, base, lengthSquared[closest], true);
        }

        boolean infected(int day, Distance separation) {
            double difference = radii.get(day) - separation.value;
            if (Math.abs(difference) > CLOSE_DISTANCE) {
                return difference > 0;
            }
            // Squared distance is numerator/denominator; compare areas without a square root.
            DoubleDouble numerator = DoubleDouble.integer(separation.base);
            if (separation.square) {
                numerator = numerator.multiply(numerator);
            }
            DoubleDouble denominator = DoubleDouble.integer(separation.denominator);
            DoubleDouble remainder = extras.get(day).multiply(denominator)
                    .subtract(new DoubleDouble(PI_HIGH, PI_LOW).multiply(numerator));
            DoubleDouble boundary = new DoubleDouble(perimeter, 0);
            DoubleDouble left = boundary.multiply(boundary).multiply(numerator)
                    .multiply(denominator);
            return remainder.nonnegative()
                    && remainder.multiply(remainder).subtract(left).nonnegative();
        }

        int day(Point query) {
            Distance separation = distance(query);
            if (separation.value == 0) {
                return 0;
            }
            int low = 0;
            int high = radii.size();
            while (low < high) {
                int middle = (low + high) / 2;
                if (radii.get(middle) >= separation.value) {
                    high = middle;
                } else {
                    low = middle + 1;
                }
            }
            while (low > 0 && infected(low - 1, separation)) {
                --low;
            }
            while (!infected(low, separation)) {
                ++low;
            }
            return low;
        }
    }

    private static final class FastInput {
        private final BufferedInputStream stream = new BufferedInputStream(System.in);

        long next() throws IOException {
            int current;
            do {
                current = stream.read();
            } while (current <= ' ' && current != -1);
            long sign = 1;
            if (current == '-') {
                sign = -1;
                current = stream.read();
            }
            long value = 0;
            while (current >= '0' && current <= '9') {
                value = value * 10 + current - '0';
                current = stream.read();
            }
            return value * sign;
        }
    }

    public static void main(String[] arguments) throws IOException {
        FastInput input = new FastInput();
        int count = (int) input.next();
        Point[] vertices = new Point[count];
        for (int i = 0; i < count; ++i) {
            vertices[i] = new Point(input.next(), input.next());
        }
        Polygon polygon = new Polygon(vertices);
        int queries = (int) input.next();
        StringBuilder output = new StringBuilder();
        for (int i = 0; i < queries; ++i) {
            output.append(polygon.day(new Point(input.next(), input.next()))).append('\n');
        }
        System.out.print(output);
    }
}
