from django import forms

class ContactoFormulario(forms.Form):
	nome = forms.CharField(label='Seu nome', max_length=100)
	email = forms.EmailField()

	mensagem = forms.CharField(
		error_messages={'required':'Campo obrigatório!'},
		widget = forms.Textarea(
			attrs={
				"class": "form-control",
				"placeholder": "Digite uma mensagem"
			}
			)
		)

	#Função de Verificar tipo de Email
	def verificar_email(self):
		email = self.cleaned_data.get("email")
		if not "gmail.com" in email:
			raise forms.ValidationError("Email deve ser gmail.com")
		return email



