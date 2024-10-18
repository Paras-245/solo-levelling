from django.shortcuts import render
from django.shortcuts import redirect,get_object_or_404
from django.contrib.auth import authenticate, login, logout 
from .forms import SignupForm, LoginForm
from .models import Player,Quest,UserQuest
from django.contrib.auth.decorators import login_required
from .utils import load
from django.utils import timezone

@login_required(login_url='login')
def dashboard(request):
    if(request.user.is_superuser):
        return redirect('admin:index')
    player = Player.objects.get(user=request.user)
    current_day = (timezone.now() - player.created_at).days + 1
    if current_day > player.day:
        player.day = current_day
        player.mana = 100
        player.save()

    quests = Quest.objects.filter(day=player.day,user = request.user)
    # Get or create user quests for tracking completion
    if not quests:
        # try:
            quests_data = load(player.goal,f"completed {player.day} days working on this ",player.day)
            for day_data in quests_data:
                day = day_data['day']
                for quest_data in day_data['quests']:
                    Quest.objects.create(
                        title=quest_data['title'],
                        objective=quest_data['objective'],
                        tasks=quest_data['tasks'],
                        day=day,
                        user=request.user
                    )
                quests = Quest.objects.filter(day=player.day,user = request.user)
            print("parsed new")
    user_quests = []
    for quest in quests:
        user_quest, created = UserQuest.objects.get_or_create(user=request.user, quest=quest)
        user_quests.append(user_quest)

    return render(request, 'dashboard.html', {'player': player, 'user_quests': user_quests})

@login_required
def quest_list(request, day):
    quests = Quest.objects.filter(day=day)
    return render(request, 'quest_list.html', {'quests': quests, 'day': day})

@login_required
def quest_detail(request, quest_id):
    quest = get_object_or_404(Quest, id=quest_id)
    user_quest, created = UserQuest.objects.get_or_create(user=request.user, quest=quest)

    if request.method == 'POST':
        completed_task = request.POST.get('completed_task')
        if completed_task and completed_task not in user_quest.completed_tasks:
            user_quest.completed_tasks.append(completed_task)
            user_quest.save()
            player = Player.objects.get(user=request.user)
            player.xp += 10
            player.save()
        return redirect('dashboard')

    return render(request, 'quest_detail.html', {'quest': quest, 'user_quest': user_quest})

def landing_page(request):
    return render(request, 'landing_page.html')

def user_signup(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            # quest load
            user = form.save()
            try:
                quests_data = load(form.cleaned_data['goal'],form.cleaned_data['goal_progress'],1)
            except:
                form.add_error(None, "Kindly sign up again")
                user.delete()
                return render(request, 'signup.html', {'form': form})
            if(quests_data == None):
                form.add_error(None, "some error occured")
                user.delete()
                return render(request, 'signup.html', {'form': form})
            for day_data in quests_data:
                day = day_data['day']
                for quest_data in day_data['quests']:
                    Quest.objects.create(
                        title=quest_data['title'],
                        objective=quest_data['objective'],
                        tasks=quest_data['tasks'],
                        day=day,
                        user=user
                    )
            Player.objects.create(
                user=user,
                rank="E",
                level=1,
                xp=0,
                mana=100,
                goal=form.cleaned_data['goal'],
                goal_progress=form.cleaned_data['goal_progress']
            )
            
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

# login page
def user_login(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)    
                return redirect('dashboard')
            else:
                form.add_error(None, "Invalid username or password.")
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

# logout page
def user_logout(request):
    logout(request)
    return redirect('login')

