from user import User
from roles_enum import Role

class Patient(User):
    def __init__(self, first_name, last_name, email, password, date_of_birth, hiv_status, \
        diagnosis_date=None, on_art=False, art_start_date=None, country_iso=None):
        super().__init__(first_name, last_name, email, password, role=Role.PATIENT)
        self.date_of_birth = date_of_birth
        self.hiv_status = hiv_status
        self.diagnosis_date = diagnosis_date
        self.on_art = on_art
        self.art_start_date = art_start_date
        self.country_iso = country_iso
        
    def registration(self, email):
        pass
    
    def login(self, email, password):
        pass
    
    def view_profile(self):
        pass
    
    def update_profile(self, **kwargs):
        pass