from rest_framework import status
from rest_framework.test import APITestCase
from .models import *
from django.urls import reverse
from .serializers import PerevalSerializer


class PerevalTestCase(APITestCase):
    '''
    Тест на проверку получения записи о созданном объекте в таблице Pereval
    '''

    def setUp(self):
        '''
        Создаем объект для проверки
        :return:
        '''
        self.pereval_1 = Pereval.objects.create(
            user=AppUser.objects.create(
                email='test@test.com',
                phone='89012345678',
                name='Test',
                surname='Testov',
                patronymic='Testovich'
            ),
            beauty_title='pereval',
            title='Pereval',
            other_titles='First Pereval',
            connect='Two Pereval and Three Pereval',
            coord_id=Coords.objects.create(
                latitude=32.456789,
                longitude=12.345678,
                height=1234
            ),
            level=Level.objects.create(
                winter='2a',
                summer='2a',
                autumn='2a',
                spring='2a'
            )
        )

    def test_pereval_detail(self):
        '''
        Тест на получение записи о созданном объекте (pereval_1) таблицы Pereval
        :return: ok
        '''
        response = self.client.get(reverse('pereval-detail', kwargs={'pk': self.pereval_1.id}))
        serializer_data = PerevalSerializer(self.pereval_1, context={'request': response.wsgi_request}).data
        self.assertEqual(serializer_data, response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
