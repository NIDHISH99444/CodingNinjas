def fractionToDecimal( numerator, denominator):
        res = ""
        if numerator>0>denominator or numerator<0<denominator:
            res+="-"
        numerator=abs(numerator)
        denominator=abs(denominator)
        res+=str(numerator//denominator)
        remainder=numerator%denominator
        if remainder>0:
            res+='.'
        hs={}
        while remainder and remainder not in hs:
            hs[remainder]=len(res)
            val=remainder*10
            res+=str(val//denominator)
            remainder=val%denominator
        if remainder in hs:
            #print(res[:hs[remainder]])
            #print(res[hs[remainder:]])

            #return res[:hs[remainder]]+'('+res[hs[remainder]:]+')'
            return res[:hs[remainder]]+'('+res[hs[remainder]:]+')'
        return res

print(fractionToDecimal(-50,8))