use std::io::{self, Read};

const AXES: usize = 3; // the row and the two diagonal strips

// the row of cell n and its two diagonal strips, from the left and from
// the right; one step across an edge changes exactly one of them
fn strips(n: i64) -> [i64; AXES] {
    let mut row = ((n - 1) as f64).sqrt() as i64;
    while row * row > n - 1 {
        row -= 1;
    }
    while (row + 1) * (row + 1) <= n - 1 {
        row += 1;
    }
    row += 1;
    let place = n - (row - 1) * (row - 1); // 1 .. 2 row - 1 within the row
    [row, (place + 1) / 2, (2 * row - place + 1) / 2]
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<i64> = input
        .split_ascii_whitespace()
        .map(|t| t.parse().unwrap())
        .collect();
    let (a, b) = (strips(v[0]), strips(v[1]));
    let total: i64 = a.iter().zip(&b).map(|(x, y)| (x - y).abs()).sum();
    println!("{}", total);
}
