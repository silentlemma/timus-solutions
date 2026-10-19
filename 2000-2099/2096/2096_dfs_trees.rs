use std::io::{self, Read, Write};

const MAX_QUERIES: usize = 100000;
const MAX_CHANGES: usize = 100000;
const SPACE: u8 = b' ';
const DIGIT_ZERO: u8 = b'0';

struct Input {
    data: Vec<u8>,
    position: usize,
}

impl Input {
    fn next(&mut self) -> u32 {
        while self.data[self.position] <= SPACE {
            self.position += 1;
        }
        let mut value = 0;
        while self.position < self.data.len() && self.data[self.position] > SPACE {
            value = value * 10 + u32::from(self.data[self.position] - DIGIT_ZERO);
            self.position += 1;
        }
        value
    }
}

struct Change {
    first: u32,
    count: u32,
    period: u32,
    value: u32,
}

fn main() -> io::Result<()> {
    let mut data = Vec::new();
    io::stdin().read_to_end(&mut data)?;
    let mut input = Input { data, position: 0 };
    let days = input.next() as usize;
    let friends = input.next() as usize;
    let mut activity: Vec<u32> = (0..days).map(|_| input.next()).collect();
    let mut child_head = vec![0_u32; friends + 1];
    let mut child_next = vec![0_u32; friends + 1];
    let mut query_head = vec![0_u32; friends + 1];
    let mut query_next = Vec::with_capacity(MAX_QUERIES);
    let mut query_day = Vec::with_capacity(MAX_QUERIES);
    let mut query_end = vec![0_usize; friends + 1];
    let mut change_start = vec![0_usize; friends + 2];
    let mut changes = Vec::with_capacity(MAX_CHANGES);
    let mut total_assignments = 0;

    for friend in 1..=friends {
        let count = input.next();
        for _ in 0..count {
            let version = input.next() as usize;
            query_day.push(input.next() - 1);
            query_next.push(query_head[version]);
            query_head[version] = query_day.len() as u32;
        }
        query_end[friend] = query_day.len();
        let parent = input.next() as usize;
        child_next[friend] = child_head[parent];
        child_head[parent] = friend as u32;
        let count = input.next();
        for _ in 0..count {
            let change = Change {
                first: input.next() - 1,
                count: input.next(),
                period: input.next(),
                value: input.next(),
            };
            total_assignments += change.count as usize;
            changes.push(change);
        }
        change_start[friend + 1] = changes.len();
    }
    drop(input);

    let mut answer = vec![0_u32; query_day.len()];
    let mut history = vec![0_u32; total_assignments];
    let mut history_size = 0;
    let mut events = Vec::with_capacity(2 * friends + 1);
    events.push(0_i32);
    while let Some(event) = events.pop() {
        if event >= 0 {
            let version = event as usize;
            for change in &changes[change_start[version]..change_start[version + 1]] {
                let mut day = change.first as usize;
                for _ in 0..change.count {
                    history[history_size] = activity[day];
                    history_size += 1;
                    activity[day] = change.value;
                    day += change.period as usize;
                }
            }
            let mut query = query_head[version];
            while query != 0 {
                let index = (query - 1) as usize;
                answer[index] = activity[query_day[index] as usize];
                query = query_next[index];
            }
            if version != 0 {
                events.push(-(version as i32));
            }
            let mut child = child_head[version];
            while child != 0 {
                events.push(child as i32);
                child = child_next[child as usize];
            }
        } else {
            let version = (-event) as usize;
            // Reverse both operation order and progression order to restore overlaps.
            for change in changes[change_start[version]..change_start[version + 1]]
                .iter()
                .rev()
            {
                for offset in (0..change.count).rev() {
                    let day = (change.first + offset * change.period) as usize;
                    history_size -= 1;
                    activity[day] = history[history_size];
                }
            }
        }
    }

    let stdout = io::stdout();
    let mut output = io::BufWriter::new(stdout.lock());
    for friend in 1..=friends {
        for query in query_end[friend - 1]..query_end[friend] {
            if query != query_end[friend - 1] {
                write!(output, " ")?;
            }
            write!(output, "{}", answer[query])?;
        }
        writeln!(output)?;
    }
    output.flush()
}
