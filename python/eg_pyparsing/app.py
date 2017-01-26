from pyparsing import Word, nums, alphas,originalTextFor,Optional,Combine,Literal

cv_text = open("cv.txt",'r').read();
first5 =Word(nums,exact=5,asKeyword=True)
# opt_dash = Optional(Literal('-'))
# opt_four = Optional(Word(nums, exact=4, asKeyword=True) )
pattern = first5 #+ Optional(Literal('-') + Word(nums, exact=4,asKeyword=True))

result = pattern.scanString(cv_text)

for t,s,e in result:
    print(t)

    # print(s)
    # print(e)
# print(result)


# housenumber = originalTextFor( numberword | Combine(Word(nums) +
#                     Optional(OPT_DASH + oneOf(list(alphas))+FollowedBy(White()))) +
#                     Optional(OPT_DASH + "1/2")
#                     )


# pattern = Word( alphas ) #+ "," + Word( alphas ) + "!"
# greeting = pattern.parseString( cv_text)
# result = pattern.scanString( cv_text)
# print(result)