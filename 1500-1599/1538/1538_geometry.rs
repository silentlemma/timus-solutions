use std::io::{self, Read};

const ENOUGH: usize = 9; // any 9 points, no three on a line, hold a convex pentagon
const SIDES: usize = 5;

#[derive(Clone, Copy)]
struct Point {
    x: i64,
    y: i64,
    id: usize,
}

fn cross(o: Point, a: Point, b: Point) -> i64 {
    (a.x - o.x) * (b.y - o.y) - (a.y - o.y) * (b.x - o.x)
}

/// The convex hull of the points, counterclockwise.
fn hull(mut points: Vec<Point>) -> Vec<Point> {
    points.sort_by_key(|p| (p.x, p.y));
    let mut h: Vec<Point> = Vec::new();
    for _ in 0..2 {
        let start = h.len();
        for &p in &points {
            while h.len() >= start + 2 && cross(h[h.len() - 2], h[h.len() - 1], p) <= 0 {
                h.pop();
            }
            h.push(p);
        }
        h.pop();
        points.reverse();
    }
    h
}

fn main() {
    let mut s = String::new();
    io::stdin().read_to_string(&mut s).unwrap();
    let mut it = s
        .split_ascii_whitespace()
        .map(|x| x.parse::<i64>().unwrap());
    let n = it.next().unwrap() as usize;
    // by the Erdos-Szekeres theorem the first nine points are enough
    let m = n.min(ENOUGH);
    let points: Vec<Point> = (0..m)
        .map(|i| Point {
            x: it.next().unwrap(),
            y: it.next().unwrap(),
            id: i + 1,
        })
        .collect();
    for mask in 0usize..1 << m {
        if mask.count_ones() as usize != SIDES {
            continue;
        }
        let five: Vec<Point> = (0..m)
            .filter(|&i| mask >> i & 1 == 1)
            .map(|i| points[i])
            .collect();
        let h = hull(five);
        if h.len() == SIDES {
            let ids: Vec<String> = h.iter().map(|p| p.id.to_string()).collect();
            println!("Yes\n{}", ids.join(" "));
            return;
        }
    }
    println!("No");
}
