# Method1

[[ $1 ]] &&  appname="${1}-geoip-service" || appname="geoip-service"
echo $appname

# Method 2
VAR=$1
a=${VAR:-20}
echo $a
