from datetime import date, timedelta

def customizeDate(year):
    
    # while year < 0:


    # date(year, month, day)
    d = date(year, 1, 1)

    #d = date(year, month, 1)
    # d = date(2018, 10, 1)

    #Finds the beginning of the work period, monday, of the work year
    def PStart(MonthStart):
        weekday = int(MonthStart.strftime('%u'))
        Monday = MonthStart - timedelta(days=(weekday-1))
        #print("The start day is", Monday.strftime('%a %b %Y'))
        return Monday

    #finds the ending of the work period, sunday, of the the work year
    def PEnd(Monday):
        Sun = Monday + timedelta(days=6)
        return Sun

    PeriodStart = PStart(d)
    PeriodEnd = PEnd(PeriodStart)

    #determines the months being produced
    SMonthNum = int(PeriodStart.strftime('%m'))
    EMonthNum = int(PeriodEnd.strftime('%m'))

    #find weeks in a month
    def TotWeeks(intial, FirstMonday):
        EndYear = int(intial.strftime('%Y')) + 1
        
        Weeks = 0
        CurrentYear = 0

        while CurrentYear < EndYear:
            NxtWeek = FirstMonday + timedelta(weeks=Weeks)
            CurrentYear = int(NxtWeek.strftime('%Y'))
            if CurrentYear < EndYear:
                Weeks += 1
            else:
                #print(NxtWeek)
                return Weeks-1

    TotalWeeks = TotWeeks(d, PeriodStart)
    #print(TotalWeeks)


    Startingdays = []

    #loads array with dates
    def PeriodsInYear(PeriodStart, TotalWeeks):
        period = 0
        
        while period < TotalWeeks:
            CurWeek = PeriodStart + timedelta(weeks=period)
            EndWeek = CurWeek + timedelta(days=6)
            
            #print(CurWeek)
            
            StartMonth = int(CurWeek.strftime('%m'))
            EndMonth = int(EndWeek.strftime('%m'))
            
            if StartMonth == EndMonth:
                comb = CurWeek.strftime('%b'), CurWeek.strftime('%#d'), EndWeek.strftime('%#d'), ",",  EndWeek.strftime('%Y')
                Startingdays.append(comb)
                #print("equal", StartMonth, EndMonth)
            else:
                comb2 = CurWeek.strftime('%b'), CurWeek.strftime('%#d'), EndWeek.strftime('%b %#d'), ",", EndWeek.strftime('%Y')
                Startingdays.append(comb2)
                #print("not equal", StartMonth, EndMonth)

            period +=1
            #print(period, "/", TotalWeeks, "\n")
            continue

    
    PeriodsInYear(PeriodStart, TotalWeeks)

    formatted_strings = [''.join([entry[0]," ", str(entry[1]), "-", str(entry[2]), str(entry[3]), " ", str(entry[4])]) for entry in Startingdays]
    #print(formatted_strings)


    # for formatted_strings in formatted_strings:
    #     print(formatted_strings)

    MonthlyCounter = []

    #finds number of week in month
    def WeekNumber(PeriodStart, TotalWeeks):
        period = 0
        count = 0

        while period < TotalWeeks:
            #print("period is", period, "Count is", count)
            CurWeek = PeriodStart + timedelta(weeks=period)
            EndWeek = CurWeek + timedelta(days=6)
            
            #print(CurWeek)
            CurMInt = int(CurWeek.strftime('%m'))
            EndMInt = int(EndWeek.strftime('%m'))
            #prints the day value
            Weekday = int(CurWeek.strftime('%d'))

            #print(Weekday)
            
            #if the start of the period 1, it has to be the first in the list
            if Weekday == 1:
                count =1
                period +=1
                #print("period is", period, "Count is", count, "\n")
                MonthlyCounter.append(count)
            
            #if the current week month matches ending week month keep counting
            elif CurMInt == EndMInt:
                count +=1
                period +=1
                #print("period is", period, "Count is", count, "\n")
                MonthlyCounter.append(count)

            #if the month changes start from the beginning
            else:
                count=1
                period +=1
                #print("period is", period, "Count is", count, "\n")
                MonthlyCounter.append(count)
                continue

    WeekNumber(PeriodStart, TotalWeeks)

    # for MonthlyCounter in MonthlyCounter:
        # print(MonthlyCounter)    

    NumPeriod = []

    countdot = [f'{number}. {item}' for number, item in zip(MonthlyCounter, formatted_strings)]

    # for countdot in countdot:
    #     print(countdot)    
    return countdot, PeriodStart, TotalWeeks