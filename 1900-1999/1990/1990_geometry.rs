use std::io::{self, Read};

#[derive(Clone, Copy)]
struct Point {
    x: i64,
    y: i64,
}

fn vertex_clearance(vertices: &[Point], other: &[Point], sign: i64) -> f64 {
    let mut result = f64::INFINITY;
    let mut index = 0;
    for p in vertices {
        while index + 1 < other.len() && other[index + 1].y <= p.y {
            index += 1;
        }
        let gap = if index + 1 == other.len() {
            (sign * (other[index].x - p.x)) as f64
        } else {
            let a = other[index];
            let b = other[index + 1];
            let numerator = (a.x - p.x) * (b.y - p.y) + (b.x - p.x) * (p.y - a.y);
            (sign * numerator) as f64 / (b.y - a.y) as f64
        };
        result = result.min(gap);
    }
    result
}
fn fraction_at(vertices: &[Point], index: &mut usize, y: i64) -> (i64, i64) {
    while *index + 1 < vertices.len() && vertices[*index + 1].y <= y {
        *index += 1;
    }
    if *index + 1 == vertices.len() {
        return (vertices[*index].x, 1);
    }
    let a = vertices[*index];
    let b = vertices[*index + 1];
    (a.x * (b.y - y) + b.x * (y - a.y), b.y - a.y)
}
fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_ascii_whitespace();
    let mut read_wall = || {
        let count: usize = tokens.next().unwrap().parse().unwrap();
        (0..count)
            .map(|_| Point {
                x: tokens.next().unwrap().parse().unwrap(),
                y: tokens.next().unwrap().parse().unwrap(),
            })
            .collect::<Vec<_>>()
    };
    let left = read_wall();
    let right = read_wall();
    let mut answer = vertex_clearance(&left, &right, 1).min(vertex_clearance(&right, &left, -1));
    let mut first = 0;
    let mut second = 0;
    let mut process = |y: i64, group: &mut Vec<i64>| {
        if y < left[0].y || y > left[left.len() - 1].y {
            return;
        }
        let (ln, ld) = fraction_at(&left, &mut first, y);
        let (rn, rd) = fraction_at(&right, &mut second, y);
        group.sort_unstable();
        let mut previous: Option<i64> = None;
        let mut best: f64 = 0.0;
        for &x in group.iter() {
            if x * ld < ln || x * rd > rn {
                continue;
            }
            let gap = match previous {
                Some(p) => (x - p) as f64,
                None => (x * ld - ln) as f64 / ld as f64,
            };
            best = best.max(gap);
            previous = Some(x);
        }
        if let Some(p) = previous {
            best = best.max((rn - p * rd) as f64 / rd as f64);
            answer = answer.min(best);
        }
    };
    let count: usize = tokens.next().unwrap().parse().unwrap();
    let mut group = Vec::new();
    let mut current_y = 0;
    for _ in 0..count {
        let x: i64 = tokens.next().unwrap().parse().unwrap();
        let y: i64 = tokens.next().unwrap().parse().unwrap();
        if !group.is_empty() && y != current_y {
            process(current_y, &mut group);
            group.clear();
        }
        current_y = y;
        group.push(x);
    }
    if !group.is_empty() {
        process(current_y, &mut group);
    }
    println!("{:.12}", answer);
}
