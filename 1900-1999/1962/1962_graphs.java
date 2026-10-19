import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
  static final long MODULUS = 1000000007L;

  static long seatingCount(int size, int[] requests) {
    if (size == 2)
      return 1;
    List<List<Integer>> neighbors = new ArrayList<>();
    for (int person = 0; person < size; person++) neighbors.add(new ArrayList<>());
    for (int person = 0; person < requests.length; person++) {
      int target = requests[person];
      if (!neighbors.get(person).contains(target)) {
        neighbors.get(person).add(target);
        neighbors.get(target).add(person);
        if (neighbors.get(person).size() > 2 || neighbors.get(target).size() > 2)
          return 0;
      }
    }
    boolean[] visited = new boolean[size];
    int components = 0, paths = 0;
    int[] stack = new int[size];
    for (int start = 0; start < size; start++) {
      if (visited[start])
        continue;
      int top = 0;
      stack[top++] = start;
      visited[start] = true;
      int vertices = 0, degrees = 0;
      while (top > 0) {
        int person = stack[--top];
        vertices++;
        degrees += neighbors.get(person).size();
        for (int target : neighbors.get(person)) {
          if (!visited[target]) {
            visited[target] = true;
            stack[top++] = target;
          }
        }
      }
      if (degrees == 2 * vertices)
        return vertices == size ? 2 : 0;
      components++;
      if (vertices > 1)
        paths++;
    }
    long answer = 1;
    for (int path = 0; path < paths; path++) answer = answer * 2 % MODULUS;
    for (int factor = 2; factor < components; factor++) answer = answer * factor % MODULUS;
    return answer;
  }

  public static void main(String[] args) {
    try (Scanner input = new Scanner(System.in)) {
      int size = input.nextInt(), count = input.nextInt();
      int[] requests = new int[count];
      for (int i = 0; i < count; i++) requests[i] = input.nextInt() - 1;
      System.out.println(seatingCount(size, requests));
    }
  }
}
