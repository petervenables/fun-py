class FindNonDuplicates:
    def moveElements(self, arr: list) -> list:
        """Find Non-duplicate numbers in a given, sorted list."""
        nnd = 1
        for idx in range(1, len(arr)):
            if arr[idx] != arr[nnd - 1]:
                arr[nnd] = arr[idx]
                nnd += 1
        return arr
