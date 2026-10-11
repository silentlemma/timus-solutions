use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input.split_ascii_whitespace();
    let n: usize = words.next().unwrap().parse().unwrap();
    let rows: Vec<&[u8]> = words.take(n).map(|w| w.as_bytes()).collect();
    // runs ending at each cell of the previous and current row, going
    // down, down-right and down-left
    let (mut down, mut right, mut left) = (vec![0usize; n], vec![0usize; n], vec![0usize; n]);
    let (mut down2, mut right2, mut left2) = (vec![0usize; n], vec![0usize; n], vec![0usize; n]);
    let mut best = [0usize; 2]; // longest runs of s and of S
    for i in 0..n {
        let row = rows[i];
        let mut across = 0;
        for j in 0..n {
            let c = row[j];
            across = if j > 0 && row[j - 1] == c {
                across + 1
            } else {
                1
            };
            down2[j] = if i > 0 && rows[i - 1][j] == c {
                down[j] + 1
            } else {
                1
            };
            right2[j] = if i > 0 && j > 0 && rows[i - 1][j - 1] == c {
                right[j - 1] + 1
            } else {
                1
            };
            left2[j] = if i > 0 && j + 1 < n && rows[i - 1][j + 1] == c {
                left[j + 1] + 1
            } else {
                1
            };
            let k = (c == b'S') as usize;
            best[k] = best[k]
                .max(across)
                .max(down2[j])
                .max(right2[j])
                .max(left2[j]);
        }
        std::mem::swap(&mut down, &mut down2);
        std::mem::swap(&mut right, &mut right2);
        std::mem::swap(&mut left, &mut left2);
    }
    let winner = if best[0] > best[1] {
        "s"
    } else if best[1] > best[0] {
        "S"
    } else {
        "?"
    };
    println!("{}\n{}", winner, best[0].max(best[1]));
}
