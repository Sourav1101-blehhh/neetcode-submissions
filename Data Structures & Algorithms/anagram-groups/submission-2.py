class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = defaultdict(list)

        for word in strs:
            # sorted(word) runs in C (Timsort) and returns a list of chars
            # tuple() converts it to a hashable key without string-joining overhead
            groups[tuple(sorted(word))].append(word)

        return list(groups.values())

