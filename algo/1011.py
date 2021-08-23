from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        wei_per_day = sum(weights) // days
        print("wei_per_day:", wei_per_day)
        print("-" * 20)
        remain = len(weights)
        day_weight = 0
        max_capa = 0
        day = 1

        for num in weights:
            if day_weight < wei_per_day and remain != days - day:
                day_weight += num
            else:
                day_weight = num
                day += 1
            remain -= 1
            if day_weight > max_capa:
                max_capa = day_weight
            print("day: {:2} num:{:3} day_weight: {:3}".format(day, num, day_weight))
            print("=" * 20)
        print(max_capa)


if __name__ == "__main__":
    weights = [
        147,
        73,
        265,
        305,
        191,
        152,
        192,
        293,
        309,
        292,
        182,
        157,
        381,
        287,
        73,
        162,
        313,
        366,
        346,
        47,
    ]
    days = 10
    Solution().shipWithinDays(weights, days)
