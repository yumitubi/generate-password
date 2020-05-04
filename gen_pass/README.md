# Генератор паролей Маркова-Иманкулова

Позволяет сгенерить простой набор правил из текста, а затем с помощью
полученный правил создавать пароли, похожие на обычные слова, но
таковыми не явлюящиеся.

Пример на основе японского словаря:

	cyodahikou
	tsuukicchu
	rihihidahi
	yuujukukij
	hadasitoto
	yokintomiy
	nozanguume
	yudoutidak
	rasseijyas
	nouejinaka

## Как пользоваться

Генерим на основе текста список правил:

	>>> from gen_pass.passengine2 import gen_pass_rules
	>>> rules = gen_pass_rules(path_to_file)

Генерим на основе правил пароль в виде псевдо-слова длиной 10 символов:

	>>> from gen_pass.passengine2 import gen_password
	>>> from gen_pass.utils import load_rules
	>>> rules = load_rules(path_to_rules)
	>>> gen_password(rules, 10)
