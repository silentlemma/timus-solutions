use std::io::{self, Read};

type Point = (i64, i64);

fn cross(a: Point, b: Point, c: Point) -> i64 {
    (b.0 - a.0) * (c.1 - a.1) - (b.1 - a.1) * (c.0 - a.0)
}
fn between(value: i64, a: i64, b: i64) -> bool {
    a.min(b) <= value && value <= a.max(b)
}
fn overlap(a: i64, b: i64, c: i64, d: i64) -> bool {
    a.min(b).max(c.min(d)) <= a.max(b).min(c.max(d))
}
fn on_segment(point: Point, a: Point, b: Point) -> bool {
    cross(a, b, point) == 0 && between(point.0, a.0, b.0) && between(point.1, a.1, b.1)
}
fn straddles(first: i64, second: i64) -> bool {
    (first <= 0 && second >= 0) || (second <= 0 && first >= 0)
}
fn intersects(a: Point, b: Point, c: Point, d: Point) -> bool {
    overlap(a.0, b.0, c.0, d.0)
        && overlap(a.1, b.1, c.1, d.1)
        && straddles(cross(a, b, c), cross(a, b, d))
        && straddles(cross(c, d, a), cross(c, d, b))
}

struct DisjointSets {
    parent: Vec<usize>,
    weights: Vec<usize>,
}
impl DisjointSets {
    fn new(size: usize) -> Self {
        Self {
            parent: (0..size).collect(),
            weights: vec![1; size],
        }
    }
    fn find(&mut self, mut vertex: usize) -> usize {
        while self.parent[vertex] != vertex {
            self.parent[vertex] = self.parent[self.parent[vertex]];
            vertex = self.parent[vertex];
        }
        vertex
    }
    fn unite(&mut self, first: usize, second: usize) {
        let (mut first, mut second) = (self.find(first), self.find(second));
        if first == second {
            return;
        }
        if self.weights[first] < self.weights[second] {
            std::mem::swap(&mut first, &mut second);
        }
        self.parent[second] = first;
        self.weights[first] += self.weights[second];
    }
}

fn all_reachable(points: &[Point], edges: &[(usize, usize)]) -> bool {
    let mut sets = DisjointSets::new(points.len());
    for &(a, b) in edges {
        sets.unite(a, b);
    }
    for (i, &(a, b)) in edges.iter().enumerate() {
        for &(c, d) in &edges[..i] {
            if intersects(points[a], points[b], points[c], points[d]) {
                sets.unite(a, c);
            }
        }
        for (vertex, &point) in points.iter().enumerate() {
            if on_segment(point, points[a], points[b]) {
                sets.unite(a, vertex);
            }
        }
    }
    let root = sets.find(0);
    (0..points.len()).all(|vertex| sets.find(vertex) == root)
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input.split_whitespace();
    let mut next = || words.next().unwrap().parse::<i64>().unwrap();
    let size = next() as usize;
    let count = next() as usize;
    let points: Vec<Point> = (0..size).map(|_| (next(), next())).collect();
    let edges: Vec<(usize, usize)> = (0..count)
        .map(|_| (next() as usize - 1, next() as usize - 1))
        .collect();
    println!(
        "{}",
        if all_reachable(&points, &edges) {
            "YES"
        } else {
            "NO"
        }
    );
}
