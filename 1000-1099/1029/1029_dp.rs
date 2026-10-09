use std::io::{self, Read};

// where the cheapest way to an office comes from
#[derive(Clone, Copy, PartialEq)]
enum From {
    Start,
    Below,
    Left,
    Right,
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<i64> = input
        .split_ascii_whitespace()
        .map(|t| t.parse().unwrap())
        .collect();
    let (m, n) = (v[0] as usize, v[1] as usize);
    let mut best: Vec<Vec<i64>> = Vec::with_capacity(m);
    let mut from: Vec<Vec<From>> = Vec::with_capacity(m);
    for i in 0..m {
        let fee = &v[2 + i * n..2 + (i + 1) * n];
        // from below first, then improve along the floor in both directions
        let (mut row, mut how) = if i == 0 {
            (fee.to_vec(), vec![From::Start; n])
        } else {
            let row = fee.iter().zip(&best[i - 1]).map(|(f, b)| f + b).collect();
            (row, vec![From::Below; n])
        };
        for j in 1..n {
            if row[j - 1] + fee[j] < row[j] {
                row[j] = row[j - 1] + fee[j];
                how[j] = From::Left;
            }
        }
        for j in (0..n - 1).rev() {
            if row[j + 1] + fee[j] < row[j] {
                row[j] = row[j + 1] + fee[j];
                how[j] = From::Right;
            }
        }
        best.push(row);
        from.push(how);
    }
    let (mut i, mut j) = (m - 1, 0);
    for k in 1..n {
        if best[i][k] < best[i][j] {
            j = k;
        }
    }
    // walk the choices back to the first floor, then print them in order
    let mut rooms = vec![j + 1];
    while from[i][j] != From::Start {
        match from[i][j] {
            From::Below => i -= 1,
            From::Left => j -= 1,
            _ => j += 1,
        }
        rooms.push(j + 1);
    }
    let words: Vec<String> = rooms.iter().rev().map(|r| r.to_string()).collect();
    println!("{}", words.join(" "));
}
