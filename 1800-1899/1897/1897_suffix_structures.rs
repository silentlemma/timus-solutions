use std::cmp::Ordering;
use std::io::{self, Read};

const ALPHABET: usize = 26;
const KEY_BITS: usize = 60;

fn suffix_array(text: &[u8]) -> (Vec<usize>, Vec<usize>) {
    let n = text.len();
    let mut order: Vec<usize> = (0..n).collect();
    let mut rank: Vec<usize> = text.iter().map(|&letter| letter as usize).collect();
    let mut buffer = vec![0; n];
    let mut following = vec![0; n];
    let mut largest = *rank.iter().max().unwrap();
    let mut count = vec![0; n.max(largest) + 2];
    let mut distance = 1;
    loop {
        for offset in [distance, 0] {
            count.fill(0);
            for &position in &order {
                let key = if position + offset < n {
                    rank[position + offset] + 1
                } else {
                    0
                };
                count[key] += 1;
            }
            let mut total = 0;
            for value in count.iter_mut().take(largest + 2) {
                let amount = *value;
                *value = total;
                total += amount;
            }
            for &position in &order {
                let key = if position + offset < n {
                    rank[position + offset] + 1
                } else {
                    0
                };
                buffer[count[key]] = position;
                count[key] += 1;
            }
            std::mem::swap(&mut order, &mut buffer);
        }
        let mut classes = 0;
        following[order[0]] = 0;
        for pair in order.windows(2) {
            let (a, b) = (pair[0], pair[1]);
            let tail_a = if a + distance < n {
                rank[a + distance] + 1
            } else {
                0
            };
            let tail_b = if b + distance < n {
                rank[b + distance] + 1
            } else {
                0
            };
            if rank[a] != rank[b] || tail_a != tail_b {
                classes += 1;
            }
            following[b] = classes;
        }
        std::mem::swap(&mut rank, &mut following);
        if classes + 1 == n {
            return (order, rank);
        }
        largest = classes;
        distance *= 2;
    }
}

struct SuffixIndex {
    order: Vec<usize>,
    rank: Vec<usize>,
    table: Vec<Vec<u32>>,
    logs: Vec<usize>,
}

impl SuffixIndex {
    fn new(text: &[u8]) -> Self {
        let n = text.len();
        let (order, rank) = suffix_array(text);
        let mut lcp = vec![0; n];
        let mut height = 0;
        for position in 0..n {
            let place = rank[position];
            if place == 0 {
                height = 0;
                continue;
            }
            let other = order[place - 1];
            while position + height < n
                && other + height < n
                && text[position + height] == text[other + height]
            {
                height += 1;
            }
            lcp[place] = height as u32;
            height = height.saturating_sub(1);
        }
        let mut table = vec![lcp];
        let mut span = 1;
        while 2 * span <= n {
            let previous = table.last().unwrap();
            let row = (0..n - 2 * span + 1)
                .map(|i| previous[i].min(previous[i + span]))
                .collect();
            table.push(row);
            span *= 2;
        }
        let mut logs = vec![0; n + 1];
        for i in 2..=n {
            logs[i] = logs[i / 2] + 1;
        }
        Self {
            order,
            rank,
            table,
            logs,
        }
    }

    fn lce(&self, a: usize, b: usize) -> usize {
        if a == b {
            return self.rank.len() - a;
        }
        let (mut left, mut right) = (self.rank[a], self.rank[b]);
        if left > right {
            std::mem::swap(&mut left, &mut right);
        }
        let level = self.logs[right - left];
        self.table[level][left + 1].min(self.table[level][right - (1 << level) + 1]) as usize
    }
}

struct Node {
    depth: usize,
    first: i32,
    next: i32,
    parent: i32,
    terminal: i32,
    representative: i32,
    parity: usize,
    winning: usize,
}

struct GameIndex {
    text: Vec<u8>,
    suffix: SuffixIndex,
    nodes: Vec<Node>,
    roots: Vec<usize>,
    keys: Vec<u64>,
    codes: [usize; ALPHABET],
    alphabet_size: usize,
    prefix_bits: usize,
    prefix_pairs: usize,
    counts: Vec<i32>,
    total: u64,
}

impl GameIndex {
    fn radius(&self, center: usize, parity: usize) -> usize {
        center.min(self.text.len() - center - parity)
    }

    fn common(&self, a: usize, b: usize, parity: usize) -> usize {
        let cap = self.radius(a, parity).min(self.radius(b, parity));
        if cap == 0 {
            return 0;
        }
        let edge = 2 * self.text.len() + 1;
        cap.min(self.suffix.lce(edge - a, edge - b))
            .min(self.suffix.lce(a + parity, b + parity))
    }

    fn compare(&self, a: usize, b: usize, parity: usize) -> Ordering {
        let key_order = self.keys[a].cmp(&self.keys[b]);
        if key_order != Ordering::Equal {
            return key_order;
        }
        let shared = self.common(a, b, parity);
        let (ra, rb) = (self.radius(a, parity), self.radius(b, parity));
        if shared == ra.min(rb) {
            return ra.cmp(&rb);
        }
        self.text[a - shared - 1]
            .cmp(&self.text[b - shared - 1])
            .then_with(|| self.text[a + shared + parity].cmp(&self.text[b + shared + parity]))
    }

    fn new_node(&mut self, depth: usize, parity: usize, terminal: i32) -> usize {
        let node = self.nodes.len();
        self.nodes.push(Node {
            depth,
            first: -1,
            next: -1,
            parent: -1,
            terminal,
            representative: -1,
            parity,
            winning: 0,
        });
        node
    }

    fn attach(&mut self, parent: usize, child: usize) {
        self.nodes[child].parent = parent as i32;
        self.nodes[child].next = self.nodes[parent].first;
        self.nodes[parent].first = child as i32;
    }

    fn build(&mut self, mut centers: Vec<usize>, parity: usize) {
        let root = self.new_node(0, parity, -1);
        self.roots.push(root);
        for &center in &centers {
            let mut key = 0;
            let radius = self.radius(center, parity);
            for offset in 0..self.prefix_pairs {
                key <<= self.prefix_bits;
                if offset < radius {
                    key += (self.codes[(self.text[center - offset - 1] - b'a') as usize]
                        * self.alphabet_size
                        + self.codes[(self.text[center + offset + parity] - b'a') as usize]
                        + 1) as u64;
                }
            }
            self.keys[center] = key;
        }
        centers.sort_unstable_by(|&a, &b| self.compare(a, b, parity));
        let mut stack = vec![root];
        let mut previous = None;
        for center in centers {
            let shared = previous.map_or(0, |other| self.common(other, center, parity));
            let mut last = None;
            while self.nodes[*stack.last().unwrap()].depth > shared {
                let popped = stack.pop().unwrap();
                if let Some(child) = last {
                    self.attach(popped, child);
                }
                last = Some(popped);
            }
            if self.nodes[*stack.last().unwrap()].depth < shared {
                let node = self.new_node(shared, parity, -1);
                self.attach(node, last.unwrap());
                stack.push(node);
            } else if let Some(child) = last {
                self.attach(*stack.last().unwrap(), child);
            }
            let radius = self.radius(center, parity);
            if radius > self.nodes[*stack.last().unwrap()].depth {
                let node = self.new_node(radius, parity, center as i32);
                stack.push(node);
            } else {
                let node = *stack.last().unwrap();
                let old = self.nodes[node].terminal;
                if old < 0
                    || self.suffix.rank[center - radius] < self.suffix.rank[old as usize - radius]
                {
                    self.nodes[node].terminal = center as i32;
                }
            }
            previous = Some(center);
        }
        while stack.len() > 1 {
            let child = stack.pop().unwrap();
            self.attach(*stack.last().unwrap(), child);
        }
    }

    fn new(text: Vec<u8>) -> Self {
        let n = text.len();
        let mut combined = text.clone();
        combined.push(b'#');
        combined.extend(text.iter().rev());
        let suffix = SuffixIndex::new(&combined);
        let mut present = [false; ALPHABET];
        for &letter in &text {
            present[(letter - b'a') as usize] = true;
        }
        let mut codes = [0; ALPHABET];
        let mut alphabet_size: usize = 0;
        for (i, found) in present.iter().enumerate() {
            if *found {
                codes[i] = alphabet_size;
                alphabet_size += 1;
            }
        }
        let prefix_bits = (usize::BITS - (alphabet_size * alphabet_size).leading_zeros()) as usize;
        let prefix_pairs = if alphabet_size == 1 {
            1
        } else {
            KEY_BITS / prefix_bits
        };
        let mut game = Self {
            text,
            suffix,
            nodes: Vec::new(),
            roots: Vec::new(),
            keys: vec![0; n],
            codes,
            alphabet_size,
            prefix_bits,
            prefix_pairs,
            counts: vec![0; n],
            total: 0,
        };
        game.build((1..n).collect(), 0);
        for letter in b'a'..=b'z' {
            let centers: Vec<_> = (0..n).filter(|&i| game.text[i] == letter).collect();
            if !centers.is_empty() {
                game.build(centers, 1);
            }
        }
        let mut traversal = Vec::new();
        let mut stack = game.roots.clone();
        while let Some(node) = stack.pop() {
            traversal.push(node);
            let mut child = game.nodes[node].first;
            while child >= 0 {
                stack.push(child as usize);
                child = game.nodes[child as usize].next;
            }
        }
        for &node in traversal.iter().rev() {
            let radius = game.nodes[node].depth;
            let mut best = game.nodes[node].terminal;
            let mut child = game.nodes[node].first;
            while child >= 0 {
                let item = &game.nodes[child as usize];
                let immediate = item.winning ^ ((item.depth - radius - 1) & 1);
                let center = item.representative;
                if immediate == 0 {
                    game.nodes[node].winning = 1;
                }
                if best < 0
                    || game.suffix.rank[center as usize - radius]
                        < game.suffix.rank[best as usize - radius]
                {
                    best = center;
                }
                child = game.nodes[child as usize].next;
            }
            game.nodes[node].representative = best;
        }
        let mut difference = vec![0; n + 2];
        for item in &game.nodes {
            if item.parent < 0 {
                if item.parity == 1 && item.winning == 1 {
                    let start = item.representative as usize;
                    difference[start] += 1;
                    difference[start + 2] -= 1;
                }
                continue;
            }
            let (low, high) = (game.nodes[item.parent as usize].depth + 1, item.depth);
            let center = item.representative as usize;
            let wanted = (center - ((high + 1 - item.winning) & 1)) & 1;
            let (mut left, mut right) = (center - high, center - low);
            if left & 1 != wanted {
                left += 1;
            }
            if right & 1 != wanted {
                if right == 0 {
                    continue;
                }
                right -= 1;
            }
            if left <= right {
                difference[left] += 1;
                difference[right + 2] -= 1;
            }
        }
        for i in 2..n {
            difference[i] += difference[i - 2];
        }
        game.counts.copy_from_slice(&difference[..n]);
        game.total = game.nodes[game.roots[0]].winning as u64
            + game.counts.iter().map(|&amount| amount as u64).sum::<u64>();
        game
    }

    fn kth(&self, mut k: u64) -> String {
        if k > self.total {
            return "no solution".to_owned();
        }
        if self.nodes[self.roots[0]].winning == 1 {
            if k == 1 {
                return "-".to_owned();
            }
            k -= 1;
        }
        let mut start = 0;
        for &position in &self.suffix.order {
            if position >= self.text.len() {
                continue;
            }
            if k > self.counts[position] as u64 {
                k -= self.counts[position] as u64;
            } else {
                start = position;
                break;
            }
        }
        let mut lengths = Vec::new();
        for item in &self.nodes {
            if item.parent < 0 {
                if item.parity == 1 && item.winning == 1 && item.representative as usize == start {
                    lengths.push(1);
                }
                continue;
            }
            let radius = item.representative - start as i32;
            if radius >= 0 {
                let radius = radius as usize;
                if self.nodes[item.parent as usize].depth < radius
                    && radius <= item.depth
                    && item.winning ^ ((item.depth - radius) & 1) == 1
                {
                    lengths.push(2 * radius + item.parity);
                }
            }
        }
        lengths.sort_unstable();
        String::from_utf8(self.text[start..start + lengths[k as usize - 1]].to_vec()).unwrap()
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_whitespace();
    let text = tokens.next().unwrap().as_bytes().to_vec();
    let k: u64 = tokens.next().unwrap().parse().unwrap();
    println!("{}", GameIndex::new(text).kth(k));
}
