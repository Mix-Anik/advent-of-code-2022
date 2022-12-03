import logging

from inputs import get_file_data
from days.day_3 import part_1, part_2


LOG = logging.getLogger()


class TestDay3Solutions:

    def setup_class(self):
        self.test_day_3_data = get_file_data('input_day3_test')
        self.day_3_data = get_file_data('input_day3')

    def test_part_1(self):
        assert part_1(self.test_day_3_data) == 157

    def test_part_2(self):
        assert part_2(self.test_day_3_data) == 70

    def teardown_class(self):
        LOG.info(f'Part 1 answer: {part_1(self.day_3_data)}')  # 8139
        LOG.info(f'Part 2 answer: {part_2(self.day_3_data)}')  # 2668
