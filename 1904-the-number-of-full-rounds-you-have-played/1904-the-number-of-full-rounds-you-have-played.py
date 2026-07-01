class Solution:
    def numberOfRounds(self, loginTime: str, logoutTime: str) -> int:
        h1,m1=map(int,loginTime.split(":"))
        h2,m2=map(int,logoutTime.split(":"))

        login=h1*60+m1
        logout=h2*60+m2
        if logout < login:
            logout += 24 * 60
        
       


        login=((login+14)//15)*15
        logout=(logout//15)*15
        return max(0, (logout - login) // 15)
        