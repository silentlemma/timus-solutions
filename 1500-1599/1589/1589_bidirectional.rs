use std::io::{self, Read, Write};
use std::time::{Duration, Instant};

// a set of grid cells, one bit each (grid <= 8 x 8)
type Mask = u64;

const SIDES: usize = 4;
const MAXCELLS: usize = 64;
const NONE: i32 = -1;
const INF: i32 = 1_000_000;
const TIME_LIMIT: Duration = Duration::from_millis(4600); // search before giving up
const DR: [i32; SIDES] = [-1, 1, 0, 0];
const DC: [i32; SIDES] = [0, 0, -1, 1];
const STEP: &[u8] = b"udlr";
const OPP: [usize; SIDES] = [1, 0, 3, 2];
const UP: usize = 0;
const DOWN: usize = 1;
const LEFT: usize = 2;
const RIGHT: usize = 3;

// One open-addressing table holds the states of both searches; pull-search
// keys carry PULLED. A slot keeps the key and the move that made it.
const PULLED: Mask = 1 << 63;
const TABLE_BITS: u32 = 22;
const TABLE: usize = 1 << TABLE_BITS;
const TABLE_MASK: usize = TABLE - 1;
const TABLE_FILL: usize = TABLE / 100 * 88; // the most keys before the table counts as full
const ROOT: u8 = 255;
const GOLDEN: Mask = 0x9E37_79B9_7F4A_7C15;
const KEY_BITS: u32 = 64;

// Open lists: buckets by f = g + WEIGHT * h, each a stack threaded through the
// table slots (a slot is queued at most once), so the memory stays fixed.
const BUCKETS: usize = 4096;
const G_BITS: u32 = 9;
const G_MASK: u32 = (1 << G_BITS) - 1;
const WEIGHT: i32 = 3;
const PUSH_ROUNDS: usize = 8; // expansions of each search per round
const PULL_ROUNDS: usize = 1;
const CLOCK_EVERY: u64 = 128;

// sets of up to MOST boxes, sets of four only with boxes NEAR the moved one
const MOST: usize = 4;
const NEAR: i32 = 3;
const TRIO: usize = 3;
const BYTE_BITS: usize = 8;

fn low(x: Mask) -> usize {
    x.trailing_zeros() as usize
}

fn has(m: Mask, c: i32) -> bool {
    (m >> c) & 1 != 0
}

fn bit(c: i32) -> Mask {
    1 << c
}

#[derive(Clone, Copy)]
struct Push {
    b: i32,
    dir: usize,
}

struct Open {
    head: Vec<u32>, // slot + 1, 0 when empty
    lowest: usize,
}

impl Open {
    fn new() -> Self {
        Open {
            head: vec![0; BUCKETS],
            lowest: BUCKETS,
        }
    }

    fn push(&mut self, next: &mut [u32], slot: usize, g: i32, f: i32) {
        let f = (f as usize).min(BUCKETS - 1);
        next[slot] = self.head[f] << G_BITS | (g as u32).min(G_MASK);
        self.head[f] = slot as u32 + 1;
        self.lowest = self.lowest.min(f);
    }

    fn pop(&mut self, next: &[u32]) -> Option<(usize, i32)> {
        while self.lowest < BUCKETS && self.head[self.lowest] == 0 {
            self.lowest += 1;
        }
        if self.lowest >= BUCKETS {
            return None;
        }
        let slot = (self.head[self.lowest] - 1) as usize;
        self.head[self.lowest] = next[slot] >> G_BITS;
        Some((slot, (next[slot] & G_MASK) as i32))
    }
}

enum Insert {
    Present,
    Full,
    At(usize),
}

struct Sokoban {
    started: Instant,
    cols: i32,
    cells: usize,
    floor: Mask,
    goals: Mask,
    dead: Mask,
    dead_pull: Mask,
    not_first_col: Mask,
    not_last_col: Mask,
    nb: [[i32; MAXCELLS]; SIDES], // the neighbour in a direction, NONE outside the grid
    start_player: i32,
    start_boxes: Mask,
    floor_count: u32,
    floor_cell: [i32; MAXCELLS],
    floor_index: [i32; MAXCELLS],
    goal_count: usize,
    frozen_as_wall: Mask,
    frozen_off_goal: bool,
    can_reach: [[Mask; MAXCELLS]; 2], // [push or pull search][cell]: targets a box there can get to
    nearest: [[i32; MAXCELLS]; 2],
    match_of: [i32; MAXCELLS],
    box_targets: [Mask; MAXCELLS],
    visited: Mask,
    table_key: Vec<Mask>,
    table_move: Vec<u8>,  // floor index of the moved box * 4 + direction
    table_next: Vec<u32>, // (next slot + 1) << G_BITS | g
    key_count: usize,
    table_full: bool,
    push_open: Open,
    pull_open: Open,
    binom: [[usize; MOST + 2]; MAXCELLS + 1],
    seen_set: Vec<u8>,
    set_table: [[Vec<Mask>; MOST + 1]; 2], // [solvable or reachable][k][set]: player cells
    dist: [[[i32; MAXCELLS]; MAXCELLS]; 2],
}

impl Sokoban {
    // the player's area: the floor reachable from p around the boxes, as bit-parallel growth
    fn grow(&self, r: Mask) -> Mask {
        r | ((r << 1) & self.not_first_col)
            | ((r >> 1) & self.not_last_col)
            | (r << self.cols)
            | (r >> self.cols)
    }

    fn flood(&self, seed: Mask, within: Mask) -> Mask {
        let mut r = seed;
        loop {
            let x = self.grow(r) & within;
            if x == r {
                return r;
            }
            r = x;
        }
    }

    fn reach(&self, p: i32, boxes: Mask) -> Mask {
        self.flood(bit(p), self.floor & !boxes)
    }

    // a state: a bit per floor cell for the boxes, then the floor index of the
    // lowest cell of the player's area
    fn pack_key(&self, boxes: Mask, player: usize) -> Mask {
        let mut k = 0;
        let mut b = boxes;
        while b != 0 {
            k |= bit(self.floor_index[low(b)]);
            b &= b - 1;
        }
        k | (self.floor_index[player] as Mask) << self.floor_count
    }

    fn key_boxes(&self, key: Mask) -> Mask {
        let mut b = 0;
        let mut k = key & (bit(self.floor_count as i32) - 1);
        while k != 0 {
            b |= bit(self.floor_cell[low(k)]);
            k &= k - 1;
        }
        b
    }

    fn key_player(&self, key: Mask) -> i32 {
        self.floor_cell[(key >> self.floor_count) as usize]
    }

    // A box is frozen when it can move along neither axis: a wall or a frozen
    // box on either side, or dead squares on both sides. Boxes already found
    // frozen count as walls while their neighbours are checked.
    fn wall_like(&self, c: i32) -> bool {
        c < 0 || !has(self.floor, c) || has(self.frozen_as_wall, c)
    }

    fn axis_blocked(&mut self, x: usize, d1: usize, d2: usize, boxes: Mask) -> bool {
        let (a, b) = (self.nb[d1][x], self.nb[d2][x]);
        if self.wall_like(a) || self.wall_like(b) {
            return true;
        }
        if has(self.dead, a) && has(self.dead, b) {
            return true;
        }
        (has(boxes, a) && self.frozen(a as usize, boxes))
            || (has(boxes, b) && self.frozen(b as usize, boxes))
    }

    fn frozen(&mut self, x: usize, boxes: Mask) -> bool {
        let saved = self.frozen_as_wall;
        self.frozen_as_wall |= bit(x as i32);
        let f = self.axis_blocked(x, LEFT, RIGHT, boxes) && self.axis_blocked(x, UP, DOWN, boxes);
        self.frozen_as_wall = saved;
        if f && !has(self.goals, x as i32) {
            self.frozen_off_goal = true;
        }
        f
    }

    // the box just pushed to x froze a box that is not on a goal
    fn freeze_deadlock(&mut self, x: usize, boxes: Mask) -> bool {
        self.frozen_as_wall = 0;
        self.frozen_off_goal = false;
        self.frozen(x, boxes) && self.frozen_off_goal
    }

    // h: the sum of each box's push distance to its nearest target; boxes that
    // cannot be matched to distinct reachable targets mean a deadlock
    fn augment(&mut self, i: usize) -> bool {
        let mut m = self.box_targets[i] & !self.visited;
        while m != 0 {
            let j = low(m);
            self.visited |= bit(j as i32);
            if self.match_of[j] < 0 || self.augment(self.match_of[j] as usize) {
                self.match_of[j] = i as i32;
                return true;
            }
            m &= m - 1;
        }
        false
    }

    fn heuristic(&mut self, boxes: Mask, dir: usize) -> i32 {
        let (mut k, mut h) = (0, 0);
        let mut b = boxes;
        while b != 0 {
            h += self.nearest[dir][low(b)];
            self.box_targets[k] = self.can_reach[dir][low(b)];
            k += 1;
            b &= b - 1;
        }
        for j in 0..self.goal_count {
            self.match_of[j] = NONE;
        }
        for i in 0..k {
            self.visited = 0;
            if !self.augment(i) {
                return NONE;
            }
        }
        h
    }

    // The pushes worth trying, or a deadlock. If every push of the boxes around
    // a region the player cannot reach goes inward and can be made now, one of
    // them is needed first, so only those are tried.
    fn generate_pushes(&self, boxes: Mask, area: Mask, out: &mut Vec<Push>) -> bool {
        out.clear();
        let mut bb = boxes;
        while bb != 0 {
            let b = low(bb);
            for d in 0..SIDES {
                let (s, t) = (self.nb[OPP[d]][b], self.nb[d][b]);
                if s >= 0 && t >= 0 && has(area, s) && has(self.floor, t) && !has(boxes, t) {
                    out.push(Push {
                        b: b as i32,
                        dir: d,
                    });
                }
            }
            bb &= bb - 1;
        }
        let open_floor = self.floor & !boxes & !area;
        let mut unreached = open_floor;
        let mut best: Vec<Push> = Vec::new();
        let mut candidates: Vec<Push> = Vec::new();
        let mut best_count = out.len() + 1;
        while unreached != 0 {
            let corral = self.flood(unreached & unreached.wrapping_neg(), open_floor);
            unreached &= !corral;
            let barrier = self.grow(corral) & boxes;
            if corral & self.goals == 0 && barrier & !self.goals == 0 {
                continue; // finished corral
            }
            let (mut inward, mut ready) = (true, true);
            candidates.clear();
            let mut bb = barrier;
            'boxes: while bb != 0 {
                let b = low(bb);
                for d in 0..SIDES {
                    let (s, t) = (self.nb[OPP[d]][b], self.nb[d][b]);
                    // the player stands outside the corral and off the barrier
                    if s < 0 || !has(self.floor, s) || has(corral, s) || has(barrier, s) {
                        continue;
                    }
                    if t < 0 || !has(self.floor, t) || has(barrier, t) {
                        continue; // blocked for good
                    }
                    if !has(corral, t) {
                        inward = false; // a push away from the corral
                        break 'boxes;
                    }
                    if has(area, s) {
                        candidates.push(Push {
                            b: b as i32,
                            dir: d,
                        });
                    } else {
                        ready = false;
                    }
                }
                bb &= bb - 1;
            }
            if !inward {
                continue;
            }
            if ready && candidates.is_empty() {
                return false; // unfinished, and no push can ever enter it
            }
            if ready && candidates.len() < best_count {
                best_count = candidates.len();
                best.clone_from(&candidates);
            }
        }
        if best_count <= out.len() {
            out.clone_from(&best);
        }
        true
    }

    fn slot_of(key: Mask) -> usize {
        (key.wrapping_mul(GOLDEN) >> (KEY_BITS - TABLE_BITS)) as usize
    }

    fn insert_key(&mut self, key: Mask) -> Insert {
        let mut h = Self::slot_of(key);
        while self.table_key[h] != 0 {
            if self.table_key[h] == key {
                return Insert::Present;
            }
            h = (h + 1) & TABLE_MASK;
        }
        if self.key_count >= TABLE_FILL {
            return Insert::Full;
        }
        self.key_count += 1;
        self.table_key[h] = key;
        Insert::At(h)
    }

    fn has_key(&self, key: Mask) -> bool {
        let mut h = Self::slot_of(key);
        while self.table_key[h] != 0 {
            if self.table_key[h] == key {
                return true;
            }
            h = (h + 1) & TABLE_MASK;
        }
        false
    }

    fn find_key(&self, key: Mask) -> usize {
        let mut h = Self::slot_of(key);
        while self.table_key[h] != key {
            h = (h + 1) & TABLE_MASK;
        }
        h
    }

    fn walk(&self, from: i32, to: i32, boxes: Mask, out: &mut Vec<u8>) {
        if from == to {
            return;
        }
        let mut prev = [-2i32; MAXCELLS];
        let mut queue = [0i32; MAXCELLS];
        let (mut head, mut tail) = (0, 0);
        prev[from as usize] = NONE;
        queue[tail] = from;
        tail += 1;
        while head < tail {
            let x = queue[head] as usize;
            head += 1;
            if x as i32 == to {
                break;
            }
            for d in 0..SIDES {
                let y = self.nb[d][x];
                if y < 0 || !has(self.floor, y) || has(boxes, y) || prev[y as usize] != -2 {
                    continue;
                }
                prev[y as usize] = (x * SIDES + d) as i32;
                queue[tail] = y;
                tail += 1;
            }
        }
        let start = out.len();
        let mut x = to as usize;
        while x as i32 != from {
            out.push(STEP[prev[x] as usize % SIDES]);
            x = prev[x] as usize / SIDES;
        }
        out[start..].reverse();
    }

    // the plan through the state key, which both searches reached (or which is solved)
    fn build_answer(&self, key: Mask) -> Vec<u8> {
        let mut pushes: Vec<Push> = Vec::new();
        let mut k = key;
        loop {
            // back from key to the start through the push search
            let mv = self.table_move[self.find_key(k)];
            if mv == ROOT {
                break;
            }
            let (b, d) = (self.floor_cell[mv as usize / SIDES], mv as usize % SIDES);
            let t = self.nb[d][b as usize];
            pushes.push(Push { b, dir: d });
            let boxes = (self.key_boxes(k) & !bit(t)) | bit(b);
            k = self.pack_key(boxes, low(self.reach(self.nb[OPP[d]][b as usize], boxes)));
        }
        pushes.reverse();
        if self.key_boxes(key) != self.goals {
            let mut k = key;
            loop {
                // forward to the goal: each pull, undone, is a push
                let mv = self.table_move[self.find_key(k | PULLED)];
                if mv == ROOT {
                    break;
                }
                let (x, d) = (self.floor_cell[mv as usize / SIDES], mv as usize % SIDES);
                let b = self.nb[d][x as usize];
                pushes.push(Push { b: x, dir: d });
                let boxes = (self.key_boxes(k) & !bit(x)) | bit(b);
                k = self.pack_key(boxes, low(self.reach(x, boxes)));
            }
        }
        let mut out = Vec::new();
        let mut boxes = self.start_boxes;
        let mut pos = self.start_player;
        for p in &pushes {
            self.walk(pos, self.nb[OPP[p.dir]][p.b as usize], boxes, &mut out);
            out.push(STEP[p.dir].to_ascii_uppercase());
            boxes = (boxes & !bit(p.b)) | bit(self.nb[p.dir][p.b as usize]);
            pos = p.b;
        }
        out
    }

    // For sets of k = 2..MOST cells, the player cells from which these boxes alone
    // can be solved (a pull search from the goals) or reached (a push search from
    // the start); a state with a failing subset is dead.
    fn set_index(&self, boxes: Mask) -> usize {
        // the combinatorial number system
        let mut index = 0;
        let mut i = 1;
        let mut b = boxes;
        while b != 0 {
            index += self.binom[self.floor_index[low(b)] as usize][i];
            i += 1;
            b &= b - 1;
        }
        index
    }

    fn first_visit(&mut self, set: Mask, area: usize) -> bool {
        let n = self.set_index(set) * self.floor_count as usize + self.floor_index[area] as usize;
        if (self.seen_set[n / BYTE_BITS] >> (n % BYTE_BITS)) & 1 != 0 {
            return false;
        }
        self.seen_set[n / BYTE_BITS] |= 1 << (n % BYTE_BITS);
        true
    }

    fn build_set_table(&mut self, dir: usize, k: usize) {
        let fc = self.floor_count as usize;
        self.seen_set = vec![0; (self.binom[fc][k] * fc + BYTE_BITS - 1) / BYTE_BITS];
        let mut table = vec![0 as Mask; self.binom[fc][k]];
        let mut queue = std::mem::take(&mut self.table_key);
        let (mut head, mut tail) = (0, 0);
        let mut at = Vec::new();
        let mut c = if dir == 1 {
            self.start_boxes
        } else {
            self.goals
        };
        while c != 0 {
            at.push(low(c) as i32);
            c &= c - 1;
        }
        let n = at.len();
        let mut pick: Vec<usize> = (0..k).collect();
        while k <= n {
            // every k of the start boxes or the goals
            let set = pick.iter().fold(0, |s, &i| s | bit(at[i]));
            if dir == 1 {
                // the player where it starts
                let area = low(self.reach(self.start_player, set));
                if self.first_visit(set, area) {
                    queue[tail] = self.pack_key(set, area);
                    tail += 1;
                }
            } else {
                // the player in any free area
                let mut rest = self.floor & !set;
                while rest != 0 {
                    let area = self.reach(low(rest) as i32, set);
                    rest &= !area;
                    if self.first_visit(set, low(area)) {
                        queue[tail] = self.pack_key(set, low(area));
                        tail += 1;
                    }
                }
            }
            let mut i = k;
            while i > 0 && pick[i - 1] == n - k + i - 1 {
                i -= 1;
            }
            if i == 0 {
                break;
            }
            pick[i - 1] += 1;
            for j in i..k {
                pick[j] = pick[j - 1] + 1;
            }
        }
        while head < tail {
            let key = queue[head];
            head += 1;
            let boxes = self.key_boxes(key);
            let area = self.reach(self.key_player(key), boxes);
            table[self.set_index(boxes)] |= area;
            let mut bb = boxes;
            while bb != 0 {
                let b = low(bb);
                bb &= bb - 1;
                for d in 0..SIDES {
                    let x = self.nb[OPP[d]][b];
                    if x < 0 || !has(area, x) {
                        continue;
                    }
                    // a push from x moves the box to y; a pull to x moves the player to y
                    let (y, to, dest) = if dir == 1 {
                        (self.nb[d][b], b as i32, self.nb[d][b])
                    } else {
                        (self.nb[OPP[d]][x as usize], self.nb[OPP[d]][x as usize], x)
                    };
                    if y < 0 || !has(self.floor, y) || has(boxes, y) {
                        continue;
                    }
                    let moved = (boxes & !bit(b as i32)) | bit(dest);
                    let wh = low(self.reach(to, moved));
                    if self.first_visit(moved, wh) {
                        queue[tail] = self.pack_key(moved, wh);
                        tail += 1;
                    }
                }
            }
        }
        queue[..tail].fill(0);
        self.table_key = queue;
        self.set_table[dir][k] = table;
    }

    fn set_solvable(&self, dir: usize, set: Mask, k: usize, player: i32) -> bool {
        has(self.set_table[dir][k][self.set_index(set)], player)
    }

    // every set of up to MOST boxes with the moved box t is in the table
    fn sets_ok(&self, dir: usize, boxes: Mask, t: i32, player: i32) -> bool {
        let mut other = [0i32; MAXCELLS];
        let mut close = [0i32; MAXCELLS];
        let (mut n, mut nc) = (0, 0);
        let mut b = boxes & !bit(t);
        while b != 0 {
            let c = low(b) as i32;
            other[n] = c;
            n += 1;
            if (c / self.cols - t / self.cols).abs() <= NEAR
                && (c % self.cols - t % self.cols).abs() <= NEAR
            {
                close[nc] = c;
                nc += 1;
            }
            b &= b - 1;
        }
        let bt = bit(t);
        for i in 0..n {
            if !self.set_solvable(dir, bt | bit(other[i]), 2, player) {
                return false;
            }
        }
        for i in 0..n {
            for j in i + 1..n {
                if !self.set_solvable(dir, bt | bit(other[i]) | bit(other[j]), TRIO, player) {
                    return false;
                }
            }
        }
        for i in 0..nc {
            for j in i + 1..nc {
                for l in j + 1..nc {
                    let set = bt | bit(close[i]) | bit(close[j]) | bit(close[l]);
                    if !self.set_solvable(dir, set, MOST, player) {
                        return false;
                    }
                }
            }
        }
        true
    }

    // Both expansions return the key of a state where the searches met (or a
    // solved state), 0 if none yet; table_full is set when the table is full.
    fn expand_push(&mut self, slot: usize, g: i32, pushes: &mut Vec<Push>) -> Mask {
        let g = g + 1;
        let key = self.table_key[slot];
        let boxes = self.key_boxes(key);
        let area = self.reach(self.key_player(key), boxes);
        if !self.generate_pushes(boxes, area, pushes) {
            return 0;
        }
        for &Push { b, dir: d } in pushes.iter() {
            let t = self.nb[d][b as usize];
            if has(self.dead, t) {
                continue;
            }
            let moved = (boxes & !bit(b)) | bit(t);
            if self.freeze_deadlock(t as usize, moved) {
                continue;
            }
            let next = self.pack_key(moved, low(self.reach(b, moved)));
            if self.has_key(next) || !self.sets_ok(0, moved, t, b) {
                continue;
            }
            let s = match self.insert_key(next) {
                Insert::Present => continue,
                Insert::Full => {
                    self.table_full = true;
                    return 0;
                }
                Insert::At(s) => s,
            };
            self.table_move[s] = (self.floor_index[b as usize] as usize * SIDES + d) as u8;
            if moved == self.goals || self.has_key(next | PULLED) {
                return next;
            }
            let h = self.heuristic(moved, 0);
            if h != NONE {
                // a deadlocked state stays in the table as visited
                self.push_open
                    .push(&mut self.table_next, s, g, g + WEIGHT * h);
            }
        }
        0
    }

    fn expand_pull(&mut self, slot: usize, g: i32) -> Mask {
        let g = g + 1;
        let key = self.table_key[slot] & !PULLED;
        let boxes = self.key_boxes(key);
        let area = self.reach(self.key_player(key), boxes);
        let mut bb = boxes;
        while bb != 0 {
            let b = low(bb);
            bb &= bb - 1;
            for d in 0..SIDES {
                // the player at x pulls the box from b to x and steps back to y
                let x = self.nb[OPP[d]][b];
                if x < 0 || !has(area, x) || has(self.dead_pull, x) {
                    continue;
                }
                let y = self.nb[OPP[d]][x as usize];
                if y < 0 || !has(self.floor, y) || has(boxes, y) {
                    continue;
                }
                let moved = (boxes & !bit(b as i32)) | bit(x);
                let next = self.pack_key(moved, low(self.reach(y, moved)));
                if self.has_key(next | PULLED) || !self.sets_ok(1, moved, x, y) {
                    continue;
                }
                let s = match self.insert_key(next | PULLED) {
                    Insert::Present => continue,
                    Insert::Full => {
                        self.table_full = true;
                        return 0;
                    }
                    Insert::At(s) => s,
                };
                self.table_move[s] = (self.floor_index[x as usize] as usize * SIDES + d) as u8;
                if self.has_key(next) {
                    return next;
                }
                let h = self.heuristic(moved, 1);
                if h != NONE {
                    self.pull_open
                        .push(&mut self.table_next, s, g, g + WEIGHT * h);
                }
            }
        }
        0
    }

    // The push search from the start and the pull search from the goal take
    // turns until some state is in both.
    fn solve(&mut self) -> Mask {
        let root = self.pack_key(
            self.start_boxes,
            low(self.reach(self.start_player, self.start_boxes)),
        );
        if let Insert::At(s) = self.insert_key(root) {
            self.table_move[s] = ROOT;
        }
        let h0 = self.heuristic(self.start_boxes, 0);
        if h0 != NONE {
            let s = self.find_key(root);
            self.push_open.push(&mut self.table_next, s, 0, WEIGHT * h0);
        }
        let hg = self.heuristic(self.goals, 1);
        let mut rest = self.floor & !self.goals;
        while rest != 0 {
            // the boxes on the goals, the player anywhere
            let area = self.reach(low(rest) as i32, self.goals);
            rest &= !area;
            let key = self.pack_key(self.goals, low(area));
            let s = match self.insert_key(key | PULLED) {
                Insert::At(s) => s,
                _ => continue,
            };
            self.table_move[s] = ROOT;
            if key == root {
                return key;
            }
            if hg != NONE {
                self.pull_open.push(&mut self.table_next, s, 0, WEIGHT * hg);
            }
        }
        let mut pushes = Vec::new();
        let mut round: u64 = 0;
        loop {
            if round % CLOCK_EVERY == 0 && self.started.elapsed() > TIME_LIMIT {
                return 0;
            }
            round += 1;
            let mut progress = false;
            for _ in 0..PUSH_ROUNDS {
                let Some((slot, g)) = self.push_open.pop(&self.table_next) else {
                    break;
                };
                progress = true;
                let k = self.expand_push(slot, g, &mut pushes);
                if k != 0 {
                    return k;
                }
                if self.table_full {
                    return 0;
                }
            }
            for _ in 0..PULL_ROUNDS {
                let Some((slot, g)) = self.pull_open.pop(&self.table_next) else {
                    break;
                };
                progress = true;
                let k = self.expand_pull(slot, g);
                if k != 0 {
                    return k;
                }
                if self.table_full {
                    return 0;
                }
            }
            if !progress {
                return 0;
            }
        }
    }

    // push distances of a lone box: dist[target][cell] to bring a box from
    // cell to the target (dir 0), or from the target to cell (dir 1)
    fn box_distances(&mut self, targets: Mask, dir: usize) -> Mask {
        let mut unreachable = self.floor;
        let mut tg = targets;
        let mut j = 0;
        while tg != 0 {
            let mut d_to = [INF; MAXCELLS];
            let mut queue = [0usize; MAXCELLS];
            let (mut head, mut tail) = (0, 0);
            d_to[low(tg)] = 0;
            queue[tail] = low(tg);
            tail += 1;
            while head < tail {
                let x = queue[head];
                head += 1;
                unreachable &= !bit(x as i32);
                for d in 0..SIDES {
                    // a box pushed from y to x (the player behind y), or from x to y
                    let (y, p) = if dir == 1 {
                        (self.nb[d][x], self.nb[OPP[d]][x])
                    } else {
                        let y = self.nb[OPP[d]][x];
                        (
                            y,
                            if y < 0 {
                                NONE
                            } else {
                                self.nb[OPP[d]][y as usize]
                            },
                        )
                    };
                    if y < 0
                        || p < 0
                        || !has(self.floor, y)
                        || !has(self.floor, p)
                        || d_to[y as usize] != INF
                    {
                        continue;
                    }
                    d_to[y as usize] = d_to[x] + 1;
                    queue[tail] = y as usize;
                    tail += 1;
                }
            }
            self.dist[dir][j] = d_to;
            j += 1;
            tg &= tg - 1;
        }
        unreachable
    }
}

fn main() {
    let started = Instant::now();
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let mut lines: Vec<&str> = text
        .split('\n')
        .map(|l| l.trim_end_matches(['\r', ' ']))
        .collect();
    // drop the empty rows and columns around the level
    while lines.last().map_or(false, |l| l.is_empty()) {
        lines.pop();
    }
    while lines.first().map_or(false, |l| l.is_empty()) {
        lines.remove(0);
    }
    let lead = lines
        .iter()
        .filter(|l| !l.is_empty())
        .map(|l| l.len() - l.trim_start_matches(' ').len())
        .min()
        .unwrap_or(0);
    let lines: Vec<&[u8]> = lines
        .iter()
        .map(|l| {
            if l.len() > lead {
                &l.as_bytes()[lead..]
            } else {
                &b""[..]
            }
        })
        .collect();
    let rows = lines.len() as i32;
    let cols = lines.iter().map(|l| l.len()).max().unwrap_or(0) as i32;
    let cells = (rows * cols) as usize;
    let mut s = Box::new(Sokoban {
        started,
        cols,
        cells,
        floor: 0,
        goals: 0,
        dead: 0,
        dead_pull: 0,
        not_first_col: 0,
        not_last_col: 0,
        nb: [[NONE; MAXCELLS]; SIDES],
        start_player: 0,
        start_boxes: 0,
        floor_count: 0,
        floor_cell: [0; MAXCELLS],
        floor_index: [0; MAXCELLS],
        goal_count: 0,
        frozen_as_wall: 0,
        frozen_off_goal: false,
        can_reach: [[0; MAXCELLS]; 2],
        nearest: [[INF; MAXCELLS]; 2],
        match_of: [NONE; MAXCELLS],
        box_targets: [0; MAXCELLS],
        visited: 0,
        table_key: vec![0; TABLE],
        table_move: vec![0; TABLE],
        table_next: vec![0; TABLE],
        key_count: 0,
        table_full: false,
        push_open: Open::new(),
        pull_open: Open::new(),
        binom: [[0; MOST + 2]; MAXCELLS + 1],
        seen_set: Vec::new(),
        set_table: Default::default(),
        dist: [[[0; MAXCELLS]; MAXCELLS]; 2],
    });
    let mut walls: Mask = 0;
    for r in 0..rows {
        for c in 0..cols {
            let ch = lines[r as usize].get(c as usize).copied().unwrap_or(b' ');
            let id = r * cols + c;
            match ch {
                b'#' => walls |= bit(id),
                b'.' => s.goals |= bit(id),
                b'$' => s.start_boxes |= bit(id),
                b'*' => {
                    s.goals |= bit(id);
                    s.start_boxes |= bit(id);
                }
                b'@' => s.start_player = id,
                b'+' => {
                    s.goals |= bit(id);
                    s.start_player = id;
                }
                _ => {}
            }
        }
    }
    for i in 0..s.cells {
        let ii = i as i32;
        for d in 0..SIDES {
            let (r, c) = (ii / cols + DR[d], ii % cols + DC[d]);
            if r >= 0 && r < rows && c >= 0 && c < cols {
                s.nb[d][i] = r * cols + c;
            }
        }
        if ii % cols != 0 {
            s.not_first_col |= bit(ii);
        }
        if ii % cols != cols - 1 {
            s.not_last_col |= bit(ii);
        }
    }
    // the floor: the cells the player reaches through non-walls; boxes on
    // goals walled off from the player never move and count as walls
    s.floor = !walls;
    if cells < MAXCELLS {
        s.floor &= bit(cells as i32) - 1;
    }
    s.floor = s.reach(s.start_player, 0);
    s.goals &= s.floor;
    s.start_boxes &= s.floor;
    let mut f = s.floor;
    while f != 0 {
        s.floor_index[low(f)] = s.floor_count as i32;
        s.floor_cell[s.floor_count as usize] = low(f) as i32;
        s.floor_count += 1;
        f &= f - 1;
    }
    s.goal_count = s.goals.count_ones() as usize;
    s.dead = s.box_distances(s.goals, 0);
    s.dead_pull = s.box_distances(s.start_boxes, 1);
    for i in 0..=MAXCELLS {
        for j in 0..=MOST + 1 {
            s.binom[i][j] = if j == 0 {
                1
            } else if i == 0 {
                0
            } else {
                s.binom[i - 1][j - 1] + s.binom[i - 1][j]
            };
        }
    }
    for k in 2..=MOST.min(s.goal_count) {
        for dir in 0..2 {
            s.build_set_table(dir, k);
        }
    }
    s.seen_set = Vec::new();
    for dir in 0..2 {
        for c in 0..s.cells {
            for j in 0..s.goal_count {
                if s.dist[dir][j][c] < INF {
                    s.can_reach[dir][c] |= bit(j as i32);
                }
                s.nearest[dir][c] = s.nearest[dir][c].min(s.dist[dir][j][c]);
            }
        }
    }
    let mut answer = Vec::new();
    if s.start_boxes != s.goals {
        let meet = s.solve();
        if meet != 0 {
            answer = s.build_answer(meet);
        }
    }
    answer.push(b'\n');
    io::stdout().write_all(&answer).unwrap();
}
