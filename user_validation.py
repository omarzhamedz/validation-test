import re
from datetime import datetime

class UserValidation:
    @staticmethod
    def validate_email(email: str) -> bool:
        """Validates if the provided email is in a proper format."""
        if not email or not isinstance(email, str):
            return False
        
        pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
        return re.match(pattern, email) is not None

    @staticmethod
    def validate_username(username: str) -> bool:
        """Validates username (3–20 chars, letters/numbers/underscore only)."""
        if not username or not isinstance(username, str):
            return False
        pattern = r"^[A-Za-z0-9_]{3,20}$"
        return re.match(pattern, username) is not None

    @staticmethod
    def validate_phone_number(phone: str) -> bool:
        """Validates Egyptian phone number."""
        if not phone or not isinstance(phone, str):
            return False
        pattern = r"^(?:20)?(10|11|12|15)\d{8}$"
        return re.match(pattern, phone) is not None

    @staticmethod
    def validate_national_id(national_id: str) -> bool:
        """Validates Egyptian national ID (14 digits with valid date and governorate code)."""
        if not national_id or not isinstance(national_id, str):
            return False
        if not re.match(r"^\d{14}$", national_id):
            return False

    
        century = national_id[0]
        year = national_id[1:3]
        month = national_id[3:5]
        day = national_id[5:7]
        gov_code = int(national_id[7:9])

       
        if century not in ['2', '3']:
            return False

       
        try:
            year_full = (1900 if century == '2' else 2000) + int(year)
            datetime(year_full, int(month), int(day))
        except ValueError:
            return False

        
        if not (1 <= gov_code <= 88):
            return False

        return True
