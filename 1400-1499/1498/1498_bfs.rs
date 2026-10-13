use std::collections::VecDeque;
use std::io::{self, Read};

const SIDES: [(i32, i32); 4] = [(1, 0), (-1, 0), (0, 1), (0, -1)];

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<i32> = input
        .split_ascii_whitespace()
        .map(|x| x.parse().unwrap())
        .collect();
    // the field, the steps, the knight and the demon
    let [n, m, limit, x1, y1, x2, y2] = v[..] else {
        panic!("seven numbers expected")
    };
    let inside = |x: i32, y: i32| x >= 1 && x <= n && y >= 1 && y <= m && (x, y) != (x2, y2);
    // the fewest steps from the knight to every cell, around the demon
    let mut dist = vec![vec![-1i32; (m + 1) as usize]; (n + 1) as usize];
    dist[x1 as usize][y1 as usize] = 0;
    let mut queue = VecDeque::from([(x1, y1)]);
    while let Some((x, y)) = queue.pop_front() {
        for &(dx, dy) in &SIDES {
            let (nx, ny) = (x + dx, y + dy);
            if inside(nx, ny) && dist[nx as usize][ny as usize] < 0 {
                dist[nx as usize][ny as usize] = dist[x as usize][y as usize] + 1;
                queue.push_back((nx, ny));
            }
        }
    }
    // the strike comes from a cell next to the demon after a straight run of
    // k steps; its start must be reachable with the steps that are left
    let mut best = 0;
    for &(ox, oy) in &SIDES {
        let (ax, ay) = (x2 + ox, y2 + oy);
        if !inside(ax, ay) {
            continue;
        }
        for &(dx, dy) in &SIDES {
            let mut k = 0;
            loop {
                let (sx, sy) = (ax - k * dx, ay - k * dy);
                if !inside(sx, sy) {
                    break;
                }
                let d = dist[sx as usize][sy as usize];
                if d >= 0 && d + k <= limit {
                    best = best.max(k + 1);
                }
                k += 1;
            }
        }
    }
    println!("{}", best);
}
