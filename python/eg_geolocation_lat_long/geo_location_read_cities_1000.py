# cities1000.txt downloaded from http://download.geonames.org/export/dump/
from  eg_decorator_TimeMe import TimeMe
from math import sin, cos, atan2, sqrt, degrees, radians, pi
from geopy.distance import great_circle as distance
from geopy.point import Point

class GeoLocation(object) :

    def __init__(self, geo_name_city_file, country_code_mapping_file ):
        self._location_lookup = {}
        self._country_code_lookup = {}
        self._state_country_code_lookup = {}
        self._city_country_code_lookup = {}
        self._country_code_to_name_lookup = {}
        self._country_name_to_code_lookup = {}
        self._US_STATE_ABBREV_TO_NAME = self.getUSStateAbbreviationMapping()
        self._US_STATE_NAME_TO_ABBREVIATION = self.getUSStateAbbreviationMapping(reverse=True)
        self._initCountryCodeMappingFile(country_code_mapping_file)
        self._initGeoNameCityFile(geo_name_city_file)



    def _initCountryCodeMappingFile(self, country_code_mapping_file):
        lines = open(country_code_mapping_file, "r", encoding="utf8").readlines()
        for l in lines :
            tokens = l.split(",")
            country_code = tokens[0].strip().upper()
            country = tokens[1].strip().upper()
            capital = tokens[2].strip().upper()
            self._country_code_to_name_lookup[country_code] = country
            self._country_name_to_code_lookup[country] = country_code

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
                "country" : self._country_code_to_name_lookup.get(country_code),
                "state_name" : self.resolveStateAbbreviationToName(state)


            }

            location_string = self._makeLocationString(city, state, country_code)

            state_country_string = self._makeStateCountryCodeString(state, country_code)
            self._location_lookup[location_string] = location_info
            cc_list = self._country_code_lookup.get(country_code)
            if(cc_list is None) :
                cc_list = []
                self._country_code_lookup[country_code] = cc_list
            cc_list.append(location_info)

            scc_list = self._state_country_code_lookup.get(state_country_string)
            if(scc_list is None) :
                scc_list = []
                self._state_country_code_lookup[state_country_string] = scc_list
            scc_list.append(location_info)

            city_country_code_string = self._makeCityCountryCodeString(city, country_code)
            ccc_list = self._city_country_code_lookup.get(city_country_code_string)
            if(ccc_list is None) :
                ccc_list=[]
                self._city_country_code_lookup[city_country_code_string] = ccc_list
            ccc_list.append(location_info)

    def _makeLocationString(self, city, state, country_code):
        return "{},{},{}".format(city, state, country_code).upper()

    def _makeStateCountryCodeString(self, state, country_code):
        return "{},{}".format(state, country_code).upper()

    def _makeCityCountryCodeString(self, city, country_code):
        return "{},{}".format(city, country_code).upper()

    @TimeMe("aaaa")
    def getLatLongList(self, country_code_or_name, state = None,  city= None):
        result = []
        if(city is not None and state is not None) :
            result = self.getLocationsByCityStateCountry(city, state, country_code_or_name, best_effort=True)
        elif(city is not None) :
            result = self.getLocationsByCityCountryCode(city, country_code_or_name)
        elif(state is not None) :
            result = self.getLocationsByStateCountryCode(state, country_code_or_name)
        elif(city is None and state is None) :
            result = self.getLocationsByCountryCode(country_code_or_name)
        return result

    def getLatLongListWithDict(self, location_dict):  # {'countryName': 'China', 'subdivision1name': '11', 'cityName': 'Beijing'}
        return self.getLatLongList(location_dict.get("countryName"), state=location_dict.get("subdivision1name"), city=location_dict.get("cityName"))


    # @classmethod
    # def centerOfPoints(cls, points ):
    #
    #     num = len(points)
    #     if(num ==0) :
    #         return None
    #     elif(num ==1 ) :
    #         return points[0]
    #     else :
    #         lats = sorted([p.latitude for p in points])
    #         lons = sorted([p.longitude for p in points])
    #         mid_lat = (lats[-1] - lats[0])/2 -3.14
    #         mid_lon = (lons[-1] - lons[0])/2 -3.14
    #         return Point(mid_lat, mid_lon)


        """
        http://www.geomidpoint.com/example.html
        http://gis.stackexchange.com/questions/6025/find-the-centroid-of-a-cluster-of-points
        """
        # sum_x, sum_y, sum_z = 0, 0, 0
        # for p in list_of_lat_long_points:
        #     lat = p.latitude
        #     lon = p.longitude
        #     ## convert lat lon to cartesian coordinates
        #     sum_x = sum_x + cos(lat) * cos(lon)
        #     sum_y = sum_y + cos(lat) * sin(lon)
        #     sum_z = sum_z + sin(lat)
        # num_points = float(len(list_of_lat_long_points))
        # avg_x = sum_x / num_points
        # avg_y = sum_y / num_points
        # avg_z = sum_z / num_points
        # center_lon = atan2(avg_y, avg_x)
        # hyp = sqrt(avg_x * avg_x + avg_y * avg_y)
        # center_lat = atan2(avg_z, hyp)
        # return Point(latitude=degrees(center_lat), longitude = degrees(center_lon))


    # def getLatLongRegionCenter(self, country_code_or_name, state = None,  city= None):
    #     locations = self.getLatLongList(country_code_or_name, state, city)
    #     len_loc = len(locations)
    #     result = {
    #         "longitude" : None,
    #         "latitude" : None
    #     }
    #     if(len_loc == 0 ) :
    #         return {}
    #     elif(len_loc == 1 ) :
    #         loc = locations[0]
    #         return {
    #             "latitude" : loc.get("latitude"),
    #             "longitude" : loc.get("longitude")
    #         }
    #     else :
    #         points = [ Point(l.get("latitude"), l.get("longitude"))for l in locations]
    #         center_point = GeoLocation.centerOfPoints(points)
    #         return {
    #             "latitude": center_point.latitude,
    #             "longitude": center_point.longitude
    #         }





        # {
        #     "coordinate": {"longitude": -80.2907943725586, "latitude": 25.772714614868164},
        #     "subdivision1Found": True,
        #     "cityFound": True,
        #     "countryFound": True,
        #     "location": {"subdivision1name": "Florida", "countryName": "United States", "cityName": "Miami"}}

    def resolveStateNameToAbbreviation(self, state):
        if(state is None) : return None
        abbrev =  self._US_STATE_NAME_TO_ABBREVIATION.get(state.upper())
        if(abbrev is not None) : return abbrev
        return state.upper()

    def resolveStateAbbreviationToName(self, state_abbrev):
        if(state_abbrev is None) : return None
        state_name = self._US_STATE_ABBREV_TO_NAME.get(state_abbrev.upper())
        if(state_name is not None) : return state_name
        return state_abbrev.upper()

    def resolveCountryNameToCode(self, country_name):
        country_name = country_name.upper()
        country_code = self._country_name_to_code_lookup.get(country_name) if (len(country_name) != 2) else country_name  # Assume that country_code is always 2 char and no conflict
        return country_code

    def getLocationsByCityStateCountry(self, city, state_or_abbrev, country_code_or_name, best_effort=False):
        country_code = self.resolveCountryNameToCode(country_code_or_name)
        state_abbrev = self.resolveStateNameToAbbreviation(state_or_abbrev)
        loc = self._location_lookup.get(self._makeLocationString(city, state_abbrev, country_code))
        if (loc is None and best_effort):
            result = self.getLocationsByCityCountryCode(city, country_code)  # try again by ignoring state
        else:
            result = [loc]
        return result

    def getLocationsByCountryCode(self, country_code_or_name):
        country_code = self.resolveCountryNameToCode(country_code_or_name)
        return self._country_code_lookup.get(country_code) # list of location_info [ { city + state + country_code + latitude + longitude}]

    def getLocationsByStateCountryCode(self, state_or_abbrev, country_code_or_name):
        country_code = self.resolveCountryNameToCode(country_code_or_name)
        state = self.resolveStateNameToAbbreviation(state_or_abbrev)
        state_country_code_string = self._makeStateCountryCodeString(state, country_code)
        return self._state_country_code_lookup.get(state_country_code_string)  # list of location_info [ { city + state + country_code + latitude + longitude}]

    def getLocationsByCityCountryCode(self, city, country_code_or_name):
        country_code = self.resolveCountryNameToCode(country_code_or_name)
        city_country_code_string = self._makeCityCountryCodeString(city, country_code)
        return self._city_country_code_lookup.get(city_country_code_string)  # list of location_info [ { city + state + country_code + latitude + longitude}]

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
xx = gl.getLatLongList("MY")

print(xx)
