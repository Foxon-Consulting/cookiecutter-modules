import unittest

from {{cookiecutter.folder_name}}.{{cookiecutter.__first_script_name_formatted}} import _{{cookiecutter.__first_script_name_formatted}}


class {{cookiecutter.__first_script_test_name_formatted}}Test(unittest.TestCase):
    def setUp(self):
        # self.task = Task("Dummy task", False)
        pass

    def tearDown(self):
        # To be implemented if required
        pass

    def test_{{cookiecutter.__first_script_name_formatted}}(self):
        self.assertEqual(
            _{{cookiecutter.__first_script_name_formatted}}("green", "blue"), {'argA': 'green', 'argB': 'blue'}
        )
