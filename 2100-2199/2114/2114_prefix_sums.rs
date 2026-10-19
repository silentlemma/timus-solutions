use std::io::{self, Read, Write};

struct FastInput {
    data: Vec<u8>,
    position: usize,
}

impl FastInput {
    fn next_usize(&mut self) -> usize {
        while self.position < self.data.len() && self.data[self.position] <= b' ' {
            self.position += 1;
        }
        let mut value = 0;
        while self.position < self.data.len() && self.data[self.position] > b' ' {
            value = value * 10 + (self.data[self.position] - b'0') as usize;
            self.position += 1;
        }
        value
    }
}

fn main() {
    let mut data = Vec::new();
    io::stdin().read_to_end(&mut data).unwrap();
    let mut input = FastInput { data, position: 0 };
    let n = input.next_usize();
    let m = input.next_usize();
    let last_diagonal = n + m;
    let mut rows = vec![vec![0_i64; m + 1]; n + 1];
    let mut diagonals = vec![vec![0_i64; n + 1]; last_diagonal + 1];
    let mut total = 0;
    for row in 1..=n {
        for column in 1..=m {
            let value = input.next_usize() as i64;
            rows[row][column] = rows[row][column - 1] + value;
            diagonals[row + column][row] = value;
            total += value;
        }
    }
    for diagonal in diagonals.iter_mut().skip(2) {
        for row in 1..=n {
            diagonal[row] += diagonal[row - 1];
        }
    }

    let queries = input.next_usize();
    let mut output = String::new();
    for _ in 0..queries {
        let wind = input.next_usize();
        if wind >= last_diagonal - 2 {
            output.push_str(&format!("{} 1 1\n", total));
            continue;
        }
        let mut below = vec![0_i64; m + 1];
        let mut best = -1;
        let mut best_row = 1;
        let mut best_column = 1;
        for row in (1..=n).rev() {
            let bottom = n.min(row + wind + 1);
            for column in 1..=m {
                let right = m.min(column + wind);
                let mut value = below[column] + rows[row][right] - rows[row][column - 1];
                let sum = row + column + wind + 1;
                // Moving upward adds a row and removes the old far diagonal.
                if sum <= last_diagonal {
                    value -= diagonals[sum][bottom] - diagonals[sum][row];
                }
                below[column] = value;
                if value > best || (value == best && row < best_row) {
                    best = value;
                    best_row = row;
                    best_column = column;
                }
            }
        }
        output.push_str(&format!("{} {} {}\n", best, best_row, best_column));
    }
    io::stdout().lock().write_all(output.as_bytes()).unwrap();
}
