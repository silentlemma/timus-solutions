import java.io.*;
import java.math.BigInteger;

public class Main {
    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        int i = (int)in.nval;
        in.nextToken();
        BigInteger current = BigInteger.valueOf((long)in.nval);
        in.nextToken();
        int j = (int)in.nval;
        in.nextToken();
        BigInteger later = BigInteger.valueOf((long)in.nval);
        in.nextToken();
        int n = (int)in.nval;
        if (i > j) {
            int index = i;
            i = j;
            j = index;
            BigInteger value = current;
            current = later;
            later = value;
        }
        BigInteger previous = BigInteger.ZERO, coefficient = BigInteger.ONE;
        for (int step = 0; step < j - i; step++) {
            BigInteger sum = previous.add(coefficient);
            previous = coefficient;
            coefficient = sum;
        }
        // F(j) = F(j-i-1)*F(i) + F(j-i)*F(i+1); division is exact.
        BigInteger following =
            later.subtract(coefficient.subtract(previous).multiply(current)).divide(previous);
        while (i < n) {
            BigInteger sum = current.add(following);
            current = following;
            following = sum;
            i++;
        }
        while (i > n) {
            BigInteger value = following.subtract(current);
            following = current;
            current = value;
            i--;
        }
        System.out.println(current);
    }
}
