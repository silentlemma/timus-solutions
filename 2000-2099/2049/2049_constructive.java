import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
  static final int SPLIT_DIVISOR = 4;
  static final int INITIAL_CAPACITY = 16;
  static final int OUTPUT_BUFFER = 1 << 16;
  static final int MAX_DIGITS = 10;

  static class Answer {
    int[] from = new int[INITIAL_CAPACITY], to = new int[INITIAL_CAPACITY];
    int size;
    void add(int donor, int receiver) {
      if (size == from.length) {
        from = Arrays.copyOf(from, size * 2);
        to = Arrays.copyOf(to, size * 2);
      }
      from[size] = donor;
      to[size++] = receiver;
    }
  }

  static class State {
    final int[] volume, previous, following, groups, valuePrevious, valueFollowing;
    int oddHead, evenHead, evenCount;
    final Answer answer = new Answer();
    State(int size, int target) {
      volume = new int[size + 1];
      previous = new int[size + 1];
      following = new int[size + 1];
      groups = new int[size + 1];
      valuePrevious = new int[size + 1];
      valueFollowing = new int[size + 1];
      volume[1] = target;
      attach(1);
      if (size != target) {
        volume[2] = size - target;
        attach(2);
      }
    }
    void attach(int index) {
      int value = volume[index], head;
      if (value % 2 != 0) {
        head = groups[value];
        if (head == 0) {
          valuePrevious[value] = 0;
          valueFollowing[value] = oddHead;
          if (oddHead != 0)
            valuePrevious[oddHead] = value;
          oddHead = value;
        }
        groups[value] = index;
      } else {
        head = evenHead;
        evenHead = index;
        evenCount++;
      }
      previous[index] = 0;
      following[index] = head;
      if (head != 0)
        previous[head] = index;
    }
    void detach(int index) {
      int value = volume[index];
      if (value == 0)
        return;
      int before = previous[index], after = following[index];
      if (before != 0)
        following[before] = after;
      else if (value % 2 != 0)
        groups[value] = after;
      else
        evenHead = after;
      if (after != 0)
        previous[after] = before;
      if (value % 2 != 0) {
        if (groups[value] == 0) {
          before = valuePrevious[value];
          after = valueFollowing[value];
          if (before != 0)
            valueFollowing[before] = after;
          else
            oddHead = after;
          if (after != 0)
            valuePrevious[after] = before;
        }
      } else {
        evenCount--;
      }
    }
    void undo(int donor, int receiver) {
      detach(donor);
      detach(receiver);
      int half = volume[receiver] / 2;
      volume[receiver] = half;
      volume[donor] += half;
      attach(donor);
      attach(receiver);
      answer.add(donor, receiver);
    }
  }

  static Answer solve(int n, int k) {
    int size = (k & (k - 1)) == 0 ? k : k + 1 + (k & 1);
    if (size > n)
      return null;
    State state = new State(size, k);
    int[] empty = new int[size];
    int unused = 0;
    for (int i = 1; i <= size; i++)
      if (state.volume[i] == 0)
        empty[unused++] = i;
    while (state.evenCount > 0) {
      int receiver = state.evenHead;
      if (state.evenCount > 1 || state.volume[receiver] % SPLIT_DIVISOR == 0) {
        state.undo(empty[--unused], receiver);
        continue;
      }
      int value = state.oddHead;
      if (value == state.volume[receiver] / 2)
        value = state.valueFollowing[value];
      if (value == 0) {
        state.undo(empty[--unused], receiver);
        continue;
      }
      int donor = state.groups[value];
      while (state.volume[receiver] % SPLIT_DIVISOR != 0) {
        state.undo(donor, receiver);
        int old = donor;
        donor = receiver;
        receiver = old;
      }
    }
    return state.answer;
  }

  static class Output {
    final byte[] buffer = new byte[OUTPUT_BUFFER], digits = new byte[MAX_DIGITS];
    int size;
    void put(int value) throws IOException {
      if (size == buffer.length)
        flush();
      buffer[size++] = (byte) value;
    }
    void number(int value) throws IOException {
      int count = 0;
      do {
        digits[count++] = (byte) ('0' + value % 10);
        value /= 10;
      } while (value > 0);
      while (count > 0) put(digits[--count]);
    }
    void flush() throws IOException {
      System.out.write(buffer, 0, size);
      size = 0;
    }
  }

  static void writeAnswer(Answer answer, Output out) throws IOException {
    if (answer == null) {
      out.put('-');
      out.number(1);
      out.put('\n');
      return;
    }
    out.number(answer.size);
    out.put('\n');
    for (int i = answer.size - 1; i >= 0; i--) {
      out.number(answer.from[i]);
      out.put(' ');
      out.number(answer.to[i]);
      out.put('\n');
    }
  }

  public static void main(String[] args) throws IOException {
    BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer fields = new StringTokenizer(in.readLine());
    int n = Integer.parseInt(fields.nextToken()), k = Integer.parseInt(fields.nextToken());
    Output out = new Output();
    writeAnswer(solve(n, k), out);
    out.flush();
  }
}
