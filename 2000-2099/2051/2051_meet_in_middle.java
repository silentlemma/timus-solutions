import java.io.IOException;
import java.util.Arrays;

public class Main {
  static final int MAX_CONTACTS = 30;
  static final int BUFFER_SIZE = 1 << 16;

  static class Curve {
    final int[] time, height;
    int size;
    Curve(int capacity) {
      time = new int[capacity];
      height = new int[capacity];
    }
    void raw(int t, int y) {
      time[size] = t;
      height[size++] = y;
    }
    void add(int t, int y) {
      if (size > 0 && time[size - 1] == t)
        return;
      while (size >= 2) {
        int a = time[size - 2], b = time[size - 1];
        int x = height[size - 2], yy = height[size - 1];
        if ((long) (yy - x) * (t - b) != (long) (y - yy) * (b - a))
          break;
        size--;
      }
      raw(t, y);
    }
  }

  static Curve contactsOf(Curve upper, Curve lower, int duration) {
    int i = 0, j = 0, time = 0;
    Curve contacts = new Curve(MAX_CONTACTS);
    while (true) {
      while (i + 2 < upper.size && upper.time[i + 1] <= time) i++;
      while (j + 2 < lower.size && lower.time[j + 1] <= time) j++;
      long hn = (long) upper.height[i] * (upper.time[i + 1] - time)
          + (long) upper.height[i + 1] * (time - upper.time[i]);
      long gn = (long) lower.height[j] * (lower.time[j + 1] - time)
          + (long) lower.height[j + 1] * (time - lower.time[j]);
      int hd = upper.time[i + 1] - upper.time[i], gd = lower.time[j + 1] - lower.time[j];
      if (hn * gd == gn * hd && time > 0 && time < duration)
        contacts.raw(time, (int) (hn / hd));
      if (time == duration)
        return contacts;
      time = Math.min(upper.time[i + 1], lower.time[j + 1]);
    }
  }

  static Curve augment(Curve curve, Curve contacts) {
    Curve result = new Curve(curve.size + contacts.size);
    int i = 0, j = 0;
    while (i < curve.size || j < contacts.size) {
      if (j == contacts.size || (i < curve.size && curve.time[i] < contacts.time[j])) {
        result.raw(curve.time[i], curve.height[i]);
        i++;
      } else if (i == curve.size || contacts.time[j] < curve.time[i]) {
        result.raw(contacts.time[j], contacts.height[j]);
        j++;
      } else {
        result.raw(curve.time[i], curve.height[i]);
        i++;
        j++;
      }
    }
    return result;
  }

  static long[] areas(Curve curve, int[] boundaries) {
    long[] result = new long[boundaries.length - 1];
    long total = 0;
    int region = 0;
    for (int i = 0; i + 1 < curve.size; i++) {
      total += (long) (curve.height[i] + curve.height[i + 1]) * (curve.time[i + 1] - curve.time[i]);
      if (curve.time[i + 1] == boundaries[region + 1]) {
        result[region++] = total;
        total = 0;
      }
    }
    return result;
  }

  static int choose(long[] weights) {
    int leftCount = weights.length / 2;
    long scale = 1L << leftCount, total = 0;
    for (long weight : weights) total += weight;
    long target = total / 2;
    long[] keys = new long[1 << leftCount];
    int size = 1;
    for (int bit = 0; bit < leftCount; bit++) {
      long step = weights[bit] * scale + (1L << bit);
      for (int i = 0; i < size; i++) keys[size + i] = keys[i] + step;
      size *= 2;
    }
    Arrays.sort(keys);
    int previous = 0;
    long rightSum = 0;
    for (int index = 0; index < (1 << (weights.length - leftCount)); index++) {
      int gray = index ^ (index >> 1);
      if (index != 0) {
        int changed = gray ^ previous;
        int bit = Integer.numberOfTrailingZeros(changed);
        rightSum += (gray & changed) != 0 ? weights[leftCount + bit] : -weights[leftCount + bit];
      }
      previous = gray;
      long need = target - rightSum, packed = need * scale;
      int low = 0, high = keys.length;
      while (low < high) {
        int middle = (low + high) / 2;
        if (keys[middle] < packed)
          low = middle + 1;
        else
          high = middle;
      }
      if (low < keys.length && keys[low] / scale == need)
        return (int) (keys[low] & (scale - 1)) | (gray << leftCount);
    }
    return 0;
  }

  static Curve[] solve(int duration, Curve originalUpper, Curve originalLower) {
    Curve contacts = contactsOf(originalUpper, originalLower, duration);
    int[] boundaries = new int[contacts.size + 2];
    for (int i = 0; i < contacts.size; i++) boundaries[i + 1] = contacts.time[i];
    boundaries[boundaries.length - 1] = duration;
    Curve upper = augment(originalUpper, contacts), lower = augment(originalLower, contacts);
    long[] ua = areas(upper, boundaries), la = areas(lower, boundaries);
    long[] weights = new long[ua.length];
    for (int i = 0; i < weights.length; i++) weights[i] = ua[i] - la[i];
    int mask = choose(weights);
    int capacity = upper.size + lower.size;
    Curve[] result = {new Curve(capacity), new Curve(capacity)};
    int hi = 0, lo = 0;
    for (int region = 0; region + 1 < boundaries.length; region++) {
      int destination = (mask & (1 << region)) != 0 ? 0 : 1, end = boundaries[region + 1];
      while (hi < upper.size && upper.time[hi] <= end) {
        result[destination].add(upper.time[hi], upper.height[hi]);
        hi++;
      }
      while (lo < lower.size && lower.time[lo] <= end) {
        result[1 - destination].add(lower.time[lo], lower.height[lo]);
        lo++;
      }
      hi--;
      lo--;
    }
    return result;
  }

  static class Input {
    final byte[] buffer = new byte[BUFFER_SIZE];
    int at, size;
    int read() throws IOException {
      if (at == size) {
        size = System.in.read(buffer);
        at = 0;
        if (size < 0)
          return -1;
      }
      return buffer[at++];
    }
    int next() throws IOException {
      int ch;
      do {
        ch = read();
      } while (ch <= ' ');
      int value = 0;
      while (ch > ' ') {
        value = value * 10 + ch - '0';
        ch = read();
      }
      return value;
    }
  }

  static class Output {
    final byte[] buffer = new byte[BUFFER_SIZE], digits = new byte[10];
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
      } while (value != 0);
      while (count > 0) put(digits[--count]);
    }
    void flush() throws IOException {
      System.out.write(buffer, 0, size);
      size = 0;
    }
  }

  static Curve readCurve(Input in) throws IOException {
    int count = in.next();
    Curve result = new Curve(count);
    for (int i = 0; i < count; i++) result.raw(in.next(), in.next());
    return result;
  }

  public static void main(String[] args) throws IOException {
    Input in = new Input();
    int duration = in.next();
    Curve upper = readCurve(in), lower = readCurve(in);
    Output out = new Output();
    for (Curve curve : solve(duration, upper, lower)) {
      out.number(curve.size);
      out.put('\n');
      for (int i = 0; i < curve.size; i++) {
        out.number(curve.time[i]);
        out.put(' ');
        out.number(curve.height[i]);
        out.put('\n');
      }
    }
    out.flush();
  }
}
