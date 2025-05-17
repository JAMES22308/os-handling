class Patient:
    def __init__(self, new_name, new_age, new_address):
        self.name = new_name
        self.age = new_age
        self.address = new_address

    def display_patient(self):
        print(f'name: {self.name}')
        print(f'age: {self.age}')
        print(f'address: {self.address}')

class Hospital:
    def __init__(self, new_name):
        self.name = new_name
        self.patients = []

    def add_patient(self, patient_info):
        self.patients.append(patient_info)
    
    def delete_patient(self, patient_name):
        for patient in self.patients:
            if patient.name == patient_name:
                self.patients.remove(patient)
                print(f'patient {patient_name} has been removed')



    def display_all_patients(self):
        print(f'{self.name}')
        for patient in self.patients:
            patient.display_patient()



def main():
    hospital = Hospital('saint luke: ')

    while True:
        ask = input('press 1 to add | press 2 to delete: ')
        if ask == '1':
            name = input('name: ')
            age = input('age: ')
            address = input('address: ')
            a_patient = Patient(name, age, address)
            hospital.add_patient(a_patient)
            hospital.display_all_patients()
        elif ask == '2':
            name = input('name: ')
            hospital.delete_patient(name)
            hospital.display_all_patients()

            
main()