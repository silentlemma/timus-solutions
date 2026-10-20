use std::io::{self, Read, Write};

struct Scanner {
    data: Vec<u8>,
    position: usize,
}

impl Scanner {
    fn next_int(&mut self) -> i64 {
        while self.data[self.position].is_ascii_whitespace() {
            self.position += 1;
        }
        let mut value = 0;
        while self.position < self.data.len() && self.data[self.position].is_ascii_digit() {
            value = value * 10 + i64::from(self.data[self.position] - b'0');
            self.position += 1;
        }
        value
    }
}

fn main() {
    let mut data = Vec::new();
    io::stdin().read_to_end(&mut data).unwrap();
    let mut input = Scanner { data, position: 0 };
    let n = input.next_int() as usize;
    let q = input.next_int() as usize;
    let mut prefix = vec![0; n + 1];
    for value in &mut prefix[1..] {
        *value = input.next_int();
    }
    for i in 1..=n {
        prefix[i] += prefix[i - 1] - input.next_int();
    }

    let mut suffix = vec![0; n + 1];
    suffix[n] = prefix[n];
    for i in (1..n).rev() {
        suffix[i] = suffix[i + 1].min(prefix[i]);
    }

    let mut thresholds = Vec::with_capacity(n);
    let mut times = Vec::with_capacity(n);
    let mut previous_maximum = 0;
    for i in 1..=n {
        // Slowing down before this second costs the previous excess over the query.
        if suffix[i] > previous_maximum {
            thresholds.push(suffix[i]);
            times.push(i);
        }
        previous_maximum = previous_maximum.max(prefix[i]);
    }

    let stdout = io::stdout();
    let mut output = io::BufWriter::new(stdout.lock());
    for _ in 0..q {
        let distance = input.next_int();
        let mut left = 0;
        let mut right = thresholds.len();
        while left < right {
            let middle = left + (right - left) / 2;
            if thresholds[middle] <= distance {
                left = middle + 1;
            } else {
                right = middle;
            }
        }
        let answer = if left < times.len() {
            times[left] as i64
        } else {
            -1
        };
        writeln!(output, "{}", answer).unwrap();
    }
}
