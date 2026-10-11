use std::collections::BTreeSet;
use std::io::{self, Read};

// the cells a ship may not use: rows top..bottom, columns left..right
#[derive(Clone, Copy)]
struct Zone {
    top: i64,
    bottom: i64,
    left: i64,
    right: i64,
}

// Places for a ship lying along the rows of a rows x cols board.
fn count_lines(rows: i64, cols: i64, zones: &[Zone], k: i64) -> i64 {
    let mut cuts: BTreeSet<i64> = [1, rows + 1].into_iter().collect();
    for z in zones {
        for e in [z.top, z.bottom + 1] {
            if e > 1 && e <= rows {
                cuts.insert(e);
            }
        }
    }
    let cuts: Vec<i64> = cuts.into_iter().collect();
    let mut total = 0;
    // rows between two cuts meet the same zones, so they count the same
    for pair in cuts.windows(2) {
        let top = pair[0];
        let mut spans: Vec<(i64, i64)> = zones
            .iter()
            .filter(|z| z.top <= top && top <= z.bottom)
            .map(|z| (z.left, z.right))
            .collect();
        spans.sort();
        spans.push((cols + 1, cols + 1));
        let (mut free, mut start) = (0, 1);
        for (left, right) in spans {
            if left > start {
                free += (left - start - k + 1).max(0);
            }
            start = start.max(right + 1);
        }
        total += free * (pair[1] - top);
    }
    total
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace();
    let mut next = || it.next().unwrap();
    let n: i64 = next().parse().unwrap();
    let m: i64 = next().parse().unwrap();
    let ships: usize = next().parse().unwrap();
    let mut zones = Vec::new();
    for _ in 0..ships {
        let col: i64 = next().parse().unwrap();
        let row: i64 = next().parse().unwrap();
        let size: i64 = next().parse().unwrap();
        let (bottom, right) = if next() == "V" {
            (row + size - 1, col)
        } else {
            (row, col + size - 1)
        };
        // no other ship may touch this one, even at a corner
        zones.push(Zone {
            top: row - 1,
            bottom: bottom + 1,
            left: col - 1,
            right: right + 1,
        });
    }
    let k: i64 = next().parse().unwrap();
    let mut total = count_lines(n, m, &zones, k);
    if k > 1 {
        let flipped: Vec<Zone> = zones
            .iter()
            .map(|z| Zone {
                top: z.left,
                bottom: z.right,
                left: z.top,
                right: z.bottom,
            })
            .collect();
        total += count_lines(m, n, &flipped, k);
    }
    println!("{}", total);
}
