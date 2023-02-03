from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()


    
@router.get("/{company_id}")
async def get_company(company_id: int):
    return JSONResponse({'id': 1, 'identifier': 'rwchsler', 'name': 'Richtungswechsler', 'personal_title': 'Psych. M. Sc.', 'personal_first_name': 'Sarah', 'personal_last_name': 'Scholl', 'description': 'Private psychologische Beratung ohne Schnickschnack', 'email': 'info@richtungswechsler.de', 'logo_url': 'https://richtungswechsler.de/logo.png', 'impress': 'https://richtungswechsler.de/impressum', 'street_and_number': 'Waldstr. 61', 'zip': '76135', 'city_name': 'Karlsruhe', 'contact_information': [{'id': 1, 'type': 'phone', 'title': 'Telefon', 'content': '+49 123 4567890'}, {'id': 2, 'type': 'website', 'title': 'Homepage', 'content': 'https://richtungswechsler.de'}]})



    
@router.put("/{company_id}")
async def update_company(company_id: int):
    return JSONResponse({'id': 1, 'identifier': 'rwchsler', 'name': 'Richtungswechsler', 'personal_title': 'Psych. M. Sc.', 'personal_first_name': 'Sarah', 'personal_last_name': 'Scholl', 'description': 'Private psychologische Beratung ohne Schnickschnack', 'email': 'info@richtungswechsler.de', 'logo_url': 'https://richtungswechsler.de/logo.png', 'impress': 'https://richtungswechsler.de/impressum', 'street_and_number': 'Waldstr. 61', 'zip': '76135', 'city_name': 'Karlsruhe', 'contact_information': [{'id': 1, 'type': 'phone', 'title': 'Telefon', 'content': '+49 123 4567890'}, {'id': 2, 'type': 'website', 'title': 'Homepage', 'content': 'https://richtungswechsler.de'}]})



    
@router.delete("/{company_id}")
async def delete_company(company_id: int):
    return JSONResponse({'id': 1, 'identifier': 'rwchsler', 'name': 'Richtungswechsler', 'personal_title': 'Psych. M. Sc.', 'personal_first_name': 'Sarah', 'personal_last_name': 'Scholl', 'description': 'Private psychologische Beratung ohne Schnickschnack', 'email': 'info@richtungswechsler.de', 'logo_url': 'https://richtungswechsler.de/logo.png', 'impress': 'https://richtungswechsler.de/impressum', 'street_and_number': 'Waldstr. 61', 'zip': '76135', 'city_name': 'Karlsruhe', 'contact_information': [{'id': 1, 'type': 'phone', 'title': 'Telefon', 'content': '+49 123 4567890'}, {'id': 2, 'type': 'website', 'title': 'Homepage', 'content': 'https://richtungswechsler.de'}]})



    
@router.get("/ids/")
async def get_company_ids():
    return JSONResponse({'ids': [1, 2, 3]})



    
@router.post("/")
async def create_company():
    return JSONResponse({'id': 1, 'identifier': 'rwchsler', 'name': 'Richtungswechsler', 'personal_title': 'Psych. M. Sc.', 'personal_first_name': 'Sarah', 'personal_last_name': 'Scholl', 'description': 'Private psychologische Beratung ohne Schnickschnack', 'email': 'info@richtungswechsler.de', 'logo_url': 'https://richtungswechsler.de/logo.png', 'impress': 'https://richtungswechsler.de/impressum', 'street_and_number': 'Waldstr. 61', 'zip': '76135', 'city_name': 'Karlsruhe', 'contact_information': [{'id': 1, 'type': 'phone', 'title': 'Telefon', 'content': '+49 123 4567890'}, {'id': 2, 'type': 'website', 'title': 'Homepage', 'content': 'https://richtungswechsler.de'}]})



    
@router.get("/users/{user_id}")
async def get_user(user_id: int):
    return JSONResponse({'id': 1, 'email': 'werner@hans.de', 'first_name': 'Hans', 'last_name': 'Werner', 'registered_since': '2023-02-03T17:14:28.221005'})



    
@router.put("/users/{user_id}")
async def update_user(user_id: int):
    return JSONResponse({'id': 1, 'email': 'werner@hans.de', 'first_name': 'Hans', 'last_name': 'Werner', 'registered_since': '2023-02-03T17:14:28.221005'})



    
@router.delete("/users/{user_id}")
async def delete_user(user_id: int):
    return JSONResponse({'id': 1, 'email': 'werner@hans.de', 'first_name': 'Hans', 'last_name': 'Werner', 'registered_since': '2023-02-03T17:14:28.221005'})



    
@router.get("/users/")
async def get_users():
    return JSONResponse({'id': 1, 'email': 'werner@hans.de', 'first_name': 'Hans', 'last_name': 'Werner', 'registered_since': '2023-02-03T17:14:28.221005'})



    
@router.post("/users/")
async def create_user():
    return JSONResponse({'id': 1, 'email': 'werner@hans.de', 'first_name': 'Hans', 'last_name': 'Werner', 'registered_since': '2023-02-03T17:14:28.221005'})



    
@router.put("/users/{user_id}/email/")
async def update_user_email(user_id: int):
    return JSONResponse({'id': 1, 'email': 'werner@hans.de', 'first_name': 'Hans', 'last_name': 'Werner', 'registered_since': '2023-02-03T17:14:28.221005'})



    
@router.put("/users/add-to-company/")
async def add_user_to_company():
    return JSONResponse({'id': 1, 'email': 'werner@hans.de', 'first_name': 'Hans', 'last_name': 'Werner', 'registered_since': '2023-02-03T17:14:28.221005'})



    
@router.get("/events/{event_id}")
async def get_event(event_id: int):
    return JSONResponse({'id': 1, 'title': 'Termin mit Sarah Scholl', 'status': 'booked', 'type': 'appointment', 'start_datetime': '2023-02-03T17:14:28.218253', 'end_datetime': '2023-02-03T18:14:28.218256', 'event_location': 'onsite', 'event_location_selection': 'onsite', 'notice': 'Notizen', 'info': 'Info Text', 'customer_id': 1})



    
@router.put("/events/{event_id}")
async def update_event(event_id: int):
    return JSONResponse({'id': 1, 'title': 'Termin mit Sarah Scholl', 'status': 'booked', 'type': 'appointment', 'start_datetime': '2023-02-03T17:14:28.218253', 'end_datetime': '2023-02-03T18:14:28.218256', 'event_location': 'onsite', 'event_location_selection': 'onsite', 'notice': 'Notizen', 'info': 'Info Text', 'customer_id': 1})



    
@router.get("/events/")
async def get_events(start_datetime: str, end_datetime: str, status: str, type: str, customer_id: int):
    return JSONResponse({'id': 1, 'title': 'Termin mit Sarah Scholl', 'status': 'booked', 'type': 'appointment', 'start_datetime': '2023-02-03T17:14:28.218253', 'end_datetime': '2023-02-03T18:14:28.218256', 'event_location': 'onsite', 'event_location_selection': 'onsite', 'notice': 'Notizen', 'info': 'Info Text', 'customer_id': 1})



    
@router.post("/events/")
async def create_events():
    return JSONResponse({'id': 1, 'title': 'Termin mit Sarah Scholl', 'status': 'booked', 'type': 'appointment', 'start_datetime': '2023-02-03T17:14:28.218253', 'end_datetime': '2023-02-03T18:14:28.218256', 'event_location': 'onsite', 'event_location_selection': 'onsite', 'notice': 'Notizen', 'info': 'Info Text', 'customer_id': 1})



    
@router.delete("/events/")
async def delete_events():
    return JSONResponse({'id': 1, 'title': 'Termin mit Sarah Scholl', 'status': 'booked', 'type': 'appointment', 'start_datetime': '2023-02-03T17:14:28.218253', 'end_datetime': '2023-02-03T18:14:28.218256', 'event_location': 'onsite', 'event_location_selection': 'onsite', 'notice': 'Notizen', 'info': 'Info Text', 'customer_id': 1})



    
@router.get("/events/customers/")
async def get_open_events_for_customers(start_datetime: str, end_datetime: str):
    return JSONResponse({'id': 1, 'start_datetime': '2023-02-03T17:14:28.217368', 'end_datetime': '2023-02-03T18:14:28.217377', 'event_location': 'onsite'})



    
@router.put("/events/{event_id}/book")
async def book_appointment(event_id: int, event_location_selection: str):
    return JSONResponse({'id': 1, 'start_datetime': '2023-02-03T17:14:28.217368', 'end_datetime': '2023-02-03T18:14:28.217377', 'event_location': 'onsite'})



    
@router.put("/events/{event_id}/manual")
async def manually_book_appointment(event_id: int):
    return JSONResponse({'id': 1, 'title': 'Termin mit Sarah Scholl', 'status': 'booked', 'type': 'appointment', 'start_datetime': '2023-02-03T17:14:28.218253', 'end_datetime': '2023-02-03T18:14:28.218256', 'event_location': 'onsite', 'event_location_selection': 'onsite', 'notice': 'Notizen', 'info': 'Info Text', 'customer_id': 1})



    
@router.put("/events/{event_id}/cancel")
async def cancel_appointment(event_id: int):
    return JSONResponse({'id': 1, 'start_datetime': '2023-02-03T17:14:28.217368', 'end_datetime': '2023-02-03T18:14:28.217377', 'event_location': 'onsite'})



    
@router.get("/customers/{customer_id}")
async def get_customer(customer_id: int):
    return JSONResponse({'id': 1, 'identifier': 'xlkSHmaed', 'gender': 'male', 'first_name': 'Hans', 'last_name': 'Werner', 'email': 'hans@werner.de'})



    
@router.put("/customers/{customer_id}")
async def update_customer(customer_id: int):
    return JSONResponse({'id': 1, 'identifier': 'xlkSHmaed', 'gender': 'male', 'first_name': 'Hans', 'last_name': 'Werner', 'email': 'hans@werner.de'})



    
@router.delete("/customers/{customer_id}")
async def delete_customer(customer_id: int):
    return JSONResponse({'id': 1, 'identifier': 'xlkSHmaed', 'gender': 'male', 'first_name': 'Hans', 'last_name': 'Werner', 'email': 'hans@werner.de'})



    
@router.get("/customers/")
async def get_customers():
    return JSONResponse({'id': 1, 'identifier': 'xlkSHmaed', 'gender': 'male', 'first_name': 'Hans', 'last_name': 'Werner', 'email': 'hans@werner.de'})



    
@router.post("/customers/")
async def create_customer():
    return JSONResponse({'id': 1, 'identifier': 'xlkSHmaed', 'gender': 'male', 'first_name': 'Hans', 'last_name': 'Werner', 'email': 'hans@werner.de'})



    
@router.put("/customers/{customer_id}/email/")
async def update_customer_email(customer_id: int):
    return JSONResponse({'id': 1, 'identifier': 'xlkSHmaed', 'gender': 'male', 'first_name': 'Hans', 'last_name': 'Werner', 'email': 'hans@werner.de'})



    
@router.get("/files/{file_id}/generate-url")
async def generate_url(file_id: int, expires_in: int = "3600"):
    return JSONResponse({'url': 'https://s3.eu-central-1.amazonaws.com/tebuto-test-bucket/1', 'expires_in': 3600})


