use std::fmt::Write as _;
use std::io::{self, Read};

// the colour of the white sheet
const WHITE: usize = 1;
// colours are at most this
const COLOURS: usize = 2500;
struct Rect {
    x1: i64,
    y1: i64,
    x2: i64,
    y2: i64,
    colour: usize,
}

fn find(skip: &mut [usize], mut j: usize) -> usize {
    while skip[j] != j {
        skip[j] = skip[skip[j]];
        j = skip[j];
    }
    j
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tok = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<i64>().unwrap());
    let (width, height) = (tok.next().unwrap(), tok.next().unwrap());
    let n = tok.next().unwrap() as usize;
    let rects: Vec<Rect> = (0..n)
        .map(|_| Rect {
            x1: tok.next().unwrap(),
            y1: tok.next().unwrap(),
            x2: tok.next().unwrap(),
            y2: tok.next().unwrap(),
            colour: tok.next().unwrap() as usize,
        })
        .collect();
    let mut xs: Vec<i64> = vec![0, width];
    let mut ys: Vec<i64> = vec![0, height];
    for r in &rects {
        xs.extend([r.x1, r.x2]);
        ys.extend([r.y1, r.y2]);
    }
    xs.sort();
    xs.dedup();
    ys.sort();
    ys.dedup();
    let at = |c: i64| ys.partition_point(|&y| y < c);
    let mut area = vec![0i64; COLOURS + 1];
    let mut skip: Vec<usize> = (0..ys.len()).collect();
    for i in 0..xs.len() - 1 {
        let strip = xs[i + 1] - xs[i];
        // the top rectangles paint the cells of this strip first, and skip[j]
        // leads past painted cells to the next unpainted one
        for (j, s) in skip.iter_mut().enumerate() {
            *s = j;
        }
        let mut painted = 0;
        for r in rects.iter().rev() {
            if painted == height {
                break;
            }
            if r.x1 > xs[i] || r.x2 < xs[i + 1] {
                continue;
            }
            let hi = at(r.y2);
            let mut got = 0;
            let mut j = find(&mut skip, at(r.y1));
            while j < hi {
                got += ys[j + 1] - ys[j];
                skip[j] = j + 1;
                j = find(&mut skip, j + 1);
            }
            area[r.colour] += got * strip;
            painted += got;
        }
        area[WHITE] += (height - painted) * strip;
    }
    let mut out = String::new();
    for (c, &a) in area.iter().enumerate().skip(1) {
        if a > 0 {
            writeln!(out, "{} {}", c, a).unwrap();
        }
    }
    print!("{}", out);
}
