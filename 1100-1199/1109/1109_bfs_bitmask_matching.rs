use std::io::{self, Read};

const BUFFER_SIZE: usize = 4096;
const WORD_BITS: usize = 64;
const UNMATCHED: usize = usize::MAX;

struct Reader<R: Read> {
    input: R,
    buffer: [u8; BUFFER_SIZE],
    position: usize,
    available: usize,
}

impl<R: Read> Reader<R> {
    fn byte(&mut self) -> u8 {
        if self.position == self.available {
            self.available = self.input.read(&mut self.buffer).unwrap();
            self.position = 0;
            if self.available == 0 {
                return 0;
            }
        }
        let c = self.buffer[self.position];
        self.position += 1;
        c
    }

    fn number(&mut self) -> usize {
        let mut c = self.byte();
        while c <= b' ' {
            c = self.byte();
        }
        let mut value = 0;
        while c.is_ascii_digit() {
            value = value * 10 + (c - b'0') as usize;
            c = self.byte();
        }
        value
    }
}

fn main() {
    let stdin = io::stdin();
    let mut input = Reader {
        input: stdin.lock(),
        buffer: [0; BUFFER_SIZE],
        position: 0,
        available: 0,
    };
    let (m, n, edges) = (input.number(), input.number(), input.number());
    let (left, right) = (m.min(n), m.max(n));
    let words = (right + WORD_BITS - 1) / WORD_BITS;
    let mut adjacent = vec![0_u64; left * words];
    let mut free = vec![u64::MAX; words];
    for _ in 0..edges {
        let (mut a, mut b) = (input.number() - 1, input.number() - 1);
        if m > n {
            std::mem::swap(&mut a, &mut b);
        }
        adjacent[a * words + b / WORD_BITS] |= 1_u64 << (b % WORD_BITS);
    }
    let mut match_l = vec![UNMATCHED; left];
    let mut match_r = vec![UNMATCHED; right];
    let mut parent = vec![0; right];
    let mut queue = vec![0; left];
    let mut size = 0;
    for root in 0..left {
        let mut seen = vec![0_u64; words];
        let (mut head, mut tail, mut target) = (0, 1, UNMATCHED);
        queue[0] = root;
        while head < tail && target == UNMATCHED {
            let v = queue[head];
            head += 1;
            for b in 0..words {
                let available = adjacent[v * words + b] & free[b];
                if available != 0 {
                    target = b * WORD_BITS + available.trailing_zeros() as usize;
                    parent[target] = v;
                    break;
                }
            }
            if target != UNMATCHED {
                break;
            }
            // Every unseen neighbor is matched, with one unique left partner.
            for b in 0..words {
                let mut options = adjacent[v * words + b] & !seen[b];
                seen[b] |= options;
                while options != 0 {
                    let u = b * WORD_BITS + options.trailing_zeros() as usize;
                    parent[u] = v;
                    queue[tail] = match_r[u];
                    tail += 1;
                    options &= options - 1;
                }
            }
        }
        if target != UNMATCHED {
            free[target / WORD_BITS] &= !(1_u64 << (target % WORD_BITS));
            // Flip old matching edges along the BFS parent chain.
            while target != UNMATCHED {
                let v = parent[target];
                let old = match_l[v];
                match_l[v] = target;
                match_r[target] = v;
                target = old;
            }
            size += 1;
        }
    }
    println!("{}", m + n - size);
}
