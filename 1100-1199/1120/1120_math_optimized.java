public class Main {
    public static void main(String[] args) throws java.io.IOException {
        // the number is parsed byte by byte from System.in, which needs much less
        // memory than Scanner
        int ch;
        do {
            ch = System.in.read();
        } while (ch != -1 && ch <= ' ');
        long sum = 0;
        while (ch >= '0' && ch <= '9') {
            sum = sum * 10 + ch - '0';
            ch = System.in.read();
        }
        // sum = length*a + length(length-1)/2 with a >= 1
        // needs length(length+1)/2 <= sum; try the longest first
        long length = (long)Math.sqrt(2 * sum);
        while (length * (length + 1) / 2 > sum) {
            length--;
        }
        // the remainder for the next shorter length is updated in O(1)
        long remainder = sum - length * (length - 1) / 2;
        while (remainder % length != 0) {
            length--;
            remainder += length;
        }
        System.out.println(remainder / length + " " + length);
    }
}
