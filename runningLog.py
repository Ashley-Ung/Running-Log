import datetime

def calculateHeartRate (age, restingHeartRate):
    heartRate = ((220 - age) - restingHeartRate) * 0.8 + restingHeartRate
    return heartRate

def calculatePace (distance, time):
    pace = time / distance
    return pace

def calculateBenefits (distance, time):
    benefits = distance * time * 0.01
    return benefits

def logRunningDetails (distance, time, age, resting_heart_rate):
    heartRate = calculateHeartRate (age, restingHeartRate)
    pace = calculatePace (distance, time)
    benefits = calculateBenefits (distance, time)
    now = datetime.datetime.now ()
    month = now.strftime ("%B")
    year = now.year
    with open (f"{month}-{year}.txt", "a") as f:
        f.write (f"{now.strftime('%Y-%m-%d %H:%M:%S')}: Distance: {distance} km, Time: {time} mins, Heart Rate: {heartRate} bpm, Pace: {pace} min/km, Benefits: {benefits} calories\n")
    print (f"Details logged successfully for {month}-{year}.")

distance = float (input ("Enter the distance (in km) ran: "))
time = float (input ("Enter the time (in mins) taken: "))
age = int (input ("Enter your age: "))
restingHeartRate = int (input ("Enter your resting heart rate: "))

# Log the running details
logRunningDetails (distance, time, age, restingHeartRate)
