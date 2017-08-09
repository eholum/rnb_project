import billboard

out = '/Users/eho/Documents/r-b-hip-hop.csv'
out_file = open(out, 'w')
out_file.write('\t'.join(['date','artist','title','peakPos','lastPos','weeks','rank','change']) + '\n')
out_file.close()

weeks = 1368
chart = billboard.ChartData('r-b-hip-hop-songs')
for i in range(weeks):
    if not chart.previousDate:
        print("last date:" + str(chart.date))
        break
              
    chart=billboard.ChartData('r-b-hip-hop-songs', date=chart.previousDate)
    out_file = open(out, 'a')
    for c in chart:
        row = [chart.date,
               '"{}"'.format(c.artist),
               '"{}"'.format(c.title),
               c.peakPos,
               c.lastPos,
               c.weeks,
               c.rank,
               c.change]
        row = [str(i) for i in row]
        line = '\t'.join(row)
        out_file.write(line + '\n')
    out_file.close()
        
    if i % 52 == 0:
        print(chart.date)
    
#
# 
#

out = '/Users/eho/Documents/pop.csv'
out_file = open(out, 'w')
out_file.write('\t'.join(['date','artist','title','peakPos','lastPos','weeks','rank','change']) + '\n')
out_file.close()

weeks = 1368
chart = billboard.ChartData('pop-songs')
for i in range(weeks):
    if not chart.previousDate:
        print("last date:" + str(chart.date))
        break
    chart=billboard.ChartData('pop-songs', date=chart.previousDate)
    
    out_file = open(out, 'a')
    for c in chart:
        row = [chart.date,
               '"{}"'.format(c.artist),
               '"{}"'.format(c.title),
               c.peakPos,
               c.lastPos,
               c.weeks,
               c.rank,
               c.change]
        row = [str(i) for i in row]
        line = '\t'.join(row)
        out_file.write(line + '\n')
    out_file.close()
        
    if i % 52 == 0:
        print(chart.date)
