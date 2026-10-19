use std::io::{self, Read, Write};

const WORD_BITS: usize = u64::BITS as usize;

fn select_bit(mut word: u64, mut rank: u32) -> usize {
    let mut position = 0;
    let mut half = WORD_BITS / 2;
    while half > 0 {
        let mask = (1u64 << half) - 1;
        let count = (word & mask).count_ones();
        if rank >= count {
            rank -= count;
            word >>= half;
            position += half;
        } else {
            word &= mask;
        }
        half >>= 1;
    }
    position
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace().map(|t| t.parse::<usize>().unwrap());
    let (n, k) = (it.next().unwrap(), it.next().unwrap());
    let buckets = (n + WORD_BITS - 1) / WORD_BITS;
    let mut alive = vec![u64::MAX; buckets];
    let mut tree = vec![0u32; buckets + 1];
    for i in 1..=buckets {
        tree[i] = (WORD_BITS * (i & i.wrapping_neg())) as u32;
    }
    let tail = n % WORD_BITS;
    if tail != 0 {
        alive[buckets - 1] = (1u64 << tail) - 1;
        tree[buckets] -= (WORD_BITS - tail) as u32;
    }
    let mut jump = 1;
    while jump << 1 <= buckets {
        jump <<= 1;
    }
    let (mut rank, mut answer) = (0usize, 0usize);
    let mut remaining = n;
    let mut round = 1;
    while remaining > 0 {
        rank = (rank + k - 1) % remaining;
        let (mut bucket, mut local_rank) = (0usize, rank as u32);
        let mut step = jump;
        while step > 0 {
            let next = bucket + step;
            if next <= buckets && tree[next] <= local_rank {
                bucket = next;
                local_rank -= tree[next];
            }
            step >>= 1;
        }
        let position = select_bit(alive[bucket], local_rank);
        let soldier = bucket * WORD_BITS + position + 1;
        answer ^= if round > soldier { round - soldier } else { soldier - round };
        alive[bucket] &= !(1u64 << position);
        let mut i = bucket + 1;
        while i <= buckets {
            tree[i] -= 1;
            i += i & i.wrapping_neg();
        }
        round += 1;
        remaining -= 1;
    }
    writeln!(io::stdout(), "{}", answer).unwrap();
}
