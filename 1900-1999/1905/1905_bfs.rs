use std::io::{self, Read};

const TIME_BASE: u64 = 1_000_001;
const UNSEEN: usize = usize::MAX;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_whitespace().map(|x| x.parse::<u64>().unwrap());
    let _planets = tokens.next().unwrap();
    let count = tokens.next().unwrap() as usize;
    let mut origins = Vec::with_capacity(count);
    let mut destinations = Vec::with_capacity(count);
    let mut keys = Vec::with_capacity(2 * count + 2);
    for _ in 0..count {
        let (from, to) = (tokens.next().unwrap(), tokens.next().unwrap());
        let (leave, enter) = (tokens.next().unwrap(), tokens.next().unwrap());
        let origin = from * TIME_BASE + leave;
        let destination = to * TIME_BASE + enter;
        origins.push(origin);
        destinations.push(destination);
        keys.push(origin);
        keys.push(destination);
    }
    let (from, to) = (tokens.next().unwrap(), tokens.next().unwrap());
    let (start, deadline) = (tokens.next().unwrap(), tokens.next().unwrap());
    let source_key = from * TIME_BASE + start;
    let goal_key = to * TIME_BASE + deadline;
    keys.push(source_key);
    keys.push(goal_key);
    keys.sort_unstable();
    keys.dedup();
    let nodes = keys.len();
    let mut head = vec![UNSEEN; nodes];
    let mut arrival = vec![0; count];
    let mut following = vec![UNSEEN; count];
    for i in 0..count {
        let departure = keys.binary_search(&origins[i]).unwrap();
        arrival[i] = keys.binary_search(&destinations[i]).unwrap();
        following[i] = head[departure];
        head[departure] = i;
    }
    let source = keys.binary_search(&source_key).unwrap();
    let goal = keys.binary_search(&goal_key).unwrap();
    let mut previous = vec![UNSEEN; nodes];
    let mut used_flight = vec![0; nodes];
    previous[source] = source;
    let mut queue = Vec::with_capacity(nodes);
    queue.push(source);
    let mut cursor = 0;
    while cursor < queue.len() && previous[goal] == UNSEEN {
        let node = queue[cursor];
        cursor += 1;
        let next = node + 1;
        if next < nodes
            && keys[node] / TIME_BASE == keys[next] / TIME_BASE
            && previous[next] == UNSEEN
        {
            previous[next] = node;
            queue.push(next);
        }
        let mut flight = head[node];
        while flight != UNSEEN {
            let to = arrival[flight];
            if previous[to] == UNSEEN {
                previous[to] = node;
                used_flight[to] = flight + 1;
                queue.push(to);
            }
            flight = following[flight];
        }
    }
    if previous[goal] == UNSEEN {
        println!("Impossible");
        return;
    }
    let mut route = Vec::new();
    let mut node = goal;
    while node != source {
        if used_flight[node] != 0 {
            route.push(used_flight[node]);
        }
        node = previous[node];
    }
    route.reverse();
    println!("{}", route.len());
    println!(
        "{}",
        route
            .iter()
            .map(|x| x.to_string())
            .collect::<Vec<_>>()
            .join(" ")
    );
}
