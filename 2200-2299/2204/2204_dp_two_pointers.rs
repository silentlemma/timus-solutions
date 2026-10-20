use std::io::{self, Read};

const OPTIONS: usize = 2;

struct Scanner {
    data: Vec<u8>,
    position: usize,
}

impl Scanner {
    fn new() -> Self {
        let mut data = Vec::new();
        io::stdin().read_to_end(&mut data).unwrap();
        Self { data, position: 0 }
    }

    fn next(&mut self) -> usize {
        while self.position < self.data.len() && self.data[self.position].is_ascii_whitespace() {
            self.position += 1;
        }
        let mut value = 0;
        while self.position < self.data.len() && self.data[self.position].is_ascii_digit() {
            value = value * 10 + usize::from(self.data[self.position] - b'0');
            self.position += 1;
        }
        value
    }
}

fn main() {
    let mut input = Scanner::new();
    let exam_count = input.next();
    let trip_count = input.next();
    let alternative_count = OPTIONS * exam_count;
    let mut exam_left = Vec::with_capacity(alternative_count);
    let mut exam_right = Vec::with_capacity(alternative_count);
    for _ in 0..alternative_count {
        exam_left.push(input.next());
        exam_right.push(input.next());
    }
    let mut trip_left = Vec::with_capacity(trip_count);
    let mut trip_right = Vec::with_capacity(trip_count);
    for _ in 0..trip_count {
        trip_left.push(input.next());
        trip_right.push(input.next());
    }

    let mut previous_first = [0; OPTIONS];
    let mut previous_end = [0; OPTIONS];
    let mut previous_cost = [0; OPTIONS];
    let mut first = 0;
    let mut end = 0;
    for exam in 0..exam_count {
        let mut current_first = [0; OPTIONS];
        let mut current_end = [0; OPTIONS];
        let mut current_cost = [0; OPTIONS];
        for option in 0..OPTIONS {
            let interval = OPTIONS * exam + option;
            while first < trip_count && trip_right[first] < exam_left[interval] {
                first += 1;
            }
            while end < trip_count && trip_left[end] <= exam_right[interval] {
                end += 1;
            }
            current_first[option] = first;
            current_end[option] = end;
            let mut best = trip_count + 1;
            for previous in 0..OPTIONS {
                // Only one trip can intersect two separated exam intervals.
                let shared = first < end
                    && previous_first[previous] < previous_end[previous]
                    && previous_end[previous] - 1 == first;
                let cost = previous_cost[previous] - usize::from(shared);
                best = best.min(cost);
            }
            current_cost[option] = end - first + best;
        }
        previous_first = current_first;
        previous_end = current_end;
        previous_cost = current_cost;
    }
    println!("{}", trip_count - previous_cost[0].min(previous_cost[1]));
}
