use std::cmp::Ordering;
use std::collections::BinaryHeap;
use std::io::{self, Read, Write};

const SEARCH_STEPS: usize = 60;
const OUTPUT_DIGITS: usize = 12;
const SAFETY_MARGIN: f64 = 1e-8;

struct Edge {
    a: usize,
    b: usize,
    speed: usize,
    length: usize,
}

#[derive(PartialEq)]
struct State {
    time: f64,
    vertex: usize,
}
impl Eq for State {}
impl Ord for State {
    fn cmp(&self, other: &Self) -> Ordering {
        other
            .time
            .total_cmp(&self.time)
            .then_with(|| other.vertex.cmp(&self.vertex))
    }
}
impl PartialOrd for State {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        Some(self.cmp(other))
    }
}

fn solve(n: usize, edges: &[Edge], deadline: f64) -> (f64, Vec<usize>) {
    let mut graph = vec![Vec::new(); n];
    let mut total_length = 0;
    for (id, e) in edges.iter().enumerate() {
        graph[e.a].push((e.b, id));
        graph[e.b].push((e.a, id));
        total_length += e.length;
    }
    let mut parent = vec![usize::MAX; n];
    let mut shortest = |extra: f64| {
        let cost: Vec<f64> = edges
            .iter()
            .map(|e| e.length as f64 / (e.speed as f64 + extra))
            .collect();
        let mut distance = vec![f64::INFINITY; n];
        parent.fill(usize::MAX);
        distance[0] = 0.0;
        let mut queue = BinaryHeap::new();
        queue.push(State {
            time: 0.0,
            vertex: 0,
        });
        while let Some(State { time, vertex }) = queue.pop() {
            if time != distance[vertex] {
                continue;
            }
            if vertex == n - 1 {
                return true;
            }
            for &(neighbor, id) in &graph[vertex] {
                let candidate = time + cost[id];
                if candidate <= deadline && candidate < distance[neighbor] {
                    distance[neighbor] = candidate;
                    parent[neighbor] = id;
                    queue.push(State {
                        time: candidate,
                        vertex: neighbor,
                    });
                }
            }
        }
        false
    };
    let (mut low, mut high) = (0.0, 0.0);
    if !shortest(0.0) {
        high = total_length as f64 / deadline;
        for _ in 0..SEARCH_STEPS {
            let middle = (low + high) / 2.0;
            if middle == low || middle == high {
                break;
            }
            if shortest(middle) {
                high = middle;
            } else {
                low = middle;
            }
        }
        shortest(high);
    }
    let extra = high + SAFETY_MARGIN * high.max(1.0);
    let mut path = Vec::new();
    let mut vertex = n - 1;
    while vertex != 0 {
        let id = parent[vertex];
        path.push(id + 1);
        vertex = edges[id].a ^ edges[id].b ^ vertex;
    }
    path.reverse();
    (extra, path)
}

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let mut input = text.split_whitespace();
    let n: usize = match input.next() {
        Some(s) => s.parse().unwrap(),
        None => return,
    };
    let m: usize = input.next().unwrap().parse().unwrap();
    let mut edges = Vec::with_capacity(m);
    for _ in 0..m {
        edges.push(Edge {
            a: input.next().unwrap().parse::<usize>().unwrap() - 1,
            b: input.next().unwrap().parse::<usize>().unwrap() - 1,
            speed: input.next().unwrap().parse().unwrap(),
            length: input.next().unwrap().parse().unwrap(),
        });
    }
    let deadline: f64 = input.next().unwrap().parse().unwrap();
    let (extra, path) = solve(n, &edges, deadline);
    let mut out = io::BufWriter::new(io::stdout().lock());
    writeln!(
        out,
        "{:.precision$} {}",
        extra,
        path.len(),
        precision = OUTPUT_DIGITS
    )
    .unwrap();
    for (i, id) in path.iter().enumerate() {
        if i > 0 {
            write!(out, " ").unwrap();
        }
        write!(out, "{}", id).unwrap();
    }
    writeln!(out).unwrap();
}
