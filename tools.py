def print_time(time):
    if time >= 60:
        time_m = time / 60
        time_s = time % 60
        if time_m >= 60:
            time_h = time_m / 60
            time_m = time_m % 60
            print 'Total time cost : %d hours %d minutes %d seconds\n' %(time_h, time_m, time_s)
        else:
            print 'Total time cost : %d minutes %d seconds\n' %(time_m, time_s)
    else:
        print 'Total time cost : %.2f seconds\n' %time