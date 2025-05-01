from datetime import timedelta

class Time:
    def __init__(self, hours=0, minutes=0, seconds=0):
       
        self.time = timedelta(hours=hours, minutes=minutes, seconds=seconds)

    def __add__(self, other):
      
        return Time(0, 0, self.time.total_seconds() + other.time.total_seconds())

    def __sub__(self, other):
        
        return Time(0, 0, self.time.total_seconds() - other.time.total_seconds())

    def __str__(self):
        
        total_seconds = int(self.time.total_seconds())
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        return f"{hours:02}:{minutes:02}:{seconds:02}"

    def compare(self, other):
        
        if self.time > other.time:
            return 
        elif self.time < other.time:
            return 
        else:
            return 

    def add_seconds(self, seconds):
       
        self.time += timedelta(seconds=seconds)

    def subtract_seconds(self, seconds):
        
        self.time -= timedelta(seconds=seconds)

    def multiply(self, factor):
        self.time *= factor

    def divide(self, divisor):
        self.time /= divisor





time1 = Time(1, 30, 45) 
time2 = Time(2, 15, 30)  

print("Time 1:", time1)
print("Time 2:", time2)


added_time = time1 + time2
print("Added Time:", added_time)

subtracted_time = time2 - time1
print("Subtracted Time:", subtracted_time)


print("Comparison Result:", time1.compare(time2))


time1.add_seconds(500)
print("Time 1 after adding 500 seconds:", time1)


time2.subtract_seconds(600)
print("Time 2 after subtracting 600 seconds:", time2)
