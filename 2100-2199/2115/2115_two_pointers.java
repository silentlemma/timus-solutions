public class Main {
    static final int BUFFER_SIZE = 4096;
    static final byte[] input = new byte[BUFFER_SIZE];
    static int position, available;

    static int read() throws java.io.IOException {
        if (position == available) {
            available = System.in.read(input);
            position = 0;
            if (available < 0)
                return -1;
        }
        return input[position++];
    }

    static int nextInt() throws java.io.IOException {
        int c = read();
        while (c <= ' ')
            c = read();
        int value = 0;
        while (c >= '0' && c <= '9') {
            value = value * 10 + c - '0';
            c = read();
        }
        return value;
    }

    static int firstBad(int[] a, int direction) {
        int i = 0;
        while (i + 1 < a.length && a[i] * direction <= a[i + 1] * direction)
            i++;
        return i;
    }

    public static void main(String[] args) throws java.io.IOException {
        int n = nextInt();
        int[] a = new int[n];
        for (int i = 0; i < n; i++)
            a[i] = nextInt();
        int up = firstBad(a, 1), down = firstBad(a, -1);
        if (up == n - 1 || down == n - 1) {
            System.out.println("Nothing to do here");
            return;
        }
        for (int direction = 1; direction >= -1; direction -= 2) {
            int left = direction == 1 ? up : down, right = n - 1;
            // Equal runs can hide the actual swapped endpoint behind a violation.
            while (left > 0 && a[left - 1] == a[left])
                left--;
            while (a[right - 1] * direction <= a[right] * direction)
                right--;
            while (right + 1 < n && a[right + 1] == a[right])
                right++;
            int saved = a[left];
            a[left] = a[right];
            a[right] = saved;
            if (firstBad(a, direction) == n - 1) {
                System.out.println("Yes");
                System.out.println((left + 1) + " " + (right + 1));
                return;
            }
            a[right] = a[left];
            a[left] = saved;
        }
        System.out.println("No hope");
    }
}
