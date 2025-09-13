def hamming_distance(start, end) -> int:
    if len(start) != len(end):
        raise ValueError("Error: Comparables not same length!")
    return sum(lch != rch for lch, rch in zip(start, end))
