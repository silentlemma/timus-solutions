use std::io::{self, Read, Write};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<i64>().unwrap());
    let n = it.next().unwrap() as usize;
    let points: Vec<(i64, i64)> = (0..n)
        .map(|_| (it.next().unwrap(), it.next().unwrap()))
        .collect();
    let extreme = |f: &dyn Fn(&(i64, i64)) -> i64| {
        let values = points.iter().map(|p| f(p));
        (values.clone().min().unwrap(), values.max().unwrap())
    };
    let (min_x, max_x) = extreme(&|p| p.0);
    let (min_y, max_y) = extreme(&|p| p.1);
    let (min_s, max_s) = extreme(&|p| p.0 + p.1);
    let (min_d, max_d) = extreme(&|p| p.0 - p.1);
    // the hull is cut out by eight lines, x, y, x + y and x - y each at
    // their extremes; going counterclockwise from the bottom edge, every
    // corner joins an axis line to a diagonal one
    let corners = [
        (min_s - min_y, min_y),
        (max_d + min_y, min_y),
        (max_x, max_x - max_d),
        (max_x, max_s - max_x),
        (max_s - max_y, max_y),
        (min_d + max_y, max_y),
        (min_x, min_x - min_d),
        (min_x, min_s - min_x),
    ];
    let mut hull: Vec<(i64, i64)> = Vec::new();
    for &p in &corners {
        if hull.last() != Some(&p) {
            hull.push(p);
        }
    }
    while hull.len() > 1 && hull[0] == hull[hull.len() - 1] {
        hull.pop();
    }
    // the sides left all point in different directions, so no corner is in
    // the middle of a straight side
    let mut out = io::BufWriter::new(io::stdout().lock());
    for (x, y) in hull {
        writeln!(out, "{} {}", x, y).unwrap();
    }
}
