use std::io::{self, Read, Write};

const EPS: f64 = 1e-9;
const HALF: f64 = 0.5; // a cell goes to an owner who held more than half of it
const LETTERS: usize = 26;
const STRAIGHT: f64 = 180.0; // degrees in a half turn
const CORNERS: usize = 4;
const TRIANGLE: usize = 3; // the fewest corners of a polygon with area

type Point = [f64; 2];

/// The part of a convex polygon with coordinate axis >= bound (or <=).
fn clip(poly: &[Point], axis: usize, bound: f64, keep_above: bool) -> Vec<Point> {
    let mut out = Vec::with_capacity(poly.len() + CORNERS);
    for i in 0..poly.len() {
        let (a, b) = (poly[i], poly[(i + 1) % poly.len()]);
        let (in_a, in_b) = if keep_above {
            (a[axis] >= bound - EPS, b[axis] >= bound - EPS)
        } else {
            (a[axis] <= bound + EPS, b[axis] <= bound + EPS)
        };
        if in_a != in_b {
            let t = (bound - a[axis]) / (b[axis] - a[axis]);
            out.push([a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t]);
        }
        if in_b {
            out.push(b);
        }
    }
    out
}

fn area(poly: &[Point]) -> f64 {
    let mut total = 0.0;
    for i in 0..poly.len() {
        let (a, b) = (poly[i], poly[(i + 1) % poly.len()]);
        total += a[0] * b[1] - b[0] * a[1];
    }
    total.abs() / 2.0
}

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let mut words = text.split_ascii_whitespace();
    let n: i64 = words.next().unwrap().parse().unwrap();
    let alpha: f64 = words.next().unwrap().parse().unwrap();
    let grid: Vec<&[u8]> = words.take(2 * n as usize).map(|w| w.as_bytes()).collect();
    let size = 2 * (2 * n as usize); // the new map covers twice the old side
    // owned area of each new cell, per owner letter
    let mut held = vec![[0.0f64; LETTERS]; size * size];
    let (sin_a, cos_a) = (alpha * std::f64::consts::PI / STRAIGHT).sin_cos();
    for row in 0..2 * n {
        let y = n - 1 - row;
        for col in 0..2 * n {
            let owner = grid[row as usize][col as usize];
            if owner == b'.' {
                continue;
            }
            let x = col - n;
            // the axes turn clockwise, so the cell turns counterclockwise
            let corners = [(x, y), (x + 1, y), (x + 1, y + 1), (x, y + 1)];
            let square: Vec<Point> = corners
                .iter()
                .map(|&(px, py)| {
                    let (px, py) = (px as f64, py as f64);
                    [px * cos_a - py * sin_a, px * sin_a + py * cos_a]
                })
                .collect();
            let x_lo = square.iter().map(|p| p[0]).fold(f64::INFINITY, f64::min);
            let x_hi = square.iter().map(|p| p[0]).fold(f64::NEG_INFINITY, f64::max);
            let y_lo = square.iter().map(|p| p[1]).fold(f64::INFINITY, f64::min);
            let y_hi = square.iter().map(|p| p[1]).fold(f64::NEG_INFINITY, f64::max);
            let x0 = (-2 * n).max((x_lo + EPS).floor() as i64);
            let x1 = (2 * n).min((x_hi - EPS).ceil() as i64);
            let y0 = (-2 * n).max((y_lo + EPS).floor() as i64);
            let y1 = (2 * n).min((y_hi - EPS).ceil() as i64);
            let letter = (owner - b'a') as usize;
            for gy in y0..y1 {
                for gx in x0..x1 {
                    let mut part = clip(&square, 0, gx as f64, true);
                    part = clip(&part, 0, (gx + 1) as f64, false);
                    part = clip(&part, 1, gy as f64, true);
                    part = clip(&part, 1, (gy + 1) as f64, false);
                    if part.len() >= TRIANGLE {
                        let cell = ((2 * n - 1 - gy) * size as i64 + gx + 2 * n) as usize;
                        held[cell][letter] += area(&part);
                    }
                }
            }
        }
    }
    let mut out = Vec::with_capacity(size * (size + 1));
    for r in 0..size {
        for c in 0..size {
            let best = held[r * size + c].iter().position(|&a| a > HALF + EPS);
            out.push(best.map_or(b'.', |i| b'a' + i as u8));
        }
        out.push(b'\n');
    }
    io::stdout().write_all(&out).unwrap();
}
