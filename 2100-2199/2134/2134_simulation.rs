use std::io::{self, Read, Write};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_ascii_whitespace();
    let height: usize = tokens.next().unwrap().parse().unwrap();
    let width: usize = tokens.next().unwrap().parse().unwrap();
    let limit: usize = tokens.next().unwrap().parse().unwrap();
    let stamp_height: usize = tokens.next().unwrap().parse().unwrap();
    let stamp_width: usize = tokens.next().unwrap().parse().unwrap();

    let mut black = Vec::new();
    for row in 0..stamp_height {
        let pattern = tokens.next().unwrap().as_bytes();
        for (column, &cell) in pattern.iter().enumerate().take(stamp_width) {
            if cell == b'#' {
                black.push(row * width + column);
            }
        }
    }

    let mut board = vec![0_u8; height * width];
    let mut uses = vec![0_u8; height * width];
    let mut repainted = 0;
    let operation_count: usize = tokens.next().unwrap().parse().unwrap();
    for operation in 1..=operation_count {
        let row: usize = tokens.next().unwrap().parse().unwrap();
        let column: usize = tokens.next().unwrap().parse().unwrap();
        let origin = (row - 1) * width + column - 1;
        if black.is_empty() || uses[origin] == 2 {
            continue;
        }
        uses[origin] += 1;
        // A third use of one placement cannot change any cell state.
        for &offset in &black {
            let cell = &mut board[origin + offset];
            if *cell == 0 {
                *cell = 1;
            } else if *cell == 1 {
                *cell = 2;
                repainted += 1;
                if repainted == limit {
                    println!("Wasted after stamp #{}", operation);
                    return;
                }
            }
        }
    }

    let mut output = Vec::with_capacity(height * (width + 1));
    for row in 0..height {
        for column in 0..width {
            output.push(if board[row * width + column] == 0 {
                b'.'
            } else {
                b'#'
            });
        }
        output.push(b'\n');
    }
    io::stdout().write_all(&output).unwrap();
}
