def largestAltitude( gain):
        altitude=[0]
        current=0
        for gain in gain:
            next_alti=(current)+(gain)
            print(next_alti)
            altitude.append(next_alti)
            current=next_alti
            
        print(altitude)
        return max(altitude)


gain = [-5,1,5,0,-7]
print(largestAltitude(gain))