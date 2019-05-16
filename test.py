import unittest
import user
import petproject


def compare_lists(tester, expected_list, result_list):
    if len(expected_list) == 0 and len(result_list) == 0:
        return

    if len(expected_list) != 0 and len(result_list) == 0:
        tester.assertListEqual(result_list, expected_list)

    for item in result_list:
        tester.assertTrue(item in expected_list)


class AccountingTester(unittest.TestCase):
    data_file = "english_test.csv"

    def test_check_burnt_in_dates(self):
        with open("english_test.csv", "r") as file:
            lines = file.read()
            self.assertEqual(lines.find("2015"), -1)
            self.assertEqual(lines.find("2016"), -1)

    def test_which_year_max(self):
        table = data_manager.get_table_from_file(self.data_file)
        result = accounting.which_year_max(table)
        self.assertEqual(result, 2015)

    def test_avg_amount(self):
        table = data_manager.get_table_from_file(self.data_file)
        result = accounting.avg_amount(table, 2016)
        self.assertEqual(result, 48.125)


def main():
    unittest.main(verbosity=2)


if __name__ == '__main__':
    main()
