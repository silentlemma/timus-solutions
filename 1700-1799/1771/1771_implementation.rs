use std::io::{self, Read};

const MINUTES: i32 = 60;
const FIRST_HOUR: i32 = 7;
const WITH_LEONID: i32 = 13;
const ALREADY_IN: i32 = 42;

struct Notes {
    place: Vec<Vec<i32>>,
    buses: Vec<(i32, usize)>,
}

impl Notes {
    // whether a passenger waiting at src for dst takes the chosen bus: no bus
    // seen by Leonid serves the trip and comes to src sooner, or at the same
    // minute reaching dst sooner, or as soon with a smaller route
    fn picked(&self, src: usize, dst: usize) -> bool {
        let &(chosen_start, chosen) = self.buses.last().unwrap();
        let here = &self.place[chosen];
        if here[src] < 0 || here[dst] < 0 || here[src] >= here[dst] {
            return false;
        }
        let mine = (chosen_start + here[src], chosen_start + here[dst], chosen);
        self.buses.iter().all(|&(start, route)| {
            let there = &self.place[route];
            start < 0
                || there[src] < 0
                || there[dst] < 0
                || there[src] >= there[dst]
                || (start + there[src], start + there[dst], route) >= mine
        })
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input
        .split(|c: char| c.is_ascii_whitespace() || c == ':')
        .filter(|w| !w.is_empty());
    let mut next = || words.next().unwrap().parse::<i32>().unwrap();
    let (n, m) = (next() as usize, next() as usize);
    let mut order: Vec<Vec<usize>> = vec![Vec::new(); m];
    let mut place = vec![vec![-1i32; n + 1]; m];
    for r in 0..m {
        loop {
            let s = next();
            if s == -1 {
                break;
            }
            place[r][s as usize] = order[r].len() as i32;
            order[r].push(s as usize);
        }
    }
    let k = next();
    let mut buses = Vec::new();
    for _ in 0..k {
        let (hh, mm) = (next(), next());
        let route = next() as usize - 1;
        // the minute this bus left the first stop of its route
        buses.push(((hh - FIRST_HOUR) * MINUTES + mm - place[route][1], route));
    }
    let chosen = buses.last().unwrap().1;
    let notes = Notes { place, buses };
    // buses not seen at stop 1 either come to a stop before it later than the
    // chosen bus, or need not run at all
    let stops = &order[chosen];
    let one = notes.place[chosen][1] as usize;
    let two = notes.place[chosen][2] as usize;
    let (mut leave_new, mut stay_new, mut leave_old, mut stay_old) = (false, false, false, false);
    for d in one + 1..stops.len() {
        let early = d < two;
        if notes.picked(1, stops[d]) {
            leave_new |= early;
            stay_new |= !early;
        }
        for s in 0..one {
            if notes.picked(stops[s], stops[d]) {
                leave_old |= early;
                stay_old |= !early;
            }
        }
    }
    // each group can all ride to a stop of one kind, so the counts are all or
    // nothing for the 13 who got on with Leonid and the 42 already inside
    let size = |flag: bool, people: i32| if flag { people } else { 0 };
    let low = size(!leave_new, WITH_LEONID) + size(!leave_old, ALREADY_IN);
    let high = size(stay_new, WITH_LEONID) + size(stay_old, ALREADY_IN);
    println!("{} {}", low, high);
}
