# cities1000.txt downloaded from http://download.geonames.org/export/dump/

class GeoLocation(object) :

    def __init__(self, geo_name_city_file ):
        self.location_lookup = {}
        self.country_code_lookup = {}
        self.state_country_code_lookup = {}
        self.city_country_code_lookup = {}
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
                "longitude" : longitude
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

    def getLatLong(self, country_code, state = None,  city= None):
        if(city is None and state is None) :
            return self.getLocationsByCountryCode(country_code)
        if(city is None) :
            return self.getLocationsByStateCountryCode(state, country_code)
        if(state is None) :
            return self.getLocationsByCityCountryCode(city, country_code)
        return [ self.location_lookup.get(self._location_string(city, state, country_code)) ]

    def getLocationsByCountryCode(self, country_code):
        return self.country_code_lookup.get(country_code) # list of location_info [ { city + state + country_code + latitude + longitude}]

    def getLocationsByStateCountryCode(self, state, country_code):
        state_country_code_string = self._state_country_code_string(state, country_code)
        return self.state_country_code_lookup.get(state_country_code_string)  # list of location_info [ { city + state + country_code + latitude + longitude}]

    def getLocationsByCityCountryCode(self, city, country_code):
        city_country_code_string = self._city_country_code_string(city, country_code)
        return self.city_country_code_lookup.get(city_country_code_string)  # list of location_info [ { city + state + country_code + latitude + longitude}]

gl = GeoLocation("cities1000.txt")
xx = gl.getLatLong("US",  city="newtown" )
for x in xx :
    print(x)

