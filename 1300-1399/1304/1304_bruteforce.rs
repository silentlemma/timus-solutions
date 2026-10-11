use std::io::{self, Read};

const SCALE: i64 = 100; // coordinates have at most two decimals
const DIGITS: usize = 2;
const VOLUME_CENT: i64 = SCALE * SCALE; // a hundredth of a volume unit, counted in 1 / SCALE^3

fn scaled(token: &str) -> i64 {
    let (whole, frac) = match token.find('.') {
        Some(dot) => (&token[..dot], &token[dot + 1..]),
        None => (token, ""),
    };
    let frac = format!("{}00", frac);
    let w: i64 = if whole.is_empty() {
        0
    } else {
        whole.parse().unwrap()
    };
    w * SCALE + frac[..DIGITS].parse::<i64>().unwrap()
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input.split_ascii_whitespace();
    let mut next = || words.next().unwrap();
    let (u, v, w) = (scaled(next()), scaled(next()), scaled(next()));
    let n: usize = next().parse().unwrap();
    let points: Vec<(i64, i64, i64)> = (0..n)
        .map(|_| (scaled(next()), scaled(next()), scaled(next())))
        // a point outside A can never be inside G
        .filter(|p| p.0 <= u && p.1 <= v && p.2 <= w)
        .collect();
    let mut xs: Vec<i64> = vec![0, u];
    xs.extend(points.iter().map(|p| p.0));
    xs.sort();
    xs.dedup();
    let mut best = 0i64;
    for i in 0..xs.len() {
        for j in (i + 1..xs.len()).rev() {
            let (x1, x2) = (xs[i], xs[j]);
            let width = x2 - x1;
            if width * v * w <= best {
                break; // the remaining x2 are closer still
            }
            let mut inside: Vec<(i64, i64)> = points
                .iter()
                .filter(|p| x1 < p.0 && p.0 < x2)
                .map(|p| (p.1, p.2))
                .collect();
            inside.sort();
            let m = inside.len();
            // the lower y face lies on the floor or on a point; the upper
            // face sweeps down from the top, and every point it passes
            // leaves the slab, so neighbouring z gaps merge into one
            for k in 0..=m {
                // k = 0 puts the lower face on the floor, k > 0 on point k - 1
                let y1 = if k == 0 { 0 } else { inside[k - 1].0 };
                if width * (v - y1) * w <= best {
                    break;
                }
                let first = k;
                // a point on the floor or the ceiling never splits a gap
                let mut zs: Vec<i64> = vec![0, w];
                zs.extend(
                    inside[first..]
                        .iter()
                        .map(|p| p.1)
                        .filter(|&z| 0 < z && z < w),
                );
                zs.sort();
                let size = zs.len();
                let mut prev: Vec<usize> = (0..size).map(|t| t.wrapping_sub(1)).collect();
                let mut nxt: Vec<usize> = (0..size).map(|t| t + 1).collect();
                let mut gap = zs.windows(2).map(|p| p[1] - p[0]).max().unwrap();
                let mut y2 = v;
                for q in (first..m).rev() {
                    best = best.max(width * (y2 - y1) * gap);
                    y2 = inside[q].0;
                    let z = inside[q].1;
                    if z <= 0 || z >= w {
                        continue;
                    }
                    let t = zs.binary_search(&z).unwrap();
                    let (lo, hi) = (prev[t], nxt[t]);
                    nxt[lo] = hi;
                    prev[hi] = lo;
                    gap = gap.max(zs[hi] - zs[lo]);
                }
                best = best.max(width * (y2 - y1) * gap);
            }
        }
    }
    let cents = (best + VOLUME_CENT / 2) / VOLUME_CENT;
    println!("{}.{:02}", cents / SCALE, cents % SCALE);
}
