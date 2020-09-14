def add_time(start, duration, day=None):
    #   By knowing the days passed, we can simply obtain the resulting day of week by incrementing the index
    #   by days passed % 7
    DAY_OF_WEEK = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

    #   Obtain the starting hour and starting minute. Starting hour is converted into 24 Hr format for easier process
    startSplit = start.split()
    startTimeSplit = startSplit[0].split(':')
    startMin = int(startTimeSplit[1])
    startHr = 0 if startSplit[1] == 'AM' and startTimeSplit[0] == '12' \
        else 12 if startSplit[1] == 'PM' and startTimeSplit[0] == '12' \
        else int(startTimeSplit[0]) + (12 if startSplit[1] == 'PM' else 0)

    #   Obtain the duration hour and duration minute
    durationMin = int(duration.split(":")[1])
    durationHr = int(duration.split(":")[0])

    #   Obtain the day of week index in the array, if it was provided as optional argument
    if day is not None:
        dayOfWeek = DAY_OF_WEEK.index(day.capitalize())

    #   Find Minutes. Simple process just adding 60 and modulo. If minute ends up lesser than starting minutes, that
    #   means it causes a hour to carry forward
    resMin = (startMin + durationMin) % 60
    if resMin < startMin: durationHr += 1

    #   Find Hour. Simple process just adding the duration Hour (But modulo 24), then modulo 24
    resHr = (startHr + durationHr % 24) % 24

    #   Find Days Passed. From duration hour find the number of days included in it. If the result Hour ends up
    #   lesser than starting hour that means it causes a day to carry forward
    resDays = (durationHr // 24) + (1 if resHr < startHr else 0)

    #   Find dayOfWeek if provided
    if day is not None:
        dayOfWeek = DAY_OF_WEEK[(dayOfWeek + resDays) % 7]

    res = "{}:{:02d} {}{}{}".format(
        12 if resHr == 0 or resHr == 12 else resHr % 12,
        resMin,
        'AM' if resHr < 12 else 'PM',
        "" if day is None else ", {}".format(dayOfWeek),
        "" if resDays == 0 else " (next day)" if resDays == 1 else " ({} days later)".format(resDays)
    )

    return res


print(add_time("3:00 PM", "3:10"), add_time("11:30 AM", "2:32", "Monday"), add_time("11:43 AM", "00:20"),
      add_time("10:10 PM", "3:30"), add_time("11:43 PM", "24:20", "tueSday"), add_time("6:30 PM", "205:12"), sep='\n')
