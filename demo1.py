#A = [1,2,3,4,5,6,7] ; sum=[7] ; output = {[7],[1,2,4],[6,1],[5,2],[4,3]}

a = [1,2,3,4,5,6,7]
target_sum = 7

output =[]

for i in range(len(a)):
    for j in range(i+1, len(a)):
        if a[i] + a[j] == target_sum:
         output.append([7] if a[i] == 7 else [a[i], a[j]])
print(output)

# class DiselEngin:
#     def run(self):
#         print("I run using disel")
#
# class ElectricEngine(DiselEngin):
#     super().run()
#     def run(self):
#         print("I run using electric power")
#
# ele = ElectricEngine()
# ele.run()

# from django.shortcuts import render
# from .models import User
#
# def user_profile(request, user_id):
#     try:
#      user = User.objects.get(id=user_id)
#     except User.DoesNotExist:
#         print("User does not exist")
#     return render(request, 'profile.html', {'user': user})

logs = ["acccricket", "bowaccling", "kaccing", "kaccohli", "baacct", "acccricket"]

substring ="acc"
modified_logs = [log.replace(substring, "") for log in logs]
print(modified_logs)

