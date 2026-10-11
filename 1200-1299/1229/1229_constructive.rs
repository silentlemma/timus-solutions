use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<usize>().unwrap());
    let (n, m) = (it.next().unwrap(), it.next().unwrap());
    let first: Vec<Vec<usize>> = (0..n)
        .map(|_| (0..m).map(|_| it.next().unwrap()).collect())
        .collect();
    let mut second = vec![vec![0usize; m]; n];
    let mut label = 0;
    // cover every 2 x 2 block with two bricks: lying flat unless a brick of
    // the first layer fills its top or bottom row, and then standing, which
    // no first-layer brick can match, as that brick holds a cell of each column
    for i in (0..n).step_by(2) {
        for j in (0..m).step_by(2) {
            let flat = first[i][j] != first[i][j + 1] && first[i + 1][j] != first[i + 1][j + 1];
            let (a, b) = (label + 1, label + 2);
            label = b;
            if flat {
                second[i][j] = a;
                second[i][j + 1] = a;
                second[i + 1][j] = b;
                second[i + 1][j + 1] = b;
            } else {
                second[i][j] = a;
                second[i + 1][j] = a;
                second[i][j + 1] = b;
                second[i + 1][j + 1] = b;
            }
        }
    }
    let lines: Vec<String> = second
        .iter()
        .map(|row| {
            row.iter()
                .map(|v| v.to_string())
                .collect::<Vec<_>>()
                .join(" ")
        })
        .collect();
    println!("{}", lines.join("\n"));
}
