import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int row(int index) {
        int before = index - 1;
        int root = (int)Math.sqrt(before);
        if ((root + 1) * (root + 1) <= before) {
            root++;
        }
        return root + 1;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer numbers = new StringTokenizer(input.readLine());
        int a = Integer.parseInt(numbers.nextToken()), b = Integer.parseInt(numbers.nextToken());
        int ra = row(a), rb = row(b);
        int leftA = a - (ra - 1) * (ra - 1), leftB = b - (rb - 1) * (rb - 1);
        int steps = Math.abs(ra - rb) + Math.abs((leftA + 1) / 2 - (leftB + 1) / 2) +
                    Math.abs(ra - leftA / 2 - (rb - leftB / 2));
        System.out.println(steps);
    }
}
