import logging

from inputs import get_file_data
from days.day_1 import part_1, part_2


LOG = logging.getLogger()


class TestDay1Solutions:

    def setup_class(self):
        self.test_day_1_data = get_file_data('input_day1_test')
        self.day_1_data = get_file_data('input_day1')

    def test_part_1(self):
        assert part_1(self.test_day_1_data) == 24000

    def test_part_2(self):
        assert part_2(self.test_day_1_data) == 45000

    def teardown_class(self):
        LOG.info(f'Part 1 answer: {part_1(self.day_1_data)}')  # 74394
        LOG.info(f'Part 2 answer: {part_2(self.day_1_data)}')  # 212836
