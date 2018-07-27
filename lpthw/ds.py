def somefunc(h,y,c):
    print(f"{h}{y}{c} this works!")


holy_crap = {"h":"holy","y":"_","c":"crap"}


somefunc(**holy_crap)