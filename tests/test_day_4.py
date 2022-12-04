import logging

from inputs import get_file_data
from days.day_4 import part_1, part_2


LOG = logging.getLogger()


class TestDay4Solutions:

    def setup_class(self):
        self.test_day_4_data = get_file_data('input_day4_test')
        self.day_4_data = get_file_data('input_day4')

    def test_part_1(self):
        assert part_1(self.test_day_4_data) == 2

    def test_part_2(self):
        assert part_2(self.test_day_4_data) == 4

    def teardown_class(self):
        LOG.info(f'Part 1 answer: {part_1(self.day_4_data)}')  # 456
        LOG.info(f'Part 2 answer: {part_2(self.day_4_data)}')  # 808
