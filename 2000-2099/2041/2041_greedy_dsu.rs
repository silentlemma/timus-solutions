use std::fmt::Write as FmtWrite;
use std::io::{self, Read};

struct Doll {
    inner: i32,
    outer: i32,
    id: u32,
}
struct Predecessor {
    parent: Vec<usize>,
    best: Vec<usize>,
    rank: Vec<u8>,
}

impl Predecessor {
    fn new(n: usize) -> Self {
        let parent: Vec<usize> = (0..=n).collect();
        Self {
            best: parent.clone(),
            parent,
            rank: vec![0; n + 1],
        }
    }
    fn find(&mut self, mut x: usize) -> usize {
        while self.parent[x] != x {
            let p = self.parent[x];
            self.parent[x] = self.parent[p];
            x = self.parent[x];
        }
        x
    }
    fn erase(&mut self, x: usize) {
        let (mut a, mut b) = (self.find(x), self.find(x - 1));
        if self.rank[a] < self.rank[b] {
            std::mem::swap(&mut a, &mut b);
        }
        self.parent[b] = a;
        self.best[a] = self.best[a].min(self.best[b]);
        if self.rank[a] == self.rank[b] {
            self.rank[a] += 1;
        }
    }
}

fn solve(mut items: Vec<Doll>) -> Option<Vec<u32>> {
    let n = items.len();
    let mut limit = items.iter().map(|item| item.outer).max().unwrap() + 1;
    items.sort_unstable_by_key(|item| (item.inner, item.outer, item.id));
    let mut available = Predecessor::new(n);
    let mut answer = Vec::with_capacity(n);
    for _ in 0..n {
        let (mut lo, mut hi) = (0, n);
        while lo < hi {
            let mid = lo + (hi - lo) / 2;
            if items[mid].inner < limit {
                lo = mid + 1;
            } else {
                hi = mid;
            }
        }
        let root = available.find(lo);
        let position = available.best[root];
        if position == 0 {
            return None;
        }
        let item = &items[position - 1];
        answer.push(item.id);
        limit = item.outer;
        available.erase(position);
    }
    Some(answer)
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_whitespace();
    let n: usize = tokens.next().unwrap().parse().unwrap();
    let items = (0..n)
        .map(|i| Doll {
            inner: tokens.next().unwrap().parse().unwrap(),
            outer: tokens.next().unwrap().parse().unwrap(),
            id: (i + 1) as u32,
        })
        .collect();
    if let Some(answer) = solve(items) {
        let mut output = String::from("Yes\n");
        for (i, id) in answer.iter().enumerate() {
            if i > 0 {
                output.push(' ');
            }
            write!(&mut output, "{}", id).unwrap();
        }
        output.push('\n');
        print!("{}", output);
    } else {
        println!("No");
    }
}
