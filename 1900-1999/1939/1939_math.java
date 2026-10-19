import java.io.BufferedInputStream;
import java.io.IOException;

public class Main {
    private static boolean canCrash(long length, long height, long gateHeight, long speed,
                                    long gateSpeed, long deceleration) {
        long stoppingBound = gateSpeed * (speed * speed + 2 * deceleration * length);
        long passingBound = 2 * deceleration * speed * (gateHeight - height);
        return stoppingBound >= passingBound;
    }

    private static long nextLong(BufferedInputStream input) throws IOException {
        int symbol;
        do {
            symbol = input.read();
        } while (symbol <= ' ' && symbol >= 0);
        long value = 0;
        while (symbol > ' ') {
            value = value * 10 + symbol - '0';
            symbol = input.read();
        }
        return value;
    }

    public static void main(String[] args) throws IOException {
        BufferedInputStream input = new BufferedInputStream(System.in);
        long length = nextLong(input);
        long height = nextLong(input);
        long gateHeight = nextLong(input);
        long speed = nextLong(input);
        long gateSpeed = nextLong(input);
        long deceleration = nextLong(input);
        System.out.println(canCrash(length, height, gateHeight, speed, gateSpeed, deceleration)
                           ? "Crash" : "Safe");
    }
}
