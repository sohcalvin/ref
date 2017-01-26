from __future__ import absolute_import
import re

US_STATES_ABBREV = {
'AL':'ALABAMA',
'AK':'ALASKA',
'AZ':'ARIZONA',
'AR':'ARKANSAS',
'CA':'CALIFORNIA',
'CO':'COLORADO',
'CT':'CONNECTICUT',
'DE':'DELAWARE',
'FL':'FLORIDA',
'GA':'GEORGIA',
'HI':'HAWAII',
'ID':'IDAHO',
'IL':'ILLINOIS',
'IN':'INDIANA',
'IA':'IOWA',
'KS':'KANSAS',
'KY':'KENTUCKY',
'LA':'LOUISIANA',
'ME':'MAINE',
'MD':'MARYLAND',
'MA':'MASSACHUSETTS',
'MI':'MICHIGAN',
'MN':'MINNESOTA',
'MS':'MISSISSIPPI',
'MO':'MISSOURI',
'MT':'MONTANA',
'NE':'NEBRASKA',
'NV':'NEVADA',
'NH':'NEW HAMPSHIRE',
'NJ':'NEW JERSEY',
'NM':'NEW MEXICO',
'NY':'NEW YORK',
'NC':'NORTH CAROLINA',
'ND':'NORTH DAKOTA',
'OH':'OHIO',
'OK':'OKLAHOMA',
'OR':'OREGON',
'PA':'PENNSYLVANIA',
'RI':'RHODE ISLAND',
'SC':'SOUTH CAROLINA',
'SD':'SOUTH DAKOTA',
'TN':'TENNESSEE',
'TX':'TEXAS',
'UT':'UTAH',
'VT':'VERMONT',
'VA':'VIRGINIA',
'WA':'WASHINGTON',
'WV':'WEST VIRGINIA',
'WI':'WISCONSIN',
'WY':'WYOMING'
}
US_STATES = ""
for k,v in US_STATES_ABBREV.items() :
    US_STATES += "|" + k +"|" + v
US_STATES = US_STATES[1:]
pstring= "\s+(" + US_STATES + ")\s*,?\s*([0-9]{5})\s+"
search_pattern= re.compile(pstring, flags=re.IGNORECASE)
split_pattern = re.compile("(" +US_STATES + ")", flags=re.IGNORECASE)
def extractStatePrecedingPostcode(text):
    res = search_pattern.findall((text))
    states =[]
    for match in res :
        state = match[0].upper()
        state = US_STATES_ABBREV.get(state , state)
        print(state)



def extractUSLocationByPostalCode(text):
    code_list = re.finditer(search_pattern, text)
    ret = []
    for match in code_list:
        m_string = match.group(0).strip()
        dum, state, code = re.split(split_pattern, m_string)
        code = re.sub(r'\s*,?\s*','',code)
        state = state.upper()
        state = US_STATES_ABBREV.get(state, state)
        ret.append({"state" : state, "post_code" : code})
    return ret

def extractStatePrecedingPostcode2(text):
    code_list = re.finditer(
        r'\s+(Alabama|Alaska|Arizona|Arkansas|California|Colorado|Connecticut|Delaware|Florida|Georgia|Hawaii|Idaho|Illinois|Indiana|Iowa|Kansas|Kentucky|Louisiana|Maine|Maryland|Massachusetts|Michigan|Minnesota|Mississippi|Missouri|Montana|Nebraska|Nevada|New Hampshire|New Jersey|New Mexico|New York|North Carolina|North Dakota|Ohio|Oklahoma|Oregon|Pennsylvania|Rhode Island|South Carolina|South Dakota|Tennessee|Texas|Utah|Vermont|Virginia|Washington|West Virginia|Wisconsin|Wyoming|AL|AK|AS|AZ|AR|CA|CO|CT|DE|DC|FL|GA|GU|HI|ID|IL|IN|IA|KS|KY|LA|ME|MD|MH|MA|MI|FM|MN|MS|MO|MT|NE|NV|NH|NJ|NM|NY|NC|ND|MP|OH|OK|OR|PW|PA|PR|RI|SC|SD|TN|TX|UT|VT|VA|VI|WA|WV|WI|WY)\s*,?\s*[0-9]{5}\s+',
        text, flags=re.IGNORECASE)
    longest_match = ''

    for match in code_list:
        # print(match.group(0))
        # print(match.end, match)
        # print("=====")
        if len(match.group(0)) > len(longest_match):
            longest_match = match.group(0)
    return longest_match




text = """
I live in PA 12345
I don't live california 67890123
I don't live arizona   67893
I don't live arizona   ,  67893
I don't livsdfsdfe ca67890
I don't live sis ak     ,   67890123
123123123
12345
"""
# print(extractUSLocationByPostalCode(text))

def testOne():
    s = "Jakarta.*01|Chengdu.*51|Beijing.*11|Moscow.*MOW|Paris.*75|Dubai.*DU|Feltham.*LND|Barcelona.*B|Virtual - Germany.*BW|Shanghai.*31|Munich.*BY|Walldorf/St. Leon-Rot.*BW|Ra'anana.*M|Milan.*MI|Reston.*Virginia|Dresden.*BW|Palo Alto.*California|Belfast.*BFS|Buenos Aires.*B|Houston.*Texas|Atlanta.*Georgia|Bogota.*DC|Montreal.*QC|St. Leon-Rot.*BW|Singapore.*01|Newtown Square.*Pennsylvania|Berlin.*BE|Chicago.*Illinois|Prague.*PR|Scottsdale.*Arizona|Riyadh.*01|São Leopoldo.*RS|Jakarta.*JK|Perth.*WA|Markdorf.*BW|Budapest.*BU|Athens.*03|Woodmead.*GT|Bucharest.*B|Washington D.C..*District of Columbia|Virtuell – Deutschland.*BW|Miami.*Florida|Muscat.*DU|Gliwice.*SL|Galway.*G|Johannesburg.*GT|Boston.*Massachusetts|Herndon.*Virginia|Potsdam.*BB|Hamburg.*BW|Seoul.*11|Downers Grove.*Illinois|Alpharetta.*Georgia|San Francisco.*California|Brussels.*BRU|Lima.*LMA|Ho Chi Minh.*65|Newtown Square.*California|Sydney.*NSW|Islamabad.*DU|St. Ingbert.*SL|Toronto.*New York|Dallas.*Texas|Melbourne.*VIC|Berlin.*BW|Regensdorf.*ZH|Bangalore.*KA|Gurgaon.*HR|Doha.*DU|New York.*New York|Irvine.*California|Vancouver.*BC|Potsdam.*BE|Mexico City.*MEX|Dublin.*D|Warszawa.*MZ|Kuwait City.*DU|Bangkok.*10|Century City.*WC|Nairobi.*110|South San Francisco.*California|Timisoara.*TM|Shenzhen.*44|Wildau.*SN|Bellevue.*Washington|Sofia.*22|São Paulo.*SP|Rome.*RM|Maidenhead.*LND|Cairo.*C|Montreal.*ON|Istanbul.*34|Mumbai.*MH|New York.*Illinois|Global.*D|Dalian.*21|Vienna.*9|Madrid.*M|Lisboa.*11|Copenhagen.*84|Dubai.*DU|Pittsburgh.*Pennsylvania|Xi’an.*61|Dresden.*SN|Toronto.*ON|Tokyo.*13|La Crosse.*Wisconsin|Dubai.*AZ|Hamburg.*HH|Düsseldorf/Ratingen.*BW|Bangalore.*11|Sofia.*23|San Jose.*California|Cincinnati.*Ohio|Berlin.*BB|Brno.*622|Manila.*00|Rabat.*CAS|Ottawa.*ON|Cluj-Napoca.*CJ|Ekaterinburg.*SVE|Schoenefeld.*BB|New Delhi.*KA|Bogota.*SJ|Madrid.*MD|Mexico City.*NLE|Paris.*75|Virtuell - Österreich.*9|San José.*SJ|Hong Kong.*HK|Boulder.*Colorado|Irving.*Texas|Palo Alto.*Colorado|Taipei.*TPE|Mexico City.*DIF|Naperville.*Illinois|Kuala Lumpur.*14|Gurgaon.*DL|Miami.*DC|Shanghai.*HK|Shanghai.*Pennsylvania|Raleigh-Durham.*North Carolina|Santiago.*RM|Burlington.*Massachusetts|Rabat.*08|Dalian.*13|Knutsford.*LND|Buenos Aires.*C|Auckland.*AUK|Canberra.*ACT|Kuala Lumpur.*01|Virtuell – Deutschland.*BE|Athens.*01|s-Hertogenbosch.*NB|Toronto.*Pennsylvania|Virtual - Germany.*BE|Freiberg.*BW|Detroit.*Michigan|Dublin.*California|Gurgaon.*KA|Palo Alto.*Pennsylvania|Minneapolis.*Minnesota|St. Louis.*Missouri|Karlsruhe.*BW|Doha.*DA|Minnetonka.*Michigan|Munich.*BW|Portland.*Oregon|San Ramon.*California|Barcelona.*34|Bangkok.*01|Singapore.*ACT|St.Gallen.*SG|Los Angeles.*California|Caen.*P|Iselin.*New Jersey|Siegen.*NW|Stockholm.*BW|Lima.*LIM|Amsterdam.*GR|Bogota.*B|Stockholm.*AB|Ljubljana.*061|Pittsburgh.*California|Perth.*AUK|Hallbergmoos.*BY|Shanghai.*11|Mumbai.*MP|Osaka.*13|Taipei.*TPQ|Hyderbad.*AP|Nanjing.*32|Lake Mary.*Florida|St. Ingbert.*BW|Osaka.*27|Guangzhou.*44|London.*LND|Shenzhen.*11|Brisbane.*QLD|Schoenefeld.*BE|Parsippany.*New Jersey|Amsterdam.*ZH|Paris.*BW|Bratislava.*BL|Waterloo.*ON|Palo Alto.*New York|Downers Grove.*Pennsylvania|Newtown Square.*PA|Sydney.*ACT|Rio de Janeiro.*RJ|Jakarta.*01|Madrid.*B|Paris.*92|Downers Grove.*New York|Woodmead.*GT|Almaty.*MOW|Feltham.*11|Barcelona.*D|Hong Kong.*11|Athens.*A1|Mumbai.*KA|St. Leon-Rot.*BY|St.Gallen.*ZH|Beijing.*31|Tokyo.*11|Bangalore.*13|Melbourne.*NSW|London.*LND|Singapore.*10|s-Hertogenbosch.*LND|Calgary.*AB|Carlsbad.*California|Barcelona.*M|Dublin.*BW|Moscow.*AST|San José.*DC|Tägerwilen.*TG|Jakarta.*12|Auckland.*AUK|Shanghai.*BW|Dubai.*01|Seoul.*13|Bangalore.*HR|Miami.*FL|Boulder.*CO|Manila.*03|Milan.*M|Feltham.*GBN|Feltham.*LND|Austin.*Texas|Bangkok.*01|Feltham.*CLR|New Delhi.*DL|Newtown Square.*New York"
    s = "(abc)[,\s]*(def)|(123)[,\s]*(456)|(xy)[,\s]*(z)"
    p = re.compile(s, flags=re.IGNORECASE)
    r = p.findall("""
        The cow jumped over the moon
        I know aBc ,   def
        I can count 123  ,, 456
        that is all I know
        abc ,, def
             """)
    # print(r)
    for i in r :
        city_state=[]
        for t in i :
            if(t != '') :
                city_state.append(t)
        print(city_state)
        # for x in i :
        #     print(x)

# testOne()

def testTwo() :
    s1 = "xNH 12345\n"
    res = re.findall(r'\bNH 12345\b', s1)
    print(res)

testTwo()
