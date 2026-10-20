use std::fmt::Write as FmtWrite;
use std::io::{self, Read};

const FULL_TURN: usize = 4;
const THREE_QUARTERS: usize = FULL_TURN - 1;

struct Event {
    x: i64,
    low: i64,
    high: i64,
    index: usize,
    sign: i32,
}

fn number(data: &mut std::str::SplitWhitespace<'_>) -> i64 {
    data.next().unwrap().parse().unwrap()
}

fn prefix(tree: &[i32], mut index: usize) -> i32 {
    let mut sum = 0;
    while index > 0 {
        sum += tree[index];
        index &= index - 1;
    }
    sum
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut data = input.split_whitespace();
    let n = number(&mut data) as usize;
    let mut points = Vec::with_capacity(n);
    for _ in 0..n {
        points.push((number(&mut data), number(&mut data)));
    }
    points.sort_unstable();
    let mut ys: Vec<i64> = points.iter().map(|p| p.1).collect();
    ys.sort_unstable();
    ys.dedup();
    let q = number(&mut data) as usize;
    let mut events = Vec::with_capacity(2 * q);
    let mut answers = Vec::new();
    let (mut tx, mut ty, mut orientation) = (0, 0, 0);
    for _ in 0..q {
        let command = data.next().unwrap();
        let (mut x, mut y) = (number(&mut data), number(&mut data));
        if command != "ask" {
            let turns = match command {
                "r90" => 1,
                "r180" => 2,
                _ => THREE_QUARTERS,
            };
            let (mut dx, mut dy) = (tx - x, ty - y);
            for _ in 0..turns {
                (dx, dy) = (-dy, dx);
            }
            (tx, ty) = (x + dx, y + dy);
            orientation = (orientation + turns) % FULL_TURN;
        } else {
            let (mut xx, mut yy) = (number(&mut data), number(&mut data));
            (x, y, xx, yy) = (x - tx, y - ty, xx - tx, yy - ty);
            // Undo the global transform on two opposite corners.
            for _ in 0..orientation {
                (x, y, xx, yy) = (y, -x, yy, -xx);
            }
            if x > xx {
                std::mem::swap(&mut x, &mut xx);
            }
            if y > yy {
                std::mem::swap(&mut y, &mut yy);
            }
            let index = answers.len();
            answers.push(0);
            events.push(Event {
                x: xx,
                low: y,
                high: yy,
                index,
                sign: 1,
            });
            events.push(Event {
                x: x - 1,
                low: y,
                high: yy,
                index,
                sign: -1,
            });
        }
    }
    events.sort_unstable_by_key(|e| e.x);
    let mut tree = vec![0; ys.len() + 1];
    let mut inserted = 0;
    for event in events {
        while inserted < n && points[inserted].0 <= event.x {
            let mut index = ys.binary_search(&points[inserted].1).unwrap() + 1;
            while index < tree.len() {
                tree[index] += 1;
                index += index & index.wrapping_neg();
            }
            inserted += 1;
        }
        let low = ys.partition_point(|&y| y < event.low);
        let high = ys.partition_point(|&y| y <= event.high);
        answers[event.index] += event.sign * (prefix(&tree, high) - prefix(&tree, low));
    }
    let mut output = String::new();
    for answer in answers {
        writeln!(output, "{}", answer).unwrap();
    }
    print!("{}", output);
}
