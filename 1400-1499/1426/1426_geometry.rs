use std::fmt::Write as _;
use std::io::{self, Read};

const POINTS: usize = 4;
const PAD: f64 = 1.0; // width given to a rectangle squeezed onto one line

/// The bounding box with sides along (dx, dy) if every point is on its border.
fn frame(p: &[(i64, i64)], dx: i64, dy: i64) -> Option<String> {
    // exact integers in the turned frame
    let us: Vec<i64> = p.iter().map(|&(x, y)| x * dx + y * dy).collect();
    let vs: Vec<i64> = p.iter().map(|&(x, y)| y * dx - x * dy).collect();
    let (lo_u, hi_u) = (*us.iter().min()?, *us.iter().max()?);
    let (lo_v, hi_v) = (*vs.iter().min()?, *vs.iter().max()?);
    if us
        .iter()
        .zip(&vs)
        .any(|(&u, &v)| u != lo_u && u != hi_u && v != lo_v && v != hi_v)
    {
        return None;
    }
    let norm = (dx as f64).hypot(dy as f64);
    // back to real lengths; a flat box gets some width, still holding every point on a side
    let (lu, mut hu) = (lo_u as f64 / norm, hi_u as f64 / norm);
    let (lv, mut hv) = (lo_v as f64 / norm, hi_v as f64 / norm);
    if hi_u == lo_u {
        hu += PAD;
    }
    if hi_v == lo_v {
        hv += PAD;
    }
    let (ex, ey) = (dx as f64 / norm, dy as f64 / norm);
    let corners = [(lu, lv), (hu, lv), (hu, hv), (lu, hv)];
    let mut out = String::from("+");
    for (u, v) in corners {
        write!(out, " {:.9} {:.9}", u * ex - v * ey, u * ey + v * ex).unwrap();
    }
    Some(out)
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input
        .split_ascii_whitespace()
        .map(|x| x.parse::<i64>().unwrap());
    let n = it.next().unwrap() as usize;
    let mut all = String::new();
    for _ in 0..n {
        let p: Vec<(i64, i64)> = (0..POINTS)
            .map(|_| (it.next().unwrap(), it.next().unwrap()))
            .collect();
        // the valid turns form a closed set whose ends make two points tie,
        // so the directions between points are enough to try
        let mut dirs = Vec::new();
        for i in 0..POINTS {
            for j in i + 1..POINTS {
                if p[i] != p[j] {
                    dirs.push((p[j].0 - p[i].0, p[j].1 - p[i].1));
                }
            }
        }
        if dirs.is_empty() {
            dirs.push((1, 0));
        }
        let line = dirs
            .iter()
            .find_map(|&(dx, dy)| frame(&p, dx, dy))
            .unwrap_or_else(|| "-".to_string());
        writeln!(all, "{}", line).unwrap();
    }
    print!("{}", all);
}
