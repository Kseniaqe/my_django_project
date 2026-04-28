from django.shortcuts import render
from .models import CalculationHistory

def index(request):
    history = CalculationHistory.objects.all().order_by('-created_at')
    
    if request.method == 'POST':
        num1 = float(request.POST.get('num1', 0))
        num2 = float(request.POST.get('num2', 0))
        operation = request.POST.get('operation', '+')
        
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            result = num1 / num2 if num2 != 0 else 'Ошибка: деление на 0'
        
        if isinstance(result, str):
            history_list = CalculationHistory.objects.all().order_by('-created_at')
            return render(request, 'calculator/index.html', {
                'history': history_list,
                'error': result,
                'num1': num1,
                'num2': num2,
                'operation': operation
            })
        
        CalculationHistory.objects.create(
            num1=num1,
            num2=num2,
            operation=operation,
            result=result
        )
        
        history = CalculationHistory.objects.all().order_by('-created_at')
        return render(request, 'calculator/index.html', {
            'history': history,
            'result': result,
            'num1': num1,
            'num2': num2,
            'operation': operation
        })
    
    return render(request, 'calculator/index.html', {'history': history})