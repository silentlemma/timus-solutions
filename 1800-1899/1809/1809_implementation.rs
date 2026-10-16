use std::io::{self, Read};

const SIDE: i32 = 20;
const COUNT: usize = 4;
const STEPS: [(i32, i32); 4] = [(1, 0), (-1, 0), (0, 1), (0, -1)];

type Cell = (i32, i32);

// whether potatoes a and b share a line with nobody between them
fn sees(p: &[Cell], a: usize, b: usize) -> bool {
    let ((xa, ya), (xb, yb)) = (p[a], p[b]);
    if xa != xb && ya != yb {
        return false;
    }
    !p.iter().enumerate().any(|(k, &(x, y))| {
        k != a
            && k != b
            && xa.min(xb) <= x
            && x <= xa.max(xb)
            && ya.min(yb) <= y
            && y <= ya.max(yb)
    })
}

fn good(p: &[Cell]) -> bool {
    for a in 0..COUNT {
        let (x, y) = p[a];
        if x < 1 || x > SIDE || y < 1 || y > SIDE || p[..a].contains(&p[a]) {
            return false;
        }
    }
    (0..COUNT).all(|a| (0..COUNT).filter(|&b| b != a && sees(p, a, b)).count() == 1)
}

fn solve(start: &[Cell]) -> Vec<Cell> {
    if good(start) {
        return start.to_vec();
    }
    for k in 0..COUNT {
        for x in 1..=SIDE {
            for y in 1..=SIDE {
                let mut p = start.to_vec();
                p[k] = (x, y);
                if good(&p) {
                    return p;
                }
            }
        }
    }
    // two moves always do: next to the two kept potatoes, or as a pair of
    // their own in rows and columns nobody else uses
    for k in 0..COUNT {
        for l in k + 1..COUNT {
            let kept: Vec<Cell> =
                (0..COUNT).filter(|&i| i != k && i != l).map(|i| start[i]).collect();
            let near: Vec<Cell> = kept
                .iter()
                .flat_map(|&(x, y)| STEPS.iter().map(move |&(dx, dy)| (x + dx, y + dy)))
                .collect();
            let mut options: Vec<(Cell, Cell)> = Vec::new();
            for &a in near.iter() {
                for &b in near.iter() {
                    options.push((a, b));
                }
            }
            let used_x = |x: i32| kept.iter().any(|c| c.0 == x);
            let used_y = |y: i32| kept.iter().any(|c| c.1 == y);
            let fx = (1..).find(|&x| !used_x(x)).unwrap();
            let fy = (1..).find(|&y| !used_y(y) && !used_y(y + 1)).unwrap();
            options.push(((fx, fy), (fx, fy + 1)));
            for (a, b) in options {
                let mut p = start.to_vec();
                p[k] = a;
                p[l] = b;
                if good(&p) {
                    return p;
                }
            }
        }
    }
    start.to_vec()
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<i32> = input.split_ascii_whitespace().map(|x| x.parse().unwrap()).collect();
    let start: Vec<Cell> = v.chunks(2).take(COUNT).map(|c| (c[0], c[1])).collect();
    for (x, y) in solve(&start) {
        println!("{} {}", x, y);
    }
}
