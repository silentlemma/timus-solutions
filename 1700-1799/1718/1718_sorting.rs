use std::io::{self, Read};

fn main() -> io::Result<()> {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input)?;
    let mut words = input.split_ascii_whitespace();
    let count: usize = words.next().unwrap().parse().unwrap();
    let mut changed = Vec::new();
    for _ in 0..count {
        let name = words.next().unwrap();
        match words.next().unwrap() {
            "AC" => changed.push((name, false)),
            "ML" | "TL" | "WA" => match words.next().unwrap() {
                "6" => changed.push((name, false)),
                "7" => changed.push((name, true)),
                _ => (),
            },
            _ => (),
        }
    }
    changed.sort_unstable();
    let mut least = 0;
    let mut most = 0;
    let mut last = "";
    let mut mandatory = false;
    for (name, forced) in changed {
        if name != last {
            most += 1;
            last = name;
            mandatory = false;
        }
        if forced && !mandatory {
            least += 1;
            mandatory = true;
        }
    }
    println!("{least} {most}");
    Ok(())
}
