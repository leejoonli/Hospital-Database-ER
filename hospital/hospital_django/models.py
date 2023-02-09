from django.db import models

# Create your models here.
class Procedure(models.Model):
    name = models.TextField()
    cost = models.FloatField()

    def __str__(self):
        return self.name

class Medication(models.Model):
    name = models.TextField()
    brand = models.CharField(max_length=150)
    description = models.TextField()

    def __str__(self):
        return self.name

class Physician(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    ssn = models.IntegerField()

    def __str__(self):
        return self.name

class Nurse(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    registered = models.BooleanField(default=True)
    ssn = models.IntegerField()

    def __str__(self):
        return self.name

class Patient(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    phone = models.CharField(max_length=10)
    insurance_id = models.TextField()
    ssn = models.IntegerField()
    pcp = models.ForeignKey(Physician, on_delete=models.CASCADE, related_name='patients')

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=100)
    head = models.ForeignKey(Physician, on_delete=models.CASCADE, related_name='departments')

    def __str__(self):
        return self.name

class Block(models.Model):
    block_floor = models.IntegerField()
    block_code = models.IntegerField()

    def __str__(self):
        return (f'FLOOR: {self.block_floor}, CODE: {self.block_code}')

class On_call(models.Model):
    nurse = models.ForeignKey(Nurse, on_delete=models.CASCADE, related_name='on_calls')
    block = models.ForeignKey(Block, on_delete=models.CASCADE, related_name='on_calls')
    on_call_start = models.DateTimeField(auto_now_add=True)
    on_call_end = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (f'{self.on_call_start} - {self.on_call_end}')

class Affiliated_with(models.Model):
    physician = models.ForeignKey(Physician, on_delete=models.CASCADE, related_name='affiliated_withs')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='affiliated_withs')
    primary_affiliation = models.BooleanField(default=True)

class Trained_in(models.Model):
    physician = models.ForeignKey(Physician, on_delete=models.CASCADE, related_name='trained_ins')
    treatment = models.ForeignKey(Procedure, on_delete=models.CASCADE, related_name='trained_ins')
    certification_date = models.DateField(auto_now_add=True)
    certification_exp = models.DateField(auto_now_add=True)

    def __str__(self):
        return (f'{self.physician} - {self.treatment}')

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='appointments')
    prep_nurse = models.ForeignKey(Nurse, on_delete=models.CASCADE, related_name='appointments')
    physician = models.ForeignKey(Physician, on_delete=models.CASCADE, related_name='appointments')
    start_dt_time = models.DateTimeField(auto_now_add=True)
    end_dt_time = models.DateTimeField(auto_now_add=True)
    examination_room = models.TextField()

    def __str__(self):
        return (f'{self.patient} - {self.start_dt_time}')

class Prescribe(models.Model):
    physician = models.ForeignKey(Physician, on_delete=models.CASCADE, related_name='prescribes')
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='prescribes')
    medication = models.ForeignKey(Medication, on_delete=models.CASCADE, related_name='prescribes')
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE, related_name='prescribes')
    date = models.DateTimeField(auto_now_add=True)
    dose = models.TextField()

    def __str__(self):
        return (f'{self.medication}, {self.physician}')

class Room(models.Model):
    block = models.ForeignKey(Block, on_delete=models.CASCADE, related_name='rooms')
    room_type = models.TextField()
    unavailable = models.BooleanField(default=False)

    def __str__(self):
        return self.room_type

class Stay(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='stays')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='stays')
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (f'{self.patient}, {self.start_time} - {self.end_time}')

class Undergo(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='undergoes')
    procedure = models.ForeignKey(Procedure, on_delete=models.CASCADE, related_name='undergoes')
    stay = models.ForeignKey(Stay, on_delete=models.CASCADE, related_name='undergoes')
    physician = models.ForeignKey(Physician, on_delete=models.CASCADE, related_name='undergoes')
    assisting_nurse = models.ForeignKey(Nurse, on_delete=models.CASCADE, related_name='undergoes')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (f'{self.patient} - {self.procedure}')