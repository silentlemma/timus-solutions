use std::io::{self, Read};

const SECONDS_PER_MINUTE: i32 = 60;
const MINUTES_PER_HOUR: i32 = 60;
const SECONDS_PER_HOUR: i32 = SECONDS_PER_MINUTE * MINUTES_PER_HOUR;

struct Schedule {
    duration: i32,
    trips: i32,
    departures: Vec<i32>,
}

fn recover(first: i32, passages: &[i32]) -> Schedule {
    let count = passages.len();
    let (offset, last) = (passages[0] - first, passages[count - 1]);
    let total_span = last - first + offset;
    let mut present = vec![false; last as usize + 1];
    let mut marked = vec![0; last as usize + 1];
    for &time in passages {
        present[time as usize] = true;
    }
    let mut epoch = 0;
    for &first_return in &passages[1..=count / 2] {
        let period = first_return - first + offset;
        if period % 2 != 0 || period <= 2 * offset {
            continue;
        }
        let trips = total_span / period;
        if trips == 0 || count % (2 * trips as usize) != 0 {
            continue;
        }
        let tram_count = count / (2 * trips as usize);
        let gap = period - 2 * offset;
        epoch += 1;
        let mut departures = Vec::new();
        let mut failed = false;
        for &time in passages {
            if marked[time as usize] == epoch {
                continue;
            }
            let departure = time - offset;
            if departure >= first + period || departures.len() == tram_count {
                failed = true;
                break;
            }
            let mut outward = time;
            for _ in 0..trips {
                let returning = outward + gap;
                if outward > last
                    || returning > last
                    || !present[outward as usize]
                    || !present[returning as usize]
                    || marked[outward as usize] == epoch
                    || marked[returning as usize] == epoch
                {
                    failed = true;
                    break;
                }
                marked[outward as usize] = epoch;
                marked[returning as usize] = epoch;
                outward += period;
            }
            if failed {
                break;
            }
            departures.push(departure);
        }
        if !failed && departures.len() == tram_count {
            return Schedule {
                duration: period / 2,
                trips,
                departures,
            };
        }
    }
    panic!("The guaranteed schedule was not found");
}

fn parse_time(text: &str) -> i32 {
    let mut parts = text.split(':').map(|word| word.parse::<i32>().unwrap());
    let hours = parts.next().unwrap();
    let minutes = parts.next().unwrap();
    let seconds = parts.next().unwrap();
    hours * SECONDS_PER_HOUR + minutes * SECONDS_PER_MINUTE + seconds
}

fn format_time(value: i32) -> String {
    format!(
        "{:02}:{:02}:{:02}",
        value / SECONDS_PER_HOUR,
        value / SECONDS_PER_MINUTE % MINUTES_PER_HOUR,
        value % SECONDS_PER_MINUTE
    )
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut times = input.split_whitespace().map(parse_time);
    let first = times.next().unwrap();
    let passages: Vec<i32> = times.collect();
    let schedule = recover(first, &passages);
    let mut output = String::new();
    for departure in schedule.departures {
        for step in 0..=2 * schedule.trips {
            if step > 0 {
                output.push(' ');
            }
            output.push_str(&format_time(departure + step * schedule.duration));
        }
        output.push('\n');
    }
    print!("{}", output);
}
