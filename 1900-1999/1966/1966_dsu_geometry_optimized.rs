use std::io::{self, Read};

#[derive(Clone, Copy)]
struct Point(i32, i32);

struct Track {
    first: Point,
    last: Point,
    bottom: i32,
    top: i32,
    endpoint: usize,
}

impl Track {
    fn side(&self, point: Point) -> i64 {
        i64::from(self.last.0 - self.first.0) * i64::from(point.1 - self.first.1)
            - i64::from(self.last.1 - self.first.1) * i64::from(point.0 - self.first.0)
    }

    fn crosses_line(&self, other: &Self) -> bool {
        let a = self.side(other.first);
        let b = self.side(other.last);
        (a <= 0 && b >= 0) || (b <= 0 && a >= 0)
    }
}

struct Components {
    parent: Vec<i16>,
    count: usize,
}

impl Components {
    fn root(&self, mut point: usize) -> usize {
        while self.parent[point] >= 0 {
            point = self.parent[point] as usize;
        }
        point
    }

    fn join(&mut self, mut a: usize, mut b: usize) {
        a = self.root(a);
        b = self.root(b);
        if a == b {
            return;
        }
        if self.parent[a] > self.parent[b] {
            std::mem::swap(&mut a, &mut b);
        }
        self.parent[a] += self.parent[b];
        self.parent[b] = a as i16;
        self.count -= 1;
    }
}

fn connected(points: &[Point], edges: impl Iterator<Item = (usize, usize)>) -> bool {
    let mut sets = Components {
        parent: vec![-1; points.len()],
        count: points.len(),
    };
    let mut tracks = Vec::new();
    for (a, b) in edges {
        sets.join(a, b);
        let (mut first, mut last) = (points[a], points[b]);
        if first.0 > last.0 {
            std::mem::swap(&mut first, &mut last);
        }
        tracks.push(Track {
            first,
            last,
            bottom: first.1.min(last.1),
            top: first.1.max(last.1),
            endpoint: a,
        });
    }
    if sets.count == 1 {
        return true;
    }
    tracks.sort_unstable_by_key(|track| track.first.0);

    // A mark with no endpoint can join the network only by lying on a track.
    for (vertex, &point) in points.iter().enumerate() {
        if sets.parent[vertex] != -1 {
            continue;
        }
        let track = tracks
            .iter()
            .take_while(|track| track.first.0 <= point.0)
            .find(|track| {
                point.0 <= track.last.0
                    && (track.bottom..=track.top).contains(&point.1)
                    && track.side(point) == 0
            });
        if let Some(track) = track {
            sets.join(vertex, track.endpoint);
        } else {
            return false;
        }
    }
    if sets.count == 1 {
        return true;
    }

    // Skip disjoint bounding boxes and tracks already in the same component.
    for (i, first) in tracks.iter().enumerate() {
        for second in &tracks[i + 1..] {
            if second.first.0 > first.last.0 {
                break;
            }
            if first.bottom <= second.top
                && second.bottom <= first.top
                && sets.root(first.endpoint) != sets.root(second.endpoint)
                && first.crosses_line(second)
                && second.crosses_line(first)
            {
                sets.join(first.endpoint, second.endpoint);
                if sets.count == 1 {
                    return true;
                }
            }
        }
    }
    false
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut numbers = input
        .split_ascii_whitespace()
        .map(|word| word.parse::<i32>().unwrap());
    let points = numbers.next().unwrap() as usize;
    let tracks = numbers.next().unwrap() as usize;
    let points: Vec<_> = (0..points)
        .map(|_| Point(numbers.next().unwrap(), numbers.next().unwrap()))
        .collect();
    let edges = (0..tracks).map(|_| {
        (
            numbers.next().unwrap() as usize - 1,
            numbers.next().unwrap() as usize - 1,
        )
    });
    println!(
        "{}",
        if connected(&points, edges) {
            "YES"
        } else {
            "NO"
        }
    );
}
