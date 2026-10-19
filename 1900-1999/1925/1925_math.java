import java.util.Scanner;

public class Main {
    static int requiredInput(int current, int[][] history) {
        int answer = current - 2;
        for (int[] reading : history) {
            answer += reading[0] - reading[1] - 2;
        }
        return answer;
    }

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int count = input.nextInt();
        int current = input.nextInt();
        int[][] history = new int[count][2];
        for (int[] reading : history) {
            reading[0] = input.nextInt();
            reading[1] = input.nextInt();
        }
        int answer = requiredInput(current, history);
        System.out.println(answer >= 0 ? Integer.toString(answer) : "Big Bang!");
    }
}
