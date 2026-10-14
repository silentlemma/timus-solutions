use std::cmp::Reverse;
use std::collections::{BTreeMap, BinaryHeap, HashSet};
use std::io::{self, Read};

/// Every piece that can ever appear is a maximal run of rings above some
/// content; such runs nest, and the children of a run are the runs above its
/// smallest content.
struct Chain {
    rings: Vec<usize>,
    low: Vec<usize>,
    grundy: Vec<usize>,
    children: Vec<Vec<usize>>,
}

impl Chain {
    fn build(&mut self, left: usize, right: usize) -> usize {
        let node = self.low.len();
        let m = *self.rings[left..=right].iter().min().unwrap();
        self.low.push(m);
        self.children.push(Vec::new());
        self.grundy.push(0);
        let mut i = left;
        while i <= right {
            if self.rings[i] > m {
                let mut j = i;
                while j < right && self.rings[j + 1] > m {
                    j += 1;
                }
                let child = self.build(i, j);
                self.children[node].push(child);
                i = j;
            }
            i += 1;
        }
        node
    }

    /// {x: xor of the pieces left by removing rings up to x} in node.
    fn after_moves(&self, node: usize) -> BTreeMap<usize, usize> {
        let mut result = BTreeMap::new();
        let mut heap = BinaryHeap::new();
        let mut x = 0;
        for &c in &self.children[node] {
            heap.push(Reverse((self.low[c], c)));
            x ^= self.grundy[c];
        }
        result.insert(self.low[node], x);
        while let Some(&Reverse((content, _))) = heap.peek() {
            while let Some(&Reverse((l, c))) = heap.peek() {
                if l != content {
                    break;
                }
                heap.pop();
                x ^= self.grundy[c];
                for &d in &self.children[c] {
                    x ^= self.grundy[d];
                    heap.push(Reverse((self.low[d], d)));
                }
            }
            result.insert(content, x);
        }
        result
    }

    fn analyse(&mut self) -> usize {
        self.build(0, self.rings.len() - 1);
        // children are built after their parents, so go backwards
        for node in (0..self.low.len()).rev() {
            let options: HashSet<usize> = self.after_moves(node).values().copied().collect();
            self.grundy[node] = (0..).find(|g| !options.contains(g)).unwrap();
        }
        self.grundy[0]
    }
}

fn main() {
    let mut s = String::new();
    io::stdin().read_to_string(&mut s).unwrap();
    let mut it = s
        .split_ascii_whitespace()
        .map(|x| x.parse::<usize>().unwrap());
    let k = it.next().unwrap();
    let mut chains: Vec<Chain> = (0..k)
        .map(|_| {
            let length = it.next().unwrap();
            Chain {
                rings: (0..length).map(|_| it.next().unwrap()).collect(),
                low: Vec::new(),
                grundy: Vec::new(),
                children: Vec::new(),
            }
        })
        .collect();
    let g: Vec<usize> = chains.iter_mut().map(|c| c.analyse()).collect();
    let total = g.iter().fold(0, |a, &b| a ^ b);
    if total == 0 {
        println!("S");
        return;
    }
    // a winning move leaves the chain with the xor of all other chains
    for (i, c) in chains.iter().enumerate() {
        let after = c.after_moves(0);
        if let Some(j) = c.rings.iter().position(|r| after[r] == total ^ g[i]) {
            println!("G\n{} {}", i + 1, j + 1);
            return;
        }
    }
}
