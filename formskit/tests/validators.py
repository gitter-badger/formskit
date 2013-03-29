from formskit.tests.base import FormskitTestCase
import formskit.validators as VAL


class ValidatorTest(FormskitTestCase):
    cls = None
    good_samples = None
    bad_samples = None

    def test_create(self):
        sample_text = 'something'
        validator = self.cls(sample_text)

        self.assertEqual(sample_text, validator.message)

    def test_success(self):
        validator = self.cls('')

        for sample in self.good_samples:
            self.assertNone(validator(sample))

    def test_fail(self):
        validator = self.cls('')

        for sample in self.bad_samples:
            self.assertRaises(VAL.ValidationError, validator, sample)


class NotEmptyValidatorTest(ValidatorTest):
    cls = VAL.NotEmpty

    good_samples = [
        'z', '0', '12312312dasd213123', ',', ' ad sda ',
    ]

    bad_samples = [
        ' ', '', None, [], {},
    ]


class IsDigitValidatorTest(ValidatorTest):
    cls = VAL.IsDigit

    good_samples = [
        '1', '123123123', '012312', '-123123',
    ]

    bad_samples = [
        'a', '', '-123213.12323', '2a',
    ]

class EmailValidatorTest(ValidatorTest):
    cls = VAL.Email

    good_samples = [
        'msocek@gmail.com',
        '1asd@asdasd.sadad.pl',
    ]

    bad_samples = [
        'a', '', '-123213.12323', '2a',
        ' ', '@asdweq.asdad.pl', '1asd@asdasd.sadad.asdpl',
    ]