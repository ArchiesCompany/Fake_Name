from faker import Faker
from rich import print
import os

fake = Faker('ru_RU')

a =1 
while a < 5:

	print(
	f"[bold green]Имя:[/bold green] {fake.name()}",
	f"[bold magenta]Профессия:[/bold magenta] {fake.job()}",
	f"Адрес: [i]{fake.address()}[/i]",
	f"День рождения: {fake.date_of_birth()}",
	f"Город проживания: {fake.city()}",
	f"Email: {fake.email()}",
	sep = "\n")

	a = a+1
else:
		print('Программа завершена.')


os.system('pause')