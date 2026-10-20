use std::io::{self, Read};

const MIN_SIDE: i64 = 3;

struct Event {
    coordinate: i64,
    low: i64,
    high: i64,
    board: usize,
    kind: usize,
}

struct Dsu {
    parent: Vec<usize>,
    size: Vec<usize>,
}

impl Dsu {
    fn new(count: usize) -> Self {
        Self {
            parent: (0..count).collect(),
            size: vec![1; count],
        }
    }

    fn find(&mut self, mut board: usize) -> usize {
        while self.parent[board] != board {
            let grandparent = self.parent[self.parent[board]];
            self.parent[board] = grandparent;
            board = grandparent;
        }
        board
    }

    fn unite(&mut self, first: usize, second: usize) {
        let mut first = self.find(first);
        let mut second = self.find(second);
        if first == second {
            return;
        }
        if self.size[first] < self.size[second] {
            std::mem::swap(&mut first, &mut second);
        }
        self.parent[second] = first;
        self.size[first] += self.size[second];
    }
}

fn connect(events: &mut [Event], dsu: &mut Dsu) {
    events.sort_unstable_by_key(|event| (event.coordinate, event.low));
    let mut coordinate = None;
    let mut latest: [Option<(i64, usize)>; 2] = [None; 2];
    for event in events {
        if coordinate != Some(event.coordinate) {
            coordinate = Some(event.coordinate);
            latest = [None; 2];
        }
        // Intervals of one kind are disjoint, so only the latest one can overlap.
        if let Some((high, board)) = latest[1 - event.kind] {
            if high >= event.low {
                dsu.unite(board, event.board);
            }
        }
        latest[event.kind] = Some((event.high, event.board));
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_whitespace();
    let count: usize = tokens.next().unwrap().parse().unwrap();
    let _bound: i64 = tokens.next().unwrap().parse().unwrap();
    let start_x: i64 = tokens.next().unwrap().parse().unwrap();
    let start_y: i64 = tokens.next().unwrap().parse().unwrap();
    let mut horizontal = Vec::with_capacity(2 * count);
    let mut vertical = Vec::with_capacity(2 * count);
    let mut start = 0;
    let mut isolated = false;

    for board in 0..count {
        let left: i64 = tokens.next().unwrap().parse().unwrap();
        let bottom: i64 = tokens.next().unwrap().parse().unwrap();
        let right: i64 = tokens.next().unwrap().parse().unwrap();
        let top: i64 = tokens.next().unwrap().parse().unwrap();
        if left <= start_x && start_x < right && bottom <= start_y && start_y < top {
            start = board;
            isolated = right - left == MIN_SIDE
                && top - bottom == MIN_SIDE
                && start_x == left + 1
                && start_y == bottom + 1;
        }
        horizontal.push(Event {
            coordinate: right + 1,
            low: bottom,
            high: top,
            board,
            kind: 0,
        });
        horizontal.push(Event {
            coordinate: left,
            low: bottom,
            high: top,
            board,
            kind: 1,
        });
        vertical.push(Event {
            coordinate: top + 1,
            low: left,
            high: right,
            board,
            kind: 0,
        });
        vertical.push(Event {
            coordinate: bottom,
            low: left,
            high: right,
            board,
            kind: 1,
        });
    }

    if isolated {
        println!("1");
        return;
    }
    let mut dsu = Dsu::new(count);
    connect(&mut horizontal, &mut dsu);
    connect(&mut vertical, &mut dsu);
    let root = dsu.find(start);
    println!("{}", dsu.size[root]);
}
