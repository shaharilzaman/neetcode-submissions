class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        desc = sorted(zip(position, speed), reverse=True)
        output = {}
        last = None  # arrival time of the fleet directly ahead

        for p, s in desc:
            time = (target - p) / s
            if last is None or time > last:   # can't catch up, so it's a new fleet
                output[time] = []
                last = time
            output[last].append(p)            # joins the fleet ahead (or its own new one)

        return len(output.keys())