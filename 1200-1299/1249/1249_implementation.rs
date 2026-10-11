use std::io::{self, BufReader, Read};

const THREE: u8 = 3;

fn main() {
    let stdin = io::stdin();
    let mut bytes = BufReader::new(stdin.lock()).bytes().map(|b| b.unwrap());
    let mut first = String::new();
    // the first line holds N and M; the cells follow byte by byte
    for b in bytes.by_ref() {
        if b == b'\n' {
            break;
        }
        first.push(b as char);
    }
    let v: Vec<usize> = first
        .split_ascii_whitespace()
        .map(|t| t.parse().unwrap())
        .collect();
    let (n, m) = (v[0], v[1]);
    // every dark region is a rectangle exactly when no 2 x 2 window holds
    // three dark cells, so two rows are enough, and the image never fits in
    // 4 MB anyway
    let (mut prev, mut cur) = (vec![0u8; m], vec![0u8; m]);
    let mut cells = bytes.filter(|&b| b == b'0' || b == b'1').map(|b| b - b'0');
    for i in 0..n {
        for j in 0..m {
            cur[j] = cells.next().unwrap();
            if i > 0 && j > 0 && prev[j - 1] + prev[j] + cur[j - 1] + cur[j] == THREE {
                println!("No");
                return;
            }
        }
        std::mem::swap(&mut prev, &mut cur);
    }
    println!("Yes");
}
