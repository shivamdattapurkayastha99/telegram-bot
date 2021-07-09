from telegram.ext import * 
from home.models import *
import django
import os
import re
os.environ['DJANGO_SETTINGS_MODULE']='telebot.settings'
django.setup()
API_KEY='1730292273:AAH-tMUMnT83s5p-KNKXuqVIfOULZlXqYpQ'
def isValidPinCode(pinCode):
     
    # Regex to check valid pin code
    # of India.
    regex = "^[1-9]{1}[0-9]{2}\\s{0,1}[0-9]{3}$"
 
    # Compile the ReGex
    p = re.compile(regex)
     
    # If the pin code is empty
    # return false
    if (pinCode == ''):
        return False
         
    # Pattern class contains matcher() method
    # to find matching between given pin code
    # and regular expression.
    m = re.match(p, pinCode)
     
    # Return True if the pin code
    # matched the ReGex else False
    if m is None:
        return False
    else:
        return True
def num_there(s):
    return any(i.isdigit() for i in s)
def handle_message(update,context):
    text=str(update.message.text).lower()
    if num_there(text):
        if isValidPinCode(text):
            cowin_objs=CowinData.objects.filter(pincode=text)
            message=f"Total {cowin_objs.count()} slots in your pincode"
            for cowin_obj in cowin_objs:
                message+=f"Place name:{cowin_obj.name},Fee Type:{cowin_obj.fee_type},State:{cowin_obj.state},Available Capacity:{cowin_obj.available_capacity} Vaccine:{cowin_obj.vaccine}"
            update.message.reply_text(f"{message}")
            return
    update.message.reply_text(f"Hi {update['message']['chat']['first_name']} from shivam bot Enter pincode")
if __name__=="__main__":
    updater=Updater(API_KEY,use_context=True)
    dp=updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text,handle_message))
    updater.start_polling(1.0)
    updater.idle()


