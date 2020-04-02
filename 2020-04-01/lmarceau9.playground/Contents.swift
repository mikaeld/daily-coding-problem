import Foundation

// Daily coding problem #9
// Brute force solution

extension Array where Element == Int {

    /// Avoid self mutation
    func add(_ value: Int) -> [Element] {
        var newList = self
        newList.append(value)
        return newList
    }
}

class HighestSumFinder {

    private let MINIMUM_INT: Int = -2147483648
    private var solutionsList: [[Int]] = []

    var solution: Int {
        return findHighestSum()
    }

    init(list: [Int]) {
        self.findSolutions(from: list)
    }

    // MARK: Private

    /// Find solutions
    private func findSolutions(from list: [Int], possibleSolution: [Int] = []) {
        guard list.count != 0 else {
            self.solutionsList.append(possibleSolution)
            return
        }

        guard list.count > 1 else {
            self.solutionsList.append(possibleSolution.add(list[0]))
            return
        }

        findSolutions(from: list.suffix(list.count - 2), possibleSolution: possibleSolution.add(list[0]))
        findSolutions(from: list.suffix(list.count - 1), possibleSolution: possibleSolution)
    }

    /// Return the highest sum from all the possibilities
    private func findHighestSum() -> Int {
        var solution: Int = MINIMUM_INT
        for possibility in self.solutionsList where sum(possibility) > solution {
            solution = sum(possibility)
        }

        return solution
    }

    /// Sum utility method
    private func sum(_ solution: [Int]) -> Int {
        return solution.reduce(0, +)
    }
}

print(HighestSumFinder(list: [2, 4, 6, 2, 5]).solution == 13)
print(HighestSumFinder(list: [5, 1, 1, 5]).solution == 10)
print(HighestSumFinder(list: [1, 5, 1, 5]).solution == 10)
print(HighestSumFinder(list: [1, -5, 1, 5]).solution == 6)
print(HighestSumFinder(list: [1, 0, 1, -6]).solution == 2)
print(HighestSumFinder(list: [1, 2, 10, 20, 11]).solution == 22)
