def translate_weekday(day):
    week_days = {
        'Monday'    : 'Poniedzialek',
        'Tuesday'   : 'Wtorek',
        'Wednesday' : 'Sroda',
        'Thursday'  : 'Czwartek',
        'Friday'    : 'Piatek',
        'Saturday'  : 'Sobota',
        'Sunday'    : 'Niedziela'
    }
    if day in week_days.keys():
        print(week_days.get(day))


translate_weekday('Wednesday')
