use std::io::{self, Read};

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let mut input = text.split_whitespace();
    let n: usize = input.next().unwrap().parse().unwrap();
    let days: usize = input.next().unwrap().parse().unwrap();
    let length: usize = input.next().unwrap().parse().unwrap();
    let moves: usize = input.next().unwrap().parse().unwrap();
    let positions = n - length + 1;
    let mut dp = vec![vec![0_i64; positions]];
    let mut prefix = vec![0_i64; n + 1];
    let mut weight = vec![0_i64; positions];
    let mut key = vec![0_i64; positions];
    let mut queue = vec![0_usize; positions];
    let mut previous_low = 0;

    for day in 1..=days {
        for j in 0..n {
            let gain: i64 = input.next().unwrap().parse().unwrap();
            prefix[j + 1] = prefix[j] + gain;
        }
        for x in 0..positions {
            weight[x] = prefix[x + length] - prefix[x];
        }
        let low = moves.saturating_sub(days - day);
        let high = day.min(moves);
        let mut next = vec![vec![0_i64; positions]; high - low + 1];
        for used in low..=high {
            let current = &mut next[used - low];
            if used < day {
                let stay = &dp[used - previous_low];
                for x in 0..positions {
                    current[x] = stay[x] + weight[x];
                }
            }
            if used == 0 {
                continue;
            }
            let previous = &dp[used - 1 - previous_low];
            for x in 0..positions {
                key[x] = previous[x] - prefix[x];
            }
            let (mut head, mut tail) = (0, 0);
            let mut best = 0;
            for y in 0..positions {
                if y >= length {
                    let x = y - length;
                    best = best.max(previous[x] + weight[x]);
                }
                while head < tail && key[queue[tail - 1]] <= key[y] {
                    tail -= 1;
                }
                queue[tail] = y;
                tail += 1;
                if y >= length && queue[head] <= y - length {
                    head += 1;
                }
                let overlap = key[queue[head]] + prefix[y + length];
                current[y] = current[y].max(overlap.max(best + weight[y]));
            }
            for x in 0..positions {
                key[x] = previous[x] + prefix[x + length];
            }
            head = 0;
            tail = 0;
            best = 0;
            for y in (0..positions).rev() {
                if y + length < positions {
                    let x = y + length;
                    best = best.max(previous[x] + weight[x]);
                }
                while head < tail && key[queue[tail - 1]] <= key[y] {
                    tail -= 1;
                }
                queue[tail] = y;
                tail += 1;
                if queue[head] >= y + length {
                    head += 1;
                }
                let overlap = key[queue[head]] - prefix[y];
                current[y] = current[y].max(overlap.max(best + weight[y]));
            }
        }
        dp = next;
        previous_low = low;
    }
    println!("{}", dp[0].iter().max().unwrap());
}
