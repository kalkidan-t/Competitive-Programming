from typing import List

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        output = []

        for i in range(left, right + 1):
            i_str = str(i)
            is_self_dividing = True

            for j_str in i_str:
                j = int(j_str)
                if j == 0 or i % j != 0:
                    is_self_dividing = False
                    break

            if is_self_dividing:
                output.append(i)

        return output
