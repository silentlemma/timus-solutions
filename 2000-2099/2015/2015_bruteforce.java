import java.io.BufferedInputStream;
import java.io.IOException;

public class Main {
  private static final int APARTMENT_FIELDS = 3;

  private static int[] solve(int budget, int[] alone, int[][] friends, int[][] apartments) {
    int best = -1;
    int[] choice = new int[2];
    for (int i = 0; i < apartments.length; ++i) {
      int rooms = apartments[i][0], price = apartments[i][1], benefit = apartments[i][2];
      if (price <= budget) {
        int score = benefit + alone[rooms - 1];
        if (score > best) {
          best = score;
          choice[0] = i + 1;
          choice[1] = 0;
        }
      }
      if (rooms == 2 && price <= 2 * budget) {
        for (int j = 0; j < friends.length; ++j) {
          if (price <= 2 * friends[j][0]) {
            int score = benefit + friends[j][1];
            if (score > best) {
              best = score;
              choice[0] = i + 1;
              choice[1] = j + 1;
            }
          }
        }
      }
    }
    return choice;
  }

  private static int readInt(BufferedInputStream in) throws IOException {
    int c;
    do {
      c = in.read();
    } while (c <= ' ' && c >= 0);
    int value = 0;
    while (c > ' ') {
      value = value * 10 + c - '0';
      c = in.read();
    }
    return value;
  }

  public static void main(String[] args) throws IOException {
    BufferedInputStream in = new BufferedInputStream(System.in);
    int budget = readInt(in);
    int[] alone = {readInt(in), readInt(in)};
    int n = readInt(in);
    int[][] friends = new int[n][2];
    for (int[] row : friends) {
      row[0] = readInt(in);
      row[1] = readInt(in);
    }
    int m = readInt(in);
    int[][] apartments = new int[m][APARTMENT_FIELDS];
    for (int[] row : apartments) {
      row[0] = readInt(in);
      row[1] = readInt(in);
      row[2] = readInt(in);
    }
    int[] choice = solve(budget, alone, friends, apartments);
    if (choice[0] == 0)
      System.out.println("Forget about apartments. Live in the dormitory.");
    else if (choice[1] == 0)
      System.out.println("You should rent the apartment #" + choice[0] + " alone.");
    else
      System.out.println(
          "You should rent the apartment #" + choice[0] + " with the friend #" + choice[1] + ".");
  }
}
