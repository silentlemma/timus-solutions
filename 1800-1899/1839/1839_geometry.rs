use std::cmp::Ordering;
use std::io::{self, Read};

const FAR: i64 = 2; // eyes lie closer to PR than twice its length
const SIDES: usize = 6; // numbers per arc

// tan at P = height/near, at R = height/far
struct Eye {
    height: i64,
    near: i64,
    far: i64,
}

fn faces(arc: &[i64], points: &[(i64, i64)]) -> i64 {
    let mut it = arc.iter().copied();
    let mut next = || it.next().unwrap();
    let (px, py, qx, qy, rx, ry) = (next(), next(), next(), next(), next(), next());
    let (ux, uy) = (rx - px, ry - py);
    let side = ux * (qy - py) - uy * (qx - px);
    let span = ux * ux + uy * uy;
    let mut eyes = Vec::new();
    for &(x, y) in points {
        let cross = ux * (y - py) - uy * (x - px);
        let near = ux * (x - px) + uy * (y - py);
        let far = -ux * (x - rx) - uy * (y - ry);
        // across PR from Q, both base angles acute, close enough to PR
        if cross == 0 || (cross > 0) == (side > 0) || near <= 0 || far <= 0 {
            continue;
        }
        if cross.abs() >= FAR * span {
            continue;
        }
        eyes.push(Eye { height: cross.abs(), near, far });
    }
    let k = eyes.len();
    let at_r =
        |a: usize, b: usize| (eyes[a].height * eyes[b].far).cmp(&(eyes[b].height * eyes[a].far));
    let at_p =
        |a: usize, b: usize| (eyes[a].height * eyes[b].near).cmp(&(eyes[b].height * eyes[a].near));
    // ranks of the angles at R, equal angles sharing a rank
    let mut by_r: Vec<usize> = (0..k).collect();
    by_r.sort_by(|&a, &b| at_r(a, b));
    let mut rank = vec![0usize; k];
    let mut r = 0;
    for i in 0..k {
        if i > 0 && at_r(by_r[i - 1], by_r[i]) == Ordering::Less {
            r += 1;
        }
        rank[by_r[i]] = r + 1;
    }
    // the line through two eyes misses PR exactly when one eye is seen
    // higher from P and lower from R: count pairs in opposite orders
    let mut by_p: Vec<usize> = (0..k).collect();
    by_p.sort_by(|&a, &b| at_p(a, b).then(rank[a].cmp(&rank[b])));
    let mut tree = vec![0i64; k + 1];
    let mut pairs = 0i64;
    for (seen, &e) in by_p.iter().enumerate() {
        let mut below = 0;
        let mut i = rank[e];
        while i > 0 {
            below += tree[i];
            i &= i - 1;
        }
        pairs += seen as i64 - below;
        let mut i = rank[e];
        while i <= k {
            tree[i] += 1;
            i += i & i.wrapping_neg();
        }
    }
    pairs
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<i64> = input.split_ascii_whitespace().map(|t| t.parse().unwrap()).collect();
    if v.is_empty() {
        return;
    }
    let (n, m) = (v[0] as usize, v[1] as usize);
    let arcs = &v[2..2 + SIDES * n];
    let coords = &v[2 + SIDES * n..2 + SIDES * n + 2 * m];
    let points: Vec<(i64, i64)> = coords.chunks(2).map(|c| (c[0], c[1])).collect();
    let total: i64 = arcs.chunks(SIDES).map(|a| faces(a, &points)).sum();
    println!("{}", total);
}
