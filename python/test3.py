import re

s='''
3999
West Chester Pike, Mountain View California
, 19999
USA

Palo Alto, Arizona, 19073  USA

'''
US_STATES="California|Arizona"
pstring = "(^|\s|,)+(" + US_STATES + ")\s*,?\s*([0-9]{5})(,|$|\s)+"
search_pattern = re.compile(pstring, flags=re.IGNORECASE|re.MULTILINE)

results = search_pattern.finditer((s))
lookback_len = 51 # Chargoggagoggmanchauggagoggchaubunagungamaugg (45 +6)

lookback_state_code = []
for r in results :
    back = r.start() - lookback_len
    if(back < 0) : back =0

    lookback = s[back:r.start()]
    state = r.groups()[1]
    p_code= r.groups()[2]
    lookback_state_code.append([lookback, state, p_code])

print(lookback_state_code)

jobs = [{ "state" : "CALIFORNIA", "city" : "Palo Alto", "country" :"United States"}]

for t in lookback_state_code :
    for j in jobs :
        lookback = t[0]
        if(j['city'] in lookback ) :
            t.append(j['city'])

print(lookback_state_code)





