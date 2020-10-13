class Utils:
    def _current_date_time(format):
        time = dt.datetime.now()
        if format == 'datetime':
            return f'{time.year}-{time.month}-{time.day} {time.hour}:{time.minute}'
        elif format == 'date':
            return f'{time.year}-{time.month}-{time.day}'