use std::fmt::Write as FmtWrite;
use std::io::{self, Read, Write};

struct Input {
    data: Vec<u8>,
    position: usize,
}

impl Input {
    fn next_i64(&mut self) -> i64 {
        while self.data[self.position].is_ascii_whitespace() {
            self.position += 1;
        }
        let mut sign = 1;
        if self.data[self.position] == b'-' {
            sign = -1;
            self.position += 1;
        }
        let mut value = 0;
        while self.position < self.data.len() && self.data[self.position].is_ascii_digit() {
            value = value * 10 + i64::from(self.data[self.position] - b'0');
            self.position += 1;
        }
        value * sign
    }
}

fn lower_bound(points: &[(i64, i64)], value: (i64, i64)) -> usize {
    let mut left = 0;
    let mut right = points.len();
    while left < right {
        let middle = left + (right - left) / 2;
        if points[middle] < value {
            left = middle + 1;
        } else {
            right = middle;
        }
    }
    left
}

fn count(points: &[(i64, i64)], fixed: i64, low: i64, high: i64) -> usize {
    lower_bound(points, (fixed, high + 1)) - lower_bound(points, (fixed, low))
}

fn main() {
    let mut data = Vec::new();
    io::stdin().read_to_end(&mut data).unwrap();
    let mut input = Input { data, position: 0 };
    let size = input.next_i64() as usize;
    let mut by_u = Vec::with_capacity(size);
    let mut by_v = Vec::with_capacity(size);
    for _ in 0..size {
        let x = input.next_i64();
        let y = input.next_i64();
        by_u.push((x + y, x - y));
        by_v.push((x - y, x + y));
    }
    by_u.sort_unstable();
    by_v.sort_unstable();

    let queries = input.next_i64() as usize;
    let mut output = String::new();
    for _ in 0..queries {
        let x = input.next_i64();
        let y = input.next_i64();
        let distance = input.next_i64();
        let u = x + y;
        let v = x - y;
        let answer = if distance == 0 {
            count(&by_u, u, v, v)
        } else {
            let mut total = count(&by_u, u - distance, v - distance, v + distance);
            total += count(&by_u, u + distance, v - distance, v + distance);
            // The vertical sides already include the four corners.
            total += count(&by_v, v - distance, u - distance + 1, u + distance - 1);
            total += count(&by_v, v + distance, u - distance + 1, u + distance - 1);
            total
        };
        writeln!(output, "{}", answer).unwrap();
    }
    let stdout = io::stdout();
    let mut writer = io::BufWriter::new(stdout.lock());
    writer.write_all(output.as_bytes()).unwrap();
}
