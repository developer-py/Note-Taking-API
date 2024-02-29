from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Note

class NoteAPITestCase(APITestCase):
    def setUp(self):
        self.note1 = Note.objects.create(title='Test Note 1', body='This is the body of test note 1')
        self.note2 = Note.objects.create(title='Another Test Note', body='This is the body of another test note')

    def test_create_note(self):
        url = reverse('note-list-create')
        data = {'title': 'New Note', 'body': 'This is a new note body'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Note.objects.count(), 3)
        self.assertEqual(Note.objects.last().title, 'New Note')

    def test_create_note_invalid_data(self):
        url = reverse('note-list-create')
        data = {'body': 'This is a new note body'}  # Missing 'title' field
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Note.objects.count(), 2)  # Ensure no new note is created

    def test_fetch_note_by_id(self):
        url = reverse('note-retrieve-update', kwargs={'pk': self.note1.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.note1.title)
        self.assertEqual(response.data['body'], self.note1.body)

    def test_fetch_non_existent_note(self):
        url = reverse('note-retrieve-update', kwargs={'pk': 9999})  # Non-existent PK
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_note_with_put(self):
        url = reverse('note-retrieve-update', kwargs={'pk': self.note2.pk})
        data = {'title': 'Updated Note', 'body': 'This is the updated body of the note'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Note.objects.get(pk=self.note2.pk).title, 'Updated Note')

    def test_update_note_with_patch(self):
        url = reverse('note-retrieve-update', kwargs={'pk': self.note2.pk})
        data = {'title': 'Patched Note'}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Note.objects.get(pk=self.note2.pk).title, 'Patched Note')

    def test_query_notes_by_title_substring(self):
        url = reverse('note-list-create') + '?title=Test'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_query_notes_by_title_substring_no_match(self):
        url = reverse('note-list-create') + '?title=NonExistent'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)

    def test_query_notes_by_title_substring_empty(self):
        url = reverse('note-list-create') + '?title='  
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_query_notes_by_title_substring_special_characters(self):
        url = reverse('note-list-create') + '?title=!*^@#$%'  
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)  


