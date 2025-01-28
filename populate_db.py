from models import Automobilis, db
from app import app

with app.app_context():
    autos = [
        Automobilis(gamintojas="Vokietija", modelis="Audi", spalva="Juoda", metai=2020),
        Automobilis(gamintojas="Vokietija", modelis="BMW", spalva="Sidabrine", metai=2021),
        Automobilis(gamintojas="Vokietija", modelis="Porsche", spalva="Melyna", metai=2019),
        Automobilis(gamintojas="Vokietija", modelis="Porsche", spalva="Raudona", metai=2024),
        Automobilis(gamintojas="JAV", modelis="Tesla", spalva="Balta", metai=2022),
        Automobilis(gamintojas="Japonija", modelis="Toyota", spalva="Melyna", metai=2020),
        Automobilis(gamintojas="Japonija", modelis="Honda", spalva="Balta", metai=2019),
        Automobilis(gamintojas="Italija", modelis="Ferrari", spalva="Raudona", metai=2017),
        Automobilis(gamintojas="JAV", modelis="Ford", spalva="Melyna", metai=2019),
        Automobilis(gamintojas="Italija", modelis="Fiat", spalva="Melyna", metai=2020),
        Automobilis(gamintojas="JAV", modelis="Tesla", spalva="Juoda", metai=2021),
        Automobilis(gamintojas="Japonija", modelis="Toyota", spalva="Juoda", metai=2022),
        Automobilis(gamintojas="Vokietija", modelis="Porsche", spalva="Juoda", metai=2024),
        Automobilis(gamintojas="JAV", modelis="Ford", spalva="Raudona", metai=2024),
        Automobilis(gamintojas="Italija", modelis="Fiat", spalva="Raudona", metai=2025),
        Automobilis(gamintojas="Japonija", modelis="Honda", spalva="Melyna", metai=2020),
        Automobilis(gamintojas="JAV", modelis="Chevrolet", spalva="Sidabrine", metai=2018),
        Automobilis(gamintojas="JAV", modelis="Tesla", spalva="Melyna", metai=2019),
        Automobilis(gamintojas="Vokietija", modelis="BMW", spalva="Juoda", metai=2023),
        Automobilis(gamintojas="Vokietija", modelis="Audi", spalva="Balta", metai=2025),
        Automobilis(gamintojas="Japonija", modelis="Honda", spalva="Juoda", metai=2023),
        Automobilis(gamintojas="JAV", modelis="Tesla", spalva="Sidabrine", metai=2024),
        Automobilis(gamintojas="Italija", modelis="Ferrari", spalva="Geltona", metai=2025),
        Automobilis(gamintojas="Japonija", modelis="Toyota", spalva="Raudona", metai=2020),
        Automobilis(gamintojas="Vokietija", modelis="Audi", spalva="Sidabrine", metai=2021),
        Automobilis(gamintojas="JAV", modelis="Ford", spalva="Juoda", metai=2020),
        Automobilis(gamintojas="JAV", modelis="Chevrolet", spalva="Raudona", metai=2019)
    ]

    db.session.add_all(autos)
    db.session.commit()
    print("Duomenys uzpildyti")
