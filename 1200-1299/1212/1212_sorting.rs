use std::io::{self, Read};

const MAX_SHIPS: usize = 30;
const MAX_LENGTH: usize = 4;
// A vertical ship excludes <=6*6 anchors, a horizontal ship <=3*9.
const MAX_ANCHORS: usize = MAX_SHIPS * (MAX_LENGTH + 2) * (MAX_LENGTH + 2);

#[derive(Clone, Copy, Default)]
struct Zone {
    top: i32,
    bottom: i32,
    left: i32,
    right: i32,
}

fn count_lines(rows: i32, cols: i32, zones: &[Zone], length: i32, flipped: bool) -> i64 {
    if cols < length {
        return 0;
    }
    let mut blocked = [0u32; MAX_ANCHORS];
    let mut used = 0;
    for source in zones {
        let z = if flipped {
            Zone {
                top: source.left,
                bottom: source.right,
                left: source.top,
                right: source.bottom,
            }
        } else {
            *source
        };
        let top = z.top.max(1);
        let bottom = z.bottom.min(rows);
        let left = (z.left - length + 1).max(1);
        let right = z.right.min(cols - length + 1);
        for row in top..=bottom {
            for col in left..=right {
                blocked[used] = ((row - 1) * cols + col - 1) as u32;
                used += 1;
            }
        }
    }
    blocked[..used].sort_unstable();
    let mut distinct = 0;
    for i in 0..used {
        if i == 0 || blocked[i] != blocked[i - 1] {
            distinct += 1;
        }
    }
    i64::from(rows) * i64::from(cols - length + 1) - distinct
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_ascii_whitespace();
    let rows: i32 = tokens.next().unwrap().parse().unwrap();
    let cols: i32 = tokens.next().unwrap().parse().unwrap();
    let ships: usize = tokens.next().unwrap().parse().unwrap();
    let mut zones = [Zone::default(); MAX_SHIPS];
    for zone in &mut zones[..ships] {
        let col: i32 = tokens.next().unwrap().parse().unwrap();
        let row: i32 = tokens.next().unwrap().parse().unwrap();
        let size: i32 = tokens.next().unwrap().parse().unwrap();
        let way = tokens.next().unwrap();
        let bottom = row + if way == "V" { size - 1 } else { 0 };
        let right = col + if way == "H" { size - 1 } else { 0 };
        *zone = Zone {
            top: row - 1,
            bottom: bottom + 1,
            left: col - 1,
            right: right + 1,
        };
    }
    let length = tokens.next().unwrap().parse().unwrap();
    let mut answer = count_lines(rows, cols, &zones[..ships], length, false);
    if length > 1 {
        answer += count_lines(cols, rows, &zones[..ships], length, true);
    }
    println!("{}", answer);
}
