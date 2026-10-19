use std::fmt::Write as FormatWrite;
use std::io::{self, Read, Write};

const DIRECTION_COUNT: usize = 4;
const LEFT_TURN: usize = 3;
const ROW_STEP: [isize; DIRECTION_COUNT] = [-1, 0, 1, 0];
const COL_STEP: [isize; DIRECTION_COUNT] = [0, 1, 0, -1];

struct Input<'a> {
    tokens: std::str::SplitWhitespace<'a>,
}

impl<'a> Input<'a> {
    fn token(&mut self) -> &'a str {
        self.tokens.next().unwrap()
    }

    fn integer(&mut self) -> usize {
        self.token().parse().unwrap()
    }
}

struct SegmentTree {
    base: usize,
    data: Vec<usize>,
}

impl SegmentTree {
    fn new(size: usize) -> Self {
        let base = size.next_power_of_two();
        Self {
            base,
            data: vec![0; base * 2],
        }
    }

    fn update(&mut self, position: usize, value: usize) {
        let mut position = position + self.base;
        while position > 0 {
            self.data[position] = value;
            position /= 2;
        }
    }

    fn query(&self, left: usize, right: usize) -> usize {
        let mut left = left + self.base;
        let mut right = right + self.base;
        let mut answer = 0;
        while left < right {
            if left % 2 == 1 {
                answer = answer.max(self.data[left]);
                left += 1;
            }
            if right % 2 == 1 {
                right -= 1;
                answer = answer.max(self.data[right]);
            }
            left /= 2;
            right /= 2;
        }
        answer
    }
}

fn lca(
    mut first: usize,
    mut second: usize,
    head: &[usize],
    parent: &[usize],
    depth: &[usize],
) -> usize {
    while head[first] != head[second] {
        if depth[head[first]] < depth[head[second]] {
            std::mem::swap(&mut first, &mut second);
        }
        first = parent[head[first]];
    }
    if depth[first] < depth[second] {
        first
    } else {
        second
    }
}

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let mut input = Input {
        tokens: text.split_whitespace(),
    };
    let n = input.integer();
    let m = input.integer();
    let mut grid = Vec::with_capacity(n * 2 - 1);
    let mut root = 0;
    for row in 0..n * 2 - 1 {
        let cells = input.token().as_bytes();
        if row % 2 == 0 {
            for col in 0..m {
                if cells[col * 2] == b'S' {
                    root = row / 2 * m + col;
                }
            }
        }
        grid.push(cells);
    }
    let count = n * m;
    let mut parent = vec![0; count];
    let mut depth = vec![0; count];
    let mut first_child = vec![count; count];
    let mut next_sibling = vec![count; count];
    let mut chosen = vec![count; count];
    let mut incoming = vec![0; count];
    let mut desired = vec![b'F'; count];
    let mut tin = vec![0; count];
    let mut size = vec![0; count];
    let mut heavy = vec![count; count];
    let mut head = vec![0; count];
    let mut endpoint = vec![0; count];
    parent[root] = root;
    let mut stack = vec![root];
    let mut order = Vec::with_capacity(count);
    while let Some(vertex) = stack.pop() {
        tin[vertex] = order.len();
        order.push(vertex);
        let row = vertex / m;
        let col = vertex % m;
        for direction in 0..DIRECTION_COUNT {
            let nr = row as isize + ROW_STEP[direction];
            let nc = col as isize + COL_STEP[direction];
            if nr < 0 || nr >= n as isize || nc < 0 || nc >= m as isize {
                continue;
            }
            let track_row = (row as isize * 2 + ROW_STEP[direction]) as usize;
            let track_col = (col as isize * 2 + COL_STEP[direction]) as usize;
            let track = grid[track_row][track_col];
            if track != b'-' && track != b'|' {
                continue;
            }
            let child = nr as usize * m + nc as usize;
            if child == parent[vertex] {
                continue;
            }
            parent[child] = vertex;
            depth[child] = depth[vertex] + 1;
            incoming[child] = direction;
            let turn = (direction + DIRECTION_COUNT - incoming[vertex]) % DIRECTION_COUNT;
            desired[child] = match turn {
                1 => b'R',
                LEFT_TURN => b'L',
                _ => b'F',
            };
            if vertex == root || desired[child] == grid[row * 2][col * 2] {
                chosen[vertex] = child;
            }
            next_sibling[child] = first_child[vertex];
            first_child[vertex] = child;
            stack.push(child);
        }
    }
    for &vertex in order.iter().rev() {
        size[vertex] = 1;
        let mut child = first_child[vertex];
        while child != count {
            size[vertex] += size[child];
            if heavy[vertex] == count || size[child] > size[heavy[vertex]] {
                heavy[vertex] = child;
            }
            child = next_sibling[child];
        }
        endpoint[vertex] = if chosen[vertex] == count {
            vertex
        } else {
            endpoint[chosen[vertex]]
        };
    }
    head[root] = root;
    for &vertex in &order {
        let mut child = first_child[vertex];
        while child != count {
            head[child] = if child == heavy[vertex] {
                head[vertex]
            } else {
                child
            };
            child = next_sibling[child];
        }
    }
    let queries = input.integer();
    let mut history = vec![0; queries + 1];
    let mut tree = SegmentTree::new(order.len());
    let mut events = Vec::new();
    let mut previous = count;
    for index in 1..=queries {
        let time = input.integer();
        let row = input.integer() - 1;
        let col = input.integer() - 1;
        let destination = row * m + col;
        history[index] = destination;
        if destination == previous {
            continue;
        }
        previous = destination;
        let mut subtree = root;
        loop {
            let latest = tree.query(tin[subtree], tin[subtree] + size[subtree]);
            let old = if latest == 0 {
                endpoint[subtree]
            } else {
                history[latest]
            };
            if old == destination {
                break;
            }
            let vertex = lca(destination, old, &head, &parent, &depth);
            let mut child = first_child[vertex];
            while tin[destination] < tin[child] || tin[destination] >= tin[child] + size[child] {
                child = next_sibling[child];
            }
            events.push((
                time + depth[vertex],
                vertex / m + 1,
                vertex % m + 1,
                desired[child],
            ));
            subtree = child;
        }
        // Every ancestor maximum becomes the newest timestamp after this update.
        tree.update(tin[destination], index);
    }
    events.sort_unstable();
    let mut output = String::new();
    writeln!(output, "{}", events.len()).unwrap();
    for (time, row, col, turn) in events {
        writeln!(output, "{} {} {} {}", time, row, col, turn as char).unwrap();
    }
    io::stdout().lock().write_all(output.as_bytes()).unwrap();
}
