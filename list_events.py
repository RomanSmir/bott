import datetime
import calendar
from cal_setup import get_calendar_service


def main():
    service = get_calendar_service()
    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
    events_result = service.events().list(
        calendarId='narussianorte@gmail.com', timeMin=now,
        maxResults=10, singleEvents=True,
        orderBy='startTime').execute()
    events = events_result.get('items', [])
    NAME = [1]
    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start']
        date = start.get('dateTime')
        name = event.get('summary')
        if date is not None:
            year = date[:4:]
            month = date[5:7]
            datee = date[8:10]
            day = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Восркресенье"][
                calendar.weekday(int(year), int(month), int(datee))]
            NAME.append(date[:16].replace('T', " ")+" "+day)
            NAME.append(name)
        elif date is None:
            date = start.get('date')
            year = date[:4]
            month = date[5:7]
            datee = date[8:10]
            day = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Восркресенье"][
                calendar.weekday(int(year), int(month), int(datee))]
            print(date)
            NAME.append(date+" "+day)
            NAME.append(name)
    return NAME


if __name__ == '__main__':
    main()
