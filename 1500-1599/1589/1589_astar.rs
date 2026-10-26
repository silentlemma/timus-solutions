use std::cmp::Reverse;
use std::collections::BinaryHeap;
use std::io::{self, Read, Write};
use std::time::Instant;

type Mask = u64;

const BOARD_WIDTH: usize = 8;
const CELL_COUNT: usize = 64;
const LAST_COORDINATE: usize = BOARD_WIDTH - 1;
const DIRECTION_COUNT: usize = 4;
const PLAYER_SHIFT: usize = 56;
const BOX_BITS: Mask = 0x00ff_ffff_ffff_ffff;
const MAX_BOXES: usize = 36;
const MATCHING_SIZE: usize = MAX_BOXES + 1;
const MAX_PLAN_LENGTH: usize = 10_000;
const UNREACHABLE: i32 = 10_000;
const LETTER_CASE_OFFSET: u8 = 32;
const INITIAL_HASH_SIZE: usize = 65_536;
const CACHE_HASH_SIZE: usize = 16;
const HASH_LOAD_NUMERATOR: usize = 7;
const HASH_LOAD_DENOMINATOR: usize = 10;
const HASH_SHIFT_FIRST: usize = 30;
const HASH_SHIFT_SECOND: usize = 27;
const HASH_SHIFT_LAST: usize = 31;
const HASH_MULTIPLIER_FIRST: Mask = 0xbf58_476d_1ce4_e5b9;
const HASH_MULTIPLIER_SECOND: Mask = 0x94d0_49bb_1331_11eb;
const DISTANCE_QUEUE_SIZE: usize = 128;
const DISTANCE_QUEUE_MASK: usize = DISTANCE_QUEUE_SIZE - 1;
const BYTE_BITS: usize = 8;
const BYTE_VALUES: usize = 256;
const BYTE_MASK: usize = BYTE_VALUES - 1;
const REGION_WIDTH: usize = 3;
const SMALL_PATTERN_SIZE: usize = 3;
const LARGE_PATTERN_SIZE: usize = 5;
const PATTERN_SIZE_COUNT: usize = LARGE_PATTERN_SIZE + 1;
const PRIORITY_SCALE: i32 = 100;
const PACKING_WEIGHT: i32 = 30;
const INITIAL_EXPANSIONS: i32 = 128;
const ROTATED_EXPANSIONS: i32 = 64;
const SMALL_BOX_EXPANSIONS: i32 = 4000;
const MANY_BOX_EXPANSIONS: i32 = 256;
const UNBOUNDED_EXPANSIONS: i32 = i32::MAX;
const NODE_CAP: usize = 600_000;
const FAST_SECONDS: f64 = 1.0;
const CLOCK_CHECK_MASK: i32 = 255;
const ROTATION_COUNT: usize = 4;
const SYMMETRY_COUNT: usize = 8;
const REFLECTION_FLAG: usize = 4;
const ROTATION_MASK: usize = 3;
const GEOMETRY_COMPONENTS: usize = 4;
const PLAYER_COMPONENT: usize = 3;
const DIRECTION_PROBE_CELL: usize = 27;
const NO_PARENT: u32 = u32::MAX;
const DIRECTION_STEP: [i32; DIRECTION_COUNT] = [-(BOARD_WIDTH as i32), BOARD_WIDTH as i32, -1, 1];
const DIRECTION_LETTER: &[u8; DIRECTION_COUNT] = b"udlr";
const ROTATED_LETTER: &[u8; DIRECTION_COUNT] = b"lrdu";

fn lowest_cell(mask: Mask) -> usize {
    mask.trailing_zeros() as usize
}

fn cell_bit(cell: usize) -> Mask {
    1 << cell
}

fn neighbor(cell: usize, direction: usize) -> usize {
    (cell as i32 + DIRECTION_STEP[direction]) as usize
}

// The wall border prevents horizontal shifts from wrapping into usable cells.
fn shift(mask: Mask, direction: usize) -> Mask {
    match direction {
        0 => mask >> BOARD_WIDTH,
        1 => mask << BOARD_WIDTH,
        2 => mask >> 1,
        _ => mask << 1,
    }
}

// Grow the player component by bit-parallel steps until it stops changing.
fn reachable_cells(mut reachable: Mask, floor: Mask) -> Mask {
    loop {
        let expanded = (reachable
            | (reachable << BOARD_WIDTH)
            | (reachable >> BOARD_WIDTH)
            | (reachable << 1)
            | (reachable >> 1))
            & floor;
        if expanded == reachable {
            return reachable;
        }
        reachable = expanded;
    }
}

// Boxes fit below the top byte, which holds the lowest reachable player cell.
fn state_key(boxes: Mask, reachable: Mask) -> Mask {
    boxes | ((lowest_cell(reachable) as Mask) << PLAYER_SHIFT)
}

fn hash_key(mut state: Mask) -> usize {
    state ^= state >> HASH_SHIFT_FIRST;
    state = state.wrapping_mul(HASH_MULTIPLIER_FIRST);
    state ^= state >> HASH_SHIFT_SECOND;
    state = state.wrapping_mul(HASH_MULTIPLIER_SECOND);
    (state ^ (state >> HASH_SHIFT_LAST)) as usize
}

fn rotate_cell(cell: usize) -> usize {
    (cell % BOARD_WIDTH) * BOARD_WIDTH + LAST_COORDINATE - cell / BOARD_WIDTH
}

fn transform_cell(mut cell: usize, symmetry: usize) -> usize {
    if symmetry & REFLECTION_FLAG != 0 {
        cell = (cell / BOARD_WIDTH) * BOARD_WIDTH + LAST_COORDINATE - cell % BOARD_WIDTH;
    }
    for _ in 0..symmetry & ROTATION_MASK {
        cell = rotate_cell(cell);
    }
    cell
}

fn transform_mask(mut mask: Mask, symmetry: usize) -> Mask {
    let mut result = 0;
    while mask != 0 {
        result |= cell_bit(transform_cell(lowest_cell(mask), symmetry));
        mask &= mask - 1;
    }
    result
}

// Values stay dense; open-addressing slots store their indices plus one.
// No cache is iterated in hash order, so its layout cannot change search ties.
struct Cache<T> {
    entries: Vec<(Mask, T)>,
    slots: Vec<u32>,
}

impl<T> Cache<T> {
    fn new() -> Self {
        Self {
            entries: Vec::new(),
            slots: Vec::new(),
        }
    }

    fn clear(&mut self) {
        self.entries.clear();
        self.slots.fill(0);
    }

    fn find(&self, key: Mask) -> Option<usize> {
        if self.slots.is_empty() {
            return None;
        }
        let mask = self.slots.len() - 1;
        let mut slot = hash_key(key) & mask;
        while self.slots[slot] != 0 {
            let index = self.slots[slot] as usize - 1;
            if self.entries[index].0 == key {
                return Some(index);
            }
            slot = (slot + 1) & mask;
        }
        None
    }

    fn insert(&mut self, key: Mask, value: T) -> usize {
        if let Some(index) = self.find(key) {
            self.entries[index].1 = value;
            return index;
        }
        if self.slots.is_empty()
            || self.entries.len() * HASH_LOAD_DENOMINATOR > self.slots.len() * HASH_LOAD_NUMERATOR
        {
            let size = if self.slots.is_empty() {
                CACHE_HASH_SIZE
            } else {
                self.slots.len() * 2
            };
            self.slots = vec![0; size];
            for (index, entry) in self.entries.iter().enumerate() {
                let mut slot = hash_key(entry.0) & (size - 1);
                while self.slots[slot] != 0 {
                    slot = (slot + 1) & (size - 1);
                }
                self.slots[slot] = index as u32 + 1;
            }
        }
        let mut slot = hash_key(key) & (self.slots.len() - 1);
        while self.slots[slot] != 0 {
            slot = (slot + 1) & (self.slots.len() - 1);
        }
        let index = self.entries.len();
        self.entries.push((key, value));
        self.slots[slot] = index as u32 + 1;
        index
    }
}

// Boundary-strip tables project outside boxes into a supply of spare boxes.
struct Region {
    mask: Mask,
    floor: Mask,
    solvable_players: Vec<Mask>,
    packed_bytes: [[usize; BYTE_VALUES]; BOARD_WIDTH],
    rows: [usize; BOARD_WIDTH],
    row_count: usize,
}

impl Region {
    fn index(&self, boxes: Mask) -> usize {
        let mut packed = 0;
        for row_index in 0..self.row_count {
            let byte = ((boxes >> (self.rows[row_index] * BYTE_BITS)) as usize) & BYTE_MASK;
            packed |= self.packed_bytes[row_index][byte];
        }
        packed
    }

    fn add(&mut self, boxes: Mask, reachable: Mask, queue: &mut Vec<Mask>) {
        let index = self.index(boxes);
        if self.solvable_players[index] & reachable != 0 {
            return;
        }
        let reachable = reachable_cells(reachable, self.floor & !boxes);
        self.solvable_players[index] |= reachable;
        queue.push(state_key(boxes, reachable));
    }

    fn build(region_mask: Mask, floor: Mask, goals: Mask, box_count: u32) -> Self {
        let mut active = goals;
        loop {
            let previous = active;
            for direction in 0..DIRECTION_COUNT {
                active |= shift(active, direction) & shift(floor, direction ^ 1) & floor;
            }
            if active == previous {
                break;
            }
        }
        let mask = region_mask & active;
        let mut cells = Vec::new();
        let mut remaining = mask;
        while remaining != 0 {
            cells.push(lowest_cell(remaining));
            remaining &= remaining - 1;
        }
        let mut region = Self {
            mask,
            floor,
            solvable_players: vec![0; 1 << cells.len()],
            packed_bytes: [[0; BYTE_VALUES]; BOARD_WIDTH],
            rows: [0; BOARD_WIDTH],
            row_count: 0,
        };
        for row in 0..BOARD_WIDTH {
            let mut masks = [0; BOARD_WIDTH];
            let mut used = false;
            for (index, &cell) in cells.iter().enumerate() {
                if cell / BOARD_WIDTH == row {
                    masks[cell % BOARD_WIDTH] = 1 << index;
                    used = true;
                }
            }
            if !used {
                continue;
            }
            let row_index = region.row_count;
            region.rows[row_index] = row;
            for byte in 1..BYTE_VALUES {
                region.packed_bytes[row_index][byte] = region.packed_bytes[row_index]
                    [byte & (byte - 1)]
                    | masks[byte.trailing_zeros() as usize];
            }
            region.row_count += 1;
        }
        let mut queue = Vec::new();
        let boxes = goals & mask;
        let mut todo = floor & !boxes;
        while todo != 0 {
            let reachable = reachable_cells(cell_bit(lowest_cell(todo)), floor & !boxes);
            region.add(boxes, reachable, &mut queue);
            todo &= !reachable;
        }
        let outside = active & !mask;
        let mut head = 0;
        while head < queue.len() {
            let state = queue[head];
            head += 1;
            let boxes = state & BOX_BITS;
            let empty = floor & !boxes;
            let reachable = reachable_cells(cell_bit((state >> PLAYER_SHIFT) as usize), empty);
            for direction in 0..DIRECTION_COUNT {
                let mut movable = boxes
                    & shift(
                        reachable & shift(empty, direction ^ 1) & active,
                        direction ^ 1,
                    );
                while movable != 0 {
                    let cell = lowest_cell(movable);
                    movable &= movable - 1;
                    let next = neighbor(cell, direction);
                    let next_boxes = (boxes ^ cell_bit(cell)) | (cell_bit(next) & mask);
                    region.add(next_boxes, cell_bit(neighbor(next, direction)), &mut queue);
                }
                if boxes.count_ones() < box_count {
                    let mut movable = outside
                        & shift(
                            reachable & shift(empty, direction ^ 1) & mask,
                            direction ^ 1,
                        );
                    while movable != 0 {
                        let cell = lowest_cell(movable);
                        movable &= movable - 1;
                        let next = neighbor(cell, direction);
                        region.add(
                            boxes | cell_bit(next),
                            cell_bit(neighbor(next, direction)),
                            &mut queue,
                        );
                    }
                }
            }
        }
        region
    }
}

type Binomial = [[usize; PATTERN_SIZE_COUNT]; MATCHING_SIZE];
type GoalDistances = [[i32; CELL_COUNT]; MAX_BOXES];

// Each fixed-box-conditioned table densely ranks subsets in combinatorial order.
struct Pattern {
    solvable_players: Vec<Mask>,
    floor: Mask,
    live_cells: Mask,
    subset_size: usize,
    cell_index: [usize; CELL_COUNT],
}

impl Pattern {
    fn rank(&self, mut boxes: Mask, binomial: &Binomial) -> usize {
        let mut rank = 0;
        let mut size = 1;
        while boxes != 0 {
            rank += binomial[self.cell_index[lowest_cell(boxes)]][size];
            size += 1;
            boxes &= boxes - 1;
        }
        rank
    }

    fn add(&mut self, boxes: Mask, reachable: Mask, queue: &mut Vec<Mask>, binomial: &Binomial) {
        let index = self.rank(boxes, binomial);
        if self.solvable_players[index] & reachable != 0 {
            return;
        }
        let reachable = reachable_cells(reachable, self.floor & !boxes);
        self.solvable_players[index] |= reachable;
        queue.push(state_key(boxes, reachable));
    }

    // Lexicographic enumeration chooses at most five boxes, so recursion is shallow.
    fn roots(
        &mut self,
        goals: &[usize],
        start: usize,
        left: usize,
        boxes: Mask,
        player: Option<usize>,
        queue: &mut Vec<Mask>,
        binomial: &Binomial,
    ) {
        if left != 0 {
            for index in start..goals.len() {
                self.roots(
                    goals,
                    index + 1,
                    left - 1,
                    boxes | cell_bit(goals[index]),
                    player,
                    queue,
                    binomial,
                );
            }
        } else if let Some(player) = player {
            self.add(boxes, cell_bit(player), queue, binomial);
        } else {
            let mut empty = self.floor & !boxes;
            while empty != 0 {
                let reachable = reachable_cells(cell_bit(lowest_cell(empty)), self.floor & !boxes);
                self.add(boxes, reachable, queue, binomial);
                empty &= !reachable;
            }
        }
    }

    fn build(
        floor: Mask,
        goals: Mask,
        size: usize,
        reverse: bool,
        player: usize,
        binomial: &Binomial,
    ) -> Self {
        let subset_size = size.min(goals.count_ones() as usize);
        let mut table = Self {
            solvable_players: Vec::new(),
            floor,
            live_cells: goals,
            subset_size,
            cell_index: [usize::MAX; CELL_COUNT],
        };
        if subset_size == 0 {
            return table;
        }
        loop {
            let previous = table.live_cells;
            for direction in 0..DIRECTION_COUNT {
                table.live_cells |= if reverse {
                    shift(table.live_cells & shift(floor, direction), direction) & floor
                } else {
                    shift(table.live_cells, direction) & shift(floor, direction ^ 1) & floor
                };
            }
            if table.live_cells == previous {
                break;
            }
        }
        let mut cell_count = 0;
        let mut remaining = table.live_cells;
        while remaining != 0 {
            table.cell_index[lowest_cell(remaining)] = cell_count;
            cell_count += 1;
            remaining &= remaining - 1;
        }
        table.solvable_players = vec![0; binomial[cell_count][subset_size]];
        let mut goal_cells = Vec::new();
        remaining = goals;
        while remaining != 0 {
            goal_cells.push(lowest_cell(remaining));
            remaining &= remaining - 1;
        }
        let mut queue = Vec::new();
        table.roots(
            &goal_cells,
            0,
            subset_size,
            0,
            if reverse { Some(player) } else { None },
            &mut queue,
            binomial,
        );
        let mut head = 0;
        while head < queue.len() {
            let state = queue[head];
            head += 1;
            let boxes = state & BOX_BITS;
            let empty = floor & !boxes;
            let reachable = reachable_cells(cell_bit((state >> PLAYER_SHIFT) as usize), empty);
            for direction in 0..DIRECTION_COUNT {
                let mut movable = if reverse {
                    boxes & shift(reachable, direction) & shift(empty, direction ^ 1)
                } else {
                    boxes & shift(reachable & shift(empty, direction ^ 1), direction ^ 1)
                };
                while movable != 0 {
                    let cell = lowest_cell(movable);
                    movable &= movable - 1;
                    let next = neighbor(cell, direction);
                    let player = if reverse {
                        cell
                    } else {
                        neighbor(next, direction)
                    };
                    table.add(
                        boxes ^ cell_bit(cell) ^ cell_bit(next),
                        cell_bit(player),
                        &mut queue,
                        binomial,
                    );
                }
            }
        }
        table
    }

    // Unchanged frozen boxes permit skipping subsets without the last moved box.
    fn subsets_good(
        &self,
        indices: &[usize],
        start: usize,
        size: usize,
        rank: usize,
        moved: usize,
        contains_moved: bool,
        reachable: Mask,
        binomial: &Binomial,
    ) -> bool {
        if size > self.subset_size {
            return (!contains_moved && moved != usize::MAX && self.subset_size != 1)
                || self.solvable_players[rank] & reachable != 0;
        }
        for index in start..indices.len() {
            let cell = indices[index];
            if !self.subsets_good(
                indices,
                index + 1,
                size + 1,
                rank + binomial[cell][size],
                moved,
                contains_moved || cell == moved,
                reachable,
                binomial,
            ) {
                return false;
            }
        }
        true
    }
}

#[derive(Clone, Copy)]
struct Node {
    state: Mask,
    parent: u32,
    encoded_push: u16,
}

struct Solver {
    started: Instant,
    floor: Mask,
    goals: Mask,
    initial_boxes: Mask,
    initial_player: usize,
    live_cells: Mask,
    target_boxes: Mask,
    reverse: bool,
    fast: bool,
    crossing_penalty: i32,
    regional: bool,
    pattern_size: usize,
    moved_box: Mask,
    parent_frozen: Mask,
    packing_weight: i32,
    goal_cells: [usize; MAX_BOXES],
    goal_count: usize,
    nodes: Vec<Node>,
    hash_table: Vec<u32>,
    heuristic_cache: Cache<i32>,
    distance_cache: Cache<GoalDistances>,
    packing: Cache<Vec<(Mask, Mask)>>,
    patterns: Cache<Pattern>,
    regions: Vec<Region>,
    binomial: Binomial,
}

impl Solver {
    fn new(started: Instant, floor: Mask, goals: Mask, boxes: Mask, player: usize) -> Self {
        let mut binomial = [[0; PATTERN_SIZE_COUNT]; MATCHING_SIZE];
        for available in 0..=MAX_BOXES {
            for size in 0..=LARGE_PATTERN_SIZE {
                binomial[available][size] = if size == 0 {
                    1
                } else if available == 0 {
                    0
                } else {
                    binomial[available - 1][size - 1] + binomial[available - 1][size]
                };
            }
        }
        Self {
            started,
            floor,
            goals,
            initial_boxes: boxes,
            initial_player: player,
            live_cells: 0,
            target_boxes: 0,
            reverse: false,
            fast: true,
            crossing_penalty: 0,
            regional: false,
            pattern_size: 0,
            moved_box: 0,
            parent_frozen: 0,
            packing_weight: 0,
            goal_cells: [0; MAX_BOXES],
            goal_count: 0,
            nodes: Vec::new(),
            hash_table: Vec::new(),
            heuristic_cache: Cache::new(),
            distance_cache: Cache::new(),
            packing: Cache::new(),
            patterns: Cache::new(),
            regions: Vec::new(),
            binomial,
        }
    }

    // Erase geometrically movable boxes to a fixed point, ignoring player access.
    fn frozen_boxes(&self, mut boxes: Mask) -> Mask {
        loop {
            let previous = boxes;
            let empty = self.floor & !boxes;
            let mut removable = 0;
            for direction in 0..DIRECTION_COUNT {
                removable |= if self.reverse {
                    shift(
                        (empty & shift(empty, direction ^ 1)) & self.live_cells,
                        direction ^ 1,
                    )
                } else {
                    shift(empty, direction) & shift(empty & self.live_cells, direction ^ 1)
                };
            }
            boxes &= !removable;
            if boxes == previous {
                return boxes;
            }
        }
    }

    // Removing accessible movable boxes grows the player region monotonically.
    fn inaccessible_boxes(&self, mut boxes: Mask, mut reachable: Mask) -> Mask {
        loop {
            let empty = self.floor & !boxes;
            let mut removable = 0;
            for direction in 0..DIRECTION_COUNT {
                removable |= if self.reverse {
                    boxes
                        & shift(
                            reachable & shift(empty, direction ^ 1) & self.live_cells,
                            direction ^ 1,
                        )
                } else {
                    boxes
                        & shift(reachable, direction)
                        & shift(empty & self.live_cells, direction ^ 1)
                };
            }
            if removable == 0 {
                return boxes;
            }
            boxes &= !removable;
            reachable = reachable_cells(reachable, self.floor & !boxes);
        }
    }

    // Restrict to a corral only when removing outside boxes enables no extra push
    // and every available boundary push goes inward.
    fn restrict_corral(&self, boxes: Mask, reachable: Mask) -> Mask {
        let mut unseen = self.floor & !(boxes | reachable);
        let fixed = self.frozen_boxes(boxes);
        while unseen != 0 {
            let corral = reachable_cells(
                cell_bit(lowest_cell(unseen)),
                self.floor & !(boxes | reachable),
            );
            unseen &= !corral;
            let border = boxes
                & ((corral << 1)
                    | (corral >> 1)
                    | (corral << BOARD_WIDTH)
                    | (corral >> BOARD_WIDTH));
            if ((border & !self.goals) | (corral & self.goals)) == 0 {
                continue;
            }
            let reduced = border | fixed;
            let relaxed = reachable_cells(reachable, self.floor & !reduced);
            let mut independent = true;
            let mut push_count = 0;
            for direction in 0..DIRECTION_COUNT {
                let possible = border
                    & shift(relaxed, direction)
                    & shift((self.floor & !reduced) & self.live_cells, direction ^ 1);
                let actual = border
                    & shift(reachable, direction)
                    & shift((self.floor & !boxes) & self.live_cells, direction ^ 1);
                if possible != actual || (shift(possible, direction) & !corral) != 0 {
                    independent = false;
                    break;
                }
                push_count += possible.count_ones();
            }
            if independent && push_count != 0 {
                return border;
            }
        }
        boxes
    }

    // Store indices plus one; zero remains the empty-slot marker.
    fn rehash(&mut self) {
        let size = if self.hash_table.is_empty() {
            INITIAL_HASH_SIZE
        } else {
            self.hash_table.len() * 2
        };
        self.hash_table = vec![0; size];
        for (index, node) in self.nodes.iter().enumerate() {
            let mut slot = hash_key(node.state) & (size - 1);
            while self.hash_table[slot] != 0 {
                slot = (slot + 1) & (size - 1);
            }
            self.hash_table[slot] = index as u32 + 1;
        }
    }

    fn state_slot(&mut self, state: Mask) -> usize {
        if self.hash_table.is_empty()
            || self.nodes.len() * HASH_LOAD_DENOMINATOR
                > self.hash_table.len() * HASH_LOAD_NUMERATOR
        {
            self.rehash();
        }
        let mask = self.hash_table.len() - 1;
        let mut slot = hash_key(state) & mask;
        while self.hash_table[slot] != 0 {
            if self.nodes[self.hash_table[slot] as usize - 1].state == state {
                break;
            }
            slot = (slot + 1) & mask;
        }
        slot
    }

    fn insert(&mut self, state: Mask, parent: u32, encoded_push: usize) -> usize {
        let slot = self.state_slot(state);
        let index = self.nodes.len();
        self.hash_table[slot] = index as u32 + 1;
        self.nodes.push(Node {
            state,
            parent,
            encoded_push: encoded_push as u16,
        });
        index
    }

    // Walk BFS uses up, down, left, right, including ties between shortest paths.
    fn shortest_walk(&self, boxes: Mask, player: usize, destination: usize) -> Option<Vec<u8>> {
        let mut queue = [0; CELL_COUNT];
        let mut previous = [usize::MAX; CELL_COUNT];
        let mut previous_direction = [0; CELL_COUNT];
        let mut tail = 1;
        queue[0] = player;
        previous[player] = player;
        let mut head = 0;
        while head < tail && previous[destination] == usize::MAX {
            let cell = queue[head];
            head += 1;
            for direction in 0..DIRECTION_COUNT {
                let next = neighbor(cell, direction);
                if next < CELL_COUNT
                    && self.floor & cell_bit(next) != 0
                    && boxes & cell_bit(next) == 0
                    && previous[next] == usize::MAX
                {
                    previous[next] = cell;
                    previous_direction[next] = direction;
                    queue[tail] = next;
                    tail += 1;
                }
            }
        }
        if previous[destination] == usize::MAX {
            return None;
        }
        let mut plan = Vec::new();
        let mut next = destination;
        while next != player {
            plan.push(DIRECTION_LETTER[previous_direction[next]]);
            next = previous[next];
        }
        plan.reverse();
        Some(plan)
    }

    // Reverse pulls become forward pushes in chain order; walks use actual positions.
    fn reconstruct_plan(&self, mut index: usize) -> Result<Vec<u8>, ()> {
        let mut pushes = Vec::new();
        while self.nodes[index].parent != NO_PARENT {
            pushes.push(self.nodes[index].encoded_push as usize);
            index = self.nodes[index].parent as usize;
        }
        if !self.reverse {
            pushes.reverse();
        }
        let mut boxes = self.initial_boxes;
        let mut player = self.initial_player;
        let mut plan = Vec::new();
        for encoded_push in pushes {
            let mut cell = encoded_push / DIRECTION_COUNT;
            let mut direction = encoded_push % DIRECTION_COUNT;
            if self.reverse {
                cell = neighbor(cell, direction);
                direction ^= 1;
            }
            plan.extend(
                self.shortest_walk(boxes, player, neighbor(cell, direction ^ 1))
                    .ok_or(())?,
            );
            plan.push(DIRECTION_LETTER[direction] - LETTER_CASE_OFFSET);
            boxes ^= cell_bit(cell) | cell_bit(neighbor(cell, direction));
            player = cell;
        }
        Ok(plan)
    }

    // Build the four live boundary strips lazily and skip duplicate masks.
    fn region_good(&mut self, boxes: Mask, reachable: Mask) -> bool {
        if self.regions.is_empty() {
            for axis in 0..2 {
                for side in 0..2 {
                    let mut minimum = BOARD_WIDTH;
                    let mut maximum = 0;
                    let mut remaining = self.floor;
                    while remaining != 0 {
                        let cell = lowest_cell(remaining);
                        remaining &= remaining - 1;
                        let coordinate = if axis != 0 {
                            cell / BOARD_WIDTH
                        } else {
                            cell % BOARD_WIDTH
                        };
                        minimum = minimum.min(coordinate);
                        maximum = maximum.max(coordinate);
                    }
                    let mut mask = 0;
                    remaining = self.live_cells;
                    while remaining != 0 {
                        let cell = lowest_cell(remaining);
                        remaining &= remaining - 1;
                        let coordinate = if axis != 0 {
                            cell / BOARD_WIDTH
                        } else {
                            cell % BOARD_WIDTH
                        };
                        if if side != 0 {
                            coordinate + REGION_WIDTH > maximum
                        } else {
                            coordinate < minimum + REGION_WIDTH
                        } {
                            mask |= cell_bit(cell);
                        }
                    }
                    if mask == 0 || self.regions.iter().any(|region| region.mask == mask) {
                        continue;
                    }
                    self.regions.push(Region::build(
                        mask,
                        self.floor,
                        self.goals,
                        self.initial_boxes.count_ones(),
                    ));
                }
            }
        }
        self.regions
            .iter()
            .all(|region| region.solvable_players[region.index(boxes)] & reachable != 0)
    }

    // Pull-erase goal boxes from each final component, retaining the fixed boxes.
    fn packing_good(&mut self, boxes: Mask, reachable: Mask, fixed: Mask) -> bool {
        let index = if let Some(index) = self.packing.find(fixed) {
            index
        } else {
            let mut results = Vec::new();
            let mut todo = self.floor & !self.goals;
            while todo != 0 {
                let mut remaining_goals = self.goals;
                let mut from_goals =
                    reachable_cells(cell_bit(lowest_cell(todo)), self.floor & !self.goals);
                todo &= !from_goals;
                loop {
                    let empty = self.floor & !remaining_goals;
                    let mut movable = 0;
                    for direction in 0..DIRECTION_COUNT {
                        movable |= remaining_goals
                            & shift(from_goals & shift(empty, direction ^ 1), direction ^ 1);
                    }
                    movable &= !fixed;
                    if movable == 0 {
                        break;
                    }
                    remaining_goals &= !movable;
                    from_goals = reachable_cells(from_goals, self.floor & !remaining_goals);
                }
                results.push((remaining_goals, from_goals));
            }
            self.packing.insert(fixed, results)
        };
        self.packing.entries[index]
            .1
            .iter()
            .any(|&(residue, region)| residue & !boxes == 0 && region & reachable != 0)
    }

    fn pattern_good(&mut self, boxes: Mask, reachable: Mask, fixed: Mask) -> bool {
        let index = if let Some(index) = self.patterns.find(fixed) {
            index
        } else {
            let table = Pattern::build(
                self.floor & !fixed,
                self.target_boxes & !fixed,
                self.pattern_size,
                self.reverse,
                self.initial_player,
                &self.binomial,
            );
            self.patterns.insert(fixed, table)
        };
        let table = &self.patterns.entries[index].1;
        if table.subset_size == 0 {
            return true;
        }
        if (boxes & !fixed) & !table.live_cells != 0 {
            return false;
        }
        let moved =
            if self.moved_box != 0 && fixed == self.parent_frozen && self.moved_box & fixed == 0 {
                table.cell_index[lowest_cell(self.moved_box)]
            } else {
                usize::MAX
            };
        let mut indices = [0; MAX_BOXES];
        let mut count = 0;
        let mut remaining = boxes & !fixed;
        while remaining != 0 {
            indices[count] = table.cell_index[lowest_cell(remaining)];
            count += 1;
            remaining &= remaining - 1;
        }
        table.subsets_good(
            &indices[..count],
            0,
            1,
            0,
            moved,
            false,
            reachable,
            &self.binomial,
        )
    }

    // Distances treat frozen goal boxes as walls. Weighted probes also charge for
    // crossing an occupied box cell or support cell, using queue relaxation.
    fn compute_distances(&self, boxes: Mask, frozen: Mask) -> GoalDistances {
        let mut distances = [[UNREACHABLE; CELL_COUNT]; MAX_BOXES];
        let available = self.floor & !frozen;
        for (goal_index, cell_distance) in distances.iter_mut().enumerate().take(self.goal_count) {
            let goal = self.goal_cells[goal_index];
            cell_distance[goal] = 0;
            if frozen & cell_bit(goal) != 0 {
                continue;
            }
            if self.crossing_penalty == 0 {
                let mut queue = [0; CELL_COUNT];
                let mut head = 0;
                let mut tail = 1;
                queue[0] = goal;
                while head < tail {
                    let cell = queue[head];
                    head += 1;
                    for direction in 0..DIRECTION_COUNT {
                        let next = neighbor(cell, direction);
                        let support = if self.reverse {
                            neighbor(cell, direction ^ 1)
                        } else {
                            neighbor(next, direction)
                        };
                        if next >= CELL_COUNT
                            || support >= CELL_COUNT
                            || available & cell_bit(next) == 0
                            || available & cell_bit(support) == 0
                            || cell_distance[next] < UNREACHABLE
                        {
                            continue;
                        }
                        cell_distance[next] = cell_distance[cell] + 1;
                        queue[tail] = next;
                        tail += 1;
                    }
                }
            } else {
                let mut queue = [0; DISTANCE_QUEUE_SIZE];
                let mut queued = [false; CELL_COUNT];
                let mut head = 0;
                let mut tail = 1;
                queue[0] = goal;
                queued[goal] = true;
                while head != tail {
                    let cell = queue[head];
                    head = (head + 1) & DISTANCE_QUEUE_MASK;
                    queued[cell] = false;
                    let distance = cell_distance[cell];
                    for direction in 0..DIRECTION_COUNT {
                        let next = neighbor(cell, direction);
                        let support = if self.reverse {
                            neighbor(cell, direction ^ 1)
                        } else {
                            neighbor(next, direction)
                        };
                        if next >= CELL_COUNT
                            || support >= CELL_COUNT
                            || available & cell_bit(next) == 0
                            || available & cell_bit(support) == 0
                        {
                            continue;
                        }
                        let cost = 1
                            + self.crossing_penalty * i32::from(boxes & cell_bit(cell) != 0)
                            + self.crossing_penalty * i32::from(boxes & cell_bit(support) != 0);
                        let next_distance = distance + cost;
                        if next_distance < cell_distance[next] {
                            cell_distance[next] = next_distance;
                            if !queued[next] {
                                queue[tail] = next;
                                tail = (tail + 1) & DISTANCE_QUEUE_MASK;
                                queued[next] = true;
                            }
                        }
                    }
                }
            }
        }
        distances
    }

    // Hungarian matching preserves ascending goal order and strict slack ties.
    fn matching(boxes: Mask, distances: &GoalDistances) -> i32 {
        let mut box_cells = [0; MATCHING_SIZE];
        let mut box_count = 0;
        let mut remaining = boxes;
        while remaining != 0 {
            box_count += 1;
            box_cells[box_count] = lowest_cell(remaining);
            remaining &= remaining - 1;
        }
        let mut box_potential = [0; MATCHING_SIZE];
        let mut goal_potential = [0; MATCHING_SIZE];
        let mut matched_box = [0; MATCHING_SIZE];
        let mut previous_goal = [0; MATCHING_SIZE];
        for index in 1..=box_count {
            matched_box[0] = index;
            let mut current_goal = 0;
            let mut slack = [UNREACHABLE; MATCHING_SIZE];
            let mut visited = [false; MATCHING_SIZE];
            loop {
                visited[current_goal] = true;
                let current_box = matched_box[current_goal];
                let mut adjustment = UNREACHABLE;
                let mut next_goal = 0;
                for goal in 1..=box_count {
                    if !visited[goal] {
                        let cost = distances[goal - 1][box_cells[current_box]];
                        let reduced = cost - box_potential[current_box] - goal_potential[goal];
                        if reduced < slack[goal] {
                            slack[goal] = reduced;
                            previous_goal[goal] = current_goal;
                        }
                        if slack[goal] < adjustment {
                            adjustment = slack[goal];
                            next_goal = goal;
                        }
                    }
                }
                if adjustment >= UNREACHABLE {
                    return -1;
                }
                for goal in 0..=box_count {
                    if visited[goal] {
                        box_potential[matched_box[goal]] += adjustment;
                        goal_potential[goal] -= adjustment;
                    } else {
                        slack[goal] -= adjustment;
                    }
                }
                current_goal = next_goal;
                if matched_box[current_goal] == 0 {
                    break;
                }
            }
            loop {
                let next_goal = previous_goal[current_goal];
                matched_box[current_goal] = matched_box[next_goal];
                current_goal = next_goal;
                if current_goal == 0 {
                    break;
                }
            }
        }
        for goal in 1..=box_count {
            if distances[goal - 1][box_cells[matched_box[goal]]] >= UNREACHABLE {
                return -1;
            }
        }
        -goal_potential[0]
    }

    // Component-dependent deadlocks precede the box-only matching cache.
    fn heuristic(&mut self, boxes: Mask, reachable: Mask) -> i32 {
        if self.inaccessible_boxes(boxes, reachable) & !self.target_boxes != 0 {
            return -1;
        }
        let frozen = self.frozen_boxes(boxes);
        if frozen & !self.target_boxes != 0 {
            return -1;
        }
        if self.regional
            && (!self.packing_good(boxes, reachable, frozen) || !self.region_good(boxes, reachable))
        {
            return -1;
        }
        if self.pattern_size != 0 && !self.pattern_good(boxes, reachable, frozen) {
            return -1;
        }
        if let Some(index) = self.heuristic_cache.find(boxes) {
            return self.heuristic_cache.entries[index].1;
        }
        let estimate = if self.crossing_penalty == 0 {
            let index = if let Some(index) = self.distance_cache.find(frozen) {
                index
            } else {
                let distances = self.compute_distances(boxes, frozen);
                self.distance_cache.insert(frozen, distances)
            };
            Self::matching(boxes, &self.distance_cache.entries[index].1)
        } else {
            Self::matching(boxes, &self.compute_distances(boxes, frozen))
        };
        self.heuristic_cache.insert(boxes, estimate);
        estimate
    }

    // Rejected states are remembered only during the capped fast chain.
    fn add(
        &mut self,
        boxes: Mask,
        reachable: Mask,
        parent: u32,
        encoded_push: usize,
        push_depth: i32,
        depth: &mut Vec<i32>,
        open: &mut BinaryHeap<Reverse<(i32, i32)>>,
    ) {
        let state = state_key(boxes, reachable);
        let slot = self.state_slot(state);
        if self.hash_table[slot] != 0 {
            return;
        }
        let mut estimate = self.heuristic(boxes, reachable);
        if estimate >= 0 && self.regional && self.packing_weight != 0 {
            let fixed = boxes & self.goals;
            self.packing_good(boxes, reachable, fixed);
            let index = self.packing.find(fixed).unwrap();
            let mut missing = MAX_BOXES as i32;
            for &(residue, _) in &self.packing.entries[index].1 {
                missing = missing.min((residue & !boxes).count_ones() as i32);
            }
            estimate += self.packing_weight * missing;
        }
        if estimate < 0 {
            if self.fast {
                self.insert(state, NO_PARENT, 0);
                depth.push(-1);
            }
            return;
        }
        let index = self.insert(state, parent, encoded_push);
        depth.push(push_depth);
        let score = PRIORITY_SCALE * (estimate - if self.regional { push_depth } else { 0 });
        open.push(Reverse((score, -(index as i32))));
    }

    // Push and pull searches keep the first parent and prefer newer equal scores.
    fn attempt(
        &mut self,
        reverse: bool,
        crossing_penalty: i32,
        regional: bool,
        table_size: usize,
        expansion_limit: i32,
    ) -> Result<Vec<u8>, ()> {
        self.reverse = reverse;
        self.crossing_penalty = crossing_penalty;
        self.regional = regional;
        self.pattern_size = table_size;
        self.moved_box = 0;
        self.parent_frozen = 0;
        self.goal_count = 0;
        self.nodes.clear();
        self.hash_table.clear();
        self.heuristic_cache.clear();
        self.distance_cache.clear();
        self.patterns.clear();
        self.target_boxes = if reverse {
            self.initial_boxes
        } else {
            self.goals
        };
        let mut remaining = self.target_boxes;
        while remaining != 0 {
            self.goal_cells[self.goal_count] = lowest_cell(remaining);
            self.goal_count += 1;
            remaining &= remaining - 1;
        }
        self.live_cells = self.target_boxes;
        loop {
            let previous = self.live_cells;
            for direction in 0..DIRECTION_COUNT {
                self.live_cells |= if reverse {
                    shift(self.live_cells & shift(self.floor, direction), direction) & self.floor
                } else {
                    shift(self.live_cells, direction)
                        & shift(self.floor, direction ^ 1)
                        & self.floor
                };
            }
            if previous == self.live_cells {
                break;
            }
        }
        let mut open = BinaryHeap::new();
        let mut depth = Vec::new();
        if reverse {
            let mut todo = self.floor & !self.goals;
            while todo != 0 {
                let reachable =
                    reachable_cells(cell_bit(lowest_cell(todo)), self.floor & !self.goals);
                self.add(
                    self.goals, reachable, NO_PARENT, 0, 0, &mut depth, &mut open,
                );
                todo &= !reachable;
            }
        } else {
            self.add(
                self.initial_boxes,
                reachable_cells(
                    cell_bit(self.initial_player),
                    self.floor & !self.initial_boxes,
                ),
                NO_PARENT,
                0,
                0,
                &mut depth,
                &mut open,
            );
        }
        let mut expanded = 0;
        let mut solved = None;
        let initial_reach = reachable_cells(
            cell_bit(self.initial_player),
            self.floor & !self.initial_boxes,
        );
        while !open.is_empty() && expanded < expansion_limit {
            if self.fast
                && (self.nodes.len() >= NODE_CAP
                    || (expanded & CLOCK_CHECK_MASK == 0
                        && self.started.elapsed().as_secs_f64() > FAST_SECONDS))
            {
                break;
            }
            let Reverse((_, negative_index)) = open.pop().unwrap();
            let index = (-negative_index) as usize;
            let state = self.nodes[index].state;
            let boxes = state & BOX_BITS;
            let reachable = reachable_cells(
                cell_bit((state >> PLAYER_SHIFT) as usize),
                self.floor & !boxes,
            );
            if boxes == self.target_boxes && (!reverse || reachable & initial_reach != 0) {
                solved = Some(index);
                break;
            }
            expanded += 1;
            if self.pattern_size != 0 {
                self.parent_frozen = self.frozen_boxes(boxes);
            }
            let empty = self.floor & !boxes;
            let allowed = if reverse {
                boxes
            } else {
                self.restrict_corral(boxes, reachable)
            };
            for direction in 0..DIRECTION_COUNT {
                let mut movable = if reverse {
                    boxes
                        & shift(
                            reachable & shift(empty, direction ^ 1) & self.live_cells,
                            direction ^ 1,
                        )
                } else {
                    allowed
                        & shift(reachable, direction)
                        & shift(empty & self.live_cells, direction ^ 1)
                };
                while movable != 0 {
                    let cell = lowest_cell(movable);
                    movable &= movable - 1;
                    let next = neighbor(cell, direction);
                    let next_boxes = boxes ^ cell_bit(cell) ^ cell_bit(next);
                    let player = if reverse {
                        neighbor(next, direction)
                    } else {
                        cell
                    };
                    let next_reachable =
                        reachable_cells(cell_bit(player), self.floor & !next_boxes);
                    self.moved_box = cell_bit(next);
                    self.add(
                        next_boxes,
                        next_reachable,
                        index as u32,
                        cell * DIRECTION_COUNT + direction,
                        depth[index] + 1,
                        &mut depth,
                        &mut open,
                    );
                }
            }
        }
        let mut plan = if let Some(index) = solved {
            self.reconstruct_plan(index)?
        } else {
            Vec::new()
        };
        if plan.len() > MAX_PLAN_LENGTH {
            plan.clear();
        }
        Ok(plan)
    }

    fn geometry(&self) -> [Mask; GEOMETRY_COMPONENTS] {
        [
            self.floor,
            self.goals,
            self.initial_boxes,
            self.initial_player as Mask,
        ]
    }

    fn set_geometry(&mut self, geometry: [Mask; GEOMETRY_COMPONENTS]) {
        self.floor = geometry[0];
        self.goals = geometry[1];
        self.initial_boxes = geometry[2];
        self.initial_player = geometry[PLAYER_COMPONENT] as usize;
    }

    // Cheap forward and reverse probes precede four rotated forward restarts.
    fn cheap_probes(&mut self) -> Result<Vec<u8>, ()> {
        let mut plan = self.attempt(false, 1, false, 0, INITIAL_EXPANSIONS)?;
        if plan.is_empty() {
            plan = self.attempt(true, 0, false, 0, INITIAL_EXPANSIONS)?;
        }
        if plan.is_empty() {
            let saved = self.geometry();
            let mut turns = 0;
            for turn in 1..=ROTATION_COUNT {
                self.floor = transform_mask(self.floor, 1);
                self.goals = transform_mask(self.goals, 1);
                self.initial_boxes = transform_mask(self.initial_boxes, 1);
                self.initial_player = rotate_cell(self.initial_player);
                plan = self.attempt(false, 2, false, 0, ROTATED_EXPANSIONS)?;
                turns = turn;
                if !plan.is_empty() {
                    break;
                }
            }
            self.set_geometry(saved);
            for _ in 0..turns {
                for letter in &mut plan {
                    let upper = *letter < b'a';
                    let lower = if upper {
                        *letter + LETTER_CASE_OFFSET
                    } else {
                        *letter
                    };
                    let direction = DIRECTION_LETTER
                        .iter()
                        .position(|&value| value == lower)
                        .unwrap();
                    *letter = ROTATED_LETTER[direction];
                    if upper {
                        *letter -= LETTER_CASE_OFFSET;
                    }
                }
            }
        }
        Ok(plan)
    }

    // Choose the lexicographically least geometry before the regional search.
    fn run_fast(&mut self) -> Result<Vec<u8>, ()> {
        let mut plan = self.cheap_probes()?;
        if plan.is_empty() {
            let saved = self.geometry();
            let mut best_geometry = saved;
            let mut best_symmetry = 0;
            for symmetry in 1..SYMMETRY_COUNT {
                let geometry = [
                    transform_mask(saved[0], symmetry),
                    transform_mask(saved[1], symmetry),
                    transform_mask(saved[2], symmetry),
                    transform_cell(saved[PLAYER_COMPONENT] as usize, symmetry) as Mask,
                ];
                if geometry < best_geometry {
                    best_geometry = geometry;
                    best_symmetry = symmetry;
                }
            }
            self.set_geometry(best_geometry);
            self.packing.clear();
            self.regions.clear();
            self.packing_weight = PACKING_WEIGHT;
            plan = self.attempt(false, 0, true, 0, UNBOUNDED_EXPANSIONS)?;
            let mut inverse_direction = [0; DIRECTION_COUNT];
            for direction in 0..DIRECTION_COUNT {
                let step = transform_cell(neighbor(DIRECTION_PROBE_CELL, direction), best_symmetry)
                    as i32
                    - transform_cell(DIRECTION_PROBE_CELL, best_symmetry) as i32;
                for other in 0..DIRECTION_COUNT {
                    if DIRECTION_STEP[other] == step {
                        inverse_direction[other] = direction;
                    }
                }
            }
            for letter in &mut plan {
                let upper = *letter < b'a';
                let lower = if upper {
                    *letter + LETTER_CASE_OFFSET
                } else {
                    *letter
                };
                let direction = DIRECTION_LETTER
                    .iter()
                    .position(|&value| value == lower)
                    .unwrap();
                *letter = DIRECTION_LETTER[inverse_direction[direction]];
                if upper {
                    *letter -= LETTER_CASE_OFFSET;
                }
            }
            self.set_geometry(saved);
        }
        Ok(plan)
    }

    // Release fast-search storage before constructing fallback tables.
    fn release(&mut self) {
        self.nodes = Vec::new();
        self.hash_table = Vec::new();
        self.heuristic_cache = Cache::new();
        self.distance_cache = Cache::new();
        self.packing = Cache::new();
        self.regions = Vec::new();
    }

    // Exact-player A* reopens cheaper states and counts both walking and pushes.
    fn length_fallback(&mut self) -> Result<Vec<u8>, ()> {
        self.reverse = false;
        self.crossing_penalty = 0;
        self.pattern_size = 0;
        self.moved_box = 0;
        self.nodes.clear();
        self.hash_table.clear();
        self.heuristic_cache.clear();
        self.distance_cache.clear();
        self.patterns.clear();
        let mut cost = vec![0];
        let mut open = BinaryHeap::new();
        self.insert(
            state_key(self.initial_boxes, cell_bit(self.initial_player)),
            NO_PARENT,
            0,
        );
        open.push(Reverse((0, 0, 0)));
        while let Some(Reverse((_, path_cost, index))) = open.pop() {
            if path_cost != cost[index] {
                continue;
            }
            let state = self.nodes[index].state;
            let boxes = state & BOX_BITS;
            let player = (state >> PLAYER_SHIFT) as usize;
            if boxes == self.goals {
                return self.reconstruct_plan(index);
            }
            let mut walk_distance = [-1; CELL_COUNT];
            let mut queue = [0; CELL_COUNT];
            let mut tail = 1;
            walk_distance[player] = 0;
            queue[0] = player;
            let mut reachable = 0;
            let mut head = 0;
            while head < tail {
                let cell = queue[head];
                head += 1;
                reachable |= cell_bit(cell);
                for direction in 0..DIRECTION_COUNT {
                    let next = neighbor(cell, direction);
                    if next < CELL_COUNT
                        && self.floor & cell_bit(next) != 0
                        && boxes & cell_bit(next) == 0
                        && walk_distance[next] < 0
                    {
                        walk_distance[next] = walk_distance[cell] + 1;
                        queue[tail] = next;
                        tail += 1;
                    }
                }
            }
            for direction in 0..DIRECTION_COUNT {
                let mut movable = boxes
                    & shift(reachable, direction)
                    & shift((self.floor & !boxes) & self.live_cells, direction ^ 1);
                while movable != 0 {
                    let cell = lowest_cell(movable);
                    movable &= movable - 1;
                    let next = neighbor(cell, direction);
                    let next_cost = path_cost + walk_distance[neighbor(cell, direction ^ 1)] + 1;
                    if next_cost > MAX_PLAN_LENGTH as i32 {
                        continue;
                    }
                    let next_boxes = boxes ^ cell_bit(cell) ^ cell_bit(next);
                    let state = state_key(next_boxes, cell_bit(cell));
                    let slot = self.state_slot(state);
                    let mut next_index = if self.hash_table[slot] == 0 {
                        None
                    } else {
                        Some(self.hash_table[slot] as usize - 1)
                    };
                    if let Some(index) = next_index {
                        if cost[index] <= next_cost {
                            continue;
                        }
                    }
                    let estimate = self.heuristic(
                        next_boxes,
                        reachable_cells(cell_bit(cell), self.floor & !next_boxes),
                    );
                    if estimate < 0 || next_cost + estimate > MAX_PLAN_LENGTH as i32 {
                        continue;
                    }
                    if let Some(next_index) = next_index {
                        self.nodes[next_index].parent = index as u32;
                        self.nodes[next_index].encoded_push =
                            (cell * DIRECTION_COUNT + direction) as u16;
                        cost[next_index] = next_cost;
                    } else {
                        next_index = Some(self.insert(
                            state,
                            index as u32,
                            cell * DIRECTION_COUNT + direction,
                        ));
                        cost.push(next_cost);
                    }
                    open.push(Reverse((
                        next_cost + estimate,
                        next_cost,
                        next_index.unwrap(),
                    )));
                }
            }
        }
        Ok(Vec::new())
    }

    // Escalate from three-box to five-box tables, then enforce exact move costs.
    fn run_safe(&mut self) -> Result<Vec<u8>, ()> {
        let mut plan = self.cheap_probes()?;
        if plan.is_empty() {
            let limit = if self.initial_boxes.count_ones() <= 10 {
                SMALL_BOX_EXPANSIONS
            } else {
                MANY_BOX_EXPANSIONS
            };
            plan = self.attempt(false, 0, false, SMALL_PATTERN_SIZE, limit)?;
        }
        if plan.is_empty() {
            plan = self.attempt(false, 0, false, LARGE_PATTERN_SIZE, UNBOUNDED_EXPANSIONS)?;
        }
        if plan.is_empty() {
            plan = self.length_fallback()?;
        }
        Ok(plan)
    }
}

// Replay every letter, including push case, and require the exact original goals.
fn valid(plan: &[u8], geometry: [Mask; GEOMETRY_COMPONENTS]) -> bool {
    if plan.len() > MAX_PLAN_LENGTH {
        return false;
    }
    let floor = geometry[0];
    let goals = geometry[1];
    let mut boxes = geometry[2];
    let mut player = geometry[PLAYER_COMPONENT] as usize;
    for &letter in plan {
        let push = letter < b'a';
        let lower = if push {
            letter + LETTER_CASE_OFFSET
        } else {
            letter
        };
        let direction = match DIRECTION_LETTER.iter().position(|&value| value == lower) {
            Some(direction) => direction,
            None => return false,
        };
        let next = neighbor(player, direction);
        if next >= CELL_COUNT || floor & cell_bit(next) == 0 {
            return false;
        }
        if boxes & cell_bit(next) != 0 {
            let destination = neighbor(next, direction);
            if !push
                || destination >= CELL_COUNT
                || floor & cell_bit(destination) == 0
                || boxes & cell_bit(destination) != 0
            {
                return false;
            }
            boxes ^= cell_bit(next) | cell_bit(destination);
        } else if push {
            return false;
        }
        player = next;
    }
    boxes == goals
}

fn main() {
    let started = Instant::now();
    let mut input = Vec::new();
    io::stdin().read_to_end(&mut input).unwrap();
    let mut floor = 0;
    let mut goals = 0;
    let mut boxes = 0;
    let mut player = 0;
    let mut row = 0;
    for line in input.split(|&byte| byte == b'\n') {
        let line = line.strip_suffix(b"\r").unwrap_or(line);
        if line.is_empty() {
            continue;
        }
        for (column, &tile) in line.iter().enumerate().take(BOARD_WIDTH) {
            let cell = row * BOARD_WIDTH + column;
            if tile != b'#' {
                floor |= cell_bit(cell);
            }
            if tile == b'.' || tile == b'*' || tile == b'+' {
                goals |= cell_bit(cell);
            }
            if tile == b'$' || tile == b'*' {
                boxes |= cell_bit(cell);
            }
            if tile == b'@' || tile == b'+' {
                player = cell;
            }
        }
        row += 1;
    }
    floor = reachable_cells(cell_bit(player), floor);
    goals &= floor;
    boxes &= floor;
    let mut plan = Vec::new();
    if boxes != goals {
        let mut solver = Solver::new(started, floor, goals, boxes, player);
        let original = solver.geometry();
        plan = solver.run_fast().unwrap_or_default();
        if !valid(&plan, original) {
            solver.release();
            solver.fast = false;
            solver.set_geometry(original);
            plan = solver.run_safe().unwrap();
        }
    }
    plan.push(b'\n');
    io::stdout().lock().write_all(&plan).unwrap();
}
