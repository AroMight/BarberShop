from django.test import TestCase
from parameterized import parameterized
from users.forms.register_form import RegisterForm


class UsersRegisterFormTest(TestCase):

    def setUp(self):
        self.form = RegisterForm()

    @parameterized.expand([
        ('username', ''),
        ('password', ''),
    ])
    def test_form_fields_help_text(self, field_name, expected_help_text):
        actual_help_text = self.form.fields[field_name].help_text
        self.assertEqual(actual_help_text, expected_help_text)

    @parameterized.expand([
        ('password2', 'Confirm Password'),
    ])
    def test_form_field_label(self, field_name, expected_label):
        actual_label = self.form.fields[field_name].label
        self.assertEqual(actual_label, expected_label)

    @parameterized.expand([
        ('username', 'form-control'),
        ('email', 'form-control'),
        ('password', 'form-control'),
        ('password2', 'form-control'),
        ('phone_number', 'form-control'),
    ])
    def test_form_field_widget_class(self, field_name, expected_widget_class):
        actual_widget_class = self.form.fields[field_name].widget.attrs['class']
        self.assertEqual(actual_widget_class, expected_widget_class)

    @parameterized.expand([
        ('username', 'Enter your username.'),
        ('email', 'Enter your email.'),
        ('password', 'Enter your password.'),
        ('password2', 'Repeat your password.'),
        ('phone_number', 'Enter your phone number.'),
    ])
    def test_form_field_widget_placeholder(self, field_name, expected_placeholder):
        actual_placeholder = self.form.fields[field_name].widget.attrs['placeholder']
        self.assertEqual(actual_placeholder, expected_placeholder)


class UsersRegisterFormIntegrationTest(TestCase):

    def setUp(self):
        self.form_data = {
            'username': 'testuser',
            'email': 'vava@lol.com',
            'password': 'Abc@123456',
            'password2': 'Abc@123456',
            'phone_number': '12345678901',
        }

    def test_form_invalid_if_passwords_do_not_match(self):
        self.form_data['password2'] = 'Testwrongpassword'
        form = RegisterForm(data=self.form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("Passwords didn't match.", form.errors['password'])

    def test_form_invalid_if_email_already_exists(self):

        # Create the initial user
        form = RegisterForm(data=self.form_data)
        form.save()

        # Try to create another user with the same email
        self.form_data['username',
                       'phone_number'] = 'anotheruser', '12345678910'
        form2 = RegisterForm(data=self.form_data)

        # Check if form is invalid and if the error message is correct
        self.assertFalse(form2.is_valid())
        self.assertIn("Email already registred.", form2.errors['email'])

    def test_form_invalid_if_username_already_exists(self):

        # Create the initial user
        form = RegisterForm(data=self.form_data)
        form.save()

        # Try to create another user with the same username
        self.form_data['email', 'phone_number'] = 'vava@lol.com', '12345678910'
        form2 = RegisterForm(data=self.form_data)

        # Check if form is invalid and if the error message is correct
        self.assertFalse(form2.is_valid())
        self.assertIn("username already registred.", form2.errors['username'])

    def test_form_invalid_if_phone_number_already_exists(self):

        # Create the initial user
        form = RegisterForm(data=self.form_data)
        form.save()

        # Try to create another user with the same phone number
        self.form_data['email', 'username'] = 'vava@lol.com', 'anotheruser'
        form2 = RegisterForm(data=self.form_data)

        # Check if form is invalid and if the error message is correct
        self.assertFalse(form2.is_valid())
        self.assertIn("This number is already in use.",
                      form2.errors['phone_number'])
