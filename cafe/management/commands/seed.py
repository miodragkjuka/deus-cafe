import datetime
import shutil

from django.conf import settings
from django.core.management.base import BaseCommand

from cafe.models import GalleryImage, MenuCategory, MenuItem, Post, TeamMember

MENU = {
    'Кафе': [
        ('Еспресо', 'Illy еспресо', 80), ('Макијато', '', 90), ('Капучино', 'Со млечна пена и цимет', 120),
        ('Лате', '', 130), ('Топло чоколадо', 'Густо, домашно', 150),
    ],
    'Безалкохолни пијалоци': [
        ('Домашна лимонада', 'Со свежа нана', 150), ('Цедено сок од портокал', '', 180),
        ('Ладен чај', 'Праска или лимон', 120), ('Минерална вода', '', 80),
    ],
    'Коктели и алкохол': [
        ('Апероли шприц', '', 350), ('Мохито', '', 380), ('Виски на мраз', '', 300), ('Домашно вино', 'Чаша', 200),
    ],
    'Лесна храна': [
        ('Тост со кашкавал и шунка', '', 220), ('Клуб сендвич', '', 320), ('Чоколаден мус', '', 200),
    ],
}

CAT_IMAGES = {
    'Кафе': 'menu/espresso.jpg', 'Безалкохолни пијалоци': 'menu/cappuccino.jpg',
    'Коктели и алкохол': 'menu/drink.jpg', 'Лесна храна': 'menu/interior.jpg',
}

GALLERY = [
    ('terrace.jpg', 'Стаклената градина на Деус'), ('interior.jpg', 'Внатрешноста на кафулето'),
    ('espresso.jpg', 'Еспресо на масата'), ('drink.jpg', 'Пијалок на мраз'),
    ('cappuccino.jpg', 'Капучино и чоколаден мус'),
]


class Command(BaseCommand):
    help = 'Fills the database with sample content'

    def handle(self, *args, **opts):
        if MenuCategory.objects.exists():
            self.stdout.write('Already seeded.')
            return
        for n, (cat, items) in enumerate(MENU.items()):
            c = MenuCategory.objects.create(name=cat, order=n, image=CAT_IMAGES[cat])
            for name, desc, price in items:
                MenuItem.objects.create(category=c, name=name, description=desc, price=price)

        (settings.MEDIA_ROOT / 'menu').mkdir(parents=True, exist_ok=True)
        for f in ('espresso', 'cappuccino', 'drink', 'interior'):
            shutil.copy(settings.BASE_DIR / 'static' / 'img' / f'{f}.jpg', settings.MEDIA_ROOT / 'menu' / f'{f}.jpg')

        dest = settings.MEDIA_ROOT / 'gallery'
        dest.mkdir(parents=True, exist_ok=True)
        for fname, title in GALLERY:
            shutil.copy(settings.BASE_DIR / 'static' / 'img' / fname, dest / fname)
            GalleryImage.objects.create(title=title, image=f'gallery/{fname}')

        Post.objects.create(title='Градината е отворена!', created=datetime.date(2026, 4, 1),
            summary='Со доаѓањето на пролетта ја отвораме нашата градина.',
            body='Со доаѓањето на пролетта ја отвораме нашата градина под стаклениот покрив. Дојдете на кафе меѓу зеленилото.\n\nВечерно време масите брзо се полнат, па резервирајте навреме.')
        Post.objects.create(title='Нов сезонски мени', created=datetime.date(2026, 10, 15),
            summary='Топли пијалоци и десерти за есенските денови.',
            body='За есента подготвивме нови топли пијалоци и десерти, меѓу кои густо топло чоколадо и чоколаден мус.')
        TeamMember.objects.create(name='Ана Петровска', role='Управител', bio='Се грижи секој гостин да се чувствува како дома.')
        TeamMember.objects.create(name='Марко Стојанов', role='Главен бариста', bio='Мајстор за еспресо и капучино.')
        TeamMember.objects.create(name='Ивана Ристева', role='Келнерка', bio='Секогаш со насмевка до вашата маса.')
        self.stdout.write('Seeded.')
