use std::io::{self, Read};

const UNSEEN: i32 = -1;

struct Input {
    data: Vec<u8>,
    position: usize,
}

impl Input {
    fn next_int(&mut self) -> i32 {
        while self.position < self.data.len() && self.data[self.position].is_ascii_whitespace() {
            self.position += 1;
        }
        let mut sign = 1;
        if self.data[self.position] == b'-' {
            sign = UNSEEN;
            self.position += 1;
        }
        let mut value = 0;
        while self.position < self.data.len() && self.data[self.position].is_ascii_digit() {
            value = value * 10 + i32::from(self.data[self.position] - b'0');
            self.position += 1;
        }
        value * sign
    }
}

struct SegmentTree {
    size: usize,
    missing: i32,
    minimum: Vec<i32>,
    maximum: Vec<i32>,
}

impl SegmentTree {
    fn new(mate: &[usize]) -> Self {
        let size = mate.len().max(1).next_power_of_two();
        let missing = mate.len() as i32;
        let mut tree = Self {
            size,
            missing,
            minimum: vec![missing; 2 * size],
            maximum: vec![UNSEEN; 2 * size],
        };
        for (rank, &other) in mate.iter().enumerate() {
            tree.minimum[size + rank] = other as i32;
            tree.maximum[size + rank] = other as i32;
        }
        for node in (1..size).rev() {
            tree.pull(node);
        }
        tree
    }

    fn pull(&mut self, node: usize) {
        self.minimum[node] = self.minimum[2 * node].min(self.minimum[2 * node + 1]);
        self.maximum[node] = self.maximum[2 * node].max(self.maximum[2 * node + 1]);
    }

    fn remove(&mut self, position: usize) {
        let mut node = self.size + position;
        self.minimum[node] = self.missing;
        self.maximum[node] = UNSEEN;
        node /= 2;
        while node > 0 {
            self.pull(node);
            node /= 2;
        }
    }

    fn witness(&self, node: usize, left: usize, right: usize) -> Option<usize> {
        if self.minimum[node] < left as i32 {
            return Some(self.minimum[node] as usize);
        }
        if self.maximum[node] > right as i32 {
            return Some(self.maximum[node] as usize);
        }
        None
    }

    fn crossing(&self, left: usize, right: usize) -> Option<usize> {
        let mut start = self.size + left + 1;
        let mut finish = self.size + right;
        while start < finish {
            if start % 2 == 1 {
                if let Some(found) = self.witness(start, left, right) {
                    return Some(found);
                }
                start += 1;
            }
            if finish % 2 == 1 {
                finish -= 1;
                if let Some(found) = self.witness(finish, left, right) {
                    return Some(found);
                }
            }
            start /= 2;
            finish /= 2;
        }
        None
    }
}

fn location(x: i32, y: i32, width: i32, height: i32) -> i32 {
    if x < 0 || x > width || y < 0 || y > height {
        return UNSEEN;
    }
    if x == 0 || x == width || y == 0 || y == height {
        return 0;
    }
    1
}

fn perimeter(x: i32, y: i32, width: i32, height: i32) -> i32 {
    if y == 0 {
        return x;
    }
    if x == width {
        return width + y;
    }
    if y == height {
        return width + height + width - x;
    }
    2 * width + height + height - y
}

fn solve(input: &mut Input) -> bool {
    let count = input.next_int() as usize;
    let width = input.next_int();
    let height = input.next_int();
    let mut points = Vec::with_capacity(2 * count);
    let mut chords = 0;
    for _ in 0..count {
        let x1 = input.next_int();
        let y1 = input.next_int();
        let x2 = input.next_int();
        let y2 = input.next_int();
        let first = location(x1, y1, width, height);
        let second = location(x2, y2, width, height);
        if first * second == UNSEEN {
            return false;
        }
        if first == 0 && second == 0 {
            points.push((perimeter(x1, y1, width, height), chords));
            points.push((perimeter(x2, y2, width, height), chords));
            chords += 1;
        }
    }
    points.sort_unstable_by_key(|point| point.0);
    let endpoints = points.len();
    let mut owner = vec![0; endpoints];
    let mut mate = vec![0; endpoints];
    let mut left = vec![endpoints; chords];
    let mut right = vec![0; chords];
    let mut color = vec![UNSEEN; chords];
    for (rank, &(_, chord)) in points.iter().enumerate() {
        owner[rank] = chord;
        if left[chord] == endpoints {
            left[chord] = rank;
        } else {
            right[chord] = rank;
            mate[rank] = left[chord];
            mate[left[chord]] = rank;
        }
    }
    let mut tree = SegmentTree::new(&mate);
    let mut queue = Vec::with_capacity(chords);
    for root in 0..chords {
        if color[root] != UNSEEN {
            continue;
        }
        color[root] = 0;
        tree.remove(left[root]);
        tree.remove(right[root]);
        queue.clear();
        queue.push(root);
        let mut head = 0;
        while head < queue.len() {
            let chord = queue[head];
            while let Some(other) = tree.crossing(left[chord], right[chord]) {
                let next = owner[other];
                color[next] = color[chord] ^ 1;
                tree.remove(left[next]);
                tree.remove(right[next]);
                queue.push(next);
            }
            head += 1;
        }
    }
    // Chords of one color must form properly nested pairs of endpoints.
    let mut stacks = [Vec::new(), Vec::new()];
    for (rank, &chord) in owner.iter().enumerate() {
        let side = color[chord] as usize;
        if rank == left[chord] {
            stacks[side].push(chord);
        } else if stacks[side].pop() != Some(chord) {
            return false;
        }
    }
    true
}

fn main() {
    let mut data = Vec::new();
    io::stdin().read_to_end(&mut data).unwrap();
    let mut input = Input { data, position: 0 };
    println!("{}", if solve(&mut input) { "YES" } else { "NO" });
}
