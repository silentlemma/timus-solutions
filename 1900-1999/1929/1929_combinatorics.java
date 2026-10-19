import java.util.Scanner;

public class Main {
    static final int TEAM_SIZE = 3;

    static int waysToChoose(int available, int count) {
        if (count < 0 || count > available) {
            return 0;
        }
        if (count == 0) {
            return 1;
        }
        if (count == 1) {
            return available;
        }
        return available * (available - 1) / 2;
    }

    static int countTeams(int total, int specialCount, int firstSpecial) {
        int special = specialCount - firstSpecial;
        int ordinary = total - specialCount - (1 - firstSpecial);
        int remainingTeams = total / TEAM_SIZE - 1;
        int answer = 0;
        for (int chosenSpecial = 0; chosenSpecial < TEAM_SIZE; chosenSpecial++) {
            int removedSpecial = firstSpecial + chosenSpecial;
            if (removedSpecial == 0 || specialCount - removedSpecial < remainingTeams) {
                continue;
            }
            answer += waysToChoose(special, chosenSpecial)
                    * waysToChoose(ordinary, TEAM_SIZE - 1 - chosenSpecial);
        }
        return answer;
    }

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int total = input.nextInt();
        int specialCount = input.nextInt();
        int firstSpecial = 0;
        for (int i = 0; i < specialCount; i++) {
            if (input.nextInt() == 1) {
                firstSpecial = 1;
            }
        }
        System.out.println(countTeams(total, specialCount, firstSpecial));
    }
}
