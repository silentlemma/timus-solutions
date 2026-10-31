use std::io::{self, Read};

const INPUT_BUFFER: usize = 4096;
// the refillable buffer holds only a chunk, never the complete input.
struct Reader<R> {
    input: R,
    buffer: [u8; INPUT_BUFFER],
    at: usize,
    size: usize,
}
impl<R: Read> Reader<R> {
    fn new(input: R) -> Self {
        Self {
            input,
            buffer: [0; INPUT_BUFFER],
            at: 0,
            size: 0,
        }
    }
    fn byte(&mut self) -> u8 {
        if self.at == self.size {
            self.size = self.input.read(&mut self.buffer).unwrap();
            self.at = 0;
            if self.size == 0 {
                return 0;
            }
        }
        let c = self.buffer[self.at];
        self.at += 1;
        c
    }
    fn next(&mut self) -> i32 {
        let mut c = self.byte();
        while c != 0 && c != b'-' && !c.is_ascii_digit() {
            c = self.byte();
        }
        let mut sign = 1;
        if c == b'-' {
            sign = -1;
            c = self.byte();
        }
        let mut value = 0;
        while c.is_ascii_digit() {
            value = value * 10 + i32::from(c - b'0');
            c = self.byte();
        }
        value * sign
    }
}

fn main() {
    let stdin = io::stdin();
    let mut input = Reader::new(stdin.lock());
    let (m, n, k) = (input.next(), input.next(), input.next() as usize);
    let (stride, column_stride) = (n + 2, m + 2);
    // coordinates <= 30000 make row-major and column-major keys fit i32.
    let mut rows = Vec::with_capacity(k);
    let mut columns = Vec::with_capacity(k);
    for _ in 0..k {
        let (x, y) = (input.next(), input.next());
        rows.push(x * stride + y);
        columns.push(y * column_stride + x);
    }
    rows.sort_unstable();
    columns.sort_unstable();
    let (mut answer, mut at) = (0, 0);
    for x in 1..=m {
        let mut previous = 0;
        loop {
            let next = if at < k && rows[at] / stride == x {
                let y = rows[at] % stride;
                at += 1;
                y
            } else {
                n + 1
            };
            let (length, cell) = (next - previous - 1, x * stride + previous + 1);
            if length >= 2
                || (length == 1
                    && (x == 1 || rows.binary_search(&(cell - stride)).is_ok())
                    && (x == m || rows.binary_search(&(cell + stride)).is_ok()))
            {
                answer += 1;
            }
            if next == n + 1 {
                break;
            }
            previous = next;
        }
    }
    at = 0;
    for y in 1..=n {
        let mut previous = 0;
        loop {
            let next = if at < k && columns[at] / column_stride == y {
                let x = columns[at] % column_stride;
                at += 1;
                x
            } else {
                m + 1
            };
            if next - previous - 1 >= 2 {
                answer += 1;
            }
            if next == m + 1 {
                break;
            }
            previous = next;
        }
    }
    println!("{}", answer);
}
