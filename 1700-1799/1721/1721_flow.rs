use std::collections::BTreeMap;
use std::io::{self, BufWriter, Read, Write};

const GAP: usize = 2;
const ROLES: usize = 3;
const WRITER: usize = 0;
const TESTER: usize = 1;

#[derive(Clone, Copy)]
struct Edge {
    target: usize,
    capacity: usize,
}

struct Network {
    links: Vec<Vec<usize>>,
    edges: Vec<Edge>,
    layer: Vec<usize>,
    next: Vec<usize>,
}

impl Network {
    fn add(&mut self, from: usize, target: usize, capacity: usize) {
        let edge = self.edges.len();
        self.links[from].push(edge);
        self.links[target].push(edge ^ 1);
        self.edges.extend([
            Edge { target, capacity },
            Edge {
                target: from,
                capacity: 0,
            },
        ]);
    }

    fn layers(&mut self, sink: usize, queue: &mut Vec<usize>) -> bool {
        self.layer.fill(usize::MAX);
        self.next.fill(0);
        self.layer[0] = 0;
        queue.clear();
        queue.push(0);
        let mut head = 0;
        while head < queue.len() {
            let from = queue[head];
            head += 1;
            for &edge in &self.links[from] {
                let Edge { target, capacity } = self.edges[edge];
                if capacity > 0 && self.layer[target] == usize::MAX {
                    self.layer[target] = self.layer[from] + 1;
                    queue.push(target);
                }
            }
        }
        self.layer[sink] != usize::MAX
    }

    fn send(&mut self, from: usize, sink: usize, amount: usize) -> usize {
        if from == sink {
            return amount;
        }
        while let Some(&edge) = self.links[from].get(self.next[from]) {
            let Edge { target, capacity } = self.edges[edge];
            if capacity > 0 && self.layer[target] == self.layer[from] + 1 {
                let sent = self.send(target, sink, capacity.min(amount));
                if sent > 0 {
                    self.edges[edge].capacity -= sent;
                    self.edges[edge ^ 1].capacity += sent;
                    return sent;
                }
            }
            self.next[from] += 1;
        }
        0
    }
}

fn writes_with(writer: usize, tester: usize) -> bool {
    writer != TESTER && tester != WRITER
}

fn main() -> io::Result<()> {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input)?;
    let mut words = input.split_ascii_whitespace();
    let count = words.next().unwrap().parse().unwrap();
    let mut grouped = BTreeMap::<_, Vec<_>>::new();
    for _ in 0..count {
        let name = words.next().unwrap();
        let role = match words.next().unwrap() {
            "statements" => WRITER,
            "testdata" => TESTER,
            _ => ROLES - 1,
        };
        let rank: usize = words.next().unwrap().parse().unwrap();
        grouped.entry((rank, role)).or_default().push(name);
    }
    let mut groups = vec![((0, 0), Vec::new())];
    groups.extend(grouped);
    let indices: BTreeMap<_, _> = groups
        .iter()
        .enumerate()
        .map(|(i, &(key, _))| (key, i))
        .collect();
    let sink = groups.len();
    let mut graph = Network {
        links: vec![Vec::new(); sink + 1],
        edges: Vec::new(),
        layer: vec![0; sink + 1],
        next: vec![0; sink + 1],
    };
    // Identical ranks and roles share every possible partner. A terminal
    // capacity caps the total flow through the group at its member count.
    for (id, &((rank, role), ref names)) in groups.iter().enumerate().skip(1) {
        if rank / GAP % 2 != 0 {
            graph.add(id, sink, names.len());
            continue;
        }
        graph.add(0, id, names.len());
        for other_rank in [rank - GAP, rank + GAP] {
            for other_role in 0..ROLES {
                if writes_with(role, other_role) || writes_with(other_role, role) {
                    if let Some(&other) = indices.get(&(other_rank, other_role)) {
                        graph.add(id, other, names.len());
                    }
                }
            }
        }
    }
    let mut total = 0;
    let mut queue = Vec::with_capacity(sink + 1);
    while graph.layers(sink, &mut queue) {
        loop {
            let sent = graph.send(0, sink, count);
            if sent == 0 {
                break;
            }
            total += sent;
        }
    }
    let mut output = BufWriter::new(io::stdout().lock());
    writeln!(output, "{}", total)?;
    for id in 1..sink {
        let (rank, role) = groups[id].0;
        if rank / GAP % 2 != 0 {
            continue;
        }
        for &edge in &graph.links[id] {
            let target = graph.edges[edge].target;
            if target != 0 {
                for _ in 0..graph.edges[edge ^ 1].capacity {
                    let a = groups[id].1.pop().unwrap();
                    let b = groups[target].1.pop().unwrap();
                    let (writer, tester) = if writes_with(role, groups[target].0 .1) {
                        (a, b)
                    } else {
                        (b, a)
                    };
                    writeln!(output, "{} {}", writer, tester)?;
                }
            }
        }
    }
    output.flush()
}
