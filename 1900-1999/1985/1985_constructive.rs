use std::fmt::Write;
use std::io::{self, Read};

const SMALL_ODD_LIMIT: usize = 5;
const FIRST_ODD_PRIME: usize = 3;
const COLUMN: usize = 2;

struct Builder {
    grid: Vec<Vec<usize>>,
    value: usize,
}

impl Builder {
    fn new(n: usize) -> Self {
        Self {
            grid: vec![vec![0; n]; n],
            value: 0,
        }
    }
    fn visit(&mut self, row: usize, col: usize) {
        self.value += 1;
        self.grid[row][col] = self.value;
    }
}

fn construct(n: usize) -> Vec<Vec<usize>> {
    let mut b = Builder::new(n);
    if n % 2 == 1 && n < SMALL_ODD_LIMIT {
        for row in 0..n {
            for step in 0..n {
                b.visit(row, if row % 2 == 0 { step } else { n - 1 - step });
            }
        }
        return b.grid;
    }
    let limit = n * n;
    let mut prime = vec![true; limit + 1];
    prime[0] = false;
    prime[1] = false;
    let mut p = 2;
    while p * p <= limit {
        if prime[p] {
            for multiple in (p * p..=limit).step_by(p) {
                prime[multiple] = false;
            }
        }
        p += 1;
    }
    let mut following = vec![0; limit + 1];
    let mut widths = vec![0; n];
    let mut largest = 0;
    for p in (0..=limit).rev() {
        following[p] = largest;
        if prime[p] {
            largest = p;
        }
    }
    if n % 2 == 0 {
        b.visit(0, 1);
        b.visit(0, 0);
        b.visit(1, 0);
        for row in (1..n - 2).step_by(2) {
            let width = (following[b.value] - b.value - 2) / 2;
            widths[row] = width;
            for col in 1..=width {
                b.visit(row, col);
            }
            b.visit(row + 1, width);
            for col in (0..width).rev() {
                b.visit(row + 1, col);
            }
            b.visit(row + 2, 0);
        }
        for col in 1..n {
            b.visit(n - 1, col);
        }
        for row in (2..n - 1).step_by(2).rev() {
            let width = widths[row - 1];
            for col in (width + 1..n).rev() {
                b.visit(row, col);
            }
            for col in width + 1..n {
                b.visit(row - 1, col);
            }
        }
        for col in (2..n).rev() {
            b.visit(0, col);
        }
        return b.grid;
    }
    let right_width = n - COLUMN - 1;
    let mut choice = None;
    for candidate in 0..=right_width {
        if candidate == right_width - 1 {
            continue;
        }
        let first = FIRST_ODD_PRIME + 2 * candidate;
        let mut current = first + 2 * n;
        if !prime[first] || !prime[current] {
            continue;
        }
        let mut valid = true;
        for row in (COLUMN + 2..n).step_by(2).rev() {
            let next_prime = following[current];
            if next_prime == 0 {
                valid = false;
                break;
            }
            let width = (next_prime - current - 2) / 2;
            if width >= right_width {
                valid = false;
                break;
            }
            widths[row] = width;
            current = next_prime;
        }
        if valid {
            choice = Some(candidate);
            break;
        }
    }
    let initial = choice.expect("No admissible prime prefix");
    b.visit(1, 1);
    b.visit(1, COLUMN);
    for col in COLUMN + 1..=COLUMN + initial {
        b.visit(1, col);
    }
    for col in (COLUMN..=COLUMN + initial).rev() {
        b.visit(0, col);
    }
    b.visit(0, 1);
    b.visit(0, 0);
    b.visit(1, 0);
    b.visit(2, 0);
    b.visit(2, 1);
    for row in (COLUMN + 1..n).step_by(2) {
        b.visit(row, 1);
        b.visit(row, 0);
        b.visit(row + 1, 0);
        b.visit(row + 1, 1);
    }
    b.visit(n - 1, COLUMN);
    for row in (COLUMN + 2..n).step_by(2).rev() {
        let width = widths[row];
        for col in COLUMN + 1..=COLUMN + width {
            b.visit(row, col);
        }
        b.visit(row - 1, COLUMN + width);
        for col in (COLUMN..COLUMN + width).rev() {
            b.visit(row - 1, col);
        }
        b.visit(row - 2, COLUMN);
    }
    let left = COLUMN + initial + 1;
    if left == n {
        for col in COLUMN + 1..n {
            b.visit(2, col);
        }
    } else {
        for col in COLUMN + 1..=left {
            b.visit(2, col);
        }
        b.visit(1, left);
        for col in left..n {
            b.visit(0, col);
        }
        for col in (left + 1..n).rev() {
            b.visit(1, col);
        }
        for col in left + 1..n {
            b.visit(2, col);
        }
    }
    for row in (COLUMN + 1..n).step_by(2) {
        let width = widths[row + 1];
        for col in (COLUMN + width + 1..n).rev() {
            b.visit(row, col);
        }
        for col in COLUMN + width + 1..n {
            b.visit(row + 1, col);
        }
    }
    b.grid
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let n = input.trim().parse().unwrap();
    let mut output = String::new();
    for row in construct(n) {
        for (col, value) in row.iter().enumerate() {
            if col > 0 {
                output.push(' ');
            }
            write!(&mut output, "{}", value).unwrap();
        }
        output.push('\n');
    }
    print!("{}", output);
}
