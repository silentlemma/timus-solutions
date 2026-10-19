use std::fmt::Write;
use std::io::{self, Read};

fn build_schedule(cannons: usize) -> Vec<Vec<usize>> {
    let size = 2 * cannons + 1;
    let mut schedule = vec![vec![0; size]; size];
    for row in 0..size {
        for column in 0..size {
            if row != column {
                schedule[row][column] = (row + column + size - 1) % size + 1;
            }
        }
    }
    schedule
}

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let cannons = text.trim().parse().unwrap();
    let mut output = String::new();
    for row in build_schedule(cannons) {
        for (column, value) in row.iter().enumerate() {
            if column > 0 {
                output.push(' ');
            }
            write!(output, "{}", value).unwrap();
        }
        output.push('\n');
    }
    print!("{}", output);
}
