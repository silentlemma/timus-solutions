import java.io.BufferedInputStream;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;

public class Main {
  private static final int MAX_FRIENDS = 100;
  private static final int BASE = 10;
  private static final String[] LABELS = {"left", "right"};
  private static final class Group {
    int time;
    int[] students;
  }
  private static final class Case {
    int[][] friends;
    Group[] groups;
  }

  private static int readInt(BufferedInputStream input) throws IOException {
    int ch;
    do {
      ch = input.read();
    } while (ch <= ' ' && ch != -1);
    int value = 0;
    while (ch > ' ') {
      value = value * BASE + ch - '0';
      ch = input.read();
    }
    return value;
  }

  private static Case readCase(BufferedInputStream input) throws IOException {
    int count = readInt(input), groupCount = readInt(input);
    Case data = new Case();
    data.friends = new int[count][];
    data.groups = new Group[groupCount];
    for (int i = 0; i < count; i++) {
      int[] row = new int[MAX_FRIENDS];
      int size = 0;
      for (int id = readInt(input); id != 0; id = readInt(input)) row[size++] = id - 1;
      data.friends[i] = Arrays.copyOf(row, size);
    }
    for (int i = 0; i < groupCount; i++) {
      Group group = new Group();
      group.time = readInt(input);
      group.students = new int[readInt(input)];
      for (int j = 0; j < group.students.length; j++) group.students[j] = readInt(input) - 1;
      data.groups[i] = group;
    }
    return data;
  }

  private static int[][] solve(int[][] friends, Group[] groups) {
    int count = friends.length;
    ArrayList<ArrayList<Integer>> queues = new ArrayList<>();
    queues.add(new ArrayList<>());
    queues.add(new ArrayList<>());
    int[] which = new int[count], position = new int[count], nextCompletion = new int[2];
    Arrays.fill(which, -1);
    Arrays.fill(position, -1);
    int[][] answer = new int[count][2];
    for (Group group : groups) {
      int now = group.time;
      for (int side = 0; side < 2; side++) {
        ArrayList<Integer> queue = queues.get(side);
        if (queue.isEmpty() || nextCompletion[side] > now)
          continue;
        int served = Math.min(queue.size(), now - nextCompletion[side] + 1);
        for (int at = 0; at < served; at++) {
          int student = queue.get(at);
          answer[student][0] = nextCompletion[side] + at;
          answer[student][1] = side;
          which[student] = -1;
        }
        queue.subList(0, served).clear();
        for (int at = 0; at < queue.size(); at++) position[queue.get(at)] = at;
        nextCompletion[side] = queue.isEmpty() ? 0 : nextCompletion[side] + served;
      }
      for (int student : group.students) {
        int[] best = {queues.get(0).size(), queues.get(1).size()};
        for (int friend : friends[student]) {
          int side = which[friend];
          if (side >= 0)
            best[side] = Math.min(best[side], position[friend] + 1);
        }
        int side = best[0] < best[1] ? 0 : 1;
        ArrayList<Integer> queue = queues.get(side);
        int at = best[side];
        queue.add(at, student);
        which[student] = side;
        for (int index = at; index < queue.size(); index++) position[queue.get(index)] = index;
        if (queue.size() == 1)
          nextCompletion[side] = now + 1;
      }
    }
    for (int side = 0; side < 2; side++) {
      ArrayList<Integer> queue = queues.get(side);
      for (int at = 0; at < queue.size(); at++) {
        int student = queue.get(at);
        answer[student][0] = nextCompletion[side] + at;
        answer[student][1] = side;
      }
    }
    return answer;
  }

  public static void main(String[] args) throws IOException {
    Case data = readCase(new BufferedInputStream(System.in));
    StringBuilder output = new StringBuilder();
    for (int[] answer : solve(data.friends, data.groups))
      output.append(answer[0]).append(' ').append(LABELS[answer[1]]).append('\n');
    System.out.print(output);
  }
}
