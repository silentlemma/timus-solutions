import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
    static final int LOW_MARK = 3;
    static final int TOP_MARK = 5;
    static final int DOUBLED_THRESHOLD = 9;

    static String classify(int count, int total, int lowest) {
        if (lowest == LOW_MARK)
            return "None";
        if (lowest == TOP_MARK)
            return "Named";
        if (2 * total >= DOUBLED_THRESHOLD * count)
            return "High";
        return "Common";
    }

    public static void main(String[] args) throws Exception {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        int count = Integer.parseInt(input.readLine().trim());
        int total = 0, lowest = TOP_MARK;
        for (int i = 0; i < count; i++) {
            int grade = Integer.parseInt(input.readLine().trim());
            total += grade;
            lowest = Math.min(lowest, grade);
        }
        System.out.println(classify(count, total, lowest));
    }
}
