use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_whitespace();
    let n: usize = tokens.next().unwrap().parse().unwrap();
    let m: usize = tokens.next().unwrap().parse().unwrap();
    let a: usize = tokens.next().unwrap().parse().unwrap();
    let b: usize = tokens.next().unwrap().parse().unwrap();

    let mut row_total: i64 = 0;
    let mut column_total: i64 = 0;
    let mut selected_row: i64 = 0;
    let mut selected_column: i64 = 0;
    for index in 1..=n {
        let value: i64 = tokens.next().unwrap().parse().unwrap();
        row_total += value;
        if index == a {
            selected_row = value;
        }
    }
    for index in 1..=m {
        let value: i64 = tokens.next().unwrap().parse().unwrap();
        column_total += value;
        if index == b {
            selected_column = value;
        }
    }

    if row_total != column_total {
        println!("0");
        return;
    }
    let lower = 0.max(selected_row + selected_column - row_total);
    let upper = selected_row.min(selected_column);
    println!("{}", upper - lower + 1);
}
