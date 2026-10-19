use std::collections::HashSet;
use std::io::{self, Read};

#[derive(Clone, Copy)]
struct Point {
    x: i64,
    y: i64,
}
#[derive(Clone, Copy)]
struct Edge {
    x: i64,
    y: i64,
    constant: i64,
}
struct Span {
    length: f64,
    visible: bool,
}
fn gcd(mut a: i64, mut b: i64) -> i64 {
    while b != 0 {
        let next = a % b;
        a = b;
        b = next;
    }
    a.abs()
}
fn line_span(points: &[Point], edges: &[Edge], p: Point, d: Point) -> Span {
    let n = points.len();
    let offset = d.x * p.y - d.y * p.x;
    let squared = d.x * d.x + d.y * d.y;
    let heights: Vec<i64> = points
        .iter()
        .map(|a| d.x * a.y - d.y * a.x - offset)
        .collect();
    let mut hits: Vec<f64> = Vec::new();
    let mut intervals: Vec<(f64, f64)> = Vec::new();
    let mut previous = heights[n - 1];
    for (i, &height) in heights.iter().enumerate() {
        if (previous > 0) != (height > 0) {
            let edge = edges[i];
            hits.push(
                (edge.constant - p.x * edge.y + p.y * edge.x) as f64 / (height - previous) as f64,
            );
        } else if height == 0 && previous == 0 {
            let (a, b) = (points[(i + n - 1) % n], points[i]);
            let first = ((a.x - p.x) * d.x + (a.y - p.y) * d.y) as f64 / squared as f64;
            let second = ((b.x - p.x) * d.x + (b.y - p.y) * d.y) as f64 / squared as f64;
            intervals.push((first.min(second), first.max(second)));
        }
        previous = height;
    }
    hits.sort_by(f64::total_cmp);
    for pair in hits.chunks_exact(2) {
        intervals.push((pair[0], pair[1]));
    }
    if intervals.is_empty() {
        return Span {
            length: 0.0,
            visible: false,
        };
    }
    intervals.sort_by(|a, b| a.0.total_cmp(&b.0).then(a.1.total_cmp(&b.1)));
    let (mut left, mut right) = intervals[0];
    let (mut best, mut visible) = (0.0_f64, false);
    for &(start, end) in &intervals[1..] {
        if start <= right {
            right = right.max(end);
        } else {
            best = best.max(right - left);
            visible |= left <= 0.0 && right >= 1.0;
            left = start;
            right = end;
        }
    }
    Span {
        length: best.max(right - left),
        visible: visible || (left <= 0.0 && right >= 1.0),
    }
}
fn longest_segment(points: &[Point]) -> f64 {
    let n = points.len();
    let mut edges: Vec<Edge> = Vec::new();
    let (mut lower, mut diameter) = (0_i64, 0_i64);
    let (mut min_x, mut max_x) = (points[0].x, points[0].x);
    let (mut min_y, mut max_y) = (points[0].y, points[0].y);
    let mut endpoint = points[0];
    let mut direction = Point { x: 0, y: 0 };
    for (i, &p) in points.iter().enumerate() {
        let a = points[(i + n - 1) % n];
        let edge = Edge {
            x: p.x - a.x,
            y: p.y - a.y,
            constant: a.x * p.y - a.y * p.x,
        };
        lower = lower.max(edge.x * edge.x + edge.y * edge.y);
        edges.push(edge);
        min_x = min_x.min(p.x);
        max_x = max_x.max(p.x);
        min_y = min_y.min(p.y);
        max_y = max_y.max(p.y);
        for q in &points[..i] {
            let (dx, dy) = (q.x - p.x, q.y - p.y);
            let squared = dx * dx + dy * dy;
            if squared > diameter {
                diameter = squared;
                endpoint = p;
                direction = Point { x: dx, y: dy };
            }
        }
    }
    let initial = line_span(points, &edges, endpoint, direction);
    if initial.visible {
        return (diameter as f64).sqrt();
    }
    let mut best = (lower as f64).max(initial.length * initial.length * diameter as f64);
    let width_squared = (max_x - min_x) * (max_x - min_x);
    let height_squared = (max_y - min_y) * (max_y - min_y);
    let mut seen = HashSet::new();
    for (i, &p) in points.iter().enumerate() {
        for q in &points[..i] {
            let (dx, dy) = (q.x - p.x, q.y - p.y);
            let squared = dx * dx + dy * dy;
            if width_squared * squared < lower * dx * dx
                || height_squared * squared < lower * dy * dy
            {
                continue;
            }
            let divisor = gcd(dx, dy);
            let (mut nx, mut ny) = (dx / divisor, dy / divisor);
            if nx < 0 || (nx == 0 && ny < 0) {
                nx = -nx;
                ny = -ny;
            }
            if !seen.insert((nx, ny, nx * p.y - ny * p.x)) {
                continue;
            }
            let current = line_span(points, &edges, p, Point { x: dx, y: dy });
            if current.visible {
                lower = lower.max(squared);
                if lower == diameter {
                    return (diameter as f64).sqrt();
                }
            }
            best = best
                .max(current.length * current.length * squared as f64)
                .max(lower as f64);
        }
    }
    best.sqrt()
}
fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let mut words = text.split_whitespace();
    let n: usize = words.next().unwrap().parse().unwrap();
    let points: Vec<Point> = (0..n)
        .map(|_| Point {
            x: words.next().unwrap().parse().unwrap(),
            y: words.next().unwrap().parse().unwrap(),
        })
        .collect();
    println!("{:.12}", longest_segment(&points));
}
