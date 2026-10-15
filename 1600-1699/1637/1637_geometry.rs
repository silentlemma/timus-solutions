use std::io::{self, Read};

const CORNERS: usize = 3;
const GLIDE: u32 = 3; // a glide reflection takes three reflections
const ORDERS: [[usize; CORNERS]; 6] =
    [[0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0]];

type Point = (i64, i64);
type Line = (i64, i64, i64); // a x + b y = c

fn cross(o: Point, a: Point, b: Point) -> i64 {
    (a.0 - o.0) * (b.1 - o.1) - (a.1 - o.1) * (b.0 - o.0)
}

fn dist2(p: Point, q: Point) -> i64 {
    (p.0 - q.0).pow(2) + (p.1 - q.1).pow(2)
}

/// the line of points as far from p as from q
fn bisector(p: Point, q: Point) -> Line {
    (2 * (q.0 - p.0), 2 * (q.1 - p.1), dist2(q, (0, 0)) - dist2(p, (0, 0)))
}

fn same_line(u: Line, v: Line) -> bool {
    u.0 * v.1 == u.1 * v.0 && u.0 * v.2 == u.2 * v.0 && u.1 * v.2 == u.2 * v.1
}

/// reflections taking cur[i] to to[i], or None when no isometry does
fn moves(cur: &[Point; CORNERS], to: &[Point; CORNERS]) -> Option<u32> {
    for i in 0..CORNERS {
        for j in i + 1..CORNERS {
            if dist2(cur[i], cur[j]) != dist2(to[i], to[j]) {
                return None;
            }
        }
    }
    if cur == to {
        return Some(0);
    }
    if (cross(cur[0], cur[1], cur[2]) > 0) == (cross(to[0], to[1], to[2]) > 0) {
        return Some(2); // a rotation or a translation: two reflections
    }
    // orientation reversed: one reflection if a single mirror fits all three
    let lines: Vec<Line> =
        (0..CORNERS).filter(|&i| cur[i] != to[i]).map(|i| bisector(cur[i], to[i])).collect();
    let mirror = lines[0];
    let fits_moved = lines.iter().all(|&l| same_line(mirror, l));
    let fits_fixed = (0..CORNERS)
        .filter(|&i| cur[i] == to[i])
        .all(|i| mirror.0 * cur[i].0 + mirror.1 * cur[i].1 == mirror.2);
    Some(if fits_moved && fits_fixed { 1 } else { GLIDE })
}

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let nums: Vec<i64> = text.split_ascii_whitespace().map(|w| w.parse().unwrap()).collect();
    let mut target = [(0, 0); CORNERS];
    let mut cur = [(0, 0); CORNERS];
    for i in 0..CORNERS {
        target[i] = (nums[2 * i], nums[2 * i + 1]);
        cur[i] = (nums[2 * (CORNERS + i)], nums[2 * (CORNERS + i) + 1]);
    }
    let best = ORDERS
        .iter()
        .filter_map(|order| {
            let to = [target[order[0]], target[order[1]], target[order[2]]];
            moves(&cur, &to)
        })
        .min();
    match best {
        Some(m) => println!("{}", m),
        None => println!("IMPOSSIBLE"),
    }
}
