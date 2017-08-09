import billboard
import datetime

def pull_charts(chart_name, out, overwrite=False, weeks=1):
    if overwrite:
        out_file = open(out, 'w')
        out_file.write('\t'.join(['date','artist','title','peakPos','lastPos','weeks','rank','change']) + '\n')
        out_file.close()

    chart = billboard.ChartData(chart_name)
    date = chart.date
    
    for i in range(weeks):
        
        if not chart.previousDate:
            print("last date:" + str(chart.date))
            break
            
        chart=billboard.ChartData(chart_name, date=chart.previousDate)

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

        date = chart.previousDate
        if i % 52 == 0:
            print(chart.date)
        

# Get the last 25 years of top 100 charts
weeks = 1368
out = '/Users/eho/Documents/hot-100.csv'
pull_charts("hot-100", out, weeks=weeks)
