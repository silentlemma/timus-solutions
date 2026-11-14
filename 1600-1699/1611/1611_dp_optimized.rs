use std::io::{self, Read, Write};

const STEP: usize = 10;

fn plan(good: &[u8], limit: usize) -> (u16, Vec<usize>) {
    // A row holds the costs for the current conductor count. A set bit
    // records that the best path entered this state by adding a friend.
    let mut cost = vec![0u16; limit + 1];
    let mut from_friend = vec![0u64; good.len() + 1];
    for (j, best) in cost.iter_mut().enumerate() {
        *best = (j / STEP) as u16;
    }
    for (index, &conductor) in good.iter().enumerate() {
        let i = index + 1;
        cost[0] += u16::from(i % STEP == 0 && conductor == b'1');
        for j in 1..=limit {
            let fined = (i + j) % STEP == 0;
            let with_conductor = cost[j] + u16::from(fined && conductor == b'1');
            let with_friend = cost[j - 1] + u16::from(fined);
            if with_friend < with_conductor {
                cost[j] = with_friend;
                from_friend[i] |= 1 << j;
            } else {
                cost[j] = with_conductor;
            }
        }
    }
    let (mut j, &best) = cost
        .iter()
        .enumerate()
        .min_by_key(|&(j, value)| (*value, j))
        .unwrap();
    let mut places = Vec::with_capacity(j);
    let mut i = good.len();
    while i != 0 || j != 0 {
        if i == 0 || from_friend[i] & (1 << j) != 0 {
            places.push(i + j);
            j -= 1;
        } else {
            i -= 1;
        }
    }
    places.reverse();
    (best, places)
}

fn main() -> io::Result<()> {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input)?;
    let mut fields = input.split_ascii_whitespace();
    if fields.next().is_none() {
        return Ok(());
    }
    let limit = fields.next().unwrap().parse().unwrap();
    let good = fields.next().unwrap_or("").as_bytes();
    let (best, places) = plan(good, limit);
    let mut output = io::BufWriter::new(io::stdout().lock());
    write!(output, "{}\n{}", best, places.len())?;
    for place in places {
        write!(output, " {}", place)?;
    }
    writeln!(output)
}
