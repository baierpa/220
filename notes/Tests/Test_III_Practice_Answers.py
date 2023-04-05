# A
class Color:
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

    def get_rgb(self):
        return [self.red, self.green, self.blue]

    def to_string(self):
        if self.red >= self.green and self.red >= self.blue:
            return "redish"
        if self.green >= self.blue:
            return "greenish"
        return "blueish"

    def set_average_color(self, numbers):
        reds = []
        greens = []
        blues = []
        i = 0
        while i < len(numbers) and len(reds) < 100:
            num = numbers[i]
            if num <= 255:
                reds.append(num)
            elif num <= 510:
                greens.append(num - 255)
            else:
                blues.append(num - 255 * 2)
            i += 1
        self.red = sum(reds) // len(reds)
        self.green = sum(greens) // len(greens)
        self.blue = sum(blues) // len(blues)

# B Continues until the 5th occurrence of 72 (your numbers will vary)
count = 0
total = 0
i = 0
while count < 5:
    curr = random_ages[i]
    if curr == 72:
        count += 1
    elif curr % 2 == 0:
        total += curr
    i += 1
print(total, i)

# C
l1 = []
l2 = []
l3 = []
for num in random_prices:
    if num < 30:
        l1.append(num)
    elif num < 60:
        l2.append(num)
    else:
        l3.append(num)
avg1 = sum(l1)/len(l1)
avg2 = sum(l2)/len(l2)
avg3 = sum(l3)/len(l3)
print('avg sum: ', avg1 + avg2 + avg3)

# D
def is_divisible(dividend, divisor):
    return dividend % divisor == 0

# Plus
class Pen:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color