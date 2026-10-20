use std::fmt::Write;
use std::io::{self, Read};

struct Scanner {
    data: Vec<u8>,
    position: usize,
}

impl Scanner {
    fn next(&mut self) -> usize {
        while self.data[self.position].is_ascii_whitespace() {
            self.position += 1;
        }
        let mut value = 0;
        while self.position < self.data.len() && self.data[self.position].is_ascii_digit() {
            value = value * 10 + (self.data[self.position] - b'0') as usize;
            self.position += 1;
        }
        value
    }
}

fn main() {
    let mut data = Vec::new();
    io::stdin().read_to_end(&mut data).unwrap();
    let mut input = Scanner { data, position: 0 };
    let levels = input.next();
    let queries = input.next();
    let count = 1 << levels;
    let mut prefix = vec![0_i64; count + 1];
    for index in 0..count {
        prefix[index + 1] = prefix[index] + input.next() as i64;
    }

    let mut elapsed = Vec::with_capacity(levels + 1);
    elapsed.push(vec![0_i64; count]);
    let mut half = 1;
    for level in 1..=levels {
        let starts = count - 2 * half + 1;
        let previous = &elapsed[level - 1];
        let mut current = vec![0_i64; starts];
        for left in 0..starts {
            let difference = 2 * prefix[left + half] - prefix[left] - prefix[left + 2 * half];
            // A merge starts when both halves have finished mixing.
            current[left] = previous[left].max(previous[left + half]) + difference.abs();
        }
        elapsed.push(current);
        half *= 2;
    }

    let mut output = String::new();
    for _ in 0..queries {
        let left = input.next() - 1;
        let level = input.next();
        writeln!(output, "{}.0", elapsed[level][left]).unwrap();
    }
    print!("{output}");
}
