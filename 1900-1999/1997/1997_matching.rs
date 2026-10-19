use std::collections::VecDeque;
use std::io::{self, Read};

const UNMATCHED: usize = usize::MAX;

struct Matcher {
    edges: Vec<Vec<usize>>,
    left: Vec<usize>,
    right: Vec<usize>,
    distance: Vec<usize>,
    cursor: Vec<usize>,
    shortest: usize,
}

impl Matcher {
    fn new(edges: Vec<Vec<usize>>) -> Self {
        let count = edges.len();
        Self {
            edges,
            left: vec![UNMATCHED; count],
            right: vec![UNMATCHED; count],
            distance: vec![UNMATCHED; count],
            cursor: vec![0; count],
            shortest: 0,
        }
    }

    fn layer(&mut self) -> bool {
        let count = self.edges.len();
        self.shortest = count + 1;
        self.distance.fill(UNMATCHED);
        self.cursor.fill(0);
        let mut queue = VecDeque::new();
        for u in 0..count {
            if self.left[u] == UNMATCHED {
                self.distance[u] = 0;
                queue.push_back(u);
            }
        }
        while let Some(u) = queue.pop_front() {
            if self.distance[u] >= self.shortest {
                continue;
            }
            for &v in &self.edges[u] {
                let mate = self.right[v];
                if mate == UNMATCHED {
                    self.shortest = self.distance[u] + 1;
                } else if self.distance[mate] == UNMATCHED {
                    self.distance[mate] = self.distance[u] + 1;
                    queue.push_back(mate);
                }
            }
        }
        self.shortest <= count
    }

    fn augment(&mut self, u: usize) -> bool {
        while self.cursor[u] < self.edges[u].len() {
            let v = self.edges[u][self.cursor[u]];
            self.cursor[u] += 1;
            let mate = self.right[v];
            if (mate == UNMATCHED && self.distance[u] + 1 == self.shortest)
                || (mate != UNMATCHED
                    && self.distance[mate] == self.distance[u] + 1
                    && self.augment(mate))
            {
                self.left[u] = v;
                self.right[v] = u;
                return true;
            }
        }
        self.distance[u] = UNMATCHED;
        false
    }
}

fn solve(a: i64, b: i64, records: &[(i64, i64)]) -> Option<Vec<(i64, i64)>> {
    let entries: Vec<i64> = records.iter().filter(|r| r.1 == 0).map(|r| r.0).collect();
    let exits: Vec<i64> = records.iter().filter(|r| r.1 == 1).map(|r| r.0).collect();
    if entries.len() != exits.len() {
        return None;
    }
    let count = entries.len();
    let mut edges = vec![Vec::new(); count];
    for (u, &entry) in entries.iter().enumerate() {
        for (v, &exit) in exits.iter().enumerate() {
            let duration = exit - entry;
            if duration > 0 && (duration <= b || duration >= a) {
                edges[u].push(v);
            }
        }
    }
    let mut h = Matcher::new(edges);
    let mut total = 0;
    while h.layer() {
        for u in 0..count {
            if h.left[u] == UNMATCHED && h.augment(u) {
                total += 1;
            }
        }
    }
    if total != count {
        return None;
    }
    Some(
        entries
            .iter()
            .enumerate()
            .map(|(u, &entry)| (entry, exits[h.left[u]]))
            .collect(),
    )
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_whitespace();
    let a: i64 = tokens.next().unwrap().parse().unwrap();
    let b: i64 = tokens.next().unwrap().parse().unwrap();
    let n: usize = tokens.next().unwrap().parse().unwrap();
    let records: Vec<(i64, i64)> = (0..n)
        .map(|_| {
            (
                tokens.next().unwrap().parse().unwrap(),
                tokens.next().unwrap().parse().unwrap(),
            )
        })
        .collect();
    match solve(a, b, &records) {
        None => println!("Liar"),
        Some(answer) => {
            let mut output = String::from("No reason\n");
            for (entry, exit) in answer {
                output.push_str(&format!("{} {}\n", entry, exit));
            }
            print!("{}", output);
        }
    }
}
