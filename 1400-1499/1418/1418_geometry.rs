use std::io::{self, Read};

type Point = (i64, i64);

fn cross(o: Point, a: Point, b: Point) -> i64 {
    (a.0 - o.0) * (b.1 - o.1) - (a.1 - o.1) * (b.0 - o.0)
}

/// Marks the points of one monotone chain, keeping points that lie on its edges.
fn chain(p: &[Point], order: impl Iterator<Item = usize>, border: &mut [bool]) {
    let mut stack: Vec<usize> = Vec::new();
    for i in order {
        while stack.len() > 1
            && cross(p[stack[stack.len() - 2]], p[stack[stack.len() - 1]], p[i]) < 0
        {
            stack.pop();
        }
        stack.push(i);
    }
    for i in stack {
        border[i] = true;
    }
}

fn flat(p: &[Point]) -> bool {
    p.iter().all(|&q| cross(p[0], p[p.len() - 1], q) == 0)
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input
        .split_ascii_whitespace()
        .map(|x| x.parse::<i64>().unwrap());
    let n = it.next().unwrap() as usize;
    let mut points: Vec<Point> = (0..n)
        .map(|_| (it.next().unwrap(), it.next().unwrap()))
        .collect();
    points.sort();
    let mut layers = 0;
    // peel hulls with their whole border while the rest still has area
    while points.len() > 2 && !flat(&points) {
        layers += 1;
        let size = points.len();
        let mut border = vec![false; size];
        chain(&points, 0..size, &mut border);
        chain(&points, (0..size).rev(), &mut border);
        points = points
            .iter()
            .zip(&border)
            .filter(|(_, &b)| !b)
            .map(|(&p, _)| p)
            .collect();
    }
    println!("{}", layers);
}
