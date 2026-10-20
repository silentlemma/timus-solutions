use std::fmt::Write as FmtWrite;
use std::io::{self, Read, Write};

const OUTPUT_WIDTH: usize = 16;

struct Scanner {
    input: Vec<u8>,
    position: usize,
}

impl Scanner {
    fn next(&mut self) -> i64 {
        while self.input[self.position].is_ascii_whitespace() {
            self.position += 1;
        }
        let negative = self.input[self.position] == b'-';
        if negative {
            self.position += 1;
        }
        let mut value = 0;
        while self.position < self.input.len() && self.input[self.position].is_ascii_digit() {
            value = value * 10 + i64::from(self.input[self.position] - b'0');
            self.position += 1;
        }
        if negative {
            -value
        } else {
            value
        }
    }
}

fn main() {
    let mut input = Vec::new();
    io::stdin().read_to_end(&mut input).unwrap();
    let mut scanner = Scanner { input, position: 0 };
    let step_count = scanner.next() as usize;
    let query_count = scanner.next() as usize;
    let steps: Vec<i64> = (0..step_count).map(|_| scanner.next()).collect();
    let queries: Vec<i64> = (0..query_count).map(|_| scanner.next()).collect();
    let maximum = queries
        .iter()
        .map(|&value| if value < 0 { -value - 1 } else { value })
        .max()
        .unwrap() as usize;

    let mut blocks = Vec::new();
    let mut left = 0;
    let mut right = maximum;
    let mut offset = 0_i64;
    for step in steps {
        offset += if (left as i64) + offset < 0 {
            step
        } else {
            -step
        };
        if (left as i64) + offset < 0 && (right as i64) + offset >= 0 {
            let split = (-offset) as usize;
            let negatives = split - left;
            let positives = right - split + 1;
            let center = 2 * split - 1;
            // Mirror the smaller side into the side kept for later steps.
            if negatives <= positives {
                blocks.push((left, split, center));
                left = split;
            } else {
                blocks.push((split, right + 1, center));
                right = split - 1;
            }
        }
    }

    let mut answers = vec![0_i64; maximum + 1];
    for i in left..=right {
        answers[i] = i as i64 + offset;
    }
    for (begin, end, center) in blocks.into_iter().rev() {
        for i in begin..end {
            answers[i] = -answers[center - i] - 1;
        }
    }

    let mut output = String::with_capacity(query_count * OUTPUT_WIDTH);
    for value in queries {
        let answer = if value < 0 {
            -answers[(-value - 1) as usize] - 1
        } else {
            answers[value as usize]
        };
        writeln!(output, "{}", answer).unwrap();
    }
    io::stdout().lock().write_all(output.as_bytes()).unwrap();
}
