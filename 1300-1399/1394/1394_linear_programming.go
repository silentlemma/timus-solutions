package main

import (
	"bufio"
	"math"
	"math/bits"
	"os"
	"sort"
)

const (
	simplexIterationLimit       = 1000
	fillingCountLimit           = 1000000
	failedStateLimit            = 100000
	initialExactBudget          = 2000
	budgetBits                  = 60
	maxExactBudget        int64 = 1 << budgetBits
	simplexEpsilon              = 1e-8
	eliminationEpsilon          = 1e-12
	feasibilityEpsilon          = 1e-7
	pricingEpsilon              = 1e-10
	infinitePrice               = 1e30
	randomSeed                  = 12345
	initialGreedyAttempts       = 6
	retryGreedyAttempts         = 16
	pricingWorkLimit            = 160
	columnIterationLimit        = 60
	maxLength                   = 100
	maxRows                     = 10
	wordBits                    = 64
	byteBits                    = 8
	inputBufferSize             = 4096
)

func smaller(left, right int) int {
	if left < right {
		return left
	}
	return right
}

func larger(left, right int) int {
	if left > right {
		return left
	}
	return right
}

func positive(value float64) float64 {
	if value > 0 {
		return value
	}
	return 0
}

// The standard MT19937 recurrence and tempering use wrapping 32-bit arithmetic.
const (
	mtSize           = 624
	mtOffset         = 397
	mtUpperMask      = 0x80000000
	mtLowerMask      = 0x7fffffff
	mtTwistMask      = 0x9908b0df
	mtSeedMultiplier = 1812433253
	mtSeedShift      = 30
	mtShiftFirst     = 11
	mtShiftSecond    = 7
	mtShiftThird     = 15
	mtShiftLast      = 18
	mtMaskSecond     = 0x9d2c5680
	mtMaskThird      = 0xefc60000
	randomWordBits   = 32
)

type mersenneTwister struct {
	state    [mtSize]uint32
	position int
}

func (generator *mersenneTwister) seed(seed uint32) {
	generator.state[0] = seed
	for i := 1; i < mtSize; i++ {
		previous := generator.state[i-1]
		generator.state[i] = mtSeedMultiplier*(previous^(previous>>mtSeedShift)) + uint32(i)
	}
	generator.position = mtSize
}

func (generator *mersenneTwister) next() uint32 {
	if generator.position == mtSize {
		for i := 0; i < mtSize; i++ {
			joined := generator.state[i]&mtUpperMask | generator.state[(i+1)%mtSize]&mtLowerMask
			value := generator.state[(i+mtOffset)%mtSize] ^ (joined >> 1)
			if joined&1 != 0 {
				value ^= mtTwistMask
			}
			generator.state[i] = value
		}
		generator.position = 0
	}
	value := generator.state[generator.position]
	generator.position++
	value ^= value >> mtShiftFirst
	value ^= (value << mtShiftSecond) & mtMaskSecond
	value ^= (value << mtShiftThird) & mtMaskThird
	value ^= value >> mtShiftLast
	return value
}

// libstdc++ uses Lemire downscaling, then shares a draw between two swaps.
func (generator *mersenneTwister) below(bound uint32) int {
	product := uint64(generator.next()) * uint64(bound)
	low := uint32(product)
	if low < bound {
		threshold := -bound % bound
		for low < threshold {
			product = uint64(generator.next()) * uint64(bound)
			low = uint32(product)
		}
	}
	return int(product >> randomWordBits)
}

func (generator *mersenneTwister) shuffle(values []int) {
	if len(values) == 0 {
		return
	}
	position := 1
	if len(values)%2 == 0 {
		other := generator.below(2)
		values[position], values[other] = values[other], values[position]
		position++
	}
	for position < len(values) {
		firstBound := position + 1
		draw := generator.below(uint32(firstBound * (firstBound + 1)))
		first, second := draw/(firstBound+1), draw%(firstBound+1)
		values[position], values[first] = values[first], values[position]
		position++
		values[position], values[second] = values[second], values[position]
		position++
	}
}

type counts [maxLength]uint8
type reachableSums []uint64

func (sums reachableSums) get(sum int) bool {
	return sum >= 0 && sum/wordBits < len(sums) && sums[sum/wordBits]>>(sum%wordBits)&1 != 0
}

// Descending updates add one ship without reusing its newly reached sums.
func (sums reachableSums) add(shift int) {
	wordShift, bitShift := shift/wordBits, uint(shift%wordBits)
	for i := len(sums) - 1; i >= wordShift; i-- {
		value := sums[i-wordShift] << bitShift
		if bitShift != 0 && i > wordShift {
			value |= sums[i-wordShift-1] >> (wordBits - bitShift)
		}
		sums[i] |= value
	}
}

func newSuffix(size, maxSum int) []reachableSums {
	width := maxSum/wordBits + 1
	storage := make([]uint64, size*width)
	result := make([]reachableSums, size)
	for i := range result {
		result[i] = storage[i*width : (i+1)*width]
	}
	return result
}

// A contiguous tableau keeps simplex scans compact; slack columns form the zero basis.
type linearProgram struct {
	constraintCount, columnCount int
	tableau                      [][]float64
	basis                        []int
}

func newLinearProgram(constraints, columns int) linearProgram {
	width := columns + constraints + 1
	storage := make([]float64, (constraints+1)*width)
	lp := linearProgram{
		constraints, columns, make([][]float64, constraints+1), make([]int, constraints),
	}
	for i := range lp.tableau {
		lp.tableau[i] = storage[i*width : (i+1)*width]
	}
	for i := range lp.basis {
		lp.tableau[i][columns+i] = 1
		lp.basis[i] = columns + i
	}
	return lp
}

func (lp *linearProgram) solve() {
	rhsColumn := lp.columnCount + lp.constraintCount
	objective := lp.tableau[lp.constraintCount]
	for iteration := 0; iteration < simplexIterationLimit; iteration++ {
		pivotColumn := -1
		for j := 0; j < rhsColumn; j++ {
			if objective[j] < -simplexEpsilon &&
				(pivotColumn < 0 || objective[j] < objective[pivotColumn]) {
				pivotColumn = j
			}
		}
		if pivotColumn < 0 {
			return
		}
		pivotRow, ratio := -1, 0.0
		for i := 0; i < lp.constraintCount; i++ {
			row := lp.tableau[i]
			if row[pivotColumn] > simplexEpsilon {
				candidateRatio := row[rhsColumn] / row[pivotColumn]
				if pivotRow < 0 || candidateRatio < ratio-simplexEpsilon ||
					(math.Abs(candidateRatio-ratio) < simplexEpsilon && lp.basis[i] < lp.basis[pivotRow]) {
					pivotRow, ratio = i, candidateRatio
				}
			}
		}
		if pivotRow < 0 {
			return
		}
		pivot := lp.tableau[pivotRow]
		pivotValue := pivot[pivotColumn]
		for j := range pivot {
			pivot[j] /= pivotValue
		}
		for i, row := range lp.tableau {
			if i == pivotRow {
				continue
			}
			factor := row[pivotColumn]
			if math.Abs(factor) > eliminationEpsilon {
				for j := range row {
					row[j] -= float64(factor * pivot[j])
				}
				row[pivotColumn] = 0
			}
		}
		lp.basis[pivotRow] = pivotColumn
	}
}

// Open addressing stores exact byte keys; hashes only locate candidates.
const (
	initialHashSize        = 256
	hashOffset      uint64 = 14695981039346656037
	hashPrime       uint64 = 1099511628211
)

type failedStates struct {
	slots  []int32
	keys   []byte
	hashes []uint64
	width  int
}

func (states *failedStates) clear(width int) {
	states.width = width
	states.keys = states.keys[:0]
	states.hashes = states.hashes[:0]
	for i := range states.slots {
		states.slots[i] = 0
	}
}

func stateHash(key []byte) uint64 {
	hash := hashOffset
	for _, value := range key {
		hash = (hash ^ uint64(value)) * hashPrime
	}
	return hash
}

func (states *failedStates) contains(key []byte) bool {
	if len(states.slots) == 0 {
		return false
	}
	hash := stateHash(key)
	mask := len(states.slots) - 1
	for slot := int(hash & uint64(mask)); states.slots[slot] != 0; slot = (slot + 1) & mask {
		entry := int(states.slots[slot]) - 1
		if states.hashes[entry] != hash {
			continue
		}
		stored := states.keys[entry*states.width : (entry+1)*states.width]
		equal := true
		for i, value := range key {
			if stored[i] != value {
				equal = false
				break
			}
		}
		if equal {
			return true
		}
	}
	return false
}

func (states *failedStates) insert(key []byte) {
	if len(states.hashes) >= failedStateLimit || states.contains(key) {
		return
	}
	if (len(states.hashes)+1)*2 >= len(states.slots) {
		size := larger(initialHashSize, len(states.slots)*2)
		states.slots = make([]int32, size)
		for entry, hash := range states.hashes {
			slot := int(hash & uint64(size-1))
			for states.slots[slot] != 0 {
				slot = (slot + 1) & (size - 1)
			}
			states.slots[slot] = int32(entry + 1)
		}
	}
	hash := stateHash(key)
	slot := int(hash & uint64(len(states.slots)-1))
	for states.slots[slot] != 0 {
		slot = (slot + 1) & (len(states.slots) - 1)
	}
	states.keys = append(states.keys, key...)
	states.hashes = append(states.hashes, hash)
	states.slots[slot] = int32(len(states.hashes))
}

type solver struct {
	rowCount, typeCount   int
	lengths, counts, rows []int
	answer                [][]int
	rng                   mersenneTwister
	failed                failedStates
	budget                int64
	budgetExhausted       bool
	suffix                [][]reachableSums
	rowFillings           []counts
}

func newSolver(ships, rows []int) *solver {
	s := &solver{rowCount: len(rows), rows: rows, answer: make([][]int, len(rows))}
	s.rng.seed(randomSeed)
	var frequencies [maxLength + 1]int
	for _, length := range ships {
		frequencies[length]++
	}
	for length := maxLength; length > 0; length-- {
		if frequencies[length] != 0 {
			s.lengths = append(s.lengths, length)
			s.counts = append(s.counts, frequencies[length])
		}
	}
	s.typeCount = len(s.lengths)
	return s
}

func (s *solver) storeRow(row int, filling counts) {
	s.answer[row] = s.answer[row][:0]
	for i, length := range s.lengths {
		for copies := 0; copies < int(filling[i]); copies++ {
			s.answer[row] = append(s.answer[row], length)
		}
	}
}

// Fewer than ten rows use the same stable insertion order as libstdc++ sort.
func (s *solver) sortRows(order []int) {
	for i := 1; i < len(order); i++ {
		row, position := order[i], i
		for position > 0 && s.rows[row] < s.rows[order[position-1]] {
			order[position] = order[position-1]
			position--
		}
		order[position] = row
	}
}

// Suffix reachability chooses each ship as early as possible in the current order.
func (s *solver) greedy(attemptLimit int) bool {
	order := make([]int, s.rowCount)
	for i := range order {
		order[i] = i
	}
	s.sortRows(order)
	for attempt := 0; attempt < attemptLimit; attempt++ {
		remainingShips := make([]int, 0, maxLength)
		for i, length := range s.lengths {
			for copies := 0; copies < s.counts[i]; copies++ {
				remainingShips = append(remainingShips, length)
			}
		}
		if attempt == 1 {
			for i, j := 0, len(remainingShips)-1; i < j; i, j = i+1, j-1 {
				remainingShips[i], remainingShips[j] = remainingShips[j], remainingShips[i]
			}
		}
		if attempt > 1 {
			s.rng.shuffle(remainingShips)
			s.rng.shuffle(order[:len(order)-1])
		}
		completed := true
		for _, row := range order[:len(order)-1] {
			remainingLength, remainingCount := s.rows[row], len(remainingShips)
			suffix := newSuffix(remainingCount+1, remainingLength)
			suffix[remainingCount][0] = 1
			for i := remainingCount - 1; i >= 0; i-- {
				copy(suffix[i], suffix[i+1])
				suffix[i].add(remainingShips[i])
			}
			if !suffix[0].get(remainingLength) {
				completed = false
				break
			}
			unusedShips := make([]int, 0, remainingCount)
			s.answer[row] = s.answer[row][:0]
			for i, length := range remainingShips {
				if length <= remainingLength && suffix[i+1].get(remainingLength-length) {
					s.answer[row] = append(s.answer[row], length)
					remainingLength -= length
				} else {
					unusedShips = append(unusedShips, length)
				}
			}
			remainingShips = unusedShips
		}
		if completed {
			s.answer[order[len(order)-1]] = remainingShips
			return true
		}
	}
	return false
}

func (s *solver) failureKey(remaining []int, activeRows int) [maxLength + 2]byte {
	var key [maxLength + 2]byte
	key[0], key[1] = byte(activeRows), byte(activeRows>>byteBits)
	for i, count := range remaining {
		key[i+2] = byte(count)
	}
	return key
}

// Count multisets by addition only, so saturating coefficients preserves the cap.
func (s *solver) countFillings(remaining []int, maxSum, limit int) []int {
	ways, next := make([]int, maxSum+1), make([]int, maxSum+1)
	ways[0] = 1
	for i, length := range s.lengths {
		for sum := range next {
			next[sum] = 0
		}
		for sum, count := range ways {
			if count == 0 {
				continue
			}
			for copies := 0; copies <= remaining[i] && sum+copies*length <= maxSum; copies++ {
				index := sum + copies*length
				next[index] = smaller(limit, next[index]+count)
			}
		}
		ways, next = next, ways
	}
	return ways
}

// Suffix sums prune partial fillings; budget exhaustion never records failure.
func (s *solver) enumerateExactRow(remaining []int, activeRows, depth, selectedRow,
	i, remainingLength int) bool {
	s.budget--
	if s.budget < 0 {
		s.budgetExhausted = true
		return false
	}
	if remainingLength == 0 {
		if s.exact(remaining, activeRows^(1<<selectedRow), depth+1) {
			s.storeRow(selectedRow, s.rowFillings[depth])
			return true
		}
		return false
	}
	if i == s.typeCount {
		return false
	}
	available := remaining[i]
	for copies := smaller(available, remainingLength/s.lengths[i]); copies >= 0; copies-- {
		if s.suffix[depth][i+1].get(remainingLength - copies*s.lengths[i]) {
			remaining[i] = available - copies
			s.rowFillings[depth][i] = uint8(copies)
			if s.enumerateExactRow(remaining, activeRows, depth, selectedRow,
				i+1, remainingLength-copies*s.lengths[i]) {
				return true
			}
			if s.budgetExhausted {
				break
			}
		}
	}
	remaining[i] = available
	s.rowFillings[depth][i] = 0
	return false
}

// The complete fallback chooses the row with the fewest multiset fillings.
func (s *solver) exact(remaining []int, activeRows, depth int) bool {
	s.budget--
	if s.budget < 0 {
		s.budgetExhausted = true
		return false
	}
	if activeRows&(activeRows-1) == 0 {
		var filling counts
		for i, count := range remaining {
			filling[i] = uint8(count)
		}
		s.storeRow(bits.TrailingZeros64(uint64(activeRows)), filling)
		return true
	}
	key := s.failureKey(remaining, activeRows)
	if s.failed.contains(key[:s.typeCount+2]) {
		return false
	}
	totalLength, maxSum := 0, 0
	for row, length := range s.rows {
		if activeRows>>row&1 != 0 {
			totalLength += length
			maxSum = larger(maxSum, length)
		}
	}
	maxSum = smaller(maxSum, totalLength/2)
	fillingCounts := s.countFillings(remaining, maxSum, fillingCountLimit)
	selectedRow := -1
	for row, length := range s.rows {
		if activeRows>>row&1 == 0 {
			continue
		}
		if fillingCounts[smaller(length, totalLength-length)] == 0 {
			return false
		}
		if length <= totalLength/2 &&
			(selectedRow < 0 || fillingCounts[length] < fillingCounts[s.rows[selectedRow]]) {
			selectedRow = row
		}
	}
	target := s.rows[selectedRow]
	suffix := newSuffix(s.typeCount+1, target)
	s.suffix[depth] = suffix
	suffix[s.typeCount][0] = 1
	for i := s.typeCount - 1; i >= 0; i-- {
		copy(suffix[i], suffix[i+1])
		for copies := 0; copies < remaining[i]; copies++ {
			suffix[i].add(s.lengths[i])
		}
	}
	s.rowFillings[depth] = counts{}
	if s.enumerateExactRow(remaining, activeRows, depth, selectedRow, 0, target) {
		return true
	}
	if !s.budgetExhausted {
		s.failed.insert(key[:s.typeCount+2])
	}
	return false
}

type column struct {
	row     int
	filling counts
}

// Dual ship prices turn column pricing into bounded subset sum.
// Branching fixes complete fillings before the independent exact fallback.
func (s *solver) generateColumns(remaining []int, pricingWork *int,
	activeRows int, inherited []column) bool {
	if activeRows&(activeRows-1) == 0 {
		var filling counts
		for i, count := range remaining {
			filling[i] = uint8(count)
		}
		s.storeRow(bits.TrailingZeros64(uint64(activeRows)), filling)
		return true
	}
	if *pricingWork > pricingWorkLimit {
		return false
	}
	activeRowCount, maxSum := bits.OnesCount64(uint64(activeRows)), 0
	var rowConstraint [maxRows]int
	constraintIndex := 0
	for row, length := range s.rows {
		if activeRows>>row&1 != 0 {
			rowConstraint[row] = constraintIndex
			constraintIndex++
			maxSum = larger(maxSum, length)
		}
	}
	// Each branch owns its columns, retaining the parent's insertion order.
	columns := make([]column, 0, len(inherited))
	for _, candidate := range inherited {
		if activeRows>>candidate.row&1 == 0 {
			continue
		}
		valid := true
		for i, count := range remaining {
			if int(candidate.filling[i]) > count {
				valid = false
				break
			}
		}
		if valid {
			columns = append(columns, candidate)
		}
	}
	width := maxSum + 1
	costStorage := make([]float64, (s.typeCount+1)*width)
	choiceStorage := make([]uint8, (s.typeCount+1)*width)
	minimumCost := make([][]float64, s.typeCount+1)
	chosenCount := make([][]uint8, s.typeCount+1)
	for i := range minimumCost {
		minimumCost[i] = costStorage[i*width : (i+1)*width]
		chosenCount[i] = choiceStorage[i*width : (i+1)*width]
	}
	shipPrices, rowPrices := make([]float64, s.typeCount), make([]float64, s.rowCount)
	var columnWeights []float64
	feasible := false
	for iteration := 0; iteration < columnIterationLimit; iteration++ {
		if *pricingWork >= pricingWorkLimit {
			break
		}
		*pricingWork++
		columnCount := len(columns)
		lp := newLinearProgram(s.typeCount+activeRowCount, columnCount)
		rhsColumn := lp.columnCount + lp.constraintCount
		for i, count := range remaining {
			lp.tableau[i][rhsColumn] = float64(count)
		}
		for i := 0; i < activeRowCount; i++ {
			lp.tableau[s.typeCount+i][rhsColumn] = 1
		}
		for j, candidate := range columns {
			lp.tableau[s.typeCount+rowConstraint[candidate.row]][j] = 1
			lp.tableau[lp.constraintCount][j] = -1
			for i := 0; i < s.typeCount; i++ {
				lp.tableau[i][j] = float64(candidate.filling[i])
			}
		}
		lp.solve()
		columnWeights = make([]float64, columnCount)
		for i, basis := range lp.basis {
			if basis < columnCount {
				columnWeights[basis] = positive(lp.tableau[i][rhsColumn])
			}
		}
		objective := lp.tableau[lp.constraintCount]
		if objective[rhsColumn] >= float64(activeRowCount)-feasibilityEpsilon {
			feasible = true
			break
		}
		for i := range shipPrices {
			shipPrices[i] = positive(objective[columnCount+i])
		}
		for row := 0; row < s.rowCount; row++ {
			if activeRows>>row&1 != 0 {
				rowPrices[row] = objective[columnCount+s.typeCount+rowConstraint[row]]
			}
		}
		for sum := range minimumCost[0] {
			minimumCost[0][sum] = infinitePrice
		}
		minimumCost[0][0] = 0
		for i, length := range s.lengths {
			previous, current := minimumCost[i], minimumCost[i+1]
			choices := chosenCount[i+1]
			copy(current, previous)
			for sum := range choices {
				choices[sum] = 0
			}
			for copies := 1; copies <= remaining[i]; copies++ {
				shift := copies * length
				cost := float64(copies) * shipPrices[i]
				for sum := shift; sum <= maxSum; sum++ {
					candidateCost := previous[sum-shift] + cost
					if candidateCost < current[sum]-pricingEpsilon {
						current[sum] = candidateCost
						choices[sum] = uint8(copies)
					}
				}
			}
		}
		added := 0
		for row, target := range s.rows {
			if activeRows>>row&1 == 0 {
				continue
			}
			if minimumCost[s.typeCount][target]+rowPrices[row] > 1-simplexEpsilon {
				continue
			}
			var filling counts
			remainingLength := target
			for i := s.typeCount; i > 0; i-- {
				copies := int(chosenCount[i][remainingLength])
				filling[i-1] = uint8(copies)
				remainingLength -= copies * s.lengths[i-1]
			}
			if remainingLength != 0 {
				continue
			}
			exists := false
			for _, candidate := range columns {
				if candidate.row == row && candidate.filling == filling {
					exists = true
					break
				}
			}
			if !exists {
				columns = append(columns, column{row, filling})
				added++
			}
		}
		if added == 0 {
			return false
		}
	}
	if !feasible {
		return false
	}
	selectedRow, largestWeight := -1, -1.0
	for j, candidate := range columns {
		if columnWeights[j] > largestWeight {
			largestWeight, selectedRow = columnWeights[j], candidate.row
		}
	}
	order := make([]int, 0)
	for j, candidate := range columns {
		if candidate.row == selectedRow {
			order = append(order, j)
		}
	}
	sort.SliceStable(order, func(left, right int) bool {
		return columnWeights[order[left]] > columnWeights[order[right]]
	})
	for _, j := range order {
		filling := columns[j].filling
		for i := range remaining {
			remaining[i] -= int(filling[i])
		}
		if s.generateColumns(remaining, pricingWork, activeRows^(1<<selectedRow), columns) {
			s.storeRow(selectedRow, filling)
			return true
		}
		for i := range remaining {
			remaining[i] += int(filling[i])
		}
		if *pricingWork >= pricingWorkLimit {
			break
		}
	}
	return false
}

func (s *solver) solve() {
	if s.greedy(initialGreedyAttempts) {
		return
	}
	pricingWork := 0
	remaining := append([]int(nil), s.counts...)
	if s.generateColumns(remaining, &pricingWork, (1<<s.rowCount)-1, nil) {
		return
	}
	s.suffix = make([][]reachableSums, s.rowCount)
	s.rowFillings = make([]counts, s.rowCount)
	s.failed.clear(s.typeCount + 2)
	// Exact budgets double without a final cutoff; each restart also retries greedy.
	for limit := int64(initialExactBudget); ; {
		remaining = append(remaining[:0], s.counts...)
		s.budgetExhausted, s.budget = false, limit
		if s.exact(remaining, (1<<s.rowCount)-1, 0) {
			return
		}
		if s.greedy(retryGreedyAttempts) {
			return
		}
		limit *= 2
		if limit > maxExactBudget {
			limit = maxExactBudget
		}
	}
}

// Buffered byte parsing and decimal output avoid reflection in the I/O path.
func readInt(reader *bufio.Reader) int {
	value := 0
	character, err := reader.ReadByte()
	for err == nil && character <= ' ' {
		character, err = reader.ReadByte()
	}
	for err == nil && character >= '0' && character <= '9' {
		value = value*10 + int(character-'0')
		character, err = reader.ReadByte()
	}
	return value
}

func writeInt(writer *bufio.Writer, value int) {
	var digits [maxRows]byte
	position := len(digits)
	for {
		position--
		digits[position] = byte(value%10) + '0'
		value /= 10
		if value == 0 {
			break
		}
	}
	writer.Write(digits[position:])
}

func main() {
	reader := bufio.NewReaderSize(os.Stdin, inputBufferSize)
	writer := bufio.NewWriterSize(os.Stdout, inputBufferSize)
	defer writer.Flush()
	shipCount, rowCount := readInt(reader), readInt(reader)
	if shipCount == 0 || rowCount == 0 {
		return
	}
	ships, rows := make([]int, shipCount), make([]int, rowCount)
	for i := range ships {
		ships[i] = readInt(reader)
	}
	for i := range rows {
		rows[i] = readInt(reader)
	}
	s := newSolver(ships, rows)
	s.solve()
	for _, row := range s.answer {
		writeInt(writer, len(row))
		writer.WriteByte('\n')
		for _, length := range row {
			writeInt(writer, length)
			writer.WriteByte(' ')
		}
		writer.WriteByte('\n')
	}
}
