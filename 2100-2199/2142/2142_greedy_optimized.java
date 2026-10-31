public class Main {

    // these inputs contain only nonnegative integers; avoid scanner's regex machinery.
    static long nextLong() throws java.io.IOException {
        int c;
        do {
            c = System.in.read();
        } while (c >= 0 && c <= ' ');
        long value = 0;
        while (c >= '0' && c <= '9') {
            value = value * 10 + c - '0';
            c = System.in.read();
        }
        return value;
    }

    public static void main(String[] args) throws java.io.IOException {
        long a = nextLong();
        long b = nextLong();
        long c = nextLong();
        long x = nextLong();
        long y = nextLong();
        long z = nextLong();
        // the dual lands first cover what the red and blue lands miss, and every
        // land left over pays for the mana of any color
        long missing = Math.max(0, x - a) + Math.max(0, y - b);
        boolean enough = missing <= c && a + b + c >= x + y + z;
        System.out.println(enough ? "It is a kind of magic" : "There are no miracles in life");
    }
}
