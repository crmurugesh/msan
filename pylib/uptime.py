def getuptime(utime):
    print utime
    print int(utime.split()[-2])

getuptime('up 20 minutes')
getuptime('up 1 year, 13 weeks, 6 days, 19 hours, 5 minutes')
