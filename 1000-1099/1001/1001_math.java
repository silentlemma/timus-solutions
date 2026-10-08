import java.io.DataInputStream;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.Arrays;
import java.util.Locale;

public class Main {
    private static final int BUFFER_SIZE = 1 << 16;

    public static void main(String[] args) throws IOException {
        DataInputStream in = new DataInputStream(System.in);
        byte[] buf = new byte[BUFFER_SIZE];
        long[] nums = new long[BUFFER_SIZE];
        int count = 0;
        long cur = 0;
        boolean inNumber = false;
        int read;
        while ((read = in.read(buf)) > 0) {
            for (int i = 0; i < read; i++) {
                byte c = buf[i];
                if (c >= '0' && c <= '9') {
                    cur = cur * 10 + (c - '0');
                    inNumber = true;
                } else if (inNumber) {
                    if (count == nums.length) {
                        nums = Arrays.copyOf(nums, count * 2);
                    }
                    nums[count++] = cur;
                    cur = 0;
                    inNumber = false;
                }
            }
        }
        if (inNumber) {
            if (count == nums.length) {
                nums = Arrays.copyOf(nums, count + 1);
            }
            nums[count++] = cur;
        }
        PrintWriter out = new PrintWriter(System.out);
        StringBuilder sb = new StringBuilder();
        for (int i = count - 1; i >= 0; i--) {
            sb.append(String.format(Locale.US, "%.4f", Math.sqrt((double) nums[i]))).append('\n');
        }
        out.print(sb);
        out.flush();
    }
}
