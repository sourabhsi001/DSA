def maxIceCream(costs,coins):
         costs.sort()
        past_num_ice=0
        num_ice=0
        if not costs:
             return 0

        if sum(costs)<coins:
            return len(costs)
        for i in costs:
            coins=coins-i
            
            num_ice+=1

            if coins==0:
                return num_ice
            elif coins<0:
                return past_num_ice
            past_num_ice=num_ice

        

        
costs=[7,3,3,6,6,6,10,5,9,2]
coins=56
print(maxIceCream(costs,coins))
print(sum(costs))