use std::io::{self, Read, Write};

const WHITE: i32 = 255;
const HALF: i32 = 127; // the carried error always stays within [-127, 127]

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<i32>().unwrap());
    let (n, m) = (it.next().unwrap() as usize, it.next().unwrap() as usize);
    let mut out = String::new();
    let mut res = vec![0i32; m];
    for i in 0..n {
        let row: Vec<i32> = it.by_ref().take(m).collect();
        // carry the rounding error along the row, in alternate directions so
        // that a window at either side meets short prefixes in half its rows
        let mut err = 0;
        for k in 0..m {
            let j = if i % 2 == 0 { k } else { m - 1 - k };
            err -= row[j];
            res[j] = 0;
            if err < -HALF {
                err += WHITE;
                res[j] = WHITE;
            }
        }
        let cells: Vec<String> = res.iter().map(|v| v.to_string()).collect();
        out.push_str(&cells.join(" "));
        out.push('\n');
    }
    io::stdout().write_all(out.as_bytes()).unwrap();
}
