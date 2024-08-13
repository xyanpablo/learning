hw_amount = '12'
hours_spent = '1.5'
course = 'Python'
tasktime = float(hours_spent) / int(hw_amount)
print('Курс:', course, ', всего задач: ', hw_amount, ', затрачено часов:', hours_spent, ', среднее время выполнения:',
      tasktime, 'часа.')
