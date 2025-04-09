class patients():
    def __init__(self,name,age,date_of_latest_admission,medical_history):
        self.name = name
        self.age = age
        self.date_of_latest_admission = date_of_latest_admission
        self.medical_history = medical_history
    def printing(self):
        print('Name:',self.name,'Age:',self.age,'Date of latest admission:',self.date_of_latest_admission,'Medical history:',self.medical_history)
a=patients('winnie',70,'2025/4/8','No')
a.printing()