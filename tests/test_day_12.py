import logging

from inputs import get_file_data
from days.day_12 import part_1, part_2

LOG = logging.getLogger()


class TestDay12Solutions:

    def setup_class(self):
        self.test_day_12_data = get_file_data('input_day12_test', False)
        self.day_12_data = get_file_data('input_day12', False)

    def test_part_1(self):
        assert part_1(self.test_day_12_data) == 31

    def test_part_2(self):
        assert part_2(self.test_day_12_data) == 29

    def teardown_class(self):
        LOG.info(f'Part 1 answer: {part_1(self.day_12_data)}')  # 361
        LOG.info(f'Part 2 answer: {part_2(self.day_12_data)}')  # 354
