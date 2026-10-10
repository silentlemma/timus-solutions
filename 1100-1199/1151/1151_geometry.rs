use std::collections::BTreeMap;
use std::io::{self, Read};

// beacons and control points lie on the grid from 1 to SIDE
const SIDE: i32 = 200;

// the numbers in a line, whatever separates them
fn numbers(line: &str) -> Vec<i32> {
    line.split(|c: char| !c.is_ascii_digit())
        .filter(|t| !t.is_empty())
        .map(|t| t.parse().unwrap())
        .collect()
}

// the cells at distance exactly r from (x, y) in the max metric
fn ring(x: i32, y: i32, r: i32) -> Vec<(i32, i32)> {
    if r == 0 {
        return vec![(x, y)];
    }
    let mut cells = Vec::new();
    for d in -r..=r {
        cells.push((x + d, y - r));
        cells.push((x + d, y + r));
    }
    for d in -r + 1..r {
        cells.push((x - r, y + d));
        cells.push((x + r, y + d));
    }
    cells
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut lines = input.lines().filter(|line| !line.trim().is_empty());
    let m = numbers(lines.next().unwrap())[0] as usize;
    let mut seen: BTreeMap<i32, Vec<(i32, i32, i32)>> = BTreeMap::new();
    for line in lines.take(m) {
        let nums = numbers(line);
        for pair in nums[2..].chunks(2) {
            if let [id, r] = pair {
                seen.entry(*id).or_default().push((nums[0], nums[1], *r));
            }
        }
    }
    let mut out = String::new();
    for (id, list) in &seen {
        let (x, y, r) = list[0];
        let places: Vec<(i32, i32)> = ring(x, y, r)
            .into_iter()
            .filter(|&(cx, cy)| {
                (1..=SIDE).contains(&cx)
                    && (1..=SIDE).contains(&cy)
                    && list
                        .iter()
                        .all(|&(px, py, pr)| (cx - px).abs().max((cy - py).abs()) == pr)
            })
            .collect();
        if places.len() == 1 {
            out += &format!("{}:{},{}\n", id, places[0].0, places[0].1);
        } else {
            out += &format!("{}:UNKNOWN\n", id);
        }
    }
    print!("{}", out);
}
