class Hamster:
    def __init__(self, h, g):
        self.h = h
        self.g = g

    def total_food_for_hamster(self, n):
        return self.h + n * self.g

    @staticmethod
    def find_amount_of_hamsters(input_file):
        with open(input_file, mode="r") as f:
            s = int(f.readline())
            c = int(f.readline())
            hamsters = []

            for i in range(c):
                hams = Hamster(*list(map(int, f.readline().split(" "))))
                if hams.h <= s:
                    hamsters.append(hams)
        amount_of_hamsters = 0

        for i in hamsters:
            amount_of_hamsters += 1

            hamsters.sort(key=lambda hamster: hamster.total_food_for_hamster(amount_of_hamsters - 1))

            current_s = sum(hamster.total_food_for_hamster(amount_of_hamsters - 1 ) for hamster in hamsters[:amount_of_hamsters - 1])

            if current_s > s:
                amount_of_hamsters -= 1
                break
        with open("hamsters_out.txt", mode="w") as f:
            f.write(f"{amount_of_hamsters}")
        return amount_of_hamsters
