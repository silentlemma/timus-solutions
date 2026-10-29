use std::io::{self, BufRead};

// the numbers are parsed by hand from the locked standard input instead of
// reading the whole input into a string
fn next_int(input: &mut impl BufRead) -> i64 {
    let mut value = 0;
    let mut sign = 1;
    let mut started = false;
    loop {
        let buffer = input.fill_buf().unwrap();
        if buffer.is_empty() {
            return value * sign;
        }
        let mut consumed = 0;
        let mut finished = false;
        for &c in buffer {
            consumed += 1;
            if c == b'-' {
                sign = -1;
                started = true;
            } else if c.is_ascii_digit() {
                value = value * 10 + i64::from(c - b'0');
                started = true;
            } else if started {
                finished = true;
                break;
            }
        }
        input.consume(consumed);
        if finished {
            return value * sign;
        }
    }
}

fn main() {
    let stdin = io::stdin();
    let mut input = stdin.lock();
    let n = next_int(&mut input) as usize;
    // the matrix is one flat vector of i8: every value is between -127 and 127
    let grid: Vec<i8> = (0..n * n).map(|_| next_int(&mut input) as i8).collect();
    let mut best = i32::from(grid[0]);
    // one vector of column sums is cleared and reused for every top row
    let mut cols = vec![0; n];
    for top in 0..n {
        cols.fill(0);
        // column sums of the rows from top to bottom, then the best run of
        // neighbouring columns by Kadane's scan
        for row in grid[top * n..].chunks_exact(n) {
            let mut run = 0;
            for (column, &value) in cols.iter_mut().zip(row) {
                *column += i32::from(value);
                run = if run < 0 { *column } else { run + *column };
                best = best.max(run);
            }
        }
    }
    println!("{}", best);
}
