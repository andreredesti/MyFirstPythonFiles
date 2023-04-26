from datetime import datetime
hoje =  datetime.now()
print(hoje)
print(f"Data:{hoje: %d/%m/%y}, horário: {hoje:%H:%M}")