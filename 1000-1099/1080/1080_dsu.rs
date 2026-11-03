use std::io::{self, Read};

const MAX_COUNTRIES: usize = 98;

struct Dsu {
    parent: [usize; MAX_COUNTRIES],
    size: [usize; MAX_COUNTRIES],
    parity: [u8; MAX_COUNTRIES],
}

impl Dsu {
    fn find(&mut self, v: usize) -> usize {
        if self.parent[v] != v {
            let old = self.parent[v];
            self.parent[v] = self.find(old);
            self.parity[v] ^= self.parity[old];
        }
        self.parent[v]
    }
}

fn main() {
    let stdin = io::stdin();
    let mut bytes = stdin.lock().bytes().map(Result::unwrap);
    let mut next = || {
        let first = bytes.by_ref().find(|&c| c > b' ').unwrap();
        let mut value = (first - b'0') as usize;
        for c in bytes.by_ref() {
            if c <= b' ' {
                break;
            }
            value = value * 10 + (c - b'0') as usize;
        }
        value
    };
    let n = next();
    let mut dsu = Dsu {
        parent: [0; MAX_COUNTRIES],
        size: [1; MAX_COUNTRIES],
        parity: [0; MAX_COUNTRIES],
    };
    for v in 0..n {
        dsu.parent[v] = v;
    }
    // Child/parent color XOR is stored. Each edge requires XOR=1.
    for a in 0..n {
        loop {
            let raw = next();
            if raw == 0 {
                break;
            }
            let b = raw - 1;
            let (mut ra, mut rb) = (dsu.find(a), dsu.find(b));
            if ra == rb {
                if dsu.parity[a] == dsu.parity[b] {
                    println!("-1");
                    return;
                }
            } else {
                if dsu.size[ra] < dsu.size[rb] {
                    std::mem::swap(&mut ra, &mut rb);
                }
                dsu.parent[rb] = ra;
                dsu.parity[rb] = dsu.parity[a] ^ dsu.parity[b] ^ 1;
                dsu.size[ra] += dsu.size[rb];
            }
        }
    }
    dsu.find(0);
    let first = dsu.parity[0];
    let mut answer = String::with_capacity(n);
    for v in 0..n {
        dsu.find(v);
        answer.push((b'0' + (dsu.parity[v] ^ first)) as char);
    }
    println!("{}", answer);
}
