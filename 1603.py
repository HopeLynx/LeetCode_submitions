class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.parkSpots = [big,medium,small]

    def addCar(self, carType: int) -> bool:
        if self.parkSpots[carType-1]:
            self.parkSpots[carType-1] -= 1
            return True
        return False


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)

# Runtime: 128 ms, faster than 97.27% of Python3 online submissions for Design Parking System.
# Memory Usage: 14.4 MB, less than 99.16% of Python3 online submissions for Design Parking System.
