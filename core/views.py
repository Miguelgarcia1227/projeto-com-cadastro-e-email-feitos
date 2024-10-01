from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required 
from django.contrib import messages
from django.conf import settings
from .forms import CustomAuthenticationForm
from django.core.mail import send_mail
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy, reverse
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.models import User  # Ou o modelo de usuário que você estiver usando
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.contrib.auth.views import PasswordResetConfirmView
from .forms import CustomPasswordResetForm

def home(request):
    return render(request, 'core/home.html');  

def quemsomos(request):
    return render(request, 'core/quemsomos.html', {'quemsomos': quemsomos});

def planos(request):
    return render(request, 'core/planos.html', {'planos': planos});

def loginmedico(request):
    return render(request, 'core/loginmedico.html', {'loginmedico': loginmedico});

def cadastro(request):
    if request.method == "GET":
        return render(request, 'core/cadastro.html', {'cadastro': cadastro})
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confirmPassword')
        
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        return redirect('home')

def esquecisenha(request):
    return render(request, 'core/esquecisenha.html', {'esquecisenha': esquecisenha});

def dentista(request):
    return render(request, 'core/dentistaT.html', {'dentista': dentista});

def cirurgia(request):
    return render(request, 'core/cirurgiaT.html', {'cirurgia': cirurgia});

def implante(request):
    return render(request, 'core/implanteT.html', {'implnate': implante});

def protese(request):
    return render(request, 'core/proteseT.html', {'protese': protese});

def invisalign(request):
    return render(request, 'core/invisalignT.html', {'invisalign': invisalign});

def ortodontia(request):
    return render(request, 'core/ortodontiaT.html', {'ortodontia': ortodontia});

def pediatra(request):
    return render(request, 'core/pediatraT.html', {'pediatra': pediatra});


def geri(request):
    return render(request, 'core/geriatriaT.html', {'geri': geri});

def login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            remember_me = form.cleaned_data.get('remember_me')

            login(request, user)
            
            # Define o tempo de expiração da sessão com base na escolha do usuário
            if remember_me:
                request.session.set_expiry(1209600)  # 2 semanas em segundos
            else:
                request.session.set_expiry(0)  # Expiração quando o navegador for fechado

            messages.success(request, 'Login realizado com sucesso!')
            return redirect('home')  # Redireciona para a página inicial
    else:
        form = CustomAuthenticationForm()
    
    return render(request, '/accounts/login', {'form': form})

def confirmaremail(request):
    if request.method == 'POST':
        email = request.POST.get('email')

        if email:
            try:
                user = User.objects.get(email=email)
                token = default_token_generator.make_token(user)
                uid = urlsafe_base64_encode(force_bytes(user.pk))

                reset_link = request.build_absolute_uri(
                    reverse('password_reset_confirm', kwargs={'uidb64': uid, 'token': token})
                )

                email_subject = 'Redefinição de Senha'
                email_body = render_to_string('core/password_reset_email.html', {
                    'user': user,
                    'reset_link': reset_link,
                })

                send_mail(
                    email_subject,
                    email_body,
                    'seu-email@gmail.com',
                    [email],
                    fail_silently=False,
                )

                return JsonResponse({'status': 'success', 'message': 'E-mail enviado com sucesso! Verifique sua caixa de entrada'})
            except User.DoesNotExist:
                return JsonResponse({'status': 'fail', 'message': 'Nenhum usuário encontrado com este e-mail!'}, status=404)
            except Exception as e:
                print("Erro ao enviar o e-mail:", e)
                return JsonResponse({'status': 'fail', 'message': 'Erro ao enviar o e-mail! Tente novamente.'}, status=500)
        else:
            return JsonResponse({'status': 'fail', 'message': 'Nenhum e-mail foi fornecido'}, status=400)

    return render(request, 'core/confirmaremail.html'); 

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
        template_name = 'core/esquecisenha.html'  # Apontar para o seu template
        success_url = reverse_lazy('password_reset_complete')  # Ajustar URL de sucesso

def password_reset_view(request):
    if request.method == 'POST':
        form = CustomPasswordResetForm(request.POST)
        if form.is_valid():
            new_password = form.cleaned_data['new_password']
            user = request.user  # O usuário autenticado
            
            # Verifique se o usuário realmente está autenticado
            if user.is_authenticated:
                user.set_password(new_password)
                user.save()
                update_session_auth_hash(request, user)
                
                return redirect('success_url')  # Substitua 'success_url' pela URL desejada
            else:
                # Se o usuário não está autenticado, redirecione ou exiba uma mensagem de erro
                return redirect('login')  # Ou outra URL adequada
    else:
        form = CustomPasswordResetForm()
    
    return render(request, 'password_reset.html', {'form': form})