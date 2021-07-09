import requests
import datetime
def get_cowin_data_by_pincode(pincode):
    try:
        current_date=datetime.date.today().strftime('%d-%m-%y')
        payload=requests.get('https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/v2/appointment/sessions/public/findByPin?pincode={pincode}&date={current_date}')
        sessions=payload.json()
        for session in sessions.get('sessions'):
            if session.get('available_capacity')>0:
                CowinData.objects.create(center_id=session.get('center_id'),
    name=session.get('name'),
    state=session.get('state_name'),
    pincode=session.get('pincode'),
    fee_type=session.get('fee_type'),
    capacity=session.get('available_capacity'),
    available_capacity_dose1=session.get('available_capacity_dose1'),
    available_capacity_dose2=session.get('available_capacity_dose2'),
    fee=session.get('fee'),
    min_age_limit=session.get('min_age_limit'),
    vaccine=session.get('vaccine'))
    # created_at=session.get('center_id'),
    # updated_at=session.get('center_id'),

    except Exception as e:
        print(e)
    return False