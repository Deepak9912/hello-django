from django.test import TestCase
from .forms import ItemForm


class TesttemForm(TestCase):

    def_test_item_name_is_required(self):
        form = ItemForm({'name'=''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'this field is required.')

    def test_done_field_is_not_required(self)
