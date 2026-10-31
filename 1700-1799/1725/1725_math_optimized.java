public class Main {

    // only one or two small integers are read; no scanner or buffer is needed.
    static int next() throws java.io.IOException {
        int c = System.in.read();
        while (c != -1 && c <= ' ')
            c = System.in.read();
        int value = 0;
        while (c >= '0' && c <= '9') {
            value = value * 10 + c - '0';
            c = System.in.read();
        }
        return value;
    }

    // everyone on the far side of Vasya can be made to trip except the two
    // seats at the far end, who always come in from their own end
    static final int SAFE = 2;

    public static void main(String[] args) throws java.io.IOException {
        int n = next(), k = next();
        int far = Math.max(k - 1, n - k);
        System.out.println(Math.max(0, far - SAFE));
    }
}
