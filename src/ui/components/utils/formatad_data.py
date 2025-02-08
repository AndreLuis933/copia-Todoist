from ui.components.utils.locale_config import temp_locale

def formatad_data(data):
    with temp_locale("en_US.UTF-8"):
        formatted_date = data.strftime("%b %d %I:%M %p")

        formatted_date = formatted_date.replace(" 12:00 AM", "")
        
        return formatted_date