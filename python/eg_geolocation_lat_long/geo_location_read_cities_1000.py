# cities1000.txt downloaded from http://download.geonames.org/export/dump/
from  eg_decorator_TimeMe import TimeMe
from math import sin, cos, atan2, sqrt, degrees, radians, pi
from geopy.distance import great_circle as distance
from geopy.point import Point

class GeoLocation(object) :

    def __init__(self, geo_name_city_file, country_code_mapping_file ):
        self.location_lookup = {}
        self.country_code_lookup = {}
        self.state_country_code_lookup = {}
        self.city_country_code_lookup = {}
        self.country_code_to_name_lookup = {}
        self.country_name_to_code_lookup = {}
        self.US_STATE_ABBREV_TO_NAME = self.getUSStateAbbreviationMapping()
        self.US_STATE_NAME_TO_ABBREVIATION = self.getUSStateAbbreviationMapping(reverse=True)
        self._initCountryCodeMappingFile(country_code_mapping_file)
        self._initGeoNameCityFile(geo_name_city_file)



    def _initCountryCodeMappingFile(self, country_code_mapping_file):
        lines = open(country_code_mapping_file, "r", encoding="utf8").readlines()
        for l in lines :
            tokens = l.split(",")
            country_code = tokens[0].strip().upper()
            country = tokens[1].strip().upper()
            capital = tokens[2].strip().upper()
            self.country_code_to_name_lookup[country_code] = country
            self.country_name_to_code_lookup[country] = country_code

    def _initGeoNameCityFile(self, geo_name_city_file) :
        lines = open(geo_name_city_file, "r", encoding="utf8").readlines()
        for l in lines :
            tokens = l.split("\t")
            geonameid         = tokens[0]
            name              = tokens[1]
            asciiname         = city = tokens[2]
            alternatenames    = tokens[3]
            latitude          = tokens[4]
            longitude         = tokens[5]
            feature_class     = tokens[6]
            feature_code      = tokens[7]
            country_code      = tokens[8]
            cc2               = tokens[9]
            admin1_code       = state = tokens[10]
            admin2_code       = tokens[11]
            admin3_code       = tokens[12]
            admin4_code       = tokens[13]
            population        = tokens[14]
            elevation         = tokens[15]
            dem               = tokens[16]
            timezone          = tokens[17]
            modification_date = tokens[18]
            location_info = {
                "city" : city,
                "state" : state,
                "country_code" : country_code,
                "latitude" : latitude,
                "longitude" : longitude,
                "country" : self.country_code_to_name_lookup.get(country_code),
                "state_name" : self.resolveStateAbbreviationToName(state)


            }
            location_string = self._location_string(city, state, country_code)

            state_country_string = self._state_country_code_string(state, country_code)
            self.location_lookup[location_string] = location_info
            cc_list = self.country_code_lookup.get(country_code)
            if(cc_list is None) :
                cc_list = []
                self.country_code_lookup[country_code] = cc_list
            cc_list.append(location_info)

            scc_list = self.state_country_code_lookup.get(state_country_string)
            if(scc_list is None) :
                scc_list = []
                self.state_country_code_lookup[state_country_string] = scc_list
            scc_list.append(location_info)

            city_country_code_string = self._city_country_code_string(city, country_code)
            ccc_list = self.city_country_code_lookup.get(city_country_code_string)
            if(ccc_list is None) :
                ccc_list=[]
                self.city_country_code_lookup[city_country_code_string] = ccc_list
            ccc_list.append(location_info)



    def _location_string(self, city, state, country_code):
        return "{},{},{}".format(city, state, country_code).upper()

    def _state_country_code_string(self, state, country_code):
        return "{},{}".format(state, country_code).upper()

    def _city_country_code_string(self, city, country_code):
        return "{},{}".format(city, country_code).upper()

    @TimeMe("aaaa")
    def getLatLongList(self, country_code_or_name, state = None,  city= None):
        country_code_or_name = country_code_or_name.upper()
        country_code = self.country_name_to_code_lookup.get(country_code_or_name) if(len(country_code_or_name) != 2) else country_code_or_name # Assume that country_code is always 2 char and no conflict

        state = self.resolveStateNameToAbbreviation(state)

        if(city is None and state is None) :
            return self.getLocationsByCountryCode(country_code)
        if(city is None) :
            return self.getLocationsByStateCountryCode(state, country_code)
        if(state is None) :
            return self.getLocationsByCityCountryCode(city, country_code)
        return [ self.location_lookup.get(self._location_string(city, state, country_code)) ]

    def getLatLongListWithDict(self, location_dict):  # {'countryName': 'China', 'subdivision1name': '11', 'cityName': 'Beijing'}
            
            self.getLatLongList(location_dict.get("countryName"), state=location_dict.get("subdivision1name"), city=location_dict.get("cityName"))


        # {
        #     "coordinate": {"longitude": -80.2907943725586, "latitude": 25.772714614868164},
        #     "subdivision1Found": True,
        #     "cityFound": True,
        #     "countryFound": True,
        #     "location": {"subdivision1name": "Florida", "countryName": "United States", "cityName": "Miami"}}

    def resolveStateNameToAbbreviation(self, state):
        if(state is None) : return None
        abbrev =  self.US_STATE_NAME_TO_ABBREVIATION.get(state.upper())
        if(abbrev is not None) : return abbrev
        return state.upper()

    def resolveStateAbbreviationToName(self, state_abbrev):
        if(state_abbrev is None) : return None
        state_name = self.US_STATE_ABBREV_TO_NAME.get(state_abbrev.upper())
        if(state_name is not None) : return state_name
        return state_abbrev.upper()

    def getLocationsByCountryCode(self, country_code):
        return self.country_code_lookup.get(country_code) # list of location_info [ { city + state + country_code + latitude + longitude}]

    def getLocationsByStateCountryCode(self, state, country_code):
        state_country_code_string = self._state_country_code_string(state, country_code)
        return self.state_country_code_lookup.get(state_country_code_string)  # list of location_info [ { city + state + country_code + latitude + longitude}]

    def getLocationsByCityCountryCode(self, city, country_code):
        city_country_code_string = self._city_country_code_string(city, country_code)
        return self.city_country_code_lookup.get(city_country_code_string)  # list of location_info [ { city + state + country_code + latitude + longitude}]

    def getUSStateAbbreviationMapping(self, reverse=False):
        US_STATE_ABBREV = {
            'AL': 'ALABAMA',
            'AK': 'ALASKA',
            'AZ': 'ARIZONA',
            'AR': 'ARKANSAS',
            'CA': 'CALIFORNIA',
            'CO': 'COLORADO',
            'CT': 'CONNECTICUT',
            'DE': 'DELAWARE',
            'FL': 'FLORIDA',
            'GA': 'GEORGIA',
            'HI': 'HAWAII',
            'ID': 'IDAHO',
            'IL': 'ILLINOIS',
            'IN': 'INDIANA',
            'IA': 'IOWA',
            'KS': 'KANSAS',
            'KY': 'KENTUCKY',
            'LA': 'LOUISIANA',
            'ME': 'MAINE',
            'MD': 'MARYLAND',
            'MA': 'MASSACHUSETTS',
            'MI': 'MICHIGAN',
            'MN': 'MINNESOTA',
            'MS': 'MISSISSIPPI',
            'MO': 'MISSOURI',
            'MT': 'MONTANA',
            'NE': 'NEBRASKA',
            'NV': 'NEVADA',
            'NH': 'NEW HAMPSHIRE',
            'NJ': 'NEW JERSEY',
            'NM': 'NEW MEXICO',
            'NY': 'NEW YORK',
            'NC': 'NORTH CAROLINA',
            'ND': 'NORTH DAKOTA',
            'OH': 'OHIO',
            'OK': 'OKLAHOMA',
            'OR': 'OREGON',
            'PA': 'PENNSYLVANIA',
            'RI': 'RHODE ISLAND',
            'SC': 'SOUTH CAROLINA',
            'SD': 'SOUTH DAKOTA',
            'TN': 'TENNESSEE',
            'TX': 'TEXAS',
            'UT': 'UTAH',
            'VT': 'VERMONT',
            'VA': 'VIRGINIA',
            'WA': 'WASHINGTON',
            'WV': 'WEST VIRGINIA',
            'WI': 'WISCONSIN',
            'WY': 'WYOMING',
            'DC': 'DISTRICT OF COLUMBIA'
        }
        if(reverse == False ) : return US_STATE_ABBREV
        reverse_map = {}
        for k, v in US_STATE_ABBREV.items() :
            reverse_map[v] = k
        return reverse_map






gl = GeoLocation("cities1000.txt", "country_code_capital_mapping.txt")
xx = gl.getLatLongList("US", state="California")

for x in xx :
    print(x)

