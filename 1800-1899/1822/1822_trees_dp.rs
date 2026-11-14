use std::io::{self, Read};

const PERCENT: u64 = 100;
const OUTPUT_SCALE: u64 = 100_000_000;
const NO_SHARE: (u32, u32) = (0, 1);
const FULL_SHARE: (u32, u32) = (1, 1);

fn main() -> io::Result<()> {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input)?;
    let mut numbers = input
        .split_ascii_whitespace()
        .map(|word| word.parse::<usize>().unwrap());
    let n = numbers.next().unwrap();
    let deadline = numbers.next().unwrap() as u32;

    let mut head = vec![0u16; n];
    let mut sibling = vec![0u16; n];
    let mut days = vec![0u32; n];
    for node in 1..n {
        let parent = numbers.next().unwrap() - 1;
        days[node] = numbers.next().unwrap() as u32;
        sibling[node] = head[parent];
        head[parent] = node as u16;
    }
    let children = |parent: usize| {
        std::iter::successors(Some(head[parent]), |&node| Some(sibling[usize::from(node)]))
            .take_while(|&node| node != 0)
            .map(usize::from)
    };

    let mut order = Vec::with_capacity(n);
    order.push(0u16);
    let mut i = 0;
    while i < order.len() {
        let node = usize::from(order[i]);
        for child in children(node) {
            days[child] += days[node];
            order.push(child as u16);
        }
        i += 1;
    }
    let mut limits = vec![NO_SHARE; n];
    let mut ranked = Vec::new();
    for node in order.into_iter().rev().map(usize::from) {
        if days[node] > deadline {
            continue;
        }
        ranked.clear();
        ranked.extend(children(node).map(|child| limits[child]));
        ranked.sort_unstable_by(|&(a, b), &(c, d)| (c * b).cmp(&(a * d)));
        let count = ranked.len() as u32;
        limits[node] = FULL_SHARE;
        for (index, &(num, den)) in ranked.iter().enumerate() {
            // Both the fraction of available children and their limits bound the share.
            let rank = index as u32 + 1;
            if rank * den >= num * count {
                limits[node] = if (rank - 1) * den < num * count {
                    (num, den)
                } else {
                    (rank - 1, count)
                };
                break;
            }
        }
    }
    let (num, den) = (u64::from(limits[0].0), u64::from(limits[0].1));
    let answer = (num * PERCENT * OUTPUT_SCALE + den / 2) / den;
    println!("{}.{:08}", answer / OUTPUT_SCALE, answer % OUTPUT_SCALE);
    Ok(())
}
