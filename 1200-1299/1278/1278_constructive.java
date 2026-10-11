import java.util.*;

public class Main {
    public static void main(String[] args) {
        long k = new Scanner(System.in).nextLong();
        // from the BELL&RET cell upwards: "CALL i + 1" at cell i doubles the
        // bells made from the next cell, a call of the last cell adds one more,
        // so the binary digits of K give the cells
        List<Boolean> doubles = new ArrayList<>();
        String bits = Long.toBinaryString(k);
        for (int i = 1; i < bits.length(); i++) {
            doubles.add(true);
            if (bits.charAt(i) == '1')
                doubles.add(false);
        }
        int last = doubles.size();
        StringBuilder out = new StringBuilder();
        for (int cell = 0; cell < last; cell++)
            out.append("CALL ").append(doubles.get(last - 1 - cell) ? cell + 1 : last).append("\n");
        out.append("BELL&RET");
        System.out.println(out);
    }
}
