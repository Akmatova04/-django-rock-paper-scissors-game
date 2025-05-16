from django.shortcuts import render
import random

CHOICES = ['таш', 'кайчы', 'кагаз']

def determine_winner(player_choice, computer_choice):
    """Таш, Кайчы, Кагаз оюнунун жеңүүчүсүн аныктайт."""
    if player_choice == computer_choice:
        return "тең чыгуу", 0, 0  # Жыйынтык, оюнчунун упайы, компьютердин упайы
    elif (player_choice == 'таш' and computer_choice == 'кайчы') or \
         (player_choice == 'кайчы' and computer_choice == 'кагаз') or \
         (player_choice == 'кагаз' and computer_choice == 'таш'):
        return "сиз уттуңуз", 1, 0
    else:
        return "компьютер утту", 0, 1

def play_rps_view(request):
    player_score = request.session.get('player_score', 0)
    computer_score = request.session.get('computer_score', 0)
    
    context = {
        'choices': CHOICES,
        'player_score': player_score,
        'computer_score': computer_score,
        'round_result': None, # Башында раунддун жыйынтыгы жок
        'player_choice_display': None,
        'computer_choice_display': None,
    }

    if request.method == 'POST':
        player_choice = request.POST.get('choice') # HTML формадан келет
        
        if player_choice in CHOICES:
            computer_choice = random.choice(CHOICES)
            
            result, p_points, c_points = determine_winner(player_choice, computer_choice)
            
            player_score += p_points
            computer_score += c_points
            
            request.session['player_score'] = player_score
            request.session['computer_score'] = computer_score
            
            context.update({
                'round_result': result,
                'player_choice_display': player_choice,
                'computer_choice_display': computer_choice,
                'player_score': player_score, # Жаңыланган упайларды кайра контекстке кошуу
                'computer_score': computer_score,
            })
        else:
            context['round_result'] = "Сураныч, туура тандоо жасаңыз."
            
    return render(request, 'gamecore/play_rps_template.html', context)

def reset_scores_view(request):
    """Упайларды тазалоо үчүн көрүнүш."""
    if 'player_score' in request.session:
        del request.session['player_score']
    if 'computer_score' in request.session:
        del request.session['computer_score']
    
    # Оюн барагына кайра багыттоо (же башкы бетке, эгер ал бар болсо)
    from django.shortcuts import redirect
    return redirect('play_rps_url') # Бул URL'ды кийин түзөбүз