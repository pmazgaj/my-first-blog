# Przykładowy projekt w Django
#
# (dowolne wersje Pythona i Django)
#
# # 1. w projekcie powinny pojawić się dwa modele:
#
# # * shop: id, name, description, logo, main_category,
# # categories, level (int), lottery (uczestniczy w loterii - boolean), data utworzenia, data aktualizacji
#
# # * category: id, name, visible (boolean)
# # 2. panel admina:
#
# # * najlepiej by widoczne były wszystkie pola modeli zarówno w sekcji shop (można pominąć pole "kategorie dodatkowe"/"categories") jak i category,
#
# * super jeśli w sekcji "shop" będzie widać miniaturki logotypów (obrazki dowolne)
#
# # * sklepy i kategorie powinno dać się sortować lub filtrować (w zależności od pola)
#
# # * niech klikalne będą nazwy rekordów, nie id
#
# # * niech opis sklepu będzie edytowalny z poziomu głównej listy sklepów
#
# # * daty utworzenia i aktualizacji nie powinny dać się modyfikować ręcznie
#
# # 3. template'y (views) do wyświetlenia w przeglądarce (upiększanie niepotrzebne):
# #
# # a) listy wszystkich sklepów,
# #     b) wybranego sklepu,
# #     c) dodania sklepu (najlepiej tylko po zalogowaniu)
# #     d) usuwania sklepu (j.w.)
#
# # 4. trzeba też stworzyć customową komendę do importu informacji o sklepach i kategoriach z załączonych arkuszy csv do bazy sqlite
#
# 5. ostatni punkt to podstawowe api stworzone za pomocą Django Rest Framework, przez które jest dostęp - po zalogownaiu (Base Auth) do
# listy sklepów (np. za pomocą /shop/list) oraz konkretnego sklepu szukanego za pomocą id (np /shop/1)
#
# Załączniki:
# -
# pliki csv z danymi do importu
#
# .
# Najwygodniejsze będzie udostępnienie projektu na GitHubie, BitBuckecie lub GitLabie,
# ponieważ to pozwoli nam obserwować postępy.
#
#
# Zrób ile będziesz w stanie. Im więcej, tym lepiej, ale nie musi być wszystko na 100% (choć zależy nam bardzo na pk. 5).
#
#
# Czas na wykonanie: ze względu na zbliżający się długi weekend umówmy się, że ostateczny termin to 4.05.2017
#
#
# Dodatkowe materiały/biblioteki:
# - csv - https://docs.python.org/2/library/csv.html (można się obeć bez niej, ale jest prościej)
# -
# Django Rest Framework: http://www.django-rest-framework.org/
# - djangowe tutoriale (część z nich jest dostępna za darmo): https://www.codingforentrepreneurs.com/projects/
#
#
