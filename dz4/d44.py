s=1000m=0p = float(input('годовой % вклада:'))if 0<p<25:    ps=p*s/100/12else:    quit('процент от 0 до 25')while s<1100:    s=s+ps    m+=1print(s, 'через', m, "месяц")