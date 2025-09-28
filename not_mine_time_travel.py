def time_traveler(jumping_points: list[int | str], k: int, max_aging: int) -> bool:
    diffs = []
    for i in range(1, len(jumping_points)):
        diffs.append(jumping_points[i] - jumping_points[i - 1])

    diffs.sort(reverse=True)
    return sum(diffs[k:]) <= max_aging


def run_tests():
    tests = [
        # Example from PDF
        (([2020, 2024], 0, 3), False),
        # Example from PDF
        (([2020, 2024], 1, 1), True),
        # Example from PDF
        (([1803, 1861, 1863, 1865, 1920, 1929, 1941, 1964, 2001, 2021], 4, 45), True),
        # Edge case: Just enough aging without jumps
        (([2000, 2001, 2002], 0, 2), True),
        # Edge case: Not enough aging without jumps
        (([2000, 2005, 2010], 0, 4), False),
        # Edge case: All gaps can be jumped
        (([1, 100, 200, 300], 3, 0), True),
        # Edge case: Jumps are necessary and sufficient
        (([1, 10, 20], 1, 9), True),
    ]
    for (jumping_points, k, max_aging), want in tests:
        got = time_traveler(jumping_points, k, max_aging)
        assert got == want, (
            f"\ntime_traveler({jumping_points}, {k}, {max_aging}): got: {got}, want: {want}\n"
        )


if __name__ == "__main__":
    run_tests()