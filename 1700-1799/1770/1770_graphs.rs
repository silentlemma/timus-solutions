use std::io::{self, Read};

const FAR: usize = 1 << 20;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input.split_ascii_whitespace().map(|w| w.parse::<usize>().unwrap());
    let n = words.next().unwrap();
    let a: Vec<Vec<usize>> =
        (0..n).map(|_| (0..n).map(|_| words.next().unwrap()).collect()).collect();
    // every road must cost at least the table in both directions, so the
    // cheapest roads allowed are taken: a free road where the table says 0
    // both ways, a road with a board seen from i where it says 1 and 0
    let mut d = vec![vec![FAR; n]; n];
    let mut grid = vec![vec![b'0'; n]; n];
    for i in 0..n {
        d[i][i] = 0;
        for j in 0..n {
            if i != j && a[i][j] + a[j][i] <= 1 {
                d[i][j] = a[i][j];
                grid[i][j] = b'1' + a[i][j] as u8;
            }
        }
    }
    // these roads give the smallest costs any network can have, so the table
    // is right exactly when they give it
    for k in 0..n {
        let dk = d[k].clone();
        for row in d.iter_mut() {
            let dik = row[k];
            for (cell, &via) in row.iter_mut().zip(&dk) {
                if dik + via < *cell {
                    *cell = dik + via;
                }
            }
        }
    }
    if d != a {
        println!("NO");
        return;
    }
    let mut out = String::from("YES\n");
    for row in &grid {
        out.push_str(std::str::from_utf8(row).unwrap());
        out.push('\n');
    }
    print!("{}", out);
}
