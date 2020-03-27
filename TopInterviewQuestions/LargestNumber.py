from functools import cmp_to_key
def largestNumber( nums):
    def cmp_func(x, y):
        """Sorted by value of concatenated string increasingly."""
        if x + y > y + x:
            return 1
        elif x == y:
            return 0
        else:
            return -1

    # Build nums contains all numbers in the String format.
    nums = [str(num) for num in nums]
    print(nums)
    # Sort nums by cmp_func decreasingly.
    nums.sort(key=cmp_to_key(cmp_func), reverse=True)

    # Remove leading 0s, if empty return '0'.
    return ''.join(nums).lstrip('0') or '0'


print(largestNumber([3,30,34,5,9]))