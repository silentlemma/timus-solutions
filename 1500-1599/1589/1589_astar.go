package main

import (
	"bufio"
	"math/bits"
	"os"
	"runtime"
	"time"
)

const (
	boardWidth                  = 8
	cellCount                   = 64
	lastCoordinate              = boardWidth - 1
	directionCount              = 4
	playerShift                 = 56
	boxBits              uint64 = 0x00ffffffffffffff
	maxBoxes                    = 36
	matchingSize                = maxBoxes + 1
	maxPlanLength               = 10000
	unreachableDistance         = 10000
	letterCaseOffset            = 32
	initialHashSize             = 65536
	hashLoadNumerator           = 7
	hashLoadDenominator         = 10
	hashShiftFirst              = 30
	hashShiftSecond             = 27
	hashShiftLast               = 31
	hashMultiplierFirst  uint64 = 0xbf58476d1ce4e5b9
	hashMultiplierSecond uint64 = 0x94d049bb133111eb
	distanceQueueSize           = 128
	distanceQueueMask           = distanceQueueSize - 1
	byteBits                    = 8
	byteValues                  = 256
	byteMask                    = byteValues - 1
	regionWidth                 = 3
	smallPatternSize            = 3
	largePatternSize            = 5
	patternSizeCount            = largePatternSize + 1
	priorityScale               = 100
	defaultPackingWeight        = 30
	initialExpansions           = 128
	rotatedExpansions           = 64
	smallBoxExpansions          = 4000
	manyBoxExpansions           = 256
	unboundedExpansions         = 2147483647
	nodeCap                     = 600000
	fastDuration                = time.Second
	clockCheckMask              = 255
	rotationCount               = 4
	symmetryCount               = 8
	reflectionFlag              = 4
	rotationMask                = 3
	geometryComponents          = 4
	playerComponent             = 3
	directionProbeCell          = 27
	noParent                    = ^uint32(0)
)

var (
	started                                      = time.Now()
	fastMode                                     = true
	directionStep                                = [directionCount]int{-boardWidth, boardWidth, -1, 1}
	directionLetter                              = "udlr"
	floorMask, goalMask, initialBoxes, liveCells uint64
	initialPlayer                                int
	reverseMode                                  bool
)

func lowestCell(mask uint64) int { return bits.TrailingZeros64(mask) }
func countBits(mask uint64) int  { return bits.OnesCount64(mask) }
func cellBit(cell int) uint64    { return uint64(1) << uint(cell) }
func timeUp() bool               { return time.Since(started) > fastDuration }
func minInt(first, second int) int {
	if first < second {
		return first
	}
	return second
}

// The wall border prevents horizontal shifts from wrapping into usable cells.
func shift(mask uint64, direction int) uint64 {
	switch direction {
	case 0:
		return mask >> boardWidth
	case 1:
		return mask << boardWidth
	case 2:
		return mask >> 1
	default:
		return mask << 1
	}
}

// Expand the player's component until no adjacent free cell remains.
func reachableCells(reachable, floor uint64) uint64 {
	for {
		expanded := (reachable | reachable<<boardWidth | reachable>>boardWidth |
			reachable<<1 | reachable>>1) & floor
		if expanded == reachable {
			return reachable
		}
		reachable = expanded
	}
}

// Boxes fit below the top byte, which stores the lowest reachable player cell.
func stateKey(boxMask, reachable uint64) uint64 {
	return boxMask | uint64(lowestCell(reachable))<<playerShift
}
func stateBoxes(state uint64) uint64 { return state & boxBits }

// Mix every key bit before linear probing in a power-of-two table.
func hashKey(state uint64) uint64 {
	state ^= state >> hashShiftFirst
	state *= hashMultiplierFirst
	state ^= state >> hashShiftSecond
	state *= hashMultiplierSecond
	return state ^ state>>hashShiftLast
}
func rotateCell(cell int) int {
	return cell%boardWidth*boardWidth + lastCoordinate - cell/boardWidth
}
func rotateMask(mask uint64) uint64 {
	var result uint64
	for ; mask != 0; mask &= mask - 1 {
		result |= cellBit(rotateCell(lowestCell(mask)))
	}
	return result
}

// Erase geometrically movable boxes to a fixed point, ignoring player access.
func frozenBoxes(boxMask uint64) uint64 {
	for {
		previous := boxMask
		emptyCells, removable := floorMask&^boxMask, uint64(0)
		for direction := 0; direction < directionCount; direction++ {
			if !reverseMode {
				removable |= shift(emptyCells, direction) &
					shift(emptyCells&liveCells, direction^1)
			} else {
				removable |= shift(emptyCells&shift(emptyCells, direction^1)&
					liveCells, direction^1)
			}
		}
		boxMask &^= removable
		if boxMask == previous {
			return boxMask
		}
	}
}

type node struct {
	state  uint64
	parent uint32
	move   uint16
}

var nodes []node
var hashTable []uint32

// Indices plus one leave zero available as an empty hash slot.
func rehash() {
	size := initialHashSize
	if len(hashTable) != 0 {
		size = len(hashTable) * 2
	}
	hashTable = make([]uint32, size)
	for index := range nodes {
		slot := int(hashKey(nodes[index].state)) & (size - 1)
		for hashTable[slot] != 0 {
			slot = (slot + 1) & (size - 1)
		}
		hashTable[slot] = uint32(index + 1)
	}
}
func findSlot(state uint64) int {
	if len(hashTable) == 0 ||
		len(nodes)*hashLoadDenominator > len(hashTable)*hashLoadNumerator {
		rehash()
	}
	slot := int(hashKey(state)) & (len(hashTable) - 1)
	for hashTable[slot] != 0 && nodes[hashTable[slot]-1].state != state {
		slot = (slot + 1) & (len(hashTable) - 1)
	}
	return slot
}
func insert(state uint64, parent uint32, move int) int {
	slot := findSlot(state)
	if hashTable[slot] != 0 {
		return -1
	}
	hashTable[slot] = uint32(len(nodes) + 1)
	nodes = append(nodes, node{state, parent, uint16(move)})
	return len(nodes) - 1
}

// A typed binary heap preserves the C++ lexicographic priority and tie order.
type entry struct{ score, tie, id int32 }
type priorityQueue []entry

func lessEntry(first, second entry) bool {
	if first.score != second.score {
		return first.score < second.score
	}
	if first.tie != second.tie {
		return first.tie < second.tie
	}
	return first.id < second.id
}
func (queue *priorityQueue) push(value entry) {
	*queue = append(*queue, value)
	index := len(*queue) - 1
	for index > 0 {
		parent := (index - 1) / 2
		if !lessEntry(value, (*queue)[parent]) {
			break
		}
		(*queue)[index] = (*queue)[parent]
		index = parent
	}
	(*queue)[index] = value
}
func (queue *priorityQueue) pop() entry {
	result := (*queue)[0]
	last := (*queue)[len(*queue)-1]
	*queue = (*queue)[:len(*queue)-1]
	if len(*queue) == 0 {
		return result
	}
	index := 0
	for {
		child := index*2 + 1
		if child >= len(*queue) {
			break
		}
		if child+1 < len(*queue) && lessEntry((*queue)[child+1], (*queue)[child]) {
			child++
		}
		if !lessEntry((*queue)[child], last) {
			break
		}
		(*queue)[index] = (*queue)[child]
		index = child
	}
	(*queue)[index] = last
	return result
}

// The box-only heuristic cache uses primitive slots; zero marks an empty value.
type estimateCache struct {
	keys   []uint64
	values []int32
	size   int
}

func (cache *estimateCache) get(key uint64) (int, bool) {
	if len(cache.keys) == 0 {
		return 0, false
	}
	slot := int(hashKey(key)) & (len(cache.keys) - 1)
	for cache.values[slot] != 0 {
		if cache.keys[slot] == key {
			return int(cache.values[slot]) - 2, true
		}
		slot = (slot + 1) & (len(cache.keys) - 1)
	}
	return 0, false
}
func (cache *estimateCache) put(key uint64, value int) int {
	if len(cache.keys) == 0 ||
		cache.size*hashLoadDenominator > len(cache.keys)*hashLoadNumerator {
		size := initialHashSize
		if len(cache.keys) != 0 {
			size = len(cache.keys) * 2
		}
		oldKeys, oldValues := cache.keys, cache.values
		cache.keys, cache.values = make([]uint64, size), make([]int32, size)
		cache.size = 0
		for index, encoded := range oldValues {
			if encoded != 0 {
				cache.put(oldKeys[index], int(encoded)-2)
			}
		}
	}
	slot := int(hashKey(key)) & (len(cache.keys) - 1)
	for cache.values[slot] != 0 && cache.keys[slot] != key {
		slot = (slot + 1) & (len(cache.keys) - 1)
	}
	if cache.values[slot] == 0 {
		cache.size++
	}
	cache.keys[slot], cache.values[slot] = key, int32(value+2)
	return value
}
func (cache *estimateCache) reset() {
	for index := range cache.values {
		cache.values[index] = 0
	}
	cache.size = 0
}

type failedWalk struct{}

// Breadth-first walks use the same up, down, left, right order as the search.
func shortestWalk(boxMask uint64, player *int, destination int) []byte {
	var queue, previousCell, previousDirection [cellCount]int
	for index := range previousCell {
		previousCell[index] = -1
	}
	queue[0], previousCell[*player] = *player, *player
	tail := 1
	for head := 0; head < tail && previousCell[destination] < 0; head++ {
		for direction, step := range directionStep {
			nextCell := queue[head] + step
			if nextCell >= 0 && nextCell < cellCount && floorMask&cellBit(nextCell) != 0 &&
				boxMask&cellBit(nextCell) == 0 && previousCell[nextCell] < 0 {
				previousCell[nextCell], previousDirection[nextCell] = queue[head], direction
				queue[tail] = nextCell
				tail++
			}
		}
	}
	if previousCell[destination] < 0 {
		panic(failedWalk{})
	}
	var plan []byte
	for cell := destination; cell != *player; cell = previousCell[cell] {
		plan = append(plan, directionLetter[previousDirection[cell]])
	}
	reverseBytes(plan)
	*player = destination
	return plan
}
func reverseBytes(data []byte) {
	for left, right := 0, len(data)-1; left < right; left, right = left+1, right-1 {
		data[left], data[right] = data[right], data[left]
	}
}

// Reverse pulls become forward pushes in chain order; rebuild the intervening walks.
func reconstructPlan(id int) []byte {
	var pushes []uint16
	for nodes[id].parent != noParent {
		pushes = append(pushes, nodes[id].move)
		id = int(nodes[id].parent)
	}
	if !reverseMode {
		for left, right := 0, len(pushes)-1; left < right; left, right = left+1, right-1 {
			pushes[left], pushes[right] = pushes[right], pushes[left]
		}
	}
	boxMask, player := initialBoxes, initialPlayer
	var plan []byte
	for _, encoded := range pushes {
		cell, direction := int(encoded)/directionCount, int(encoded)%directionCount
		if reverseMode {
			cell += directionStep[direction]
			direction ^= 1
		}
		plan = append(plan, shortestWalk(boxMask, &player, cell-directionStep[direction])...)
		plan = append(plan, directionLetter[direction]-letterCaseOffset)
		boxMask ^= cellBit(cell) | cellBit(cell+directionStep[direction])
		player = cell
	}
	return plan
}

var (
	boxCrossingPenalty, goalCount int
	goals                         [maxBoxes]int
	targetBoxes                   uint64
)

// Restrict a corral only if removing outside boxes enables no extra boundary push
// and every available boundary push goes inward.
func restrictCorral(boxMask, reachable uint64) uint64 {
	unseen, fixed := floorMask&^(boxMask|reachable), frozenBoxes(boxMask)
	for unseen != 0 {
		corral := reachableCells(unseen&-unseen, floorMask&^(boxMask|reachable))
		unseen &^= corral
		border := boxMask & (corral<<1 | corral>>1 |
			corral<<boardWidth | corral>>boardWidth)
		if (border&^goalMask)|(corral&goalMask) == 0 {
			continue
		}
		reduced := border | fixed
		relaxed := reachableCells(reachable, floorMask&^reduced)
		independent, pushCount := true, 0
		for direction := 0; direction < directionCount && independent; direction++ {
			possible := border & shift(relaxed, direction) &
				shift(floorMask&^reduced&liveCells, direction^1)
			actual := border & shift(reachable, direction) &
				shift(floorMask&^boxMask&liveCells, direction^1)
			if possible != actual || shift(possible, direction)&^corral != 0 {
				independent = false
			}
			pushCount += countBits(possible)
		}
		if independent && pushCount != 0 {
			return border
		}
	}
	return boxMask
}

// A boundary projection records every player component that can solve each subset.
type region struct {
	mask, floor, active uint64
	cells               []int
	solvablePlayers     []uint64
	packedBytes         [boardWidth][byteValues]int32
	rows                [boardWidth]int
	rowCount            int
}

func (table *region) index(boxMask uint64) int {
	packed := int32(0)
	for row := 0; row < table.rowCount; row++ {
		packed |= table.packedBytes[row][boxMask>>uint(table.rows[row]*byteBits)&byteMask]
	}
	return int(packed)
}
func (table *region) build(regionMask uint64) {
	table.floor, table.active = floorMask, goalMask
	for {
		previous := table.active
		for direction := 0; direction < directionCount; direction++ {
			table.active |= shift(table.active, direction) &
				shift(table.floor, direction^1) & table.floor
		}
		if table.active == previous {
			break
		}
	}
	regionMask &= table.active
	table.mask = regionMask
	for remaining := regionMask; remaining != 0; remaining &= remaining - 1 {
		table.cells = append(table.cells, lowestCell(remaining))
	}
	table.solvablePlayers = make([]uint64, 1<<uint(len(table.cells)))
	for row := 0; row < boardWidth; row++ {
		var masks [boardWidth]int32
		used := false
		for index, cell := range table.cells {
			if cell/boardWidth == row {
				masks[cell%boardWidth] = 1 << uint(index)
				used = true
			}
		}
		if !used {
			continue
		}
		table.rows[table.rowCount] = row
		for value := 1; value < byteValues; value++ {
			table.packedBytes[table.rowCount][value] =
				table.packedBytes[table.rowCount][value&(value-1)] |
					masks[lowestCell(uint64(value))]
		}
		table.rowCount++
	}
	var queue []uint64
	add := func(boxMask, reachable uint64) {
		packed := table.index(boxMask)
		if table.solvablePlayers[packed]&reachable != 0 {
			return
		}
		reachable = reachableCells(reachable, table.floor&^boxMask)
		table.solvablePlayers[packed] |= reachable
		queue = append(queue, stateKey(boxMask, reachable))
	}
	boxMask := goalMask & table.mask
	for todo := table.floor &^ boxMask; todo != 0; {
		reachable := reachableCells(todo&-todo, table.floor&^boxMask)
		add(boxMask, reachable)
		todo &^= reachable
	}
	outside := table.active &^ table.mask
	for head := 0; head < len(queue); head++ {
		boxMask := stateBoxes(queue[head])
		emptyCells := table.floor &^ boxMask
		reachable := reachableCells(cellBit(int(queue[head]>>playerShift)), emptyCells)
		for direction, step := range directionStep {
			movable := boxMask & shift(reachable&shift(emptyCells, direction^1)&
				table.active, direction^1)
			for ; movable != 0; movable &= movable - 1 {
				cell := lowestCell(movable)
				nextCell := cell + step
				nextBoxes := (boxMask ^ cellBit(cell)) | (cellBit(nextCell) & table.mask)
				add(nextBoxes, cellBit(nextCell+step))
			}
			if countBits(boxMask) < countBits(initialBoxes) {
				movable = outside & shift(reachable&shift(emptyCells, direction^1)&
					table.mask, direction^1)
				for ; movable != 0; movable &= movable - 1 {
					nextCell := lowestCell(movable) + step
					add(boxMask|cellBit(nextCell), cellBit(nextCell+step))
				}
			}
		}
	}
}

var regions []*region
var useRegional bool

// Use live cells in each three-cell boundary strip, skipping duplicate masks.
func buildRegions() {
	for axis := 0; axis < 2; axis++ {
		for side := 0; side < 2; side++ {
			minimum, maximum := boardWidth, 0
			for remaining := floorMask; remaining != 0; remaining &= remaining - 1 {
				cell := lowestCell(remaining)
				coordinate := cell % boardWidth
				if axis != 0 {
					coordinate = cell / boardWidth
				}
				if coordinate < minimum {
					minimum = coordinate
				}
				if coordinate > maximum {
					maximum = coordinate
				}
			}
			var regionMask uint64
			for remaining := liveCells; remaining != 0; remaining &= remaining - 1 {
				cell := lowestCell(remaining)
				coordinate := cell % boardWidth
				if axis != 0 {
					coordinate = cell / boardWidth
				}
				if side != 0 && coordinate > maximum-regionWidth ||
					side == 0 && coordinate < minimum+regionWidth {
					regionMask |= cellBit(cell)
				}
			}
			if regionMask == 0 {
				continue
			}
			duplicate := false
			for _, table := range regions {
				if table.mask == regionMask {
					duplicate = true
				}
			}
			if duplicate {
				continue
			}
			table := new(region)
			table.build(regionMask)
			regions = append(regions, table)
		}
	}
}
func regionGood(boxMask, reachable uint64) bool {
	if len(regions) == 0 {
		buildRegions()
	}
	for _, table := range regions {
		if table.solvablePlayers[table.index(boxMask)]&reachable == 0 {
			return false
		}
	}
	return true
}

type goalDistances [maxBoxes][cellCount]int32

var distanceCache map[uint64]*goalDistances
var heuristicCache estimateCache

// Erase boxes movable from the expanding player component until it stops growing.
func inaccessibleBoxes(boxMask, reachable uint64) uint64 {
	for {
		emptyCells, removable := floorMask&^boxMask, uint64(0)
		for direction := 0; direction < directionCount; direction++ {
			if reverseMode {
				removable |= boxMask & shift(reachable&shift(emptyCells, direction^1)&
					liveCells, direction^1)
			} else {
				removable |= boxMask & shift(reachable, direction) &
					shift(emptyCells&liveCells, direction^1)
			}
		}
		if removable == 0 {
			return boxMask
		}
		boxMask &^= removable
		reachable = reachableCells(reachable, floorMask&^boxMask)
	}
}

type packingResult struct{ boxes, reachable uint64 }

var packing map[uint64][]packingResult
var packingWeight int

// Pull-erase goal boxes from every final component while retaining fixed boxes.
// A compatible residue must be present and its player region must intersect.
func packingGood(boxMask, reachable, fixed uint64) bool {
	results, found := packing[fixed]
	if !found {
		for todo := floorMask &^ goalMask; todo != 0; {
			remainingGoals := goalMask
			reachableFromGoals := reachableCells(todo&-todo, floorMask&^goalMask)
			todo &^= reachableFromGoals
			for {
				emptyCells, movable := floorMask&^remainingGoals, uint64(0)
				for direction := 0; direction < directionCount; direction++ {
					movable |= remainingGoals & shift(reachableFromGoals&
						shift(emptyCells, direction^1), direction^1)
				}
				movable &^= fixed
				if movable == 0 {
					break
				}
				remainingGoals &^= movable
				reachableFromGoals = reachableCells(reachableFromGoals, floorMask&^remainingGoals)
			}
			results = append(results, packingResult{remainingGoals, reachableFromGoals})
		}
		packing[fixed] = results
	}
	for _, result := range results {
		if result.boxes&^boxMask == 0 && result.reachable&reachable != 0 {
			return true
		}
	}
	return false
}

var patternSize int
var binomial [matchingSize][patternSizeCount]int

type pattern struct {
	solvablePlayers         []uint64
	floor, goals, liveCells uint64
	subsetSize, cellCount   int
	cellIndex               [cellCount]int
}

var patterns map[uint64]*pattern
var movedBox, parentFrozenBoxes uint64

// The combinatorial number system densely ranks sorted live-cell subsets.
func rankPattern(boxMask uint64, table *pattern) int {
	rank, subsetSize := 0, 1
	for ; boxMask != 0; boxMask &= boxMask - 1 {
		rank += binomial[table.cellIndex[lowestCell(boxMask)]][subsetSize]
		subsetSize++
	}
	return rank
}

// Remove frozen goals from the floor, then mark solvable components by retrograde BFS.
func getPattern(fixed uint64) *pattern {
	if table, found := patterns[fixed]; found {
		return table
	}
	table := &pattern{floor: floorMask &^ fixed, goals: targetBoxes &^ fixed}
	patterns[fixed] = table
	table.subsetSize = minInt(patternSize, countBits(table.goals))
	if table.subsetSize < 1 {
		return table
	}
	table.liveCells = table.goals
	for {
		previous := table.liveCells
		for direction := 0; direction < directionCount; direction++ {
			if reverseMode {
				table.liveCells |= shift(table.liveCells&shift(table.floor, direction),
					direction) & table.floor
			} else {
				table.liveCells |= shift(table.liveCells, direction) &
					shift(table.floor, direction^1) & table.floor
			}
		}
		if table.liveCells == previous {
			break
		}
	}
	for cell := range table.cellIndex {
		table.cellIndex[cell] = -1
	}
	for remaining := table.liveCells; remaining != 0; remaining &= remaining - 1 {
		table.cellIndex[lowestCell(remaining)] = table.cellCount
		table.cellCount++
	}
	table.solvablePlayers = make([]uint64, binomial[table.cellCount][table.subsetSize])
	var queue []uint64
	add := func(boxMask, reachable uint64) {
		index := rankPattern(boxMask, table)
		if table.solvablePlayers[index]&reachable != 0 {
			return
		}
		reachable = reachableCells(reachable, table.floor&^boxMask)
		table.solvablePlayers[index] |= reachable
		queue = append(queue, stateKey(boxMask, reachable))
	}
	var goalCells [maxBoxes]int
	goalCount := 0
	for remaining := table.goals; remaining != 0; remaining &= remaining - 1 {
		goalCells[goalCount] = lowestCell(remaining)
		goalCount++
	}
	// Increasing indices enumerate the same lexicographic subsets as nested loops.
	var roots func(int, int, uint64)
	roots = func(first, needed int, boxMask uint64) {
		if needed != 0 {
			for index := first; index < goalCount; index++ {
				roots(index+1, needed-1, boxMask|cellBit(goalCells[index]))
			}
			return
		}
		if reverseMode {
			add(boxMask, cellBit(initialPlayer))
			return
		}
		for empty := table.floor &^ boxMask; empty != 0; {
			reachable := reachableCells(empty&-empty, table.floor&^boxMask)
			add(boxMask, reachable)
			empty &^= reachable
		}
	}
	roots(0, table.subsetSize, 0)
	for head := 0; head < len(queue); head++ {
		boxMask := stateBoxes(queue[head])
		emptyCells := table.floor &^ boxMask
		reachable := reachableCells(cellBit(int(queue[head]>>playerShift)), emptyCells)
		for direction, step := range directionStep {
			var movable uint64
			if reverseMode {
				movable = boxMask & shift(reachable, direction) & shift(emptyCells, direction^1)
			} else {
				movable = boxMask & shift(reachable&shift(emptyCells, direction^1), direction^1)
			}
			for ; movable != 0; movable &= movable - 1 {
				cell := lowestCell(movable)
				nextCell := cell + step
				player := nextCell + step
				if reverseMode {
					player = cell
				}
				add(boxMask^cellBit(cell)^cellBit(nextCell), cellBit(player))
			}
		}
	}
	return table
}

// Unchanged frozen boxes let us retest only subsets containing the moved box.
func patternGood(boxMask, reachable, fixed uint64) bool {
	table := getPattern(fixed)
	if table.subsetSize < 1 {
		return true
	}
	if boxMask&^fixed&^table.liveCells != 0 {
		return false
	}
	moved := -1
	if movedBox != 0 && fixed == parentFrozenBoxes {
		moved = table.cellIndex[lowestCell(movedBox)]
	}
	if movedBox&fixed != 0 {
		moved = -1
	}
	var indices [maxBoxes]int
	boxCount := 0
	for remaining := boxMask &^ fixed; remaining != 0; remaining &= remaining - 1 {
		indices[boxCount] = table.cellIndex[lowestCell(remaining)]
		boxCount++
	}
	var check func(int, int, int, bool) bool
	check = func(first, size, rank int, containsMoved bool) bool {
		if size > table.subsetSize {
			if table.subsetSize > 1 && moved >= 0 && !containsMoved {
				return true
			}
			return table.solvablePlayers[rank]&reachable != 0
		}
		for index := first; index < boxCount; index++ {
			cell := indices[index]
			if !check(index+1, size+1, rank+binomial[cell][size],
				containsMoved || cell == moved) {
				return false
			}
		}
		return true
	}
	return check(0, 1, 0, false)
}

// Component-dependent deadlocks precede the box-only cache and minimum-cost matching.
func heuristic(boxMask, reachable uint64) int {
	if inaccessibleBoxes(boxMask, reachable)&^targetBoxes != 0 {
		return -1
	}
	frozen := frozenBoxes(boxMask)
	if frozen&^targetBoxes != 0 {
		return -1
	}
	if useRegional &&
		(!packingGood(boxMask, reachable, frozen) || !regionGood(boxMask, reachable)) {
		return -1
	}
	if patternSize != 0 && !patternGood(boxMask, reachable, frozen) {
		return -1
	}
	if estimate, found := heuristicCache.get(boxMask); found {
		return estimate
	}
	var computed goalDistances
	var distances *goalDistances
	if boxCrossingPenalty == 0 {
		distances = distanceCache[frozen]
	}
	if distances == nil {
		distances = &computed
		available := floorMask &^ frozen
		for goalIndex := 0; goalIndex < goalCount; goalIndex++ {
			cellDistance := &distances[goalIndex]
			for cell := range cellDistance {
				cellDistance[cell] = unreachableDistance
			}
			cellDistance[goals[goalIndex]] = 0
			if frozen&cellBit(goals[goalIndex]) != 0 {
				continue
			}
			if boxCrossingPenalty == 0 {
				var queue [cellCount]int
				head, tail := 0, 1
				queue[0] = goals[goalIndex]
				for head < tail {
					cell := queue[head]
					head++
					for _, step := range directionStep {
						nextCell, supportCell := cell+step, cell+2*step
						if reverseMode {
							supportCell = cell - step
						}
						if nextCell < 0 || nextCell >= cellCount ||
							supportCell < 0 || supportCell >= cellCount ||
							available&cellBit(nextCell) == 0 ||
							available&cellBit(supportCell) == 0 ||
							cellDistance[nextCell] < unreachableDistance {
							continue
						}
						cellDistance[nextCell] = cellDistance[cell] + 1
						queue[tail] = nextCell
						tail++
					}
				}
			} else {
				// Queue relaxation charges for crossing occupied box and support cells.
				var queue [distanceQueueSize]int
				var queued [cellCount]bool
				head, tail := 0, 1
				queue[0], queued[goals[goalIndex]] = goals[goalIndex], true
				for head != tail {
					cell := queue[head]
					head = (head + 1) & distanceQueueMask
					queued[cell] = false
					distance := cellDistance[cell]
					for _, step := range directionStep {
						nextCell, supportCell := cell+step, cell+2*step
						if reverseMode {
							supportCell = cell - step
						}
						if nextCell < 0 || nextCell >= cellCount ||
							supportCell < 0 || supportCell >= cellCount ||
							available&cellBit(nextCell) == 0 ||
							available&cellBit(supportCell) == 0 {
							continue
						}
						cost := 1
						if boxMask&cellBit(cell) != 0 {
							cost += boxCrossingPenalty
						}
						if boxMask&cellBit(supportCell) != 0 {
							cost += boxCrossingPenalty
						}
						nextDistance := distance + int32(cost)
						if nextDistance < cellDistance[nextCell] {
							cellDistance[nextCell] = nextDistance
							if !queued[nextCell] {
								queue[tail] = nextCell
								tail = (tail + 1) & distanceQueueMask
								queued[nextCell] = true
							}
						}
					}
				}
			}
		}
		if boxCrossingPenalty == 0 {
			saved := new(goalDistances)
			*saved = computed
			distanceCache[frozen] = saved
			distances = saved
		}
	}
	var boxCells [matchingSize]int
	boxCount := 0
	for remaining := boxMask; remaining != 0; remaining &= remaining - 1 {
		boxCount++
		boxCells[boxCount] = lowestCell(remaining)
	}
	// Strict improvements and increasing goal indices preserve Hungarian matching ties.
	var boxPotential, goalPotential, matchedBox, previousGoal [matchingSize]int
	for box := 1; box <= boxCount; box++ {
		matchedBox[0] = box
		currentGoal := 0
		var slack [matchingSize]int
		for index := range slack {
			slack[index] = unreachableDistance
		}
		var visitedGoal [matchingSize]bool
		for {
			visitedGoal[currentGoal] = true
			currentBox := matchedBox[currentGoal]
			adjustment, nextGoal := unreachableDistance, 0
			for goal := 1; goal <= boxCount; goal++ {
				if visitedGoal[goal] {
					continue
				}
				cost := int(distances[goal-1][boxCells[currentBox]])
				reducedCost := cost - boxPotential[currentBox] - goalPotential[goal]
				if reducedCost < slack[goal] {
					slack[goal], previousGoal[goal] = reducedCost, currentGoal
				}
				if slack[goal] < adjustment {
					adjustment, nextGoal = slack[goal], goal
				}
			}
			if adjustment >= unreachableDistance {
				return heuristicCache.put(boxMask, -1)
			}
			for goal := 0; goal <= boxCount; goal++ {
				if visitedGoal[goal] {
					boxPotential[matchedBox[goal]] += adjustment
					goalPotential[goal] -= adjustment
				} else {
					slack[goal] -= adjustment
				}
			}
			currentGoal = nextGoal
			if matchedBox[currentGoal] == 0 {
				break
			}
		}
		for {
			nextGoal := previousGoal[currentGoal]
			matchedBox[currentGoal] = matchedBox[nextGoal]
			currentGoal = nextGoal
			if currentGoal == 0 {
				break
			}
		}
	}
	for goal := 1; goal <= boxCount; goal++ {
		if distances[goal-1][boxCells[matchedBox[goal]]] >= unreachableDistance {
			return heuristicCache.put(boxMask, -1)
		}
	}
	return heuristicCache.put(boxMask, -goalPotential[0])
}

// Reuse primitive storage across attempts while discarding their cached meaning.
func resetSearch() {
	nodes = nodes[:0]
	hashTable = hashTable[:0]
	heuristicCache.reset()
	distanceCache = make(map[uint64]*goalDistances)
	patterns = make(map[uint64]*pattern)
}

// Search push or pull states, retaining the first visit and preferring newer ties.
func attempt(pullSearch bool, crossingPenalty int, regional bool,
	tableSize, expansionLimit int) []byte {
	reverseMode, boxCrossingPenalty = pullSearch, crossingPenalty
	useRegional, patternSize = regional, tableSize
	movedBox, parentFrozenBoxes, goalCount = 0, 0, 0
	resetSearch()
	targetBoxes = goalMask
	if reverseMode {
		targetBoxes = initialBoxes
	}
	for remaining := targetBoxes; remaining != 0; remaining &= remaining - 1 {
		goals[goalCount] = lowestCell(remaining)
		goalCount++
	}
	liveCells = targetBoxes
	for {
		previous := liveCells
		for direction := 0; direction < directionCount; direction++ {
			if reverseMode {
				liveCells |= shift(liveCells&shift(floorMask, direction), direction) & floorMask
			} else {
				liveCells |= shift(liveCells, direction) &
					shift(floorMask, direction^1) & floorMask
			}
		}
		if liveCells == previous {
			break
		}
	}
	var open priorityQueue
	var depth []int32
	add := func(boxMask, reachable uint64, parent uint32, encodedPush, pushDepth int) {
		state := stateKey(boxMask, reachable)
		slot := findSlot(state)
		if hashTable[slot] != 0 {
			return
		}
		estimate := heuristic(boxMask, reachable)
		if estimate >= 0 && useRegional && packingWeight != 0 {
			fixed := boxMask & goalMask
			packingGood(boxMask, reachable, fixed)
			missingGoals := maxBoxes
			for _, result := range packing[fixed] {
				missingGoals = minInt(missingGoals, countBits(result.boxes&^boxMask))
			}
			estimate += packingWeight * missingGoals
		}
		if estimate < 0 {
			if fastMode {
				insert(state, noParent, 0)
				depth = append(depth, -1)
			}
			return
		}
		id := insert(state, parent, encodedPush)
		depth = append(depth, int32(pushDepth))
		if useRegional {
			estimate -= pushDepth
		}
		open.push(entry{int32(priorityScale * estimate), -int32(id), int32(id)})
	}
	if reverseMode {
		for todo := floorMask &^ goalMask; todo != 0; {
			reachable := reachableCells(todo&-todo, floorMask&^goalMask)
			add(goalMask, reachable, noParent, 0, 0)
			todo &^= reachable
		}
	} else {
		add(initialBoxes, reachableCells(cellBit(initialPlayer), floorMask&^initialBoxes),
			noParent, 0, 0)
	}
	expanded, solved := 0, -1
	initialReach := reachableCells(cellBit(initialPlayer), floorMask&^initialBoxes)
	for len(open) != 0 && expanded < expansionLimit &&
		(!fastMode || len(nodes) < nodeCap && !(expanded&clockCheckMask == 0 && timeUp())) {
		id := int(open.pop().id)
		boxMask := stateBoxes(nodes[id].state)
		reachable := reachableCells(cellBit(int(nodes[id].state>>playerShift)), floorMask&^boxMask)
		if boxMask == targetBoxes && (!reverseMode || reachable&initialReach != 0) {
			solved = id
			break
		}
		expanded++
		if patternSize != 0 {
			parentFrozenBoxes = frozenBoxes(boxMask)
		}
		emptyCells, allowed := floorMask&^boxMask, boxMask
		if !reverseMode {
			allowed = restrictCorral(boxMask, reachable)
		}
		for direction, step := range directionStep {
			var movable uint64
			if reverseMode {
				movable = boxMask & shift(reachable&shift(emptyCells, direction^1)&
					liveCells, direction^1)
			} else {
				movable = allowed & shift(reachable, direction) &
					shift(emptyCells&liveCells, direction^1)
			}
			for ; movable != 0; movable &= movable - 1 {
				cell := lowestCell(movable)
				nextCell := cell + step
				nextBoxes := boxMask ^ cellBit(cell) ^ cellBit(nextCell)
				player := cell
				if reverseMode {
					player = nextCell + step
				}
				nextReachable := reachableCells(cellBit(player), floorMask&^nextBoxes)
				movedBox = cellBit(nextCell)
				add(nextBoxes, nextReachable, uint32(id), cell*directionCount+direction,
					int(depth[id])+1)
			}
		}
	}
	if solved < 0 {
		return nil
	}
	plan := reconstructPlan(solved)
	if len(plan) > maxPlanLength {
		return nil
	}
	return plan
}

// Cheap forward and reverse probes precede four rotated forward restarts.
func cheapProbes() []byte {
	plan := attempt(false, 1, false, 0, initialExpansions)
	if len(plan) == 0 {
		plan = attempt(true, 0, false, 0, initialExpansions)
	}
	if len(plan) == 0 {
		savedFloor, savedGoals, savedBoxes := floorMask, goalMask, initialBoxes
		savedPlayer, turns := initialPlayer, 0
		for turn := 1; turn <= rotationCount && len(plan) == 0; turn++ {
			floorMask, goalMask = rotateMask(floorMask), rotateMask(goalMask)
			initialBoxes, initialPlayer = rotateMask(initialBoxes), rotateCell(initialPlayer)
			plan = attempt(false, 2, false, 0, rotatedExpansions)
			turns = turn
		}
		floorMask, goalMask, initialBoxes = savedFloor, savedGoals, savedBoxes
		initialPlayer = savedPlayer
		for turn := 0; turn < turns; turn++ {
			for index, letter := range plan {
				upper := letter < 'a'
				if upper {
					letter += letterCaseOffset
				}
				direction := 0
				for directionLetter[direction] != letter {
					direction++
				}
				letter = "lrdu"[direction]
				if upper {
					letter -= letterCaseOffset
				}
				plan[index] = letter
			}
		}
	}
	return plan
}

func transformCell(cell, symmetry int) int {
	if symmetry&reflectionFlag != 0 {
		cell = cell/boardWidth*boardWidth + lastCoordinate - cell%boardWidth
	}
	for turn := 0; turn < symmetry&rotationMask; turn++ {
		cell = rotateCell(cell)
	}
	return cell
}
func transformMask(mask uint64, symmetry int) uint64 {
	var result uint64
	for ; mask != 0; mask &= mask - 1 {
		result |= cellBit(transformCell(lowestCell(mask), symmetry))
	}
	return result
}

// Regional and packing tests use the lexicographically least symmetric geometry.
func runFast() []byte {
	plan := cheapProbes()
	if len(plan) != 0 {
		return plan
	}
	savedFloor, savedGoals, savedBoxes := floorMask, goalMask, initialBoxes
	savedPlayer, bestSymmetry := initialPlayer, 0
	best := [geometryComponents]uint64{floorMask, goalMask, initialBoxes, uint64(initialPlayer)}
	for symmetry := 1; symmetry < symmetryCount; symmetry++ {
		state := [geometryComponents]uint64{
			transformMask(savedFloor, symmetry), transformMask(savedGoals, symmetry),
			transformMask(savedBoxes, symmetry), uint64(transformCell(savedPlayer, symmetry)),
		}
		for component := 0; component < geometryComponents; component++ {
			if state[component] == best[component] {
				continue
			}
			if state[component] < best[component] {
				best, bestSymmetry = state, symmetry
			}
			break
		}
	}
	floorMask, goalMask, initialBoxes = best[0], best[1], best[2]
	initialPlayer = int(best[playerComponent])
	packing, regions = make(map[uint64][]packingResult), nil
	packingWeight = defaultPackingWeight
	plan = attempt(false, 0, true, 0, unboundedExpansions)
	var inverseDirection [directionCount]int
	for direction, step := range directionStep {
		transformedStep := transformCell(directionProbeCell+step, bestSymmetry) -
			transformCell(directionProbeCell, bestSymmetry)
		for index, candidate := range directionStep {
			if candidate == transformedStep {
				inverseDirection[index] = direction
			}
		}
	}
	for index, letter := range plan {
		upper := letter < 'a'
		if upper {
			letter += letterCaseOffset
		}
		direction := 0
		for directionLetter[direction] != letter {
			direction++
		}
		letter = directionLetter[inverseDirection[direction]]
		if upper {
			letter -= letterCaseOffset
		}
		plan[index] = letter
	}
	floorMask, goalMask, initialBoxes = savedFloor, savedGoals, savedBoxes
	initialPlayer = savedPlayer
	return plan
}

// Only failed reconstruction is recoverable; unexpected panics remain visible.
func tryFast() (plan []byte) {
	defer func() {
		if failure := recover(); failure != nil {
			if _, expected := failure.(failedWalk); !expected {
				panic(failure)
			}
			plan = nil
		}
	}()
	return runFast()
}

// Release fast-search storage before constructing the fallback tables.
func release() {
	nodes, hashTable = nil, nil
	heuristicCache = estimateCache{}
	distanceCache, packing, regions = nil, nil, nil
	runtime.GC()
}

// Exact-player A* reopens cheaper states and caps walking-plus-push costs.
func lengthFallback() []byte {
	reverseMode = false
	boxCrossingPenalty, patternSize, movedBox = 0, 0, 0
	resetSearch()
	var cost []int32
	var open priorityQueue
	insert(stateKey(initialBoxes, cellBit(initialPlayer)), noParent, 0)
	cost = append(cost, 0)
	open.push(entry{0, 0, 0})
	for len(open) != 0 {
		top := open.pop()
		pathCost, id := int(top.tie), int(top.id)
		if pathCost != int(cost[id]) {
			continue
		}
		boxMask := stateBoxes(nodes[id].state)
		player := int(nodes[id].state >> playerShift)
		if boxMask == goalMask {
			return reconstructPlan(id)
		}
		var walkDistance, queue [cellCount]int
		for cell := range walkDistance {
			walkDistance[cell] = -1
		}
		walkDistance[player], queue[0] = 0, player
		tail, reachable := 1, uint64(0)
		for head := 0; head < tail; head++ {
			cell := queue[head]
			reachable |= cellBit(cell)
			for _, step := range directionStep {
				nextCell := cell + step
				if nextCell >= 0 && nextCell < cellCount && floorMask&cellBit(nextCell) != 0 &&
					boxMask&cellBit(nextCell) == 0 && walkDistance[nextCell] < 0 {
					walkDistance[nextCell] = walkDistance[cell] + 1
					queue[tail] = nextCell
					tail++
				}
			}
		}
		for direction, step := range directionStep {
			movable := boxMask & shift(reachable, direction) &
				shift(floorMask&^boxMask&liveCells, direction^1)
			for ; movable != 0; movable &= movable - 1 {
				cell := lowestCell(movable)
				nextCell, nextCost := cell+step, pathCost+walkDistance[cell-step]+1
				if nextCost > maxPlanLength {
					continue
				}
				nextBoxes := boxMask ^ cellBit(cell) ^ cellBit(nextCell)
				state := stateKey(nextBoxes, cellBit(cell))
				slot := findSlot(state)
				nextID := int(hashTable[slot]) - 1
				if nextID >= 0 && int(cost[nextID]) <= nextCost {
					continue
				}
				estimate := heuristic(nextBoxes,
					reachableCells(cellBit(cell), floorMask&^nextBoxes))
				if estimate < 0 || nextCost+estimate > maxPlanLength {
					continue
				}
				if nextID < 0 {
					nextID = insert(state, uint32(id), cell*directionCount+direction)
					cost = append(cost, int32(nextCost))
				} else {
					nodes[nextID].parent = uint32(id)
					nodes[nextID].move = uint16(cell*directionCount + direction)
					cost[nextID] = int32(nextCost)
				}
				open.push(entry{int32(nextCost + estimate), int32(nextCost), int32(nextID)})
			}
		}
	}
	return nil
}

// Escalate from three-box to five-box tables, then exact-player A*.
func runSafe() []byte {
	plan := cheapProbes()
	if len(plan) == 0 {
		budget := manyBoxExpansions
		if countBits(initialBoxes) <= 10 {
			budget = smallBoxExpansions
		}
		plan = attempt(false, 0, false, smallPatternSize, budget)
	}
	if len(plan) == 0 {
		plan = attempt(false, 0, false, largePatternSize, unboundedExpansions)
	}
	if len(plan) == 0 {
		plan = lengthFallback()
	}
	return plan
}

var originalFloor, originalGoals, originalBoxes uint64
var originalPlayer int

// Replay every step, including push letter case, and require the exact goal mask.
func valid(plan []byte) bool {
	if len(plan) > maxPlanLength {
		return false
	}
	boxMask, player := originalBoxes, originalPlayer
	for _, letter := range plan {
		push := letter < 'a'
		if push {
			letter += letterCaseOffset
		}
		direction := 0
		for direction < directionCount && directionLetter[direction] != letter {
			direction++
		}
		if direction == directionCount {
			return false
		}
		nextCell := player + directionStep[direction]
		if nextCell < 0 || nextCell >= cellCount || originalFloor&cellBit(nextCell) == 0 {
			return false
		}
		if boxMask&cellBit(nextCell) != 0 {
			destination := nextCell + directionStep[direction]
			if !push || destination < 0 || destination >= cellCount ||
				originalFloor&cellBit(destination) == 0 || boxMask&cellBit(destination) != 0 {
				return false
			}
			boxMask ^= cellBit(nextCell) | cellBit(destination)
		} else if push {
			return false
		}
		player = nextCell
	}
	return boxMask == originalGoals
}

func main() {
	input := bufio.NewScanner(os.Stdin)
	output := bufio.NewWriter(os.Stdout)
	defer output.Flush()
	row := 0
	for input.Scan() {
		line := input.Bytes()
		if len(line) == 0 {
			continue
		}
		for column := 0; column < len(line) && column < boardWidth; column++ {
			tile, cell := line[column], row*boardWidth+column
			if tile != '#' {
				floorMask |= cellBit(cell)
			}
			if tile == '.' || tile == '*' || tile == '+' {
				goalMask |= cellBit(cell)
			}
			if tile == '$' || tile == '*' {
				initialBoxes |= cellBit(cell)
			}
			if tile == '@' || tile == '+' {
				initialPlayer = cell
			}
		}
		row++
	}
	floorMask = reachableCells(cellBit(initialPlayer), floorMask)
	goalMask, initialBoxes = goalMask&floorMask, initialBoxes&floorMask
	originalFloor, originalGoals, originalBoxes = floorMask, goalMask, initialBoxes
	originalPlayer = initialPlayer
	if initialBoxes == goalMask {
		output.WriteByte('\n')
		return
	}
	// Pascal recurrence supplies the subset ranks used by pattern tables.
	for available := 0; available <= maxBoxes; available++ {
		for size := 0; size <= largePatternSize; size++ {
			if size == 0 {
				binomial[available][size] = 1
			} else if available != 0 {
				binomial[available][size] = binomial[available-1][size-1] +
					binomial[available-1][size]
			}
		}
	}
	plan := tryFast()
	if !valid(plan) {
		release()
		fastMode = false
		floorMask, goalMask, initialBoxes = originalFloor, originalGoals, originalBoxes
		initialPlayer = originalPlayer
		plan = runSafe()
	}
	output.Write(plan)
	output.WriteByte('\n')
}
