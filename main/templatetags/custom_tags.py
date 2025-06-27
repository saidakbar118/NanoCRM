from django import template

register = template.Library()

@register.filter
def get_attendance(attendance_dict, student_day):
    student_id, day = student_day
    return attendance_dict.get((student_id, day))

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

@register.filter
def to_range(start, end):
    return range(start, end + 1)

@register.filter
def get_month_name(month):
    months = [
        "", "Yanvar", "Fevral", "Mart", "Aprel", "May", "Iyun",
        "Iyul", "Avgust", "Sentabr", "Oktabr", "Noyabr", "Dekabr"
    ]
    return months[month]
