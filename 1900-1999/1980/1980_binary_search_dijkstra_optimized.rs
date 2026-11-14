use std::cmp::Ordering;
use std::collections::BinaryHeap;
use std::io::{self, BufWriter, Read, Write};

const MAX_SPEED: usize = 300;
const NO_LINK: u16 = u16::MAX;
const TOLERANCE: f64 = 1e-9;
const OUTPUT_GUARD: f64 = 1e-8;
const OUTPUT_DIGITS: usize = 12;

struct Road {
    a: u16,
    b: u16,
    speed: u16,
    length: u16,
}

struct Link {
    to: u16,
    road: u16,
    next: u16,
}

#[derive(PartialEq)]
struct State {
    time: f64,
    vertex: u16,
}

impl Eq for State {}
impl Ord for State {
    fn cmp(&self, other: &Self) -> Ordering {
        other
            .time
            .total_cmp(&self.time)
            .then_with(|| self.vertex.cmp(&other.vertex))
    }
}
impl PartialOrd for State {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        Some(self.cmp(other))
    }
}

struct Search {
    heads: Vec<u16>,
    links: Vec<Link>,
    costs: Vec<f64>,
    distance: Vec<f64>,
    parents: Vec<u16>,
    queue: BinaryHeap<State>,
}

impl Search {
    fn new(n: usize, roads: &[Road]) -> Self {
        let mut heads = vec![NO_LINK; n];
        let mut links = Vec::with_capacity(2 * roads.len());
        for (id, road) in roads.iter().enumerate() {
            for (from, to) in [(road.a, road.b), (road.b, road.a)] {
                let head = &mut heads[usize::from(from)];
                let next = *head;
                *head = links.len() as u16;
                links.push(Link {
                    to,
                    road: id as u16,
                    next,
                });
            }
        }
        Self {
            heads,
            links,
            costs: vec![0.0; roads.len()],
            distance: vec![0.0; n],
            parents: vec![0; n],
            queue: BinaryHeap::new(),
        }
    }

    fn shortest(&mut self, deadline: f64) -> f64 {
        self.distance.fill(f64::INFINITY);
        self.distance[0] = 0.0;
        self.queue.clear();
        self.queue.push(State {
            time: 0.0,
            vertex: 0,
        });
        let target = self.heads.len() - 1;
        while let Some(State { time, vertex }) = self.queue.pop() {
            let at = usize::from(vertex);
            if time != self.distance[at] {
                continue;
            }
            if at == target {
                return time;
            }
            let mut link_id = self.heads[at];
            while link_id != NO_LINK {
                let link = &self.links[usize::from(link_id)];
                let next = usize::from(link.to);
                let arrival = time + self.costs[usize::from(link.road)];
                if arrival <= deadline && arrival < self.distance[next] {
                    self.distance[next] = arrival;
                    self.parents[next] = link.road;
                    self.queue.push(State {
                        time: arrival,
                        vertex: link.to,
                    });
                }
                link_id = link.next;
            }
        }
        f64::INFINITY
    }

    fn feasible(&mut self, roads: &[Road], extra: f64, deadline: f64) -> bool {
        let mut inverse = [0.0; MAX_SPEED + 1];
        for (cost, road) in self.costs.iter_mut().zip(roads) {
            let rate = &mut inverse[usize::from(road.speed)];
            if *rate == 0.0 {
                *rate = 1.0 / (f64::from(road.speed) + extra);
            }
            *cost = f64::from(road.length) * *rate;
        }
        self.shortest(deadline) <= deadline
    }
}

fn solve(n: usize, roads: &[Road], deadline: f64) -> (f64, Vec<u16>) {
    let mut search = Search::new(n, roads);
    let mut allowance = OUTPUT_GUARD;
    if !search.feasible(roads, 0.0, deadline) {
        let mut slowest = roads[0].speed;
        let mut fastest = slowest;
        for (cost, road) in search.costs.iter_mut().zip(roads) {
            *cost = f64::from(road.length);
            slowest = slowest.min(road.speed);
            fastest = fastest.max(road.speed);
        }
        // The shortest physical route bounds the required allowance.
        let speed = search.shortest(f64::INFINITY) / deadline;
        let mut low = (speed - f64::from(fastest)).max(0.0);
        let mut high = (speed - f64::from(slowest)).max(low);
        while high - low > TOLERANCE * high.max(1.0) {
            let middle = (low + high) / 2.0;
            if search.feasible(roads, middle, deadline) {
                high = middle;
            } else {
                low = middle;
            }
        }
        allowance = high + OUTPUT_GUARD * high.max(1.0);
        assert!(search.feasible(roads, allowance, deadline));
    }
    let mut path = Vec::new();
    let mut vertex = (n - 1) as u16;
    while vertex != 0 {
        let id = search.parents[usize::from(vertex)];
        path.push(id + 1);
        let road = &roads[usize::from(id)];
        vertex ^= road.a ^ road.b;
    }
    (allowance, path)
}

fn main() -> io::Result<()> {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text)?;
    let mut input = text.split_ascii_whitespace();
    let n: usize = input.next().unwrap().parse().unwrap();
    let m: usize = input.next().unwrap().parse().unwrap();
    let mut number = || input.next().unwrap().parse::<u16>().unwrap();
    let roads: Vec<_> = (0..m)
        .map(|_| Road {
            a: number() - 1,
            b: number() - 1,
            speed: number(),
            length: number(),
        })
        .collect();
    let deadline: f64 = input.next().unwrap().parse().unwrap();
    let (extra, path) = solve(n, &roads, deadline);
    let mut output = BufWriter::new(io::stdout().lock());
    writeln!(output, "{extra:.OUTPUT_DIGITS$} {}", path.len())?;
    let mut ids = path.iter().rev();
    if let Some(id) = ids.next() {
        write!(output, "{id}")?;
        for id in ids {
            write!(output, " {id}")?;
        }
    }
    writeln!(output)?;
    output.flush()
}
