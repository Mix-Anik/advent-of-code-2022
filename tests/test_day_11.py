import logging

from inputs import get_file_data
from days.day_11 import part_1, part_2

LOG = logging.getLogger()


class TestDay11Solutions:

    def setup_class(self):
        self.test_day_11_data = get_file_data('input_day11_test', False)
        self.day_11_data = get_file_data('input_day11', False)

    def test_part_1(self):
        assert part_1(self.test_day_11_data) == 10605

    def test_part_2(self):
        assert part_2(self.test_day_11_data) == 2713310158

    def teardown_class(self):
        LOG.info(f'Part 1 answer: {part_1(self.day_11_data)}')  # 58794
        LOG.info(f'Part 2 answer: {part_2(self.day_11_data)}')  # 20151213744
