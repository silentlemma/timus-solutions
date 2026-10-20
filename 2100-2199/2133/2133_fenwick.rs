use std::io::{self, Read, Write};

struct Scanner {
    input: Vec<u8>,
    position: usize,
}

impl Scanner {
    fn new() -> Self {
        let mut input = Vec::new();
        io::stdin().read_to_end(&mut input).unwrap();
        Self { input, position: 0 }
    }

    fn next(&mut self) -> usize {
        while self.position < self.input.len() && self.input[self.position].is_ascii_whitespace() {
            self.position += 1;
        }
        let mut value = 0;
        while self.position < self.input.len() && self.input[self.position].is_ascii_digit() {
            value = value * 10 + usize::from(self.input[self.position] - b'0');
            self.position += 1;
        }
        value
    }
}

struct Operation {
    index: usize,
    height: usize,
}

struct Fenwick {
    tree: Vec<i32>,
}

impl Fenwick {
    fn new(mut counts: Vec<i32>) -> Self {
        for index in 1..counts.len() {
            let parent = index + (index & index.wrapping_neg());
            if parent < counts.len() {
                let value = counts[index];
                counts[parent] += value;
            }
        }
        Self { tree: counts }
    }

    fn add(&mut self, mut index: usize, delta: i32) {
        while index < self.tree.len() {
            self.tree[index] += delta;
            index += index & index.wrapping_neg();
        }
    }

    fn prefix(&self, mut index: usize) -> i32 {
        let mut result = 0;
        while index > 0 {
            result += self.tree[index];
            index &= index - 1;
        }
        result
    }

    fn replace(&mut self, old_height: usize, new_height: usize, weight: i32) {
        if old_height != new_height {
            self.add(old_height, -weight);
            self.add(new_height, weight);
        }
    }
}

fn main() {
    let mut scanner = Scanner::new();
    let n = scanner.next();
    let mut heights: Vec<usize> = (0..n).map(|_| scanner.next()).collect();
    let mut values = heights.clone();
    let q = scanner.next();
    let mut operations = Vec::with_capacity(q);
    for _ in 0..q {
        let operation_type = scanner.next();
        let index = if operation_type == 1 {
            scanner.next()
        } else {
            0
        };
        let height = scanner.next();
        operations.push(Operation { index, height });
        values.push(height);
    }

    values.sort_unstable();
    values.dedup();
    for height in &mut heights {
        *height = values.binary_search(height).unwrap() + 1;
    }
    for operation in &mut operations {
        operation.height = values.binary_search(&operation.height).unwrap() + 1;
    }

    let mut counts = vec![0; values.len() + 1];
    for index in 0..n {
        counts[heights[index]] += 1;
        if index > 0 {
            counts[heights[index - 1].min(heights[index])] -= 1;
        }
    }
    let mut fenwick = Fenwick::new(counts);
    let mut output = Vec::new();

    // Active buildings minus active adjacent pairs equals the number of runs.
    for operation in operations {
        let height = operation.height;
        if operation.index == 0 {
            writeln!(output, "{}", 1 - fenwick.prefix(height - 1)).unwrap();
            continue;
        }

        let index = operation.index - 1;
        let old_height = heights[index];
        if old_height == height {
            continue;
        }
        fenwick.replace(old_height, height, 1);
        if index > 0 {
            fenwick.replace(
                old_height.min(heights[index - 1]),
                height.min(heights[index - 1]),
                -1,
            );
        }
        if index + 1 < n {
            fenwick.replace(
                old_height.min(heights[index + 1]),
                height.min(heights[index + 1]),
                -1,
            );
        }
        heights[index] = height;
    }

    let mut stdout = io::BufWriter::new(io::stdout().lock());
    stdout.write_all(&output).unwrap();
}
