use std::io::{self, Read, Write};

const BLOCK: usize = 32; // block size of the range maximum over the node lists

struct Words {
    pool: Vec<u8>,  // all words, one after another
    off: Vec<u32>,  // word i is pool[off[i]..off[i + 1]]
}

impl Words {
    fn len(&self, i: u32) -> u32 {
        self.off[i as usize + 1] - self.off[i as usize]
    }

    fn word(&self, i: u32) -> &[u8] {
        &self.pool[self.off[i as usize] as usize..self.off[i as usize + 1] as usize]
    }

    fn common_prefix(&self, i: u32, j: u32) -> u32 {
        self.word(i).iter().zip(self.word(j)).take_while(|(x, y)| x == y).count() as u32
    }

    fn common_suffix(&self, i: u32, j: u32) -> u32 {
        let (x, y) = (self.word(i), self.word(j));
        x.iter().rev().zip(y.iter().rev()).take_while(|(p, q)| p == q).count() as u32
    }
}

// suffix tree of the words: node[off[i] + b - 1] is the node of the last b letters of word i,
// and the words below node u, by increasing number, are ids[start[u]..start[u + 1]]
struct Suffixes {
    node: Vec<u32>,
    start: Vec<u32>,
    ids: Vec<u32>,
    table: Vec<Vec<u32>>, // maxima of word lengths over blocks of ids, a sparse table over them
}

impl Suffixes {
    fn build(w: &Words) -> Suffixes {
        let n = w.off.len() as u32 - 1;
        let mut order: Vec<u32> = (0..n).collect();
        order.sort_unstable_by(|&i, &j| w.word(i).iter().rev().cmp(w.word(j).iter().rev()));
        // nodes are numbered in the order the sorted reversed words open them
        let mut node = vec![0u32; w.pool.len()];
        let mut path: Vec<u32> = vec![0];
        let mut nodes = 0u32;
        for k in 0..order.len() {
            let i = order[k];
            let common = if k > 0 { w.common_suffix(order[k - 1], i) } else { 0 };
            path.truncate(common as usize + 1);
            while path.len() <= w.len(i) as usize {
                path.push(nodes);
                nodes += 1;
            }
            let base = w.off[i as usize] as usize;
            for b in 1..=w.len(i) as usize {
                node[base + b - 1] = path[b];
            }
        }
        drop(order);
        let mut start = vec![0u32; nodes as usize + 1];
        for &u in &node {
            start[u as usize + 1] += 1;
        }
        for u in 0..nodes as usize {
            start[u + 1] += start[u];
        }
        let mut ids = vec![0u32; w.pool.len()];
        for i in 0..n {
            let base = w.off[i as usize] as usize;
            for b in 1..=w.len(i) as usize {
                let u = node[base + b - 1] as usize;
                ids[start[u] as usize] = i;
                start[u] += 1;
            }
        }
        for u in (1..=nodes as usize).rev() {
            start[u] = start[u - 1];
        }
        start[0] = 0;
        let blocks = (ids.len() + BLOCK - 1) / BLOCK;
        let maxima = ids.chunks(BLOCK).map(|c| c.iter().map(|&i| w.len(i)).max().unwrap());
        let mut table = vec![maxima.collect::<Vec<_>>()];
        let mut h = 1;
        while (1 << h) <= blocks {
            let prev = &table[h - 1];
            let row: Vec<u32> =
                (0..blocks - (1 << h) + 1).map(|k| prev[k].max(prev[k + (1 << (h - 1))])).collect();
            table.push(row);
            h += 1;
        }
        Suffixes { node, start, ids, table }
    }

    // the longest word among ids[l..r]
    fn longest(&self, w: &Words, l: usize, r: usize) -> u32 {
        if l >= r {
            return 0;
        }
        let (bl, br) = (l / BLOCK, (r - 1) / BLOCK);
        if bl == br {
            return self.ids[l..r].iter().map(|&i| w.len(i)).max().unwrap();
        }
        let mut best = self.ids[l..(bl + 1) * BLOCK].iter().map(|&i| w.len(i)).max().unwrap();
        best = best.max(self.ids[br * BLOCK..r].iter().map(|&i| w.len(i)).max().unwrap());
        if bl + 1 < br {
            let (x, y) = (bl + 1, br - 1);
            let k = (usize::BITS - 1 - (y - x + 1).leading_zeros()) as usize;
            best = best.max(self.table[k][x].max(self.table[k][y + 1 - (1 << k)]));
        }
        best
    }

    // no other word has the first a and the last b letters of word i and room for both:
    // the words with that prefix are the numbers lo..=hi
    fn unique(&self, w: &Words, i: u32, a: u32, b: u32, lo: u32, hi: u32) -> bool {
        let u = self.node[(w.off[i as usize] + b - 1) as usize] as usize;
        let (from, to) = (self.start[u] as usize, self.start[u + 1] as usize);
        let list = &self.ids[from..to];
        let l = from + list.partition_point(|&x| x < lo);
        let r = from + list.partition_point(|&x| x <= hi);
        let me = from + list.partition_point(|&x| x < i);
        self.longest(w, l, me).max(self.longest(w, me + 1, r)) < a + b
    }
}

fn main() {
    let mut input = Vec::new();
    io::stdin().read_to_end(&mut input).unwrap();
    let mut tokens = input.split(|c| c.is_ascii_whitespace()).filter(|t| !t.is_empty());
    let n: usize = std::str::from_utf8(tokens.next().unwrap()).unwrap().parse().unwrap();
    let mut w = Words { pool: Vec::new(), off: vec![0u32; n + 1] };
    for i in 0..n {
        w.pool.extend_from_slice(tokens.next().unwrap());
        w.off[i + 1] = w.pool.len() as u32;
    }
    drop(input);
    let s = Suffixes::build(&w);
    let n = n as u32;
    // last[off[i] + a - 1]: the last word sharing the first a letters of word i
    let mut last = vec![0u32; w.pool.len()];
    let mut run: Vec<u32> = Vec::new();
    for i in (0..n).rev() {
        let common = if i + 1 < n { w.common_prefix(i, i + 1) } else { 0 };
        run.truncate(common as usize + 1);
        run.resize(common as usize + 1, i);
        run.resize(w.len(i) as usize + 1, i);
        let base = w.off[i as usize] as usize;
        for a in 1..=w.len(i) as usize {
            last[base + a - 1] = run[a];
        }
    }
    drop(run);
    let mut first: Vec<u32> = Vec::new(); // first[a]: the first word sharing the first a letters
    let mut out = Vec::with_capacity(w.pool.len() * 2);
    for i in 0..n {
        let m = w.len(i);
        let before = if i > 0 { w.common_prefix(i - 1, i) } else { 0 };
        let after = if i + 1 < n { w.common_prefix(i, i + 1) } else { 0 };
        first.truncate(before as usize + 1);
        first.resize(before as usize + 1, i);
        first.resize(m as usize + 1, i);
        // the whole word costs m; the shortest unique prefix with a dot costs one more
        let (mut cost, mut kind, mut best_a, mut best_b) = (m, 0, 0, 0);
        let dot = before.max(after) + 1;
        if dot + 1 < m {
            cost = dot + 1;
            kind = 1;
            best_a = dot;
        }
        // with a hyphen: as the prefix gets shorter, the shortest unique suffix grows
        let base = w.off[i as usize];
        let mut b = 1;
        for a in (1..m).rev() {
            let (lo, hi) = (first[a as usize], last[(base + a - 1) as usize]);
            while b <= m - a && !s.unique(&w, i, a, b, lo, hi) {
                b += 1;
            }
            if b <= m - a && a + b + 1 < cost {
                cost = a + b + 1;
                kind = 2;
                best_a = a;
                best_b = b;
            }
        }
        let word = w.word(i);
        match kind {
            0 => out.extend_from_slice(word),
            1 => {
                out.extend_from_slice(&word[..best_a as usize]);
                out.push(b'.');
            }
            _ => {
                out.extend_from_slice(&word[..best_a as usize]);
                out.push(b'-');
                out.extend_from_slice(&word[(m - best_b) as usize..]);
            }
        }
        out.push(b'\n');
    }
    io::stdout().write_all(&out).unwrap();
}
