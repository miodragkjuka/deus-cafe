from django.db import models


class MenuCategory(models.Model):
    name = models.CharField('Име', max_length=80)
    order = models.PositiveIntegerField('Редослед', default=0)
    image = models.ImageField('Слика', upload_to='menu/', blank=True)

    class Meta:
        ordering = ['order', 'name']
        verbose_name = 'Категорија'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    category = models.ForeignKey(MenuCategory, on_delete=models.CASCADE, related_name='items', verbose_name='Категорија')
    name = models.CharField('Име', max_length=120)
    description = models.CharField('Опис', max_length=250, blank=True)
    price = models.PositiveIntegerField('Цена (ден.)')

    class Meta:
        ordering = ['category__order', 'name']
        verbose_name = 'Ставка од менито'
        verbose_name_plural = 'Мени'

    def __str__(self):
        return self.name


class TeamMember(models.Model):
    name = models.CharField('Име', max_length=100)
    role = models.CharField('Улога', max_length=100)
    bio = models.CharField('Кратко за', max_length=250, blank=True)
    photo = models.ImageField('Фотографија', upload_to='team/', blank=True)

    class Meta:
        verbose_name = 'Член на тимот'
        verbose_name_plural = 'Тим'

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField('Наслов', max_length=150)
    summary = models.CharField('Краток опис', max_length=250)
    body = models.TextField('Содржина')
    image = models.ImageField('Слика', upload_to='news/', blank=True)
    created = models.DateField('Датум')

    class Meta:
        ordering = ['-created']
        verbose_name = 'Вест'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.title


class GalleryImage(models.Model):
    title = models.CharField('Опис', max_length=120)
    image = models.ImageField('Слика', upload_to='gallery/')

    class Meta:
        verbose_name = 'Слика'
        verbose_name_plural = 'Галерија'

    def __str__(self):
        return self.title


class Reservation(models.Model):
    name = models.CharField('Име и презиме', max_length=100)
    phone = models.CharField('Телефон', max_length=30)
    date = models.DateField('Датум')
    time = models.TimeField('Време')
    guests = models.PositiveIntegerField('Број на гости')
    note = models.TextField('Забелешка', blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']
        verbose_name = 'Резервација'
        verbose_name_plural = 'Резервации'

    def __str__(self):
        return f'{self.name} – {self.date} {self.time:%H:%M}'


class ContactMessage(models.Model):
    name = models.CharField('Име', max_length=100)
    email = models.EmailField('Е-пошта')
    message = models.TextField('Порака')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']
        verbose_name = 'Порака'
        verbose_name_plural = 'Пораки'

    def __str__(self):
        return f'{self.name} ({self.email})'
