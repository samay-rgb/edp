pl=4.0 #reference path loss coefficient,
alpha=2.3 #path loss exponent
def dist(rssi):
    '''This method will calculate the distance of each access point from the device using the RSSI values'''
    d=[]
    for val in rssi:
        x = 10**((pl-val)/(10*alpha))
        if val==0:
            x=0
        d.append(x)
    return d

def calcWeight(dist):
    '''This method will calculate the weight of each access point from the device using the distance values'''
    w=[]
    tot = 0
    for x in dist:
        tot=tot+1/x
    for val in dist:
        x = 1/(val*tot)
        w.append(x)
    return w

def calcLocation(weights,wifiLocs):
    '''This method will calculate the location of the device using the weights and the location of the access points'''
    x=0
    y=0
    for locs in wifiLocs:
        xi=locs[0]
        yi=locs[1]
        x=x+xi*weights[wifiLocs.index(locs)]
        y=y+yi*weights[wifiLocs.index(locs)]
    return x,y

def main():
    '''WPL algorithm'''
    rssi = [-55,-65,-70,-80]
    wifiLocs = [[0,0],[0,10],[10,0],[10,10]]
    dists = dist(rssi)
    weights = calcWeight(dists)
    x,y = calcLocation(weights,wifiLocs)
    print("Location of the device is: ",x,y)
