import java.io.BufferedInputStream;
import java.io.IOException;

public strictfp class Main {
    private static final int SCALE = 1000;
    private static final int OUTPUT_SCALE = SCALE * SCALE;
    private static final int FULL_TURN = 360000;
    private static final int HALF_TURN = FULL_TURN / 2;
    private static final int QUARTER_TURN = HALF_TURN / 2;
    private static final int EIGHTH_TURN = QUARTER_TURN / 2;
    private static final int QUADRANT_COUNT = 2 * 2;
    private static final int BUFFER_SIZE = 65536;
    private static final int OUTPUT_DECIMALS = 6;
    private static final double PI = 3.141592653589793;
    private static final double ANGLE_EPS = 1e-11;
    private static final double ROUND_HALF = 0.5;
    private static final double[] SIN_COEFFICIENTS = {
        2.8114572543455206e-15, -7.647163731819816e-13,
        1.6059043836821613e-10, -2.505210838544172e-8,
        2.7557319223985893e-6, -0.0001984126984126984,
        0.008333333333333333, -0.16666666666666666, 1
    };
    private static final double[] COS_COEFFICIENTS = {
        -1.5619206968586225e-16, 4.779477332387385e-14,
        -1.1470745597729725e-11, 2.08767569878681e-9,
        -2.755731922398589e-7, 2.48015873015873e-5,
        -0.001388888888888889, 0.041666666666666664, -0.5, 1
    };

    private static long[] x;
    private static long[] y;
    private static long[] prefix;
    private static long total;
    private static double sine;
    private static double cosine;

    private static final class FastInput {
        private final BufferedInputStream input = new BufferedInputStream(System.in, BUFFER_SIZE);

        private String next() throws IOException {
            StringBuilder token = new StringBuilder();
            int current;
            do {
                current = input.read();
            } while (current >= 0 && current <= ' ');
            while (current > ' ') {
                token.append((char) current);
                current = input.read();
            }
            return token.toString();
        }

        private int integer() throws IOException {
            return Integer.parseInt(next());
        }

        private long scaled() throws IOException {
            String token = next();
            boolean negative = token.charAt(0) == '-';
            long result = 0;
            for (int index = negative ? 1 : 0; index < token.length(); ++index) {
                char digit = token.charAt(index);
                if (digit != '.') {
                    result = result * 10 + digit - '0';
                }
            }
            return negative ? -result : result;
        }
    }

    private static void trigonometry(long angle) {
        int normalized = (int) (angle % FULL_TURN);
        if (normalized < 0) {
            normalized += FULL_TURN;
        }
        int quadrant = normalized / QUARTER_TURN;
        int reduced = normalized % QUARTER_TURN;
        boolean mirror = reduced > EIGHTH_TURN;
        if (mirror) {
            reduced = QUARTER_TURN - reduced;
        }
        double radians = reduced * (PI / HALF_TURN);
        double square = radians * radians;
        double sinPolynomial = 0;
        for (double coefficient : SIN_COEFFICIENTS) {
            sinPolynomial = sinPolynomial * square + coefficient;
        }
        double cosPolynomial = 0;
        for (double coefficient : COS_COEFFICIENTS) {
            cosPolynomial = cosPolynomial * square + coefficient;
        }
        double sinValue = radians * sinPolynomial;
        double cosValue = cosPolynomial;
        if (reduced == EIGHTH_TURN) {
            sinValue = cosValue;
        }
        if (mirror) {
            double temporary = sinValue;
            sinValue = cosValue;
            cosValue = temporary;
        }
        if (quadrant == 0) {
            sine = sinValue;
            cosine = cosValue;
        } else if (quadrant == 1) {
            sine = cosValue;
            cosine = -sinValue;
        } else if (quadrant == 2) {
            sine = -sinValue;
            cosine = -cosValue;
        } else if (quadrant == QUADRANT_COUNT - 1) {
            sine = -cosValue;
            cosine = sinValue;
        }
    }

    private static double height(int index) {
        return x[index] * sine + y[index] * cosine;
    }

    private static double capacity(long angle) {
        trigonometry(angle);
        double first = height(0);
        if (first == 0) {
            double horizontal = x[0] * cosine - y[0] * sine;
            return horizontal < 0 ? total : 0;
        }
        boolean below = first < 0;
        int left = 0;
        int right = x.length - 1;
        while (right - left > 1) {
            int middle = (left + right) / 2;
            if ((height(middle) < 0) == below) {
                left = middle;
            } else {
                right = middle;
            }
        }
        double leftHeight = height(left);
        double rightHeight = height(right);
        double fraction = leftHeight / (leftHeight - rightHeight);
        fraction = Math.max(0, Math.min(1, fraction));
        long triangle = prefix[right] - prefix[left];
        double answer;
        if (below) {
            answer = prefix[left] + fraction * triangle;
        } else {
            answer = total - prefix[right] + (1 - fraction) * triangle;
        }
        return answer;
    }

    private static void appendAnswer(StringBuilder output, double area) {
        long units = (long) (area * ROUND_HALF + ROUND_HALF);
        output.append(units / OUTPUT_SCALE).append('.');
        String fraction = Long.toString(units % OUTPUT_SCALE);
        for (int index = fraction.length(); index < OUTPUT_DECIMALS; ++index) {
            output.append('0');
        }
        output.append(fraction).append("000\n");
    }

    public static void main(String[] arguments) throws IOException {
        FastInput input = new FastInput();
        int count = input.integer();
        long[] originalX = new long[count];
        long[] originalY = new long[count];
        for (int index = 0; index < count; ++index) {
            originalX[index] = input.scaled();
            originalY[index] = input.scaled();
        }
        long holeX = input.scaled();
        long holeY = input.scaled();
        int start = 0;
        for (int index = 0; index < count; ++index) {
            originalX[index] -= holeX;
            originalY[index] -= holeY;
        }
        for (int index = 0; index < count; ++index) {
            int next = (index + 1) % count;
            long cross = originalX[index] * originalY[next];
            cross -= originalY[index] * originalX[next];
            long dot = originalX[index] * originalX[next];
            dot += originalY[index] * originalY[next];
            if (cross == 0 && dot < 0) {
                start = next;
                break;
            }
        }
        x = new long[count];
        y = new long[count];
        prefix = new long[count];
        for (int index = 0; index < count; ++index) {
            int source = (start + index) % count;
            x[index] = originalX[source];
            y[index] = originalY[source];
            if (index > 0) {
                long triangle = x[index - 1] * y[index] - y[index - 1] * x[index];
                prefix[index] = prefix[index - 1] + triangle;
            }
        }
        total = prefix[count - 1];
        double zero = -Math.atan2(y[0], x[0]) * (HALF_TURN / PI);
        double lower = zero > 0 ? zero - FULL_TURN : zero;
        double upper = zero > 0 ? zero : zero + FULL_TURN;
        boolean empty = y[0] == 0 && x[0] > 0;
        double answer = empty ? 0 : capacity(0);
        long angle = 0;
        int queries = input.integer();
        StringBuilder output = new StringBuilder();
        appendAnswer(output, answer);
        for (int query = 0; query < queries; ++query) {
            angle += input.scaled();
            if (!empty && (angle <= lower + ANGLE_EPS || angle >= upper - ANGLE_EPS)) {
                empty = true;
                answer = 0;
            }
            if (!empty) {
                answer = Math.min(answer, capacity(angle));
            }
            appendAnswer(output, answer);
        }
        System.out.print(output);
    }
}
