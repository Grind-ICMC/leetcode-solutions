class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = len(position)
        fleet_lead_time = -1.0

        for p, s in sorted(zip(position, speed), reverse=True):
            curr_time = (target - p) / s

            if curr_time <= fleet_lead_time:
                fleets -= 1
            else:
                fleet_lead_time = curr_time
        
        return fleets






        





        