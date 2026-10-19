use std::fmt::Write as FmtWrite;
use std::io::{self, Read};

fn solve(grid: &[&str], inputs: &[i32]) -> String {
    const ALPHABET: usize = 26;
    const VALUE_LIMIT: i32 = 100000;
    const TICKS: usize = 1000000;
    const DIRECTIONS: usize = 4;
    const UP: usize = 3;
    let dr = [0, 1, 0, -1];
    let dc = [1, 0, -1, 0];
    let mut memory = [0; ALPHABET];
    let (mut row, mut column, mut direction, mut current, mut cursor) = (0, 0, 0, 0, 0);
    let mut output = String::new();
    for _ in 0..TICKS {
        let op = grid[row as usize].as_bytes()[column as usize];
        match op {
            b'#' => return output,
            b'>' => direction = 0,
            b'v' => direction = 1,
            b'<' => direction = 2,
            b'^' => direction = UP,
            b'?' => {
                current = inputs[cursor];
                if cursor + 1 < inputs.len() {
                    cursor += 1;
                }
            }
            b'!' => {
                writeln!(output, "{}", current).unwrap();
                current = 0;
            }
            b'+' => current += 1,
            b'-' => current -= 1,
            b'@' => {
                direction =
                    (direction + if current == 0 { DIRECTIONS - 1 } else { 1 }) % DIRECTIONS;
            }
            b'A'..=b'Z' => {
                std::mem::swap(&mut current, &mut memory[(op - b'A') as usize]);
            }
            _ => {}
        }
        if current < -VALUE_LIMIT || current > VALUE_LIMIT {
            output.push_str("OVERFLOW ERROR\n");
            return output;
        }
        row += dr[direction];
        column += dc[direction];
        if row < 0 || row >= grid.len() as i32 || column < 0 || column >= grid[0].len() as i32 {
            output.push_str("RUNTIME ERROR\n");
            return output;
        }
    }
    output.push_str("TIME LIMIT EXCEEDED\n");
    output
}

fn read_number(token: &str) -> i32 {
    let bytes = token.as_bytes();
    let (mut sign, mut index) = (1, 0);
    if bytes[0] == b'-' || bytes[0] == b'+' {
        sign = if bytes[0] == b'-' { -1 } else { 1 };
        index += 1;
    }
    let mut value = 0;
    for &digit in &bytes[index..] {
        value = value * 10 + i32::from(digit - b'0');
    }
    sign * value
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_whitespace();
    let height = read_number(tokens.next().unwrap()) as usize;
    let _width = read_number(tokens.next().unwrap()) as usize;
    let grid: Vec<&str> = tokens.by_ref().take(height).collect();
    let count = read_number(tokens.next().unwrap()) as usize;
    let inputs: Vec<i32> = tokens.take(count).map(read_number).collect();
    print!("{}", solve(&grid, &inputs));
}
